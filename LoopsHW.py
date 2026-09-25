print("Type response to order, or type 0 to end order")
#Variables
MuffinStock = 10
CupcakeStock = 10

#Inputs
CxReply = str(input("Would you like a muffin or a cupcake? "))

#Processing
while CxReply != "0":
        if CxReply == "muffin":
            if MuffinStock > 0:
                MuffinStock = MuffinStock - 1
            else:
                print("I'm sorry, muffins are out of stock.")
        elif CxReply == "cupcake":
            if CupcakeStock > 0:
                CupcakeStock = CupcakeStock - 1
            else:
                print("I'm sorry, cupcakes are out of stock.")
        CxReply = str(input("Would you like a muffin or a cupcake? "))
#Display Output
print("Muffins:", MuffinStock, "Cupcakes:", CupcakeStock)