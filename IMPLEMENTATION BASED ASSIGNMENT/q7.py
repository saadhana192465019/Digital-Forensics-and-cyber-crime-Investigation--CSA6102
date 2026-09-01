# Q7 - Artifact Analysis and Point of Compromise

from datetime import datetime

# Create timeline data again
timeline = [
    ("2026-03-11 23:58:02", "AUTH",
     "FAILED_LOGIN from 203.0.113.44"),

    ("2026-03-11 23:58:11", "AUTH",
     "FAILED_LOGIN from 203.0.113.44"),

    ("2026-03-11 23:58:19", "AUTH",
     "FAILED_LOGIN from 203.0.113.44"),

    ("2026-03-11 23:58:52", "AUTH",
     "SUCCESSFUL_LOGIN for jsmith"),

    ("2026-03-12 00:18:05", "FILE",
     "CREATED svc_update.exe"),

    ("2026-03-12 00:19:12", "FILE",
     "MODIFIED payroll_master.xlsx"),

    ("2026-03-12 00:20:47", "FILE",
     "DELETED finance_report_q1.pdf"),

    ("2026-03-12 00:22:05", "NETWORK",
     "Outbound connection to 198.51.100.77:4444"),

    ("2026-03-12 00:23:40", "NETWORK",
     "Large data transfer to 198.51.100.77")
]

# Sort timeline
timeline.sort(
    key=lambda x: datetime.strptime(
        x[0], "%Y-%m-%d %H:%M:%S"
    )
)

print("=" * 75)
print("ARTIFACT ANALYSIS AND POINT OF COMPROMISE")
print("=" * 75)

# Find suspicious events
suspicious_events = []

for event in timeline:
    description = event[2].upper()

    if any(word in description for word in [
        "FAILED_LOGIN",
        "SUCCESSFUL_LOGIN",
        "CREATED",
        "MODIFIED",
        "DELETED",
        "OUTBOUND",
        "TRANSFER"
    ]):
        suspicious_events.append(event)

# Earliest suspicious event
earliest = suspicious_events[0]

print("\nEarliest Suspicious Event:")
print(earliest[0], "|", earliest[1], "|", earliest[2])

print("\nSubsequent Related Activity:")

for event in suspicious_events[1:]:
    print(event[0], "|", event[1], "|", event[2])

print("\nPoint of Compromise:")
print("Repeated failed login attempts were the earliest suspicious activity.")
print("A successful login was followed by unauthorized file activity")
print("and outbound network communication.")

print("\nEvidence Used:")
print("- Authentication logs")
print("- File activity logs")
print("- Network logs")

print("\nResult:")
print("Artifact analysis and point-of-compromise identification completed.")