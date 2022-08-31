sum=0
item=0
while True:
    UserInput=input("Enter price : ")
    if UserInput != "q":
        sum=sum+int(UserInput)
        item+=1
        print(f"Order total so far {sum}")
    else:
        print(f"Total price {sum}. And total {item} item added\n  Thanks for coming !")
        break    