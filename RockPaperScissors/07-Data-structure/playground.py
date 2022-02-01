

# 1. Dict
# 2. List/arrays
# 3. Sets

x = [1, 5, 5, 11, 12]
print(x)
x.reverse()
print(x)
qty = x.count(12)
print(x)
x.append(15)
print(x)
x.sort()
print(x)


# Sets:
st = {1, 5, 5, 11, 7}
st.add(11)
print(st)

# Dict
d = {
    "Bob": 0,
    "sarah": 0,
    "defeated_by": {"paper", "wolf"},
    "defeats": {"scissors", "sponge"}
}
print(d['Bob'])
d['Bob'] += 1
print(d)
d["Yves"] = 7
print(d)

print(f"You defeat {d['defeats']}")

print(d.get("other", 42))

z = dict(yves=2, kate=0, tom=4)
print(z)
name = "Fred"
wins = z.get(name, 0)
print(f"Wins by {name} are {wins}")
if wins == 0:
    print("This player has never played!!!")