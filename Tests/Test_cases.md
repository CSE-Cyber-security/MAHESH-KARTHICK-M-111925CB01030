#
Test Case
Input
Expected Result
1
Add a valid asset
Asset ID: A104, Type: Server, IP: 192.168.1.30, Risk: High, Status: Warning
Asset is added and saved to data/assets.json; success message shown
2
Add asset with duplicate Asset ID
Asset ID: A101 (already exists)
System rejects the ID and re-prompts
3
Add asset with invalid IP
IP: 999.999.1.1
System rejects the IP and re-prompts until a valid one is entered
4
Add asset with invalid Asset Type
Type: Firewall (not in allowed list)
System rejects the value and re-prompts
5
Display all assets
Menu option 2
All stored assets printed in formatted layout, ending with a summary
6
Search existing asset
Asset ID: A102
Full details of Web-Server printed
7
Search non-existing asset
Asset ID: A999
"No asset found" message shown
8
Update an existing asset
Asset ID: A103, change Risk Level to Critical
Asset's risk level updated and persisted; other fields unchanged
9
Update non-existing asset
Asset ID: A999
"No asset found" message shown
10
Delete an existing asset (confirmed)
Asset ID: A101, confirm "y"
Asset removed from inventory and file updated
