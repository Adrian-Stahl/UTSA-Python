print("Welcome to the House of Pies! Here are our pies: ")

pie_list = ["Pecan", "Apple Crisp", "Bean", "Banoffee", "Black Bun",
            "Blueberry", "Buko", "Burek", "Tamale", "Steak"]

for i in pie_list:
    print("("+str(pie_list.index(i)+1)+") " + i)

buy = "y"
count = 0
purchase = []

while buy == "y":
    order = int(input("Please tell us the number of the pie you like: "))
    print(f"Great! We'll have the {pie_list[order-1]}")
    purchase.append(str(pie_list[order-1]))
    count = count + 1
    buy = input("Do you want to make another order? ")

print("Total pies ordered: " + str(count))