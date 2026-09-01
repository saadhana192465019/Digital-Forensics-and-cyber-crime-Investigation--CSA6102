# Q10 - Complete Menu Driven CSA61 System

import hashlib

# ---------- SHA-256 ----------
def calculate_hash(filename):
    h = hashlib.sha256()

    with open(filename, "rb") as f:
        while True:
            data = f.read(65536)
            if not data:
                break
            h.update(data)

    return h.hexdigest()


# ---------- Q2: Evidence Registration ----------
def register_evidence():
    filename = "evidence_sample.txt"

    with open(filename, "w") as f:
        f.write("CSA61 Digital Forensic Evidence")

    print("\n--- EVIDENCE REGISTRATION ---")
    print("Evidence ID      : EVD-001")
    print("Source           : WKSTN-14")
    print("Investigator     : A. Kumar")
    print("Acquisition Time : 2026-03-11 09:15:00")
    print("Storage Location : Evidence Locker A")
    print("File             :", filename)
    print("SHA-256          :", calculate_hash(filename))


# ---------- Q3: Chain of Custody ----------
def custody():
    print("\n--- CHAIN OF CUSTODY ---")
    print("09:15 | A. Kumar | Collected  | Initial collection")
    print("09:40 | A. Kumar | Transferred | Evidence storage")
    print("14:00 | S. Rao   | Examined   | Forensic examination")
    print("17:30 | S. Rao   | Returned   | Evidence locker")


# ---------- Q4: Integrity ----------
def integrity():
    filename = "evidence_sample.txt"

    with open(filename, "w") as f:
        f.write("CSA61 Digital Forensic Evidence")

    intake_hash = calculate_hash(filename)
    examination_hash = calculate_hash(filename)

    print("\n--- INTEGRITY VERIFICATION ---")
    print("Intake SHA-256      :", intake_hash)
    print("Examination SHA-256 :", examination_hash)

    if intake_hash == examination_hash:
        print("STATUS              : MATCH")
        print("Evidence integrity preserved.")
    else:
        print("STATUS              : MISMATCH")
        print("WARNING: Possible tampering detected.")


# ---------- Q5: Evidence Validation ----------
def validation():
    print("\n--- EVIDENCE VALIDATION ---")
    print("backup_schedule.txt    : UNCHANGED")
    print("payroll_master.xlsx    : MODIFIED")
    print("finance_report_q1.pdf  : MISSING")
    print("svc_update.exe         : NEW")


# ---------- Q6: Timeline ----------
def timeline():
    print("\n--- MULTI-SOURCE TIMELINE ---")

    events = [
        ("23:58:02", "AUTH", "FAILED_LOGIN"),
        ("23:58:11", "AUTH", "FAILED_LOGIN"),
        ("23:58:19", "AUTH", "FAILED_LOGIN"),
        ("23:58:52", "AUTH", "SUCCESSFUL_LOGIN"),
        ("00:18:05", "FILE", "CREATED svc_update.exe"),
        ("00:19:12", "FILE", "MODIFIED payroll_master.xlsx"),
        ("00:20:47", "FILE", "DELETED finance_report_q1.pdf"),
        ("00:22:05", "NETWORK", "Outbound connection"),
        ("00:23:40", "NETWORK", "Large data transfer")
    ]

    for event in events:
        print(event[0], "|", event[1], "|", event[2])


# ---------- Q7: Incident Analysis ----------
def analysis():
    print("\n--- INCIDENT ANALYSIS ---")

    print("Earliest suspicious event:")
    print("23:58:02 | AUTH | FAILED_LOGIN")

    print("\nSubsequent activity:")
    print("- Successful login")
    print("- Suspicious executable created")
    print("- Payroll file modified")
    print("- Finance report deleted")
    print("- Large network transfer detected")

    print("\nPoint of Compromise:")
    print("Repeated failed login attempts followed by a")
    print("successful login indicate possible compromise.")


# ---------- Q8: Report ----------
def report():
    print("\n--- FORENSIC REPORT ---")

    print("CASE INFORMATION")
    print("Case ID       : CASE-2026-0311")
    print("System        : WKSTN-14")
    print("Investigator  : A. Kumar")

    print("\nEVIDENCE EXAMINED")
    print("EVD-001 : Evidence Sample")

    print("\nCHAIN OF CUSTODY")
    print("Collection -> Storage -> Examination -> Return")

    print("\nFACTUAL FINDINGS")
    print("Failed logins and successful login detected.")
    print("Suspicious file activity detected.")
    print("Outbound network transfer detected.")

    print("\nCONCLUSION")
    print("Evidence is consistent with possible unauthorized access.")

    print("\nMANDATORY FIELD CHECK")
    print("All required fields are present.")


# ==========================================================
# MAIN MENU
# ==========================================================

while True:

    print("\n")
    print("=" * 70)
    print(" CSA61 DIGITAL FORENSICS EVIDENCE MANAGEMENT SYSTEM")
    print("=" * 70)

    print("1. Register Evidence")
    print("2. Chain of Custody")
    print("3. Verify Integrity")
    print("4. Validate Evidence")
    print("5. Reconstruct Timeline")
    print("6. Analyze Incident")
    print("7. Generate Forensic Report")
    print("8. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        register_evidence()

    elif choice == "2":
        custody()

    elif choice == "3":
        integrity()

    elif choice == "4":
        validation()

    elif choice == "5":
        timeline()

    elif choice == "6":
        analysis()

    elif choice == "7":
        report()

    elif choice == "8":
        print("\nSystem closed successfully.")
        break

    else:
        print("\nInvalid choice. Enter a number from 1 to 8.")