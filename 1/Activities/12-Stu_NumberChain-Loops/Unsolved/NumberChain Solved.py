User_play = "y"

while User_play == "y":
    user_number = int(input("How many numbers?"))
    for x in range(user_number):
        print(x)
    user_play = input("Continue: (y)es or (n)o? ")