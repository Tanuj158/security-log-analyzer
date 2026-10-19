# Python Security Log Analyzer


## Project Overview

A Python-based cybersecurity tool that analyzes simulated
authentication logs to identify repeated failed login attempts.

The tool tracks failed login attempts by username and source
IP address and generates security alerts when three or more
failed attempts are detected.


## Features

- Reads authentication events from a log file.
- Identifies failed login attempts.
- Extracts usernames and source IP addresses.
- Counts failed login attempts for each username.
- Counts failed login attempts for each IP address.
- Generates alerts when failed attempts reach three.


## Technologies Used

- Python 3
- Fedora Linux
- Git
- GitHub
- Nano Text Editor


## Project Structure

```text
security-log-analyzer/
├── log_analyzer.py
├── auth.log
└── README.md
```


## How to Run

### Prerequisites

- Python 3 installed on your system.
- Git installed for cloning the repository.

### Run the Analyzer

Open a terminal and navigate to the project directory:

```bash
cd security-log-analyzer
```

Run the Python script:

```bash
python3 log_analyzer.py
```


## Expected Output

When the analyzer processes the sample authentication logs,
it generates the following security alerts:

```text
ALERT: admin has 3 failed login attempts
ALERT: IP 192.168.1.10 has 3 failed login attempts
```


## Security Notes

- This project uses simulated authentication logs for educational purposes.
- Failed login alerts indicate potentially suspicious activity, not confirmed attacks.
- The analyzer uses a fixed threshold of three failed login attempts.
- The current implementation does not analyze login attempts within a specific time window.
- The tool is intended for learning and is not a production-ready security monitoring system.


