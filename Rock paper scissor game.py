import random
def gameWIn(comp,you):
    if comp==you:
        return None
    if comp=="P":
        if you=="R": 
            return False
    elif comp=="R":
        if you=="P":
            return True
    elif comp=="P":
        if you=="S":
            return True
    elif comp=="S":
        if you=="P":
            return False
    elif comp=="S":
        if you=="R":  
            return True
    elif comp=="R":
        if you =="S":
            return False                                       

print("computer turn : ?")
randno=random.randint(1,3)
# print(randno)
if randno==1:
    comp="R"
elif randno==2:
    comp="P"
elif randno==3:
    comp="S"       

you=input("your turn: rock(R),paper(P),scisor(S) :\n")
a=gameWIn(comp,you) 
print(f"computer choose {comp}") 
print(f"you choose {you}")
if a==None:
    print("you are tied")
elif a==True:
    print("you win !") 
else:
    print("u loose")       