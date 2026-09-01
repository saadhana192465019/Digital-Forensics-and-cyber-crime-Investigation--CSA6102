# Q6 - Multi-Source Timeline Reconstruction

from datetime import datetime

auth_log = [
    ("2026-03-11 23:58:02", "AUTH", "FAILED_LOGIN from 203.0.113.44"),
    ("2026-03-11 23:58:11", "AUTH", "FAILED_LOGIN from 203.0.113.44"),
    ("2026-03-11 23:58:19", "AUTH", "FAILED_LOGIN from 203.0.113.44"),
    ("2026-03-11 23:58:52", "AUTH", "SUCCESSFUL_LOGIN for jsmith")
]

file_log = [
    ("2026-03-12 00:18:05", "FILE", "CREATED svc_update.exe"),
    ("2026-03-12 00:19:12", "FILE", "MODIFIED payroll_master.xlsx"),
    ("2026-03-12 00:20:47", "FILE", "DELETED finance_report_q1.pdf")
]

network_log = [
    ("2026-03-12 00:22:05", "NETWORK",
     "Outbound connection to 198.51.100.77:4444"),
    ("2026-03-12 00:23:40", "NETWORK",
     "Large data transfer to 198.51.100.77")
]

timeline = auth_log + file_log + network_log

timeline.sort(
    key=lambda x: datetime.strptime(
        x[0], "%Y-%m-%d %H:%M:%S"
    )
)

print("=" * 90)
print("MULTI-SOURCE INCIDENT TIMELINE")
print("=" * 90)

for event in timeline:
    print(
        event[0],
        "|",
        event[1],
        "|",
        event[2]
    )

print("\nResult:")
print("Authentication, file and network events merged successfully.")