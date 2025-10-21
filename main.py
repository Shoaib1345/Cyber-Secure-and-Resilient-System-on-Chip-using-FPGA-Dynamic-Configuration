# main.py
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from modules.signer import generate_keys, sign_bitstream
from modules.pr_manager import program_partial
from modules.monitor import detect_anomaly
import random

class CyberFPGAApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cyber Secure FPGA System")
        self.root.geometry("700x500")
        self.root.configure(bg="#0e1111")

        tk.Label(root, text="🛡️ Cyber Secure FPGA Prototype",
                 bg="#0e1111", fg="white", font=("Arial", 18, "bold")).pack(pady=10)

        self.log_box = scrolledtext.ScrolledText(root, width=80, height=20, bg="#1c1f1f", fg="lime", font=("Consolas", 10))
        self.log_box.pack(padx=10, pady=10)

        frame = tk.Frame(root, bg="#0e1111")
        frame.pack(pady=10)

        tk.Button(frame, text="🔑 Generate RSA Keys", command=self.generate_keys, width=22, bg="#2b6cb0", fg="white").grid(row=0, column=0, padx=5)
        tk.Button(frame, text="✍️ Sign Bitstream", command=self.sign_bitstream, width=22, bg="#2b6cb0", fg="white").grid(row=0, column=1, padx=5)
        tk.Button(frame, text="⚙️ Reconfigure FPGA", command=self.reconfigure_fpga, width=22, bg="#2b6cb0", fg="white").grid(row=0, column=2, padx=5)
        tk.Button(frame, text="📊 Monitor System", command=self.monitor_system, width=22, bg="#2b6cb0", fg="white").grid(row=0, column=3, padx=5)

    def log(self, msg):
        self.log_box.insert(tk.END, msg + "\n")
        self.log_box.see(tk.END)

    def generate_keys(self):
        priv, pub = generate_keys()
        self.log(f"[INFO] RSA Keys generated:\nPrivate: {priv}\nPublic: {pub}")

    def sign_bitstream(self):
        path = filedialog.askopenfilename(title="Select Bitstream (.bit)", filetypes=[("Bitstream Files", "*.bit")])
        if not path:
            return
        try:
            sig_path = sign_bitstream(path, "data/private.pem")
            self.log(f"[OK] Bitstream signed successfully:\nSignature: {sig_path}")
        except Exception as e:
            self.log(f"[ERROR] {str(e)}")

    def reconfigure_fpga(self):
        path = filedialog.askopenfilename(title="Select Bitstream to Load", filetypes=[("Bitstream Files", "*.bit")])
        if not path:
            return
        program_partial(path, self.log)

    def monitor_system(self):
        data = [random.randint(0, 10) for _ in range(10)]
        data.append(random.randint(0, 50))  # simulate anomaly
        if detect_anomaly(data):
            self.log("[ALERT] Anomaly detected! Triggering safe reconfiguration...")
            program_partial("data/safe_module.bit", self.log)
        else:
            self.log("[OK] System running normally.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CyberFPGAApp(root)
    root.mainloop()
