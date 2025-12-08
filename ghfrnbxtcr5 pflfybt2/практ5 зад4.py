mass = [14, -6, 3, 11, 6, 8.5, 99, -20, -6, 10, 40, 0.25, -4, 5]

mass = [x for x in mass if x >= 0]
mass_asc = sorted(mass)
mass_desc = sorted(mass, reverse=True)
print(mass_asc)
print(mass_desc)
