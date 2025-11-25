age = int(input("Enter your age: "))
has_id = input("Do you have an ID? (yes/no): ").lower() == "yes"

is_adult = age >= 18
id_valid = has_id

if is_adult and id_valid:
    print("Access granted.")
elif is_adult and not id_valid:
    print("You are old enough but need an ID.")
else:
    print("Access denied.")
