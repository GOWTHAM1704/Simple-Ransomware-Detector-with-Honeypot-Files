# 🍯 Honeypot Ransomware Detector

![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

A simple, lightweight, and highly effective ransomware detection script that uses **honeypot files** as digital tripwires. Instead of resource-intensive full-directory scans, this tool places decoy files in a directory and alerts the user the moment one is touched.

This project is an excellent demonstration of an efficient, high-fidelity security monitoring technique.

---

## 🛡️ Features

* **Extremely Lightweight**: Uses minimal CPU and disk resources by only monitoring a few decoy files.
* **High-Confidence Alerts**: Generates almost zero false positives. If a honeypot is modified, it's a strong sign of unauthorized activity.
* **Fast Detection**: Triggers an alert instantly upon the modification or deletion of a honeypot file.
* **Automatic Setup**: Automatically creates and deploys decoy files in the target directory.
* **Simple & Standalone**: Requires no external libraries or API keys.

---

## ⚙️ How It Works

This tool operates on the simple but powerful principle of a tripwire. Ransomware typically works by iterating through a file system and encrypting files one by one. This detector exploits that behavior.

1.  **Deploy Decoys**: Upon starting, the script creates a number of inconspicuous decoy files (e.g., `~document_1.txt`, `~report_4.xlsx`) within the directory you want to protect.
2.  **Set the Trap**: It immediately calculates and stores the initial hash (a digital fingerprint) of these newly created honeypot files.
3.  **Monitor the Tripwire**: The script then enters a monitoring loop, repeatedly checking **only the honeypot files** to see if their state has changed.
4.  **Trigger the Alert**: Since no legitimate user or process should ever modify or delete these specific decoy files, **any change** is treated as a high-priority threat. The script immediately triggers a loud alert, indicating a potential ransomware attack is in progress.

[Image of a digital tripwire in a network]

---

## 🚀 Getting Started

### Prerequisites

* Python 3.x

### Installation

1.  Clone the repository to your local machine:
    ```sh
    git clone [https://github.com/your-username/honeypot-ransomware-detector.git](https://github.com/your-username/honeypot-ransomware-detector.git)
    ```
2.  Navigate into the project directory:
    ```sh
    cd honeypot-ransomware-detector
    ```
    No further installation is needed!

### Usage

1.  Open `honeypot_detector.py` and change the `DIRECTORY_TO_PROTECT` variable to a test directory path.
2.  Run the script from your terminal:
    ```sh
    python honeypot_detector.py
    ```
3.  The script will create the decoy files and begin monitoring.
4.  To test it, **modify or delete one of the honeypot files** (any file starting with `~`). This will trigger the alert.

---

## 📋 Example Output

When a honeypot file is modified, you will see an immediate alert like this:
