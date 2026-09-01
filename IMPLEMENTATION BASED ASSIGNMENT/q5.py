# Q5 - Evidence Validation

baseline = {
    "backup_schedule.txt": "AAA111",
    "hr_policies.docx": "BBB222",
    "payroll_master.xlsx": "CCC333",
    "finance_report_q1.pdf": "DDD444",
    "system_config.ini": "EEE555"
}

current = {
    "backup_schedule.txt": "AAA111",
    "hr_policies.docx": "BBB222",
    "payroll_master.xlsx": "CCC999",
    "system_config.ini": "EEE555",
    "svc_update.exe": "NEW777"
}

print("=" * 70)
print("BASELINE VS CURRENT SNAPSHOT VALIDATION")
print("=" * 70)

all_files = sorted(set(baseline) | set(current))

for file in all_files:

    if file in baseline and file in current:

        if baseline[file] == current[file]:
            status = "UNCHANGED"
        else:
            status = "MODIFIED"

    elif file in current:
        status = "NEW"

    else:
        status = "MISSING"

    print(f"{file:<30} : {status}")

print("\nResult:")
print("Evidence snapshot validation completed.")