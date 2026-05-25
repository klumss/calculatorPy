dec = True
total = 0
while(True):
    user1 = input("Number 1: ")
    if user1 != "":
        user1 = int(user1)
        op = input("Operation: ")
        if op == "":
            total += user1
        else:
            user2= int(input("Number 2: "))
        if op == "+":
            total += user1 + user2
        elif op == "-":
            total += user1 - user2
        elif op == "/":
            total += user1 / user2
        elif op == "*":
            total += user1 * user2
        print("Current total:", total)
    else:
        break
print(f"Final total : {total}")