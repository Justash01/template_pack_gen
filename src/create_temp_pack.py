import os
import sys
import json
import random
import uuid
uuidv4 = uuid.uuid4()
# Config
mcAppdataFolder = os.path.expanduser("~") + "\\AppData\\Local\\Packages\\Microsoft.MinecraftUWP_8wekyb3d8bbwe\\LocalState\\games\\com.mojang"

manifestJson = {
  "format_version": 2,
  "header": {
    "uuid": uuidv4,
    "version": [ 1, 0, 0 ],
    "min_engine_version": [ 1, 19, 30 ]
  },
  "modules": [
    {
      "uuid": uuidv4,
      "version": [ 1, 0, 0 ]
    }
  ]
}

print("Minecraft Template Pack Generator v1.0 by @Justash01")
print("This script will generate a template pack for you to use in Minecraft.")
print("\n")

pack_name = input("Enter the name of the pack: ")
while pack_name == "":
    print("Invalid pack name, please try again." + "\n")
    pack_name = input("Enter the name of the pack: ")


pack_description = input("Enter the description of the pack (Optional): ")
# check what type of pack user wants to generate, 1. Resource pack or 2. Behavior pack or 3. Both (Dependent)

print("Which type of pack do you want to generate?" + "\n")
print("1. Resource Pack")
print("2. Behavior Pack")
print("3. Both (Dependent)")
pack_type = input("> ")

if pack_type == "1":
    pack_type = "resource_pack"
elif pack_type == "2":
    pack_type = "behavior_pack"
elif pack_type == "3":
    pack_type = "both"
else:
    print("Defaulting to behavior pack.")
    pack_type = "behavior_pack"

print("\n")
print("Generating pack...")
print("\n")

# create pack folder in current directory if not exists
# for behavior pack, create in mcAppdataFolder + "\\development_behavior_packs"
# for resource pack, create in mcAppdataFolder + "\\development_resource_packs"

if pack_type == "behavior_pack":
    if not os.path.exists(mcAppdataFolder + "\\development_behavior_packs\\" + pack_name):
        os.makedirs(mcAppdataFolder + "\\development_behavior_packs\\" + pack_name)
        print("Created behavior pack folder: " + pack_name)
    else:
        pack_name = pack_name + str(random.randint(1, 100))
        os.makedirs(mcAppdataFolder + "\\development_behavior_packs\\" + pack_name)
        print("Created behavior pack folder: " + pack_name)

    # create pack_manifest.json
    with open(mcAppdataFolder + "\\development_behavior_packs\\" + pack_name + "\\manifest.json", "w") as f:
        # add name and description to manifestJson
        manifestJson["header"]["name"] = pack_name
        manifestJson["header"]["description"] = pack_description
        manifestJson["modules"][0]["type"] = "data"
        f.write(json.dumps(manifestJson, indent=2))
        f.close()
        print("Created manifest.json")