import random

def generate_customer_preferences(H, num_customers):
    customers = []

    for _ in range(num_customers):
        num_prefs = random.randint(1, H)  # At least 1 hop per customer
        airborne_included = False
        prefs = []

        hop_indices = random.sample(range(H), num_prefs)
        for h in hop_indices:
            if not airborne_included and random.random() < 0.3:
                prefs.append((h, 'airborne'))
                airborne_included = True
            else:
                prefs.append((h, 'by-sea'))

        customers.append(prefs)

    return customers

def save_to_file(filename, H, customers):
    with open(filename, "w") as f:
        f.write(f"{H}\n")
        f.write(f"{len(customers)}\n")

        for prefs in customers:
            formatted = ', '.join(f"{h} {t}" for h,t in prefs)
            f.write(formatted + "\n")

    print(f" File saved as: {filename}")

# Parameters
H = 3
num_customers = 5
filename = "input_250.txt"

# Generate and save
customers = generate_customer_preferences(H, num_customers)
save_to_file(filename,H,customers)