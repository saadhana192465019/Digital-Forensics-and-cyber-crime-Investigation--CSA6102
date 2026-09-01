# Q4 - Integrity Verification

import hashlib

def calculate_hash(filename):
    h = hashlib.sha256()

    with open(filename, "rb") as f:
        while True:
            data = f.read(65536)
            if not data:
                break
            h.update(data)

    return h.hexdigest()

# Create original evidence
filename = "integrity_test.txt"

with open(filename, "w") as f:
    f.write("Original forensic evidence")

# Intake hash
intake_hash = calculate_hash(filename)

# Examination hash
examination_hash = calculate_hash(filename)

print("=" * 60)
print("EVIDENCE INTEGRITY VERIFICATION")
print("=" * 60)

print("Intake SHA-256      :", intake_hash)
print("Examination SHA-256 :", examination_hash)

if intake_hash == examination_hash:
    print("\nSTATUS: MATCH")
    print("Evidence integrity preserved.")
else:
    print("\nSTATUS: MISMATCH")
    print("WARNING: Possible tampering detected.")

print("\nResult:")
print("SHA-256 integrity verification completed.")