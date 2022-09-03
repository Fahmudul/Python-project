import random
randNum=random.randint(1,5)
users=None
Guess=0

while(users != randNum):

    # users=int(input("Enter your guess : "))
    # print(f'randNum Guess is : {randNum}')
    users=int(input("Enter your guess : "))

    Guess+=1
    if users==randNum:
        print(f"Your guess is right ! You guess at {Guess}")
    else:
        if(users>randNum):
            print("Your guess is wrong ! Try a lower !")
        else:
            print("Your guess is wrong ! Try a higher !")

with open("Highscore.txt") as f:
    Highscore=int(f.read())
if (Guess<Highscore):
    print("You just broke the record !")    
    with open("Highscore.txt","w") as f:
        f.write(str(Guess))
    

        
