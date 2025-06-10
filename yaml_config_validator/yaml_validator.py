import yaml

with open("config.yaml") as f:
    config = yaml.safe_load(f)
if "version" not in config:
    config["version"] = input("Enter version: ")
with open("config.yaml", "w") as f:
    yaml.safe_dump(config, f)
print("Config updated.")