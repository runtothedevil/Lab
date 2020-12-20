def a(mass):
    seen = set()
    seen_add = seen.add
    return [x for x in mass if not (x in seen or seen_add(x))]
mass=[4,7,6,1,7,5,5,1,2,4,6]
print(a(mass))