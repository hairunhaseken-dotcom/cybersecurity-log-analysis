
import csv
import sys
from collections import Counter

THRESHOLD = 3


def analyze_logs(filename):
    failed_attempts = Counter()
    total_records = 0

    try:
        with open(filename, "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)

            for row in reader:
                if len(row) != 3:
                    print("Skipping invalid record:", row)
                    continue

                timestamp, ip_address, status = [
                    value.strip() for value in row
                ]

                if status not in ("SUCCESS", "FAILED"):
                    print("Skipping unknown status:", status)
                    continue

                total_records += 1

                if status == "FAILED":
                    failed_attempts[ip_address] += 1

    except FileNotFoundError:
        print("Error: Log file not found:", filename)
        return

    print("CYBERSECURITY LOG ANALYSIS")
    print("--------------------------")
    print("Total valid records:", total_records)
    print("Unique IP addresses:", len(failed_attempts))

    print("\nFailed login attempts:")
    if not failed_attempts:
        print("No failed login attempts found.")
    else:
        for ip_address, count in sorted(failed_attempts.items()):
            print(f"{ip_address}: {count}")

    print("\nIP addresses flagged for review:")
    flagged = [
        (ip, count)
        for ip, count in failed_attempts.items()
        if count >= THRESHOLD
    ]

    if flagged:
        for ip_address, count in sorted(flagged):
            print(
                f"WARNING: {ip_address} has {count} failed attempts."
            )
    else:
        print("No IP addresses reached the threshold.")

    print("\nAnalysis complete.")
    print("A flagged address is not proof of an attack.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python analyze_logs.py sample_logs.txt")
    else:
        analyze_logs(sys.argv[1])
