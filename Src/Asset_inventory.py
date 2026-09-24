import json
import os
import re

# ---------------------------------------------------------------------------
# Configuration / constants
# ---------------------------------------------------------------------------

DATA_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                          "data", "assets.json")

ASSET_TYPES = ["Workstation", "Server", "Router", "Switch", "Application"]
RISK_LEVELS = ["Low", "Medium", "High", "Critical"]
SECURITY_STATUSES = ["Secure", "Warning", "Vulnerable"]

IP_REGEX = re.compile(
    r"^(25[0-5]|2[0-4][0-9]|1?[0-9]?[0-9])(\.(25[0-5]|2[0-4][0-9]|1?[0-9]?[0-9])){3}$"
)


# ---------------------------------------------------------------------------
# Persistence helpers
# ---------------------------------------------------------------------------

def load_assets():
    """Load the asset list from the JSON data file, if it exists."""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            print("Warning: could not read existing data file. Starting fresh.\n")
    return []


def save_assets(assets):
    """Persist the asset list to the JSON data file."""
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(assets, f, indent=4)


# ---------------------------------------------------------------------------
# Input helpers / validation
# ---------------------------------------------------------------------------

def prompt_nonempty(label):
    while True:
        value = input(f"{label}: ").strip()
        if value:
            return value
        print("  -> This field cannot be empty. Please try again.")


def prompt_choice(label, choices):
    choice_str = "/".join(choices)
    while True:
        value = input(f"{label} ({choice_str}): ").strip().capitalize()
        if value in choices:
            return value
        print(f"  -> Invalid value. Choose one of: {choice_str}")


def prompt_ip(label="IP Address"):
    while True:
        value = input(f"{label}: ").strip()
        if IP_REGEX.match(value):
            return value
        print("  -> Invalid IP address format (expected e.g. 192.168.1.10).")


def prompt_unique_id(assets, label="Asset ID"):
    while True:
        value = input(f"{label}: ").strip()
        if not value:
            print("  -> Asset ID cannot be empty.")
            continue
        if any(a["asset_id"].lower() == value.lower() for a in assets):
            print("  -> An asset with this ID already exists. Try another.")
            continue
        return value


# ---------------------------------------------------------------------------
# Core operations
# ---------------------------------------------------------------------------

def add_asset(assets):
    print("\n--- Add New Asset ---")
    asset = {
        "asset_id": prompt_unique_id(assets),
        "asset_name": prompt_nonempty("Asset Name"),
        "asset_type": prompt_choice("Asset Type", ASSET_TYPES),
        "ip_address": prompt_ip(),
        "os": prompt_nonempty("Operating System"),
        "department": prompt_nonempty("Owner/Department"),
        "risk_level": prompt_choice("Risk Level", RISK_LEVELS),
        "security_status": prompt_choice("Security Status", SECURITY_STATUSES),
    }
    assets.append(asset)
    save_assets(assets)
    print(f"\nAsset '{asset['asset_id']}' added successfully.\n")


def find_asset(assets, asset_id):
    for asset in assets:
        if asset["asset_id"].lower() == asset_id.lower():
            return asset
    return None


def search_asset(assets):
    print("\n--- Search Asset ---")
    if not assets:
        print("No assets in inventory.\n")
        return
    asset_id = input("Enter Asset ID to search: ").strip()
    asset = find_asset(assets, asset_id)
    if asset:
        print()
        display_single(asset)
    else:
        print(f"No asset found with ID '{asset_id}'.\n")


def update_asset(assets):
    print("\n--- Update Asset ---")
    if not assets:
        print("No assets in inventory.\n")
        return
    asset_id = input("Enter Asset ID to update: ").strip()
    asset = find_asset(assets, asset_id)
    if not asset:
        print(f"No asset found with ID '{asset_id}'.\n")
        return

    print("Leave a field blank to keep its current value.\n")

    new_name = input(f"Asset Name [{asset['asset_name']}]: ").strip()
    if new_name:
        asset["asset_name"] = new_name

    new_type = input(f"Asset Type [{asset['asset_type']}] ({'/'.join(ASSET_TYPES)}): ").strip().capitalize()
    if new_type:
        if new_type in ASSET_TYPES:
            asset["asset_type"] = new_type
        else:
            print("  -> Invalid asset type, keeping previous value.")

    new_ip = input(f"IP Address [{asset['ip_address']}]: ").strip()
    if new_ip:
        if IP_REGEX.match(new_ip):
            asset["ip_address"] = new_ip
        else:
            print("  -> Invalid IP format, keeping previous value.")

    new_os = input(f"Operating System [{asset['os']}]: ").strip()
    if new_os:
        asset["os"] = new_os

    new_dept = input(f"Owner/Department [{asset['department']}]: ").strip()
    if new_dept:
        asset["department"] = new_dept

    new_risk = input(f"Risk Level [{asset['risk_level']}] ({'/'.join(RISK_LEVELS)}): ").strip().capitalize()
    if new_risk:
        if new_risk in RISK_LEVELS:
            asset["risk_level"] = new_risk
        else:
            print("  -> Invalid risk level, keeping previous value.")

    new_status = input(f"Security Status [{asset['security_status']}] ({'/'.join(SECURITY_STATUSES)}): ").strip().capitalize()
    if new_status:
        if new_status in SECURITY_STATUSES:
            asset["security_status"] = new_status
        else:
            print("  -> Invalid security status, keeping previous value.")

    save_assets(assets)
    print(f"\nAsset '{asset_id}' updated successfully.\n")


