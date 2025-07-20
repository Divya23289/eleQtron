import sys
from itertools import product

def parse_input():
 with open('input_250.txt', 'r') as file:
    lines = [line.strip() for line in file if line.strip()]
    H =int(lines[0])
    C =int(lines[1])
    customers = []

    for line in lines[2:]:
        preferences = []
        entries = line.split(", ")

        for entry in entries:
            hop_str, t = entry.split()
            hop = int(hop_str)
            preferences.append((hop, t))
        customers.append(preferences)

    return H, customers

def check_satisfaction(itinerary, customer_prefs):
    # Customer is satisfied if at least one preference matches
    for hop, mode in customer_prefs:
        if itinerary[hop] == mode:
            return True
    return False

def main():
    H, customers = parse_input()

    min_airborne = H + 1
    best_itinerary = None

    # Iterate over all possible combinations of transport modes for the H hops
    for combo in product(['by-sea', 'airborne'], repeat=H):
        #print(combo)
        # Check if all customers are satisfied
        if all(check_satisfaction(combo, prefs) for prefs in customers):
            airborne_count = combo.count("airborne")
            if airborne_count < min_airborne:
                min_airborne = airborne_count
                best_itinerary = combo

    if best_itinerary is None:
        print("NO ITINERARY")
    else:
        # Output in format: "0 mode, 1 mode, ... "
        print(', '.join(f"{i} {best_itinerary[i]}" for i in range(H)))

if __name__ == "__main__":
    main()