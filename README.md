<img width="1359" height="717" alt="image" src="https://github.com/user-attachments/assets/417a29f4-ddd5-4cba-acef-2db6e28d2155" />


## 🛡️ Cyber Secure FPGA Prototype

A **Python-based GUI simulation** of a **Cyber Secure and Resilient System-on-Chip (SoC)** using **FPGA dynamic configuration principles**.
This prototype demonstrates how **hardware-level cybersecurity**, **bitstream integrity**, and **dynamic reconfiguration** can be simulated and managed through an interactive GUI.

---

### 🧠 Project Overview

This project provides a **software-based prototype** (no physical FPGA needed) that mimics secure FPGA operations such as:

* **Key generation (RSA)** for cryptographic security
* **Bitstream signing and verification**
* **Dynamic reconfiguration simulation** of FPGA logic
* **System monitoring and intrusion detection simulation**

It serves as an **academic or industrial prototype** for showcasing secure hardware systems, adaptable to **defense, IoT, and AI-based embedded systems**.

---

### 🧩 Core Features

| Feature                        | Description                                                              |
| ------------------------------ | ------------------------------------------------------------------------ |
| 🔐 **RSA Key Generation**      | Generates secure private/public key pairs stored in `data/`.             |
| 🧾 **Bitstream Signing**       | Signs simulated FPGA bitstreams using private RSA keys for authenticity. |
| ⚙️ **Dynamic Reconfiguration** | Simulates reconfiguration of FPGA modules based on signed bitstreams.    |
| 📊 **System Monitoring**       | Tracks operations and logs system activity for anomaly detection.        |
| 💻 **Modern GUI (Tkinter)**    | Professional dark-themed interface for user interaction.                 |

---

### 🧱 System Architecture

```
+---------------------------------------------+
|         Cyber Secure FPGA Prototype         |
+---------------------------------------------+
| 1. RSA Key Manager      -> Generates keys   |
| 2. Bitstream Signer     -> Signs configs    |
| 3. FPGA Reconfig Engine -> Loads bitstreams |
| 4. Monitor Module       -> Detects threats  |
+---------------------------------------------+
| GUI Layer (Tkinter) -> User Interaction     |
+---------------------------------------------+
```

---



### 🧰 Requirements

**Python Version:** 3.9 or above
**Dependencies:**

```bash
pip install cryptography tkinter
```

---

### 🚀 How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/Shoaib1345/cyber-secure-fpga.git
   cd cyber-secure-fpga
   ```

2. Run the main script:

   ```bash
   python main.py
   ```

3. The GUI will open:

   * Click **“Generate RSA Keys”** to create encryption keys.
   * Click **“Sign Bitstream”** to sign a simulated FPGA configuration file.
   * Click **“Reconfigure FPGA”** to simulate secure dynamic reconfiguration.
   * Click **“Monitor System”** to view logs and security alerts.

---

### 🧪 Folder Structure

```
cyber-secure-fpga/
│
├── main.py                # GUI + main application
├── core/
│   ├── rsa_manager.py     # Handles key generation
│   ├── signer.py          # Bitstream signing logic
│   ├── fpga_simulator.py  # FPGA reconfiguration simulation
│   ├── monitor.py         # System monitoring
│
├── data/
│   ├── private.pem        # Generated private key
│   ├── public.pem         # Generated public key
│   └── signed_bitstream.bin
│
├── assets/
│   └── gui_screenshot.png # GUI preview image
│
└── README.md
```

---

### 🔍 Example Output

```
[INFO] RSA Keys generated:
Private: data/private.pem
Public: data/public.pem
[INFO] Bitstream successfully signed.
[INFO] FPGA reconfigured with secure bitstream.
[ALERT] No intrusion detected.
```

---

### 💡 Future Enhancements

* Integrate with a real **FPGA board (Xilinx/Intel)**
* Add **hardware-based secure boot verification**
* Include **AI-based anomaly detection** on FPGA telemetry data
* Implement **blockchain-based bitstream validation**

---

### 👨‍💻 Author

**Shoaib Ahmed Bullo**
📍 Pakistan | 💼 AI & Cybersecurity Engineer
🔗 [GitHub](https://github.com/Shoaib1345)

---




