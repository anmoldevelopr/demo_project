menu = {
    "pizza": 50,
    "pasta": 60,
    "maggie":40,
    "coffie":30,
    "burger":40,
}   
print("Welcome to my cafe")
print("pizza: Rs 50\npasta: Rs 60\nmaggie:Rs 40\ncoffie:Rs 30\nburger:Rs 40")


order_total = 0

item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    
    print(f"Your item {item_1} has been added to your order")
else:
    print(f" Ordered item {item_1} is not available yet")
    
another_order = input("Do you want to add another item?(Yes/No)")
    
if another_order == "Yes":
    item_2 = input("Enter the name of second item =")
         
    if item_2 in menu:
            order_total+= menu [item_2]
            print(f"Item {item_2}has been added to order")
             
    else:
        print(f"Ordered item{item_2}is not available! ")

print(f"The total amount of item to pay is {order_total}")
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
    


