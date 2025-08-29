import os
import hashlib
import time
import random

# --- CONFIGURATION ---
# The directory you want to protect.
# WARNING: CHOOSE A TEST DIRECTORY FIRST.
DIRECTORY_TO_PROTECT = "path/to/your/test_folder"

# How many decoy files to create.
HONEYPOT_COUNT = 10

# How many seconds to wait between checks.
SCAN_INTERVAL_SECONDS = 5
# --- END CONFIGURATION ---

def calculate_hash(filepath):
    """Calculates the SHA-256 hash of a file."""
    sha256_hash = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
            return sha256_hash.hexdigest()
    except (IOError, PermissionError):
        return None

def setup_honeypots(directory):
    """Creates decoy files and returns a dictionary of their paths and initial hashes."""
    honeypots = {}
    print(f"[*] Setting up {HONEYPOT_COUNT} honeypot files in '{directory}'...")
    
    # Common file names and extensions to appear legitimate
    file_names = ["document", "report", "data", "archive", "important", "private_key"]
    extensions = ["txt", "docx", "pdf", "xlsx", "jpg"]

    for i in range(HONEYPOT_COUNT):
        name = f"~{random.choice(file_names)}_{i}.{random.choice(extensions)}"
        filepath = os.path.join(directory, name)
        
        try:
            with open(filepath, "w") as f:
                f.write(f"This is a decoy file. Do not modify or delete. Timestamp: {time.time()}")
            
            file_hash = calculate_hash(filepath)
            if file_hash:
                honeypots[filepath] = file_hash
                print(f"[+] Created honeypot: {filepath}")
        except (IOError, PermissionError) as e:
            print(f"[-] Could not create honeypot file: {filepath}. Error: {e}")
            
    return honeypots

def monitor_honeypots(honeypots):
    """Monitors the honeypot files for any changes."""
    if not honeypots:
        print("[E] No honeypots were created. Exiting.")
        return

    print("\n[*] Honeypot monitoring started. Press CTRL+C to stop.")
    while True:
        for filepath, original_hash in honeypots.items():
            if not os.path.exists(filepath):
                trigger_alert(f"Honeypot file was deleted or renamed: {filepath}")
                return # Stop monitoring after an alert

            current_hash = calculate_hash(filepath)
            if current_hash != original_hash:
                trigger_alert(f"Honeypot file was modified (encrypted?): {filepath}")
                return # Stop monitoring after an alert
        
        time.sleep(SCAN_INTERVAL_SECONDS)

def trigger_alert(reason):
    """Prints a high-priority alert."""
    print("\n" + "="*60)
    print("  🚨🚨🚨 RANSOMWARE ALERT! IMMEDIATE ACTION REQUIRED! 🚨🚨🚨")
    print("="*60)
    print(f"\n  REASON: {reason}")
    print("\n  A decoy 'honeypot' file was modified or deleted.")
    print("  This is a strong indicator of a ransomware attack in progress.")
    print("  RECOMMENDATION: Disconnect this machine from the network immediately.")
    print("="*60)

if __name__ == "__main__":
    if not os.path.isdir(DIRECTORY_TO_PROTECT):
        print(f"[E] Error: The directory '{DIRECTORY_TO_PROTECT}' does not exist.")
    else:
        honeypot_baseline = setup_honeypots(DIRECTORY_TO_PROTECT)
        try:
            monitor_honeypots(honeypot_baseline)
        except KeyboardInterrupt:
            print("\n[+] Monitoring stopped by user.")
