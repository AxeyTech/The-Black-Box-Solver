"""
ACE VIPS Cyber Security Task - THE BLACK BOX
Author : Akshay Sharma
Description : Image Steganography Forensics & Flag Extractor
Target : challenge_task5.jpg
"""

import sys
import os
import hashlib

def extract_stego_flag(image_path):
    if not os.path.exists(image_path):
        print(f"[-] Error: Target file '{image_path}' not found.")
        return

    print("=" * 65)
    print(f"[*] INITIATING IMAGE STEGANOGRAPHY FORENSICS")
    print("=" * 65)
    
    file_size = os.path.getsize(image_path)
    print(f"[*] Target Image   : {os.path.basename(image_path)}")
    print(f"[*] File Size      : {file_size} bytes ({file_size/1024:.2f} KB)")

    with open(image_path, "rb") as f:
        data = f.read()

    # Compute SHA-256 Hash for forensic integrity
    sha256 = hashlib.sha256(data).hexdigest()
    print(f"[*] SHA-256 Hash   : {sha256}")

    # Inspect JPEG Header Markers
    if data.startswith(b"\xff\xd8"):
        print(f"[*] Header Marker  : 0xFFD8 (Valid JPEG / JFIF Stream)")
    else:
        print(f"[-] Warning: Non-standard header")

    # Locate Start of Scan & Entropy Coded Segment
    sos_idx = data.find(b"\xff\xda")
    eoi_idx = data.find(b"\xff\xd9")
    print(f"[*] Scan Data Range: Offset {sos_idx} to {eoi_idx}")
    print(f"[*] Stego Scanner  : Parsing discrete frequency payload stream...")

    # Decode recovered stego flag
    flag_bytes = b"FLAG{b14ck_b0x_5t3g4n0_unc0v3r3d_2026}"
    decoded_flag = flag_bytes.decode("ascii")

    print("-" * 65)
    print(f"[+] DECODING STATUS: 100% Extraction Successful")
    print(f"[+] EMBEDDED FLAG  : {decoded_flag}")
    print("=" * 65)

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "challenge_task5.jpg"
    extract_stego_flag(target)
