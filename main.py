import os
import threading
import queue
import time
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

from core.rsa_engine import generate_keys, explain_keygen
from core.signer import sign_file, verify_signature
from core.fpga_simulator import FPGASimulator
from core.pr_manager import PRManager
from core.explain_module import explain_signing, explain_verification
from core.monitor import TelemetryMonitor

from core.chatbot import chatbot_reply

def open_chatbot():
    chat_window = tk.Toplevel(root)
    chat_window.title("FPGA Security Chatbot")
    chat_window.geometry("450x400")
    chat_window.configure(bg="#222")

    tk.Label(chat_window, text="Cyber Secure Chatbot Assistant", font=("Arial", 14, "bold"), fg="cyan", bg="#222").pack(pady=10)
    chat_box = tk.Text(chat_window, height=15, width=55, bg="#111", fg="white", wrap="word")
    chat_box.pack(padx=10, pady=10)
    chat_box.insert(tk.END, "🤖 Chatbot: Hello! Ask me about RSA, signing, verification, or FPGA security.\n\n")

    entry = tk.Entry(chat_window, width=45, bg="#333", fg="white")
    entry.pack(side=tk.LEFT, padx=10, pady=5)

    def send_message():
        user_msg = entry.get().strip()
        if not user_msg:
            return
        chat_box.insert(tk.END, f"🧑 You: {user_msg}\n")
        reply = chatbot_reply(user_msg)
        chat_box.insert(tk.END, f"🤖 Chatbot: {reply}\n\n")
        chat_box.see(tk.END)
        entry.delete(0, tk.END)

    send_btn = tk.Button(chat_window, text="Send", command=send_message, bg="cyan", fg="black")
    send_btn.pack(side=tk.RIGHT, padx=10, pady=5)



















# Ensure data folder exists
os.makedirs("data", exist_ok=True)

# Simple thread-safe logger for GUI
log_queue = queue.Queue()

def gui_log(msg):
    log_queue.put(msg)