def delete_asset(assets):
    print("\n--- Delete Asset ---")
    if not assets:
        print("No assets in inventory.\n")
        return
    asset_id = input("Enter Asset ID to delete: ").strip()
    asset = find_asset(assets, asset_id)
    if not asset:
        print(f"No asset found with ID '{asset_id}'.\n")
        return
    confirm = input(f"Are you sure you want to delete '{asset_id}'? (y/n): ").strip().lower()
    if confirm == "y":
        assets.remove(asset)
        save_assets(assets)
        print(f"Asset '{asset_id}' deleted successfully.\n")
    else:
        print("Deletion cancelled.\n")


def display_single(asset):
    print("-----------------------------------------")
    print(f"Asset ID      : {asset['asset_id']}")
    print(f"Asset Name    : {asset['asset_name']}")
    print(f"Asset Type    : {asset['asset_type']}")
    print(f"IP Address    : {asset['ip_address']}")
    print(f"OS            : {asset['os']}")
    print(f"Department    : {asset['department']}")
    print(f"Risk Level    : {asset['risk_level']}")
    print(f"Status        : {asset['security_status']}")
    print("-----------------------------------------")


def display_all(assets):
    print("\n=========================================")
    print(" CYBERSECURITY ASSET INVENTORY")
    print("=========================================")
    if not assets:
        print("No assets in inventory.")
        print("=========================================\n")
        return

    for asset in assets:
        print(f"Asset ID      : {asset['asset_id']}")
        print(f"Asset Name    : {asset['asset_name']}")
        print(f"Asset Type    : {asset['asset_type']}")
        print(f"IP Address    : {asset['ip_address']}")
        print(f"OS            : {asset['os']}")
        print(f"Department    : {asset['department']}")
        print(f"Risk Level    : {asset['risk_level']}")
        print(f"Status        : {asset['security_status']}")
        print("-----------------------------------------")

    print_summary(assets, footer_only=True)


def print_summary(assets, footer_only=False):
    total = len(assets)
    critical = sum(1 for a in assets if a["risk_level"] == "Critical")
    high = sum(1 for a in assets if a["risk_level"] == "High")
    medium = sum(1 for a in assets if a["risk_level"] == "Medium")
    low = sum(1 for a in assets if a["risk_level"] == "Low")
    vulnerable = sum(1 for a in assets if a["security_status"] == "Vulnerable")
    warning = sum(1 for a in assets if a["security_status"] == "Warning")
    secure = sum(1 for a in assets if a["security_status"] == "Secure")

    if not footer_only:
        print("\n=========================================")
        print(" SECURITY SUMMARY")
        print("=========================================")

    print(f"Total Assets       : {total}")
    print(f"Critical Assets    : {critical}")
    print(f"High Risk Assets   : {high}")
    print(f"Medium Risk Assets : {medium}")
    print(f"Low Risk Assets    : {low}")
    print(f"Vulnerable Assets  : {vulnerable}")
    print(f"Warning Assets     : {warning}")
    print(f"Secure Assets      : {secure}")
    print("=========================================\n")


# ---------------------------------------------------------------------------
# Menu / main loop
# ---------------------------------------------------------------------------

MENU = """
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
"""


def main():
    assets = load_assets()

    while True:
        print(MENU)
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            add_asset(assets)
        elif choice == "2":
            display_all(assets)
        elif choice == "3":
            search_asset(assets)
        elif choice == "4":
            update_asset(assets)
        elif choice == "5":
            delete_asset(assets)
        elif choice == "6":
            print_summary(assets)
        elif choice == "7":
            print("\nExiting Cybersecurity Asset Inventory System. Goodbye!\n")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 7.\n")


if __name__ == "__main__":
    main()
      
