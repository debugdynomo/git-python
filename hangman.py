import random

name_list=["binary","vishnu","variable","malayalam","ship","aboard","jennifer","depth","telnet",""]
random_num=random.randint(0,len(name_list)-1)
name_str=name_list[random_num]
freq=[]
hangman="HANGMAN"
chance=["^"," "," "," "," "," "," "]
point=0
count=0
flag=0
answer=[0]*len(name_str)
print(name_str)
for j in range(0,len(name_str)):
    answer[j]="_"#answer #intialised
    freq.append(j)
for i in range(0,len(name_str)):
    flag=0
    for j in range(0,len(name_str)):
        if name_str[i]==name_str[j]:
            flag+=1
            if flag>=2:
                freq.append(j)
while point!=6 and count!=len(name_str):
    print(answer)
    position=0
    add=0
    given=input("Enter the character\n")
    for k in range(0,len(name_str)):
        if given==name_str[k] and k in freq:#input checked
            add=k
            position+=1
            freq.remove(k)
            break
    if position==0:#chance reduced
        print("OOPS!! wrong character\n")
        point+=1
        chance[point]="^"
        chance[point-1]=" "
        print(chance)
    else:
        answer[add]=given#char added
        count+=1
        print("HANGMAN\n")
        print(chance)
if count==len(name_str):
    print("!!nice job!!")
else:
    print("OOPS please retry")