"""
pr_manager.py
Orchestrates secure partial reconfiguration:
 - verify signature
 - program simulated FPGA
 - run self-test
 - rollback to a safe image if needed
"""
import os
import time
from core.signer import verify_signature
from core.explain_module import explain_reconfiguration

class PRManager:
    def __init__(self, fpga_simulator, public_key_path="data/public.pem", safe_image="data/safe_module.bit", log_callback=print):
        self.fpga = fpga_simulator
        self.pubkey = public_key_path
        self.safe_image = safe_image
        self.log = log_callback

    def install_and_validate(self, bitstream_path, sig_path, do_self_test=True):
        # Explain step to user
        self.log(explain_reconfiguration(bitstream_path))
        # Verify signature
        ok, msg = verify_signature(self.pubkey, bitstream_path, sig_path)
        self.log(f"[PRManager] Signature check: {msg}")
        if not ok:
            self.log("[PRManager] Aborting installation due to invalid signature.")
            return False
        # Program device
        prog_ok = self.fpga.program_partial(bitstream_path, log_callback=self.log)
        if not prog_ok:
            self.log("[PRManager] Programming failed.")
            return False
        # Self-test
        if do_self_test:
            self.log("[PRManager] Running self-test...")
            time.sleep(0.5)
            if not self.fpga.self_test(log_callback=self.log):
                self.log("[PRManager] Self-test failed. Initiating rollback.")
                self.rollback()
                return False
        self.log("[PRManager] Installation successful.")
        return True

    def rollback(self):
        if not self.safe_image or not os.path.exists(self.safe_image):
            self.log("[PRManager] No safe image available for rollback.")
            return False
        self.log(f"[PRManager] Rolling back to safe image: {self.safe_image}")
        ok = self.fpga.program_partial(self.safe_image, log_callback=self.log)
        if ok:
            self.log("[PRManager] Rollback programming complete. Running self-test on safe image...")
            if self.fpga.self_test(log_callback=self.log):
                self.log("[PRManager] Rollback success.")
                return True
            else:
                self.log("[PRManager] Rollback self-test failed.")
                return False
        else:
            self.log("[PRManager] Rollback programming failed.")
            return False