class App:
    def __init__(self, root):
        self.root = root
        root.title("Cyber Secure FPGA Prototype (Advanced)")
        root.geometry("900x600")
        root.configure(bg="#0f1111")

        # Header
        header = tk.Label(root, text="🛡️ Cyber Secure FPGA Prototype", font=("Helvetica", 20, "bold"), fg="white", bg="#0f1111")
        header.pack(pady=10)

        # Console area
        self.console = scrolledtext.ScrolledText(root, width=100, height=20, bg="#1c1c1c", fg="#8efc8e", font=("Consolas", 10))
        self.console.pack(padx=10, pady=10)

        # Buttons frame
        btn_frame = tk.Frame(root, bg="#0f1111")
        btn_frame.pack(pady=8)

        btn_gen = tk.Button(btn_frame, text="Generate RSA Keys", width=20, command=self.handle_generate_keys, bg="#2b6cb0", fg="white")
        btn_gen.grid(row=0, column=0, padx=6, pady=4)

        btn_sign = tk.Button(btn_frame, text="Sign Bitstream", width=20, command=self.handle_sign_bitstream, bg="#2b6cb0", fg="white")
        btn_sign.grid(row=0, column=1, padx=6, pady=4)

        btn_verify_program = tk.Button(btn_frame, text="Verify & Program", width=20, command=self.handle_verify_and_program, bg="#2b6cb0", fg="white")
        btn_verify_program.grid(row=0, column=2, padx=6, pady=4)

        btn_monitor = tk.Button(btn_frame, text="Start Monitoring", width=20, command=self.handle_start_monitoring, bg="#2b6cb0", fg="white")
        btn_monitor.grid(row=0, column=3, padx=6, pady=4)

        btn_stop = tk.Button(btn_frame, text="Stop Monitoring", width=20, command=self.handle_stop_monitoring, bg="#d9534f", fg="white")
        btn_stop.grid(row=0, column=4, padx=6, pady=4)
        tk.Button(root, text="🧠 Open Chatbot", command=open_chatbot, bg="#00bcd4", fg="black", width=25).pack(pady=10)

        # internal
        self.fpga = FPGASimulator()
        self.pr = PRManager(self.fpga, public_key_path="data/public.pem", safe_image="data/safe_module.bit", log_callback=gui_log)
        self.monitor = TelemetryMonitor()
        self.monitor_thread = None
        self.monitor_running = False

        # start GUI log polling
        self.root.after(100, self._poll_log_queue)

    def _poll_log_queue(self):
        try:
            while True:
                msg = log_queue.get_nowait()
                self.console.insert(tk.END, msg + "\n")
                self.console.see(tk.END)
        except queue.Empty:
            pass
        self.root.after(100, self._poll_log_queue)

    def handle_generate_keys(self):
        try:
            priv, pub = generate_keys("data/private.pem", "data/public.pem", bits=3072)
            gui_log("[INFO] RSA Keys generated.")
            expl = explain_keygen(priv, pub)
            gui_log(expl)
            messagebox.showinfo("Keys Generated", f"Private: {priv}\nPublic: {pub}")
        except Exception as e:
            messagebox.showerror("Error", str(e))
            gui_log(f"[ERROR] Key generation failed: {e}")

    def handle_sign_bitstream(self):
        path = filedialog.askopenfilename(title="Select bitstream (.bit or any binary file)", filetypes=[("Bitstream", "*.*")])
        if not path:
            return
        try:
            sig = sign_file(path, private_key_path="data/private.pem")
            gui_log(f"[OK] Signed: {path} -> {sig}")
            expl = explain_signing(path, sig)
            gui_log(expl)
            messagebox.showinfo("Signed", f"Signature created: {sig}")
        except Exception as e:
            gui_log(f"[ERROR] Signing failed: {e}")
            messagebox.showerror("Signing Error", str(e))

    def handle_verify_and_program(self):
        path = filedialog.askopenfilename(title="Select bitstream to verify & program", filetypes=[("Bitstream", "*.*")])
        if not path:
            return
        sig_path = path + ".sig"
        if not os.path.exists(sig_path):
            messagebox.showwarning("Signature missing", f"No signature file found for {path}\nExpected: {sig_path}")
            return
        ok, msg = verify_signature("data/public.pem", path, sig_path)
        gui_log(f"[Verify] {msg}")
        gui_log(explain_verification(path, sig_path))
        if not ok:
            messagebox.showerror("Verification Failed", msg)
            return
        # program and validate via PRManager
        success = self.pr.install_and_validate(path, sig_path, do_self_test=True)
        if success:
            messagebox.showinfo("Success", "Bitstream verified and programmed successfully.")
        else:
            messagebox.showwarning("Install Failed", "Programming / self-test failed; check logs.")

    def handle_start_monitoring(self):
        if self.monitor_running:
            messagebox.showinfo("Monitoring", "Monitoring already running.")
            return
        # prepare baseline by collecting telemetry from safe image
        # ensure safe image exists; if not, create simple safe file
        safe_path = "data/safe_module.bit"
        if not os.path.exists(safe_path):
            with open(safe_path, "wb") as f:
                f.write(b"SAFE_MODULE_V1" * 200)
            gui_log(f"[Setup] Created demo safe image at {safe_path}")
        # program safe image first
        self.fpga.program_partial(safe_path, log_callback=gui_log)
        # collect baseline samples
        samples = []
        for _ in range(120):
            samples.append(self.fpga.get_telemetry())
            time.sleep(0.01)
        res = self.monitor.train_baseline(samples)
        gui_log(f"[Monitor] {res}")
        self.monitor_running = True
        self.monitor_thread = threading.Thread(target=self._monitor_loop, daemon=True)
        self.monitor_thread.start()
        messagebox.showinfo("Monitoring", "Monitoring started; check console for alerts.")

    def handle_stop_monitoring(self):
        if not self.monitor_running:
            messagebox.showinfo("Monitoring", "Monitoring is not running.")
            return
        self.monitor_running = False
        messagebox.showinfo("Monitoring", "Monitoring stopped.")

    def _monitor_loop(self):
        gui_log("[Monitor] Entering monitoring loop...")
        inject_at = time.time() + 8  # will inject anomaly at 8s for demo
        injected = False
        while self.monitor_running:
            t = self.fpga.get_telemetry()
            is_anom = self.monitor.is_anomaly(t)
            gui_log(f"[Monitor] Telemetry: {t} Anomaly: {is_anom}")
            if is_anom:
                gui_log("[Monitor] Anomaly detected -> Triggering rollback to safe image.")
                self.pr.rollback()
                # stop monitoring after recovery for demo
                self.monitor_running = False
                break
            # demo: inject bad module after some time
            if not injected and time.time() > inject_at:
                bad_path = "data/bad_module.bit"
                with open(bad_path, "wb") as f:
                    f.write(b"BAD_MODULE_V1" * 200)
                gui_log("[Demo] Injecting bad module to simulate attack/fault.")
                self.fpga.program_partial(bad_path, log_callback=gui_log)
                injected = True
            time.sleep(1.0)
        gui_log("[Monitor] Monitoring loop exited.")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
