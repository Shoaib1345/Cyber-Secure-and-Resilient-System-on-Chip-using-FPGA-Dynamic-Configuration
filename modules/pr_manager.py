# modules/pr_manager.py
import time
import os

def program_partial(bitstream, log_callback=print):
    """Mock FPGA reconfiguration."""
    if not os.path.exists(bitstream):
        log_callback("[ERROR] Bitstream not found!")
        return False
    log_callback(f"[INFO] Reconfiguring FPGA with {bitstream} ...")
    time.sleep(2)
    log_callback("[OK] Partial Reconfiguration Complete.")
    return True
