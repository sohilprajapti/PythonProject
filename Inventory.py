import pprint
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'rope', "Dragon's scale", "Dragon's breath", "Bones", "Bones", "Bones", "Bones", "Bones", "Bones"]

def addinventory(inventory, add):
    print("Inventory:")
    for i,j in enumerate(add):
        hello = inventory.setdefault(j , 0)
        hello = hello + 1
        inventory[j] = hello
    for i,j in inventory.items():
        print(f"{i}: {j}")

addinventory(stuff , dragonLoot)
