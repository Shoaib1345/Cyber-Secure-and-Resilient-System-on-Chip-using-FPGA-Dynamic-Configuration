
import os
import time
import zlib
import random

class FPGASimulator:
    def __init__(self, pr_region="PR0"):
        self.current_image = None
        self.pr_region = pr_region
        self.program_count = 0
        self._state = {}

    def program_partial(self, bitstream_path, log_callback=print):
        if not os.path.exists(bitstream_path):
            log_callback(f"[FPGA] ERROR: Bitstream not found: {bitstream_path}")
            return False
        log_callback(f"[FPGA] Programming {bitstream_path} into region {self.pr_region} ...")
        # simulate programming time
        time.sleep(1.0 + random.random()*0.8)
        self.current_image = bitstream_path
        self.program_count += 1
        log_callback("[FPGA] Programming complete.")
        return True

    def readback_crc(self):
        if self.current_image is None:
            return None
        data = open(self.current_image, "rb").read()
        return zlib.crc32(data) & 0xffffffff

    def self_test(self, log_callback=print):
        # simulate self-test using CRC: certain CRC residues simulate failure
        crc = self.readback_crc()
        if crc is None:
            log_callback("[FPGA] Self-test: no image loaded.")
            return False
        # transient random failure
        if random.randint(0, 49) == 0:
            log_callback("[FPGA] Self-test: TRANSIENT ERROR")
            return False
        if crc % 17 == 0:
            log_callback("[FPGA] Self-test: CRC-based deterministic failure")
            return False
        log_callback(f"[FPGA] Self-test: PASS (CRC=0x{crc:08x})")
        return True

    def get_telemetry(self):
        # Return simulated telemetry values: packet_rate, errors, cpu_load
        base = 1000
        if self.current_image and "stress" in os.path.basename(self.current_image).lower():
            base += random.randint(0, 300)
        if self.current_image and "bad" in os.path.basename(self.current_image).lower():
            errors = random.randint(10, 60)
            packet_rate = base // 4
            cpu = random.randint(50, 95)
        else:
            errors = random.randint(0, 2)
            packet_rate = base + random.randint(-10, 10)
            cpu = random.randint(5, 30)
        return {"packet_rate": packet_rate, "errors": errors, "cpu": cpu}
