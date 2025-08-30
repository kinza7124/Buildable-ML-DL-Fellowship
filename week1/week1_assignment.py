# 1.except Tuple Example (Immutable)
print("1. Tuple Example")
my_tuple = (10, 20, 30)
print("Original tuple:", my_tuple)

try:
    my_tuple[1] = 50  # Attempting to modify an element
except TypeError as e:
    print("Error:", e)

print("Explanation: Tuples are immutable, so you cannot change their elements once created.\n")

# 2. List Example (Mutable)
print("2. List Example")
my_list = [10, 20, 30]
print("Original list:", my_list)

my_list[1] = 50  # Modifying an element
print("Modified list:", my_list)
print("Explanation: Lists are mutable, so we can modify,add,or remove elements.\n")

# 3. Dictionary Example (Mutable)
print("3. Dictionary Example")
my_dict = {"name": "Alice", "age": 25}
print("Original dictionary:", my_dict)

my_dict["age"] = 26  # Updating a value
print("Updated dictionary:", my_dict)
print("Explanation: Dictionaries are mutable, so values for keys can be updated directly.\n")

# 4. Tuple Containing Sub-lists (Mutable Elements Inside Immutable Tuple)
print("4. Tuple Containing Lists")
tuple_with_lists = ([1, 2], [3, 4])
print("Original tuple:", tuple_with_lists)

tuple_with_lists[0][1] = 99  # Modifying an element inside a sub-list
print("Modified tuple:", tuple_with_lists)
print("Explanation: The tuple itself is immutable, so we cannot change which objects it contains.\n"
      "However, the sub-lists inside the tuple are mutable, so their contents can be changed.\n")

# Question 3 – User Information Dictionary (Validation + Logic)
def get_valid_name():
    while True:
        name = input("Enter your name: ").strip()
        if name.isalpha():
            return name
        print("Invalid name! Please enter letters only.")

def get_valid_age():
    while True:
        try:
            age = int(input("Enter your age: "))
            if 0 < age < 100:
                return age
            else:
                print("Age must be between 1 and 99.")
        except ValueError:
            print("Invalid input! Please enter a number.")

def get_valid_email():
    while True:
        email = input("Enter your email: ").strip()
        if (
            "@" in email
            and "." in email
            and not email[0] in "@."
            and not email[-1] in "@."
        ):
            return email
        print("Invalid email! Must contain '@' and '.', and not start/end with special characters.")

def get_valid_fav_number():
    while True:
        try:
            fav_number = int(input("Enter your favorite number (1-100): "))
            if 1 <= fav_number <= 100:
                return fav_number
            else:
                print("Number must be between 1 and 100.")
        except ValueError:
            print("Invalid input! Please enter a number.")

user_info = {}

user_info["name"] = get_valid_name()
user_info["age"] = get_valid_age()
user_info["email"] = get_valid_email()
user_info["favorite_number"] = get_valid_fav_number()

print(f"\nWelcome {user_info['name']}!Your account has been registered with email {user_info['email']}.")
print("User Information Stored:", user_info)

# Cinema Ticket Pricing System
def calculate_ticket_price(age, is_student, is_weekend):
    # Validate age
    if age < 0 or age > 120:
        raise ValueError("Invalid age entered!")

    if age < 12:
        price = 5
    elif 13 <= age <= 17:
        price = 8
    elif 18 <= age <= 59:
        price = 12
    else:
        price = 6  

    # Apply student discount (20%) if applicable (only if age > 12)
    if is_student and age > 12:
        price *= 0.8

    # Add weekend surcharge
    if is_weekend:
        price += 2

    return round(price, 2)

customers = []
total_revenue = 0

# Ask for number of customers
while True:
    try:
        num_customers = int(input("Enter the number of customers: "))
        if num_customers <= 0:
            print("Number of customers must be greater than 0!")
            continue
        break
    except ValueError:
        print("Please enter a valid number.")

# Process each customer
for i in range(num_customers):
    print(f"\n--- Customer {i + 1} ---")
    # Validate age input
    while True:
        try:
            age = int(input("Enter age: "))
            if age < 0 or age > 120:
                print("Please enter a realistic age (0-120).")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid number for age.")

    # Student input validation
    while True:
        is_student_input = input("Are you a student? (yes/no): ").strip().lower()
        if is_student_input in ["yes", "no"]:
            is_student = is_student_input == "yes"
            break
        else:
            print("Please enter 'yes' or 'no'.")

    # Weekend input validation
    while True:
        is_weekend_input = input("Is it a weekend? (yes/no): ").strip().lower()
        if is_weekend_input in ["yes", "no"]:
            is_weekend = is_weekend_input == "yes"
            break
        else:
            print("Please enter 'yes' or 'no'.")

    # Calculate ticket price
    try:
        ticket_price = calculate_ticket_price(age, is_student, is_weekend)
    except ValueError as e:
        print(e)
        continue

    # Store customer details
    customer = {
        "Customer": i + 1,
        "Age": age,
        "Student": is_student,
        "Weekend": is_weekend,
        "Ticket Price": ticket_price
    }
    customers.append(customer)
    # Add to total revenue
    total_revenue += ticket_price

# Apply group discount if there are 4 or more customers
discount_applied = False
if num_customers >= 4:
    discount_applied = True
    total_revenue *= 0.9  # 10% discount

