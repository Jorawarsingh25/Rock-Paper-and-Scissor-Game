import random
comp=0
user=0

option=['rock','paper','scissor']

while True:
    user_input=input('Type Rock/Paper/Scissor or Q for quite?: ').lower()
    if user_input=='q':
        break
    if user_input not in option:
        continue

    random_number=random.randint(0,2)
    #0 for rock or 1 for paper and 2 for scissor....
    computer_pick=option[random_number]
    print('computer pick',computer_pick + '.')

    if user_input=='Rock' and computer_pick=='Scissor':
        print("You Won!")
        user +=1

    elif user_input=='paper' and computer_pick=='Rock':
        print("You Won")
        user +=1

    elif user_input=='Scissor' and computer_pick=='paper':
        print('You Won!')
        user +=1

    else:
        print("You Lost!!!")
        comp +=1
    
print('You Won',user, 'times')
print('The Computer Won',comp,'times')
print('Good Byeeeee!!')