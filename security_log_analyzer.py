def load_logs():
    with open("security_log.txt", "r") as file:
        logs = file.readlines()
        return logs

def analyze_logs(logs):
    successful_logins = 0
    failed_attempts = 0
    failed_users = {}

    for log in logs:
        parts = log.split()

        if "SUCCESS" in log:
            successful_logins += 1
            
        if "FAILED" in log:
            failed_attempts += 1
            username = parts[3]
            if username in failed_users:
                failed_users[username] += 1
            else:
                failed_users[username] = 1
    return successful_logins, failed_attempts, failed_users

def show_report(successful_logins, failed_attempts, failed_users):
    print("\n===== SECURITY LOG REPORT =====")
    print("Successful logins:", successful_logins)

    print("\nFailed attempts by user:")
    for username, count in failed_users.items():
        print(f"{username} -> {count} failed attempt(s)")

    suspicious_users = 0

    print("\nUser Security Status:")

    for username, count in failed_users.items():
        if count >= 3:
            print(f"⚠ {username} 'n SUSPICIOUS: {count} failed attempts!")
            suspicious_users += 1
        else:
            print(f"✔ {username} 'n Normal: {count} failed attempt(s)")

    print("\nSuspicious users:", suspicious_users)

    if suspicious_users > 0:
        print("Overall status: REVIEW REQUIRED")
    else:
        print("Overall status: NORMAL")

def main():
    logs = load_logs()

    successful_logins, failed_attempts, failed_users = analyze_logs(logs)
 
    show_report(successful_logins, 
                failed_attempts, 
                failed_users
    )

main()
