# MAHESH-KARTHICK-M-111925CB01030
Week 01 – Cybersecurity Asset Inventory System
A command-line Python application that lets a security administrator add, search, update, delete, and display an organization's IT assets (workstations, servers, routers, switches, applications), and view a live security summary.
Features
Add new assets with input validation (asset type, IP address, risk level, security status)
Display all assets in a clean, formatted report
Search for a specific asset by Asset ID
Update any field of an existing asset
Delete an asset (with confirmation prompt)
Automatic security summary: total assets, counts by risk level, and vulnerable/warning/secure counts
Data persists between runs in data/assets.json
Project Structure
Week-01-Cybersecurity-Asset-Inventory/
│
├── src/
│   └── asset_inventory.py     # main program
│
├── data/
│   └── assets.json            # persisted asset data (pre-seeded with sample assets)
│
├── tests/
│   └── test_cases.md          # manual test case checklist
│
├── screenshots/               # add your own run screenshots here
│
└── README.md
Requirements
Python 3.7+
No external dependencies (uses only the standard library: json, os, re)
How to Run
cd src
python asset_inventory.py
Sample Menu
=========================================
   CYBERSECURITY ASSET INVENTORY SYSTEM
=========================================
1. Add Asset
2. Display All Assets
3. Search Asset
4. Update Asset
5. Delete Asset
6. Security Summary
7. Exit
=========================================
Field Definitions
Field
Allowed Values
Asset Type
Workstation, Server, Router, Switch, Application
Risk Level
Low, Medium, High, Critical
Security Status
Secure, Warning, Vulnerable
Sample Output
=========================================
 CYBERSECURITY ASSET INVENTORY
=========================================
Asset ID      : A101
Asset Name    : HR-PC-01
Asset Type    : Workstation
IP Address    : 192.168.1.10
OS            : Windows 11
Department    : HR
Risk Level    : Medium
Status        : Secure
-----------------------------------------
Asset ID      : A102
Asset Name    : Web-Server
Asset Type    : Server
IP Address    : 192.168.1.20
OS            : Ubuntu
Department    : IT
Risk Level    : Critical
Status        : Vulnerable
-----------------------------------------
Asset ID      : A103
Asset Name    : Core-Router
Asset Type    : Router
IP Address    : 192.168.1.1
OS            : Cisco IOS
Department    : Network
Risk Level    : High
Status        : Warning
-----------------------------------------
Total Assets       : 3
Critical Assets    : 1
High Risk Assets   : 1
Medium Risk Assets : 1
Low Risk Assets    : 0
Vulnerable Assets  : 1
Warning Assets     : 1
Secure Assets      : 1
=========================================
Notes
Screenshots of each menu operation (add, display, search, update, delete, summary, validation) should be placed in the screenshots/ folder as per the required repository structure.
Test cases used for manual verification are documented in tests/test_cases.md.
