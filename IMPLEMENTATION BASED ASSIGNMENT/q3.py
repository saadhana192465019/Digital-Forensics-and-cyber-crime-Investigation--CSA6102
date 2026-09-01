# Q3 - Chain of Custody

from datetime import datetime

custody = []

def add_custody(evidence_id, handler, action, purpose, timestamp):
    custody.append({
        "evidence_id": evidence_id,
        "handler": handler,
        "action": action,
        "purpose": purpose,
        "timestamp": timestamp
    })

# Add custody records
add_custody(
    "EVD-001",
    "A. Kumar",
    "Collected",
    "Initial evidence collection",
    "2026-03-11 09:15:00"
)

add_custody(
    "EVD-001",
    "A. Kumar",
    "Transferred",
    "Placed in evidence locker",
    "2026-03-11 09:40:00"
)

add_custody(
    "EVD-001",
    "S. Rao",
    "Examined",
    "Forensic examination",
    "2026-03-12 14:00:00"
)

add_custody(
    "EVD-001",
    "S. Rao",
    "Returned",
    "Returned to evidence locker",
    "2026-03-12 17:30:00"
)

print("=" * 75)
print("CHAIN OF CUSTODY - EVD-001")
print("=" * 75)

for c in custody:
    print(
        c["timestamp"], "|",
        c["handler"], "|",
        c["action"], "|",
        c["purpose"]
    )

print("\nResult:")
print("Complete chain-of-custody history recorded successfully.")