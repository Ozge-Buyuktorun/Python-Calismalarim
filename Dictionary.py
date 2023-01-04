stuff = {"food":15, "energy":100, "enemies":3}

print(stuff.get("food"))
print(stuff.get("energy"))
print(stuff.get("enemies"))
print(stuff.items())
print(stuff.keys())
print(stuff.popitem("food"))
print(stuff)
print(Stuff.setdefault("friends",123))
print(stuff)

#update function
new_items = {"rocks":4, "arrows":18}
stuff.update(new_items)
print(stuff)

new_items = {"rocks":2 , "arrows":5}
stuff.update(new_items)
print(stuff)

up_new = {"food":3 ,"webs":2}
stuff.update(up_new)
print(stuff)
stuff.update(food = 450, cookies = 6)
print(stuff)