# Q9 - Reflection

reflection = """
CSA61 REFLECTION

The Campus Digital Forensics Evidence Management and Incident
Reconstruction System was designed as a simple Python application
to demonstrate the digital forensic evidence lifecycle. Python was
selected because it provides useful built-in modules for file
handling, SHA-256 hashing, CSV processing and timestamp handling.

The system registers evidence using unique evidence IDs and stores
important information such as source, investigator, acquisition
time and storage location. SHA-256 hashing is used to verify that
evidence has not changed between acquisition and examination. The
chain-of-custody component records every transfer and examination
event so that the complete history of an evidence item can be
reconstructed.

The evidence validation component compares a trusted baseline with
a later snapshot. This allows modified, missing, new and unchanged
files to be identified. Authentication, file activity and network
events are merged into one chronological timeline. This makes it
possible to understand the sequence of activity and identify the
earliest suspicious event.

The project has real-world and legal relevance because digital
evidence must be preserved carefully and its integrity should be
demonstrable. Separating factual findings from investigator
interpretation also improves the clarity of a forensic report.

The project supports SDG 9 by promoting secure and resilient digital
infrastructure. It supports SDG 16 through trustworthy institutions,
accountability and reliable evidence handling. It supports SDG 17
because effective incident investigation requires cooperation among
security teams, investigators and other stakeholders.

The main challenges were maintaining consistent timestamps,
preserving evidence hashes and correlating events from different
sources. Through this implementation, I learned how evidence
registration, hashing, custody tracking, validation, timeline
reconstruction and forensic reporting work together in a complete
digital forensic investigation.
"""

print("=" * 70)
print("REFLECTION")
print("=" * 70)
print(reflection)

with open("CSA61_Reflection.txt", "w") as f:
    f.write(reflection)

print("\nReflection saved as: CSA61_Reflection.txt")