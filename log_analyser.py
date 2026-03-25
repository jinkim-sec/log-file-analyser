import re
from collections import Counter

def analyse_log(filepath):
    failed_logins = []
    ip_pattern = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')
    
    try:
        with open(filepath, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        return

    for line in lines:
        if 'failed' in line.lower() or 'invalid' in line.lower():
            ips = ip_pattern.findall(line)
            failed_logins.extend(ips)

    if not failed_logins:
        print("No failed login attempts found.")
        return

    print(f"\nTotal failed login attempts: {len(failed_logins)}")
    print("\nTop suspicious IPs:")
    
    for ip, count in Counter(failed_logins).most_common(5):
        print(f"  {ip} — {count} attempts")

if __name__ == "__main__":
    path = input("Enter log file path: ")
    analyse_log(path)