# Display customer ticket details
print("\n=== Customer Ticket Details ===")
for customer in customers:
    print(f"Customer {customer['Customer']}: Age={customer['Age']}, "
          f"Student={'Yes' if customer['Student'] else 'No'}, "
          f"Weekend={'Yes' if customer['Weekend'] else 'No'}, "
          f"Ticket Price=${customer['Ticket Price']}")

# Display total revenue
print("\n=== Summary ===")
print(f"Total Revenue: ${round(total_revenue, 2)}")
if discount_applied:
    print("Group Discount Applied: 10% OFF ✅")

# Identify highest and lowest paying customers
highest_payer = max(customers, key=lambda x: x["Ticket Price"])
lowest_payer = min(customers, key=lambda x: x["Ticket Price"])
print(f"Highest Paying Customer: Customer {highest_payer['Customer']} - ${highest_payer['Ticket Price']}")
print(f"Lowest Paying Customer: Customer {lowest_payer['Customer']} - ${lowest_payer['Ticket Price']}")

#5. Weather Alert System
def weather_alert(temp_celsius, condition):
    # Convert temperatures
    temp_fahrenheit = (temp_celsius * 9/5) + 32
    temp_kelvin = temp_celsius + 273.15

    # Check conditions and return appropriate alerts
    if temp_celsius < 0 and condition.lower() == "snowy":
        alert = "Heavy snow alert! Stay indoors."
    elif temp_celsius > 35 and condition.lower() == "sunny":
        alert = "Heatwave warning! Stay hydrated."
    elif condition.lower() == "rainy" and temp_celsius < 15:
        alert = "Cold rain alert! Wear warm clothes."
    else:
        alert = "Normal weather conditions."

    # Include converted temperatures in the output
    return (f"{alert}\n"
            f"Temperature: {temp_celsius}°C | {temp_fahrenheit:.2f}°F | {temp_kelvin:.2f}K")


try:
    temp = float(input("Enter current temperature in °C: "))
    condition = input("Enter weather condition (sunny, rainy, snowy, etc.): ")
    result = weather_alert(temp, condition)
    print("\n" + result)

except ValueError:
    print("Invalid input! Please enter a numeric temperature.")

#6 Sale Analytics 
def analyze_sales(sales_list):
    # Sorting the sales list to calculate median
    sorted_sales = sorted(sales_list)
    # Maximum and minimum sales
    max_sales = max(sorted_sales)
    min_sales = min(sorted_sales)
    # Calculate median
    n = len(sorted_sales)
    if n % 2 == 0:  # Even number of sales
        median = (sorted_sales[n // 2 - 1] + sorted_sales[n // 2]) / 2
    else:  # Odd number of sales
        median = sorted_sales[n // 2]
    
    return max_sales, min_sales, median

sales = []
while True:
    try:
        n = int(input("Enter the number of daily sales records: "))
        if n < 5:
            print("You must enter at least 5 daily sales values. Try again.")
            continue
        
        # Get sales input from the user
        for i in range(n):
            while True:
                try:
                    amount = float(input(f"Enter sales amount for day {i + 1}: $"))
                    if amount < 0:
                        raise ValueError("Sales cannot be negative.")
                    sales.append(amount)
                    break
                except ValueError as e:
                    print(f"Invalid input: {e}. Please enter a valid number.")
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

max_sales, min_sales, median_sales = analyze_sales(sales)

print("\nSales Summary:")
print(f"Highest sales day: ${max_sales}")
print(f"Lowest sales day: ${min_sales}")
print(f"Median sales: ${median_sales}")

#7 Inventory Management System
def update_inventory(inventory_dict, item, quantity):
    if item in inventory_dict:
        if quantity < 0 and abs(quantity) > inventory_dict[item]:
            print(f"Not enough stock for '{item}'. Available: {inventory_dict[item]}")
        else:
            inventory_dict[item] = max(0, inventory_dict[item] + quantity)
    else:
        print(f"Item '{item}' not found in inventory!")
    return inventory_dict


def display_inventory(inventory_dict):
    print("\nUpdated Inventory:")
    for item, qty in inventory_dict.items():
        print(f"   {item}: {qty} in stock")

    # Find most stocked and least stocked products
    most_stocked = max(inventory_dict, key=inventory_dict.get)
    least_stocked = min(inventory_dict, key=inventory_dict.get)

    print(f"\nMost stocked product: {most_stocked} ({inventory_dict[most_stocked]} in stock)")
    print(f"Least stocked product: {least_stocked} ({inventory_dict[least_stocked]} in stock)")


inventory = {
    "Laptop": 10,
    "Smartphone": 15,
    "Headphones": 25,
    "Keyboard": 12,
    "Monitor": 8
}

print("Welcome to the E-commerce Inventory Management System!")
display_inventory(inventory)

# Simulate user shopping for 3 items
print("\n=== Shopping Cart ===")
for i in range(3):
    item = input(f"\nEnter the name of item {i+1}: ").strip().title()
    try:
        qty = int(input(f"Enter the quantity for '{item}': "))
    except ValueError:
        print("Invalid quantity! Please enter a number.")
        continue
    # Deduct stock (use negative quantity)
    inventory = update_inventory(inventory, item, -qty)

display_inventory(inventory)
