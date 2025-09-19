foods = []
prices = []
quantities = []

total = 0

while True:
    food = input("Enter the food item (or 'done' to finish): ")
    if food.lower() == 'done':
        break
    price = float(input(f"Enter the price of {food}: "))
    quantity = int(input(f"Enter the quantity of {food}: "))
    
    foods.append(food)
    prices.append(price)
    quantities.append(quantity)
    
    total += price * quantity
    print(f"Added {quantity} x {food} at ${price:.2f} each. Current total: ${total:.2f}")


print("\nShopping Cart Summary:")
for i in range(len(foods)):
    print(f"{quantities[i]} x {foods[i]} at ${prices[i]:.2f} each")
print(f"Total cost: ${total:.2f}") # Shopping Cart Program
