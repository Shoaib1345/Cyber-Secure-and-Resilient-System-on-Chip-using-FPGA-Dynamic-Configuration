<img width="1360" height="479" alt="image" src="https://github.com/user-attachments/assets/cf213287-39fb-425c-88b5-28cff8e768f9" />
<img width="802" height="434" alt="image" src="https://github.com/user-attachments/assets/891d5b8a-9a3b-4666-b7b7-5ec352f5ef7f" />

 🛡️ Cyber Secure & Resilient FPGA System (Advanced Python Prototype)

A next-generation **cybersecurity and educational prototype** built in **Python** that simulates a **Cyber Secure and Resilient System-on-Chip (SoC)** using **FPGA dynamic configuration principles**.  

This project not only performs secure tasks such as **RSA key generation**, **bitstream signing**, and **secure FPGA reconfiguration**, but also **explains each process in real time** — making it ideal for **learning, research, and simulation** in cybersecurity and hardware security.

---

## 🧠 Overview

This advanced system simulates how **real FPGA chips maintain trust and integrity** during reconfiguration.  
It demonstrates:
- How cryptographic keys are generated and used
- How bitstreams (FPGA configuration files) are signed and verified
- How unauthorized changes are detected and blocked  
- Why each step is crucial for building secure, resilient hardware

Every action in the GUI produces:
- Real **cryptographic output**
- **AI-style explanations**
- **Confirmation and educational reasoning**

---

## ⚙️ Key Features

| Feature | Description |
|----------|--------------|
| 🔐 **RSA Key Generation (Explained)** | Generates secure public/private key pairs and explains their purpose in hardware trust and authentication. |
| 🧾 **Bitstream Signing (Integrity Check)** | Signs FPGA bitstream files with a private key to prevent tampering. |
| ⚙️ **FPGA Reconfiguration Simulation** | Emulates loading secure or unsafe FPGA modules, verifying authenticity first. |
| 📊 **Monitoring Dashboard** | Displays live security logs and reasoning messages. |
| 🧠 **Explainable Security Layer** | Each process includes detailed text explaining the *why*, *how*, and *where used* of the step. |

---

## 🖥️ GUI Preview

A minimal, dark-themed, Tkinter-based GUI that displays:
- Live cryptographic operations  
- Educational commentary  
- System logs with real-time feedback

Example view:

```

[INFO] RSA Keys Generated Successfully.
Explanation:
RSA is an asymmetric cryptography method used to ensure trust and authenticity.
Private Key → used by the manufacturer to sign FPGA configurations.
Public Key → embedded in FPGA to verify that the bitstream is genuine.
Use Case:
This prevents attackers from loading unauthorized logic into the FPGA.
✅ Keys saved to data/private.pem and data/public.pem

````

---

## 🧰 Installation

**Requirements:**
- Python 3.9+
- Dependencies:
  ```bash
  pip install cryptography tkinter
````

**Run the program:**

```bash
python main.py
```

---

## 📁 Folder Structure

```
Cyber-Secure-and-Resilient-System-on-Chip-using-FPGA-Dynamic-Configuration/
│
├── main.py                        # Main Tkinter GUI
├── modules/
│   ├── signer.py                  # RSA key generation + bitstream signing
│   ├── pr_manager.py              # Simulated partial reconfiguration
│   └── monitor.py                 # Security monitoring system
│
├── data/
│   ├── private.pem                # Private RSA key
│   ├── public.pem                 # Public RSA key
│   ├── moduleA.bit                # Example bitstream file
│   └── safe_module.bit            # Trusted bitstream
│
├── requirements.txt
└── README.md
```

---

## 🧠 Explanation Flow

| Step | Operation             | Explanation                                                                                                   |
| ---- | --------------------- | ------------------------------------------------------------------------------------------------------------- |
| 1️⃣  | **Generate RSA Keys** | Creates `private.pem` and `public.pem`. Explains why asymmetric encryption is critical for FPGA authenticity. |
| 2️⃣  | **Sign Bitstream**    | Uses private key to sign bitstream file. Teaches how digital signatures protect configuration integrity.      |
| 3️⃣  | **Reconfigure FPGA**  | Simulates a secure FPGA module load. Explains verification and why only signed modules are allowed.           |
| 4️⃣  | **Monitor System**    | Displays detailed logs with AI-style reasoning and confirmation.                                              |

---
Architecture Update
+--------------------------------------------------------------+
|          Cyber Secure FPGA System (with Chatbot)             |
+--------------------------------------------------------------+
|  RSA Key Engine  |  Bitstream Signer  |  FPGA Simulator       |
|  Monitor & Logger |  Explainable Layer |  🤖 Chatbot Assistant  |
+--------------------------------------------------------------+
|         Tkinter GUI + Chat Console + Interactive Prompts     |
+--------------------------------------------------------------+




## 🧬 How It Works

1. **RSA Engine**
   Generates 2048-bit asymmetric keys for signing and verification.

   * Private Key → signs the bitstream
   * Public Key → embedded in FPGA logic for verification

2. **Bitstream Signing**
   The `.bit` file is read, hashed, and digitally signed.
   Any tampered file will fail verification.

3. **FPGA Reconfiguration**
   Simulates partial reconfiguration with dynamic loading of modules — only verified ones are accepted.

4. **Monitoring System**
   Tracks each step, showing alerts or confirmations in the GUI log console.

---

## 💡 Educational Insights

Each module in this system provides not only security but also learning outcomes:

* 🔑 *Cryptography Concepts:* asymmetric encryption, signing, verification
* 🧩 *FPGA Concepts:* dynamic configuration, hardware security
* 🧠 *AI in Security Education:* explainable operations for users to understand real-world logic

---

## 🧠 Future Enhancements

* Integrate **AI-based anomaly detection** for malicious FPGA activity
* Add **real FPGA integration (Xilinx / Intel)**
* Implement **voice narration** for educational demos
* Add **blockchain-based trust log**
* Introduce **attack simulation mode**

---

## 👨‍💻 Author

**Shoaib Ahmed Bullo**
🎓 AI & Cybersecurity Researcher
📍 Pakistan
🔗 [GitHub Profile](https://github.com/Shoaib1345)

---

## 🪪 License

This project is licensed under the **MIT License** — free for research and educational use.

---

## 📘 Repository Information

**Repository Name:** `cyber-secure-fpga-advanced`
**Description:**

> Advanced explainable prototype for a Cyber Secure & Resilient System-on-Chip using Python — integrates cryptographic key management, bitstream integrity verification, and secure FPGA reconfiguration through a Tkinter GUI.

---(including how to demonstrate the prototype for evaluation)?
```
