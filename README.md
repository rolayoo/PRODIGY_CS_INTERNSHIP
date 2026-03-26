🛡️ Prodigy InfoTech: Cybersecurity Internship Portfolio
Author: Morolayo Jaiyeola 

Role: Cybersecurity Intern

Duration: March 2026

Focus: Cryptography, Network Security, & Ethical Hacking

📋 Executive Summary
This repository serves as a comprehensive technical portfolio documenting the successful completion of five core cybersecurity tasks during my tenure at Prodigy InfoTech. The projects transition from fundamental cryptographic algorithms to active network traffic analysis and system monitoring, demonstrating a multi-layered understanding of the Cyber Security landscape.

🛠️ Technical Deep Dive
Task 01: Caesar Cipher Algorithm
Objective: Develop a tool to perform character-level encryption using modular arithmetic.

Technology: Python 3.x

How it Works: The script iterates through a string, shifting each character's ASCII value by a user-defined key while maintaining case sensitivity and ignoring non-alphabetic symbols.

Key Logic: (char_index + shift) % 26

Task 02: Image Encryption Tool
Objective: Securely manipulate image pixel data to prevent unauthorized viewing.

Technology: Python, Pillow (PIL)

Advanced Implementation: Switched from basic addition to Bitwise XOR (Exclusive OR) encryption. XOR is a symmetric cipher; applying the same key twice perfectly restores the data.

Result: Transforms images into "colored noise" static that is visually unreadable without the numeric key.

Task 03: Password Complexity Checker
Objective: Implement a policy-based validation tool for credential security.

Technology: Python, re (Regular Expressions)

Metrics Tracked:

Minimum Length (8+ chars)

Presence of Uppercase (A-Z)

Presence of Lowercase (a-z)

Numeric Content (0-9)

Special Characters (@, #, $, etc.)

Task 04: Basic Keylogger
Objective: Explore the mechanics of keystroke logging and event listening.

Technology: Python, pynput.keyboard

Functionality: Captures hardware input events in real-time and logs them to a local hidden text file (keylog.txt).

Ethical Context: This task demonstrates how attackers capture sensitive data like credentials via background processes.

Task 05: Network Packet Sniffer
Objective: Analyze live network traffic to understand protocol headers and routing.

Technology: Python, Scapy, Npcap

Capability: Intercepts raw packets on the Network Interface Card (NIC), parsing the IP Layer (Source/Destination) and the Transport Layer (TCP/UDP).

Learning Outcome: Gained insight into the structure of TCP payloads and how data travels across local networks.

🖥️ Installation & Environment Setup
To replicate these security tools in a controlled lab environment:

Clone the Repository:

Bash
git clone https://github.com/[YOUR_USERNAME]/PRODIGY_CS_INTERNSHIP.git
cd PRODIGY_CS_INTERNSHIP
Install System Dependencies (Windows):

Install Python 3.10+.

Install Npcap (required for Task 05) from npcap.com.

Install Python Libraries:

Bash
python -m pip install Pillow pynput scapy
🔐 Ethical Disclaimer & Usage
These tools were developed strictly for educational research and to better understand defensive security posture.

Unauthorized Access: Running these tools on networks or devices you do not own is strictly prohibited.

Safety: Task 04 and Task 05 may be flagged by Antivirus software as they mimic malware behaviors. Use a dedicated lab environment or VM for testing.

📈 Next Steps
Following this internship, I am leveraging these skills to:

Develop technical deep-dives for my blog, Tech Support HQ.

Create cybersecurity awareness content for The Cyber Desk (YouTube).

Volunteer as a Cybersecurity instructor to help students in Lagos understand digital safety.