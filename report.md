# Cybersecurity Log Analysis Report

## 1. Objective
The objective of this project is to analyse fictional login
records and identify repeated failed login attempts.

## 2. Tools
- Python 3.11
- Windows 11
- GitHub

## 3. Method
The Python program reads a text file containing timestamps,
IP addresses, and login statuses. It counts failed attempts
for each IP address and flags addresses with three or more
failed attempts.

## 4. Findings
The sample dataset contains eight login records.
The address 203.0.113.25 has three failed login attempts.
The address 198.51.100.8 has two failed login attempts.

## 5. Recommendations
- Review repeated failed login attempts.
- Check related authentication events.
- Apply multi-factor authentication where appropriate.
- Monitor unusual login activity.

## 6. Limitations
The records are fictional and the detection threshold is fixed.
A flagged IP address does not prove malicious activity.
More evidence is required before confirming a security incident.

## 7. Learning Reflection
This project helped me practise basic Python, file processing,
data analysis, and security monitoring concepts.
