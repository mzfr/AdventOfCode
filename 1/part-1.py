"""
https://adventofcode.com/2019/day/1#part1
"""
with open("mass.txt", 'r') as f:
    masses = f.read().split("\n")

total = list()

# Remove empty string from the list and map each string as integer
masses = map(int,filter(None,masses))

for mass in masses:
    fuel = int(mass/3)-2
    total.append(fuel)

print("The sum of fuel requirements is: ",sum(total))
