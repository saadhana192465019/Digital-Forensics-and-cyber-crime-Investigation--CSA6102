# Q8 - Forensic Report Generation

from datetime import datetime

report = f"""
======================================================================
              DIGITAL FORENSIC EXAMINATION REPORT
======================================================================

CASE INFORMATION
----------------------------------------------------------------------
Case ID           : CASE-2026-0311
Investigator      : A. Kumar
System            : WKSTN-14
Report Date       : {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

EVIDENCE EXAMINED
----------------------------------------------------------------------
EVD-001 : WKSTN-14 Disk Image
EVD-002 : WKSTN-14 RAM Capture
EVD-003 : Authentication Log
EVD-004 : Network Log

CHAIN OF CUSTODY
----------------------------------------------------------------------
EVD-001 : Collection -> Storage -> Examination -> Return

FACTUAL FINDINGS
----------------------------------------------------------------------
1. Multiple failed login attempts were recorded.
2. A successful login followed the failed attempts.
3. svc_update.exe was created.
4. payroll_master.xlsx was modified.
5. finance_report_q1.pdf was deleted.
6. Outbound network connections were recorded.
7. Large data transfer activity was observed.

INTEGRITY
----------------------------------------------------------------------
SHA-256 verification was performed on the evidence.
Evidence integrity was verified when recorded and examination
hashes matched.

EVIDENCE VALIDATION
----------------------------------------------------------------------
payroll_master.xlsx       : MODIFIED
finance_report_q1.pdf     : MISSING
svc_update.exe             : NEW

CONCLUSION
----------------------------------------------------------------------
The available evidence is consistent with an external account
compromise followed by unauthorized file activity and possible
data exfiltration.

The earliest suspicious activity was the sequence of failed
authentication attempts followed by a successful login.

MANDATORY FIELD CHECK
----------------------------------------------------------------------
All required evidence fields are present.

======================================================================
END OF REPORT
======================================================================
"""

print(report)

with open("CSA61_Forensic_Report.txt", "w") as f:
    f.write(report)

print("\nReport saved as: CSA61_Forensic_Report.txt")