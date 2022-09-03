from time import *
import random as r

def mistake(para_type,user_type):
    error = 0
    for i in range(len(para_type)):
        try:
            if para_type[i] != user_type[i]:
                error+=1
        except :
            error+=1
    return error

def speed(time_s,time_e,word):
    time_delay = time_e - time_s
    r_time = round(time_delay)
    speed = len(word)/r_time
    return round(speed)


paragraph_list = ['''----peech to text, a dream for decades now comes true. You can type by just speaking. 
The online system works with a speech recognition system; which recognizes your voice and convert into text.
It's much faster than conventional keyboard typing.---''','''---You use it to type anything, anywhere, anytime. This will help you very much in completing your 
day-to-days tasks and save lots of time and money.
You could type articles, blogs, emails etc. by using speech to text services---''','''---The search inventory released showed that classified documents had
been mixed in with personal items and other materials in the boxes in which they were stored.
Federal investigators also retrieved more than 11,000 non-classified government documents from former President Donald Trump's Florida home and resort.---''']
r_1 = r.choice(paragraph_list)
print("********************************** Typing Speed **********************************")
print(r_1)
time_1=time()
user_paragraph = input("Start typing : \n")
time_2=time()
print(f"Speed  = {speed(time_1,time_2,user_paragraph)} w/s ")
print(f"Error = {mistake(r_1,user_paragraph)}")