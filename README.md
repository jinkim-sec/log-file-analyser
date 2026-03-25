# Log File Analyser

A Python tool that parses log files to detect failed 
login attempts and identify suspicious IP addresses. 
Built as part of a cybersecurity learning portfolio 
to demonstrate basic log analysis and threat detection.

## Features
- Detects failed login attempts from log files
- Identifies and ranks suspicious IP addresses
- Displays top 5 most active suspicious IPs

## Requirements
- Python 3.x
- No external libraries required

## Usage
```bash
python log_analyser.py
```
Enter the path to your log file when prompted.

## Sample Data
A sample log file is provided in the `sample_data/` 
folder for testing purposes.
```bash
python log_analyser.py
Enter log file path: sample_data/sample_log.txt
```

## Example Output
```
Total failed login attempts: 6

Top suspicious IPs:
  192.168.1.1 — 3 attempts
  10.0.0.5 — 2 attempts
  172.16.0.3 — 1 attempt
```

## Disclaimer
This tool is for educational purposes only.
Only use on log files you own or have explicit 
permission to analyse.

## Author
Jin Hyuck Kim
