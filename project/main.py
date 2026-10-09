from x import resource_invet, borrow, Returns


print("----- Welcome to Learn2earn Lends ------")
print("---- AVAILABLE DOINGS ----\n1.add_resource\n2.borrow\n3.return\n4.search/filter\n5.reports\n6.exist")


while True:
    user_input = input("Enter Mode of transaction: ")
    if user_input == "1":
        user_input1 = input("Enter id: ")
        user_input2 = input("Enter name: ")
        user_input3 = input("Enter category: ")
        try:
          user_input4 = int(input("Enter total: "))
        except ValueError:
           print("total is an integer!")  

        resource_invet(user_input1, user_input2, user_input3, user_input4)
    elif user_input == "2":
        user_input1 = input("Enter fellow_id: ")
        user_input2 = input("Enter resource_id: ")
        try:
          user_input3 = int(input("Enter quantity: "))
        except ValueError:  
            print("Invalid input try numbers")
        borrow(user_input1, user_input2, user_input3)

    elif user_input == "3":
        user_input1 = input("Enter fellow_id: ") 
        user_input2 = input("Enter resource_id: ")
        try:
           user_input3 = int(input("enter amount: "))
        except ValueError:
           print("amount need to be an integer")
        Returns(user_input1, user_input2, user_input3)