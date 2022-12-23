key_materials = {"shards": 0, "fragments": 0, "motes": 0}
junk = {}
is_found = False
legendary_item = ""
while not is_found:
    line = input().split(" ")
    if is_found:
        break
    keys = [str(line[x]).lower() for x in range(1, len(line), 2)]
    values = [int(line[x]) for x in range(0, len(line), 2)]
    for key, val in zip(keys, values):

        if key == "shards":
            key_materials["shards"] += val
            if key_materials["shards"] >= 250:
                key_materials["shards"] -= 250
                legendary_item = "Shadowmourne"
                is_found = True
                break

        elif key == "fragments":
            key_materials["fragments"] += val
            if key_materials["fragments"] >= 250:
                key_materials["fragments"] -= 250
                legendary_item = "Valanyr"
                is_found = True
                break

        elif key == "motes":
            key_materials["motes"] += val
            if key_materials["motes"] >= 250:
                key_materials["motes"] -= 250
                legendary_item = "Dragonwrath"
                is_found = True
                break

        else:
            if key not in junk.keys():
                junk[key] = val
            else:
                junk[key] += val

print(f"{legendary_item} obtained!")
for k, v in key_materials.items():
    print(f"{k}: {v}")
for k, v in junk.items():
    print(f"{k}: {v}")