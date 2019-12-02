
TOTAL = list()

def calculate_fuel(mass):
    """
    Just do the simple calculation for fuel
    """
    return int(mass/3)-2

def recursive_fuel(mass):
    """
    recursively calculate the fuel value.
    Ex: 654 + 216 + 70 + 21 + 5 = 966
    """
    fuel = calculate_fuel(mass)
    if fuel < 0:
        return
    TOTAL.append(fuel)
    recursive_fuel(fuel)

def main():
    with open("mass.txt", 'r') as f:
        masses = f.read().split("\n")
    
    # Remove NULL values and convert all strings to numbers
    masses = map(int,filter(None,masses))

    for mass in masses:
        recursive_fuel(mass)

    print("The total sum of fuel requirement is: ", sum(TOTAL))

if __name__ == "__main__":
    main()
