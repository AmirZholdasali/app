import json

with open("work/sample-data.json", "r") as file:
    data = json.load(file)

interfaces = data["imdata"]

print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<10} {'MTU':<5}")
print("-" * 80)

for item in interfaces:
    attr = item["l1PhysIf"]["attributes"]
    dn = attr["dn"]
    description = attr.get("descr", " ")
    speed = attr.get("speed", "inherit")
    mtu = attr.get("mtu", "N/A")

    print(f"{dn:<50} {description:<20} {speed:<10} {mtu:<5}")
