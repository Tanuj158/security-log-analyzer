# Security Log Analyzer
# Detect accounts with multiple failed login attempts

failed_logins = {}
failed_ips = {}


with open("auth.log", "r") as file:
	for line in file:
		if line.startswith("Failed password for "):
			username = line.split()[3]
			failed_logins[username] = failed_logins.get(username, 0) + 1


			ip_address = line.split()[5]
			failed_ips[ip_address] = failed_ips.get(ip_address, 0) + 1



def detect_failed_logins(logins):
	for user, count in logins.items():
		if count >= 3:
           		 print(f"ALERT: {user} has {count} failed login attempts")



detect_failed_logins(failed_logins)


def detect_suspicious_ips(ip_counts):
	for ip, count in ip_counts.items():
		if count >= 3:
			print(f"ALERT: IP {ip} has {count} failed login attempts")


detect_suspicious_ips(failed_ips)
