#Print hello (name), you are (age) years old
name=input("Enter your name: ")
age=int(input("Enter your age: "))
print(f"Hello {name}, you are {age} years old.")

#Convert celsius to fahrenheit and print with one decimal place
celsius=float(input("Enter temperature in Celsius: "))
fahrenheit=(celsius * 9/5) + 32
print(f"Temperature in Fahrenheit: {fahrenheit:.1f}")

#Formatted receipt with 3 items name, price and total
item1_name = input("Enter the name of the first item: ")
item1_price = float(input("Enter the price of the first item: "))
item1_quantity = int(input("Enter the quantity of the first item: "))

item2_name = input("Enter the name of the second item: ")
item2_price = float(input("Enter the price of the second item: "))
item2_quantity = int(input("Enter the quantity of the second item: "))

item3_name = input("Enter the name of the third item: ")
item3_price = float(input("Enter the price of the third item: "))
item3_quantity = int(input("Enter the quantity of the third item: "))

total1 = item1_price * item1_quantity
total2 = item2_price * item2_quantity
total3 = item3_price * item3_quantity

print("\n--- Receipt ---")
print(f"{item1_name}: ${item1_price:.2f} x {item1_quantity} = ${total1:.2f}")
print(f"{item2_name}: ${item2_price:.2f} x {item2_quantity} = ${total2:.2f}")
print(f"{item3_name}: ${item3_price:.2f} x {item3_quantity} = ${total3:.2f}")
print(f"Total: ${total1 + total2 + total3:.2f}")