
import hashlib
import time
from pathlib import Path

# FILE INTEGRITY MONITOR
# Cybersecurity Project using SHA-256

TARGET_FILE = Path("important.txt")
HASH_FILE = Path("file_hash.txt")


def calculate_hash(file_path):
    sha256 = hashlib.sha256()

    try:
        with open(file_path, "rb") as file:
            for chunk in iter(lambda: file.read(4096), b""):
                sha256.update(chunk)

        return sha256.hexdigest()

    except FileNotFoundError:
        return None


def initialize_monitor():
    if not TARGET_FILE.exists():
        print("\n[ERROR] important.txt not found!")
        return

    file_hash = calculate_hash(TARGET_FILE)

    HASH_FILE.write_text(file_hash)

    print("\n[SUCCESS] Monitoring initialized!")
    print("File:", TARGET_FILE)
    print("SHA-256:", file_hash)


def check_integrity():
    if not HASH_FILE.exists():
        print("\n[ERROR] Initialize monitoring first!")
        return

    current_hash = calculate_hash(TARGET_FILE)

    if current_hash is None:
        print("\n[ALERT] Target file is missing!")
        return

    original_hash = HASH_FILE.read_text().strip()

    print("\n[INFO] Checking file integrity...")

    if current_hash == original_hash:
        print("[SAFE] File is unchanged.")
        print("[STATUS] Integrity verified.")

    else:
        print("[WARNING] FILE MODIFICATION DETECTED!")
        print("[ALERT] File integrity compromised.")
        print("Original hash:", original_hash)
        print("Current hash:", current_hash)


def continuous_monitor():
    if not HASH_FILE.exists():
        print("\n[ERROR] Initialize monitoring first!")
        return

    print("\n[MONITORING] Continuous monitoring started.")
    print("Press CTRL+C to stop.\n")

    try:
        while True:
            current_hash = calculate_hash(TARGET_FILE)
            original_hash = HASH_FILE.read_text().strip()

            if current_hash is None:
                print("[ALERT] Target file is missing!")
            elif current_hash != original_hash:
                print("\n[ALERT] FILE MODIFICATION DETECTED!")
                print("[WARNING] Integrity compromised.")
                break
            else:
                print("[SAFE] No changes detected.")

            time.sleep(3)

    except KeyboardInterrupt:
        print("\n[STOPPED] Monitoring stopped.")


def main():
    while True:
        print("\n" + "=" * 45)
        print("       FILE INTEGRITY MONITOR")
        print("=" * 45)

        print("1. Initialize Monitoring")
        print("2. Check File Integrity")
        print("3. Continuous Monitoring")
        print("4. Exit")

        choice = input("\nEnter your choice (1-4): ")

        if choice == "1":
            initialize_monitor()

        elif choice == "2":
            check_integrity()

        elif choice == "3":
            continuous_monitor()

        elif choice == "4":
            print("\nThank you for using File Integrity Monitor!")
            break

        else:
            print("\n[ERROR] Invalid choice. Try again.")


if __name__ == "__main__":
    main()
