-> The Black Box Solver - ACE VIPS Cybersecurity Assessment
Automated forensic steganography extraction script developed for the ACE VIPS Selection Assessment (Task 5 - The Black Box).

---- Challenge Overview ----
- Task: The Black Box (Hard)
- Domain: Cybersecurity / Digital Forensics / Steganography
- Target File: challenge_task5.jpg
- Objective: Analyze the file structure and extract the hidden flag appended beyond standard image markers.

---- How It Works (Forensic Methodology) ---- 
Standard JPEG images terminate at the EOI (End of Image) hex marker:
FF D9

Threat actors and CTF creators often hide arbitrary payloads by appending data directly after this marker (trailing data injection). This Python script:
1. Reads challenge_task5.jpg in raw binary mode.
2. Locates the last occurrence of the JPEG EOI marker (\xFF\xD9).
3. Carves out all trailing appended bytes.
4. Locates and decodes the hidden ASCII flag sequence.

---- How to Run ---- 
1. Clone or download this repository.
2. Ensure challenge_task5.jpg is in the same directory as extract_flag.py.
3. Run the script using Python:
   python extract_flag.py

---- Flag Recovered ---- 
FLAG{b14ck_b0x_5t3g4n0_unc0v3r3d_2026}
