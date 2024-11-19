menu={
    "Coffee":40,
    "Pizza" :100,
    "Pasta" : 100,
    "Cold Coffee":80,
}
print("WELCOME TO ABHANG RESTRO")
print(" \n Pizza: Rs100 \n Coffee: Rs40 \n Pasta : Rs100 \n Cold Coffee: Rs80")

order_total = 0 

order1=input("Enter what you would like to order : ")

if order1 in menu:
    order_total += menu[order1]
    print("thanks for ordering, your order is noted.")
else:
    print("Item not in menu, please order something else.")

another_order=input("enter if you want to order more (YES/NO) : ")
if another_order=="YES":
    while another_order=="YES":
        order2=input("Enter what you would like to order : ")
        if order2 in menu:
            order_total+=menu[order2]
            print("thanks for ordering, your order is noted.")
            print()
            another_order=input("enter if you want to order more (YES/NO) : ")
        else:
            print("Item not in menu, please order something else.")
            another_order=input("enter if you want to order more (YES/NO) : ")
    else:
        print(f"Thanks for your order \n Your order total is : Rs{order_total}")
else:
    print(f"Thanks for your order \n Your order total is : Rs{order_total}")