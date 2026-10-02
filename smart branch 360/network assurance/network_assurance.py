# SmartBranch 360 - Network Assurance Tool

def check_network(config):
    print("========================================")
    print("     SMARTBRANCH 360 NETWORK ASSURANCE")
    print("========================================")
    print()

    checks = {
        "VLAN 10 - Employee": "VLAN 10" in config,
        "VLAN 20 - Guest": "VLAN 20" in config,
        "VLAN 30 - Server": "VLAN 30" in config,
        "VLAN 99 - Management": "VLAN 99" in config,
        "Employee Gateway": "10.10.10.1" in config,
        "Guest Gateway": "10.10.20.1" in config,
        "Server Gateway": "10.10.30.1" in config,
        "Management Gateway": "10.10.99.1" in config,
        "DNS Server": "10.10.30.10" in config,
        "Guest ACL": "GUEST_RESTRICT" in config,
        "NAT Configuration": "ip nat inside source" in config,
        "Default Route": "0.0.0.0 0.0.0.0" in config
    }

    passed = 0
    failed = 0

    print("Network Configuration Checks")
    print("----------------------------------------")

    for name, result in checks.items():
        if result:
            print("[PASS] " + name)
            passed += 1
        else:
            print("[FAIL] " + name)
            failed += 1

    print()
    print("----------------------------------------")
    print("Total Checks :", len(checks))
    print("Passed       :", passed)
    print("Failed       :", failed)
    print("----------------------------------------")

    if failed == 0:
        print("STATUS: NETWORK CONFIGURATION HEALTHY")
    else:
        print("STATUS: REVIEW REQUIRED")

    print()


# Read the sample network configuration
with open("sample_config.txt", "r") as file:
    configuration = file.read()

check_network(configuration)