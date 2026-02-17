#! /usr/bin/env python3

import random
import sys
import cowsay


import subprocess
def print_lolcat(text):
    # Use 'subprocess.Popen' to run the 'lolcat' command and capture its input
    process = subprocess.Popen(['lolcat'], stdin=subprocess.PIPE, stdout=sys.stdout, stderr=sys.stderr, text=True)
    # Communicate the text to lolcat's standard input
    stdout, stderr = process.communicate(input=text)

# print_lolcat(cowsay.cowsay("hi",cow="tux"))

def find_pos(a: int)-> int: 
    for i in range(0,9):
        if shuffled[i] == a:
            return i
        
def find_next(a: int, b: int) -> int:
    a=a+b
    if (a>=10):
        a=int(str(a)[0])+int(str(a)[1])
    return a

def print_current():
    print("\n\033[1;96mCurrent Order: ",end="")
    for i in shuffled:
        print(f"{i}" ,end=" ")
    print("\033[0m")

def reversing():
    global recording_stack, choice_stack
    if len(recording_stack) <2 :
        print("\n\033[1;31mDat's the wrong move!!!\033[0m")
        return 
    else:
        shuffled[recording_stack[-1]],shuffled[recording_stack[-2]] = shuffled[recording_stack[-2]],shuffled[recording_stack[-1]]
        print(f"\n\033[1;33mSwapping back {shuffled[recording_stack[-1]]} and {shuffled[recording_stack[-2]]}\033[0m")
        recording_stack.pop()
        recording_stack.pop()
        choice_stack.pop()

    if len(recording_stack) == 0:
        choice_stack=[]
        global first_time
        first_time = True
    else:
        global next_changer
        next_changer = find_next(shuffled[recording_stack[-1]],shuffled[recording_stack[-2]])
    
def starting():
    global shuffled
    global temp_arr
    qon=input("\n\033[1;31mDo you need the game description? (Y/n) \033[0m")
    print("\n\033[1;37m----------------------------\033[0m")
    if (qon == 'Y' or qon =='y' or qon == 'yes' or qon =="Yes"):
        print("\033[1;31mThis is a kind of sorting game.\033[0m")
        print("\033[1;33mYour goal is to sort the randomized 1~9 in ascending order.\033[0m")
        print("\033[1;93mYou'll have to pick two numbers first to swap them.\033[0m")
        print("\033[1;32mThen, the sum of the two numbers would be one of the two numbers we'll swap in the next round.\033[0m")
        print("\033[1;34mOfc the other number is chosen by you.\033[0m")
        print("\033[1;35mBTW, if the sum of the two numbers is bigger than 10, we'll sum the two digits of the summed-number and make it the new summed-number to swap.\033[0m")
        print("\033[1;36mAnyways, GL&HF :)\033[0m")
    else:
        print("\n\033[1;32mI'll regard this as you don't need that.\033[0m")
    mon = input("\n\033[1;31mWould you like manual ordering? (Y/n) \033[0m")
    if (mon == 'Y' or mon =='y' or mon == 'yes' or mon =="Yes"):
        while True:
            cmper = [0,0,0,0,0,0,0,0,0]
            conter=False
            temp_arr = list(map(int,input("\033[1;33mInput 1~9 in the order you want: \033[0m").split()))
            if (len(temp_arr)!= 9):
                print("\n\033[1;31mNot 9 numbers!!!\033[0m")
                continue

            for i in temp_arr:
                if i>=10 or i<=0:
                    print(f"\n\033[1;31m{i} is not accpeted!!!\033[0m")
                    conter=True
                    break
                cmper[i-1] = 1
            if conter:
                continue

            for i in cmper:
                if i != 1:
                    print(f"\n\033[1;31mNot having {i}!!!\033[0m")
                    conter=True
                    break
            if conter:
                continue

            for i in temp_arr:
                shuffled.append(i)

            break
    else:
        shuffled = random.sample(list(range(1,10)),9)
        while (shuffled == seikai):
            shuffled = random.sample(list(range(1,10)),9)
        for i in shuffled:
            temp_arr.append(i) 

    print("\n\033[1;37m----------------------------\033[0m\n")

def ending():
    print("\n\033[1;37m----------------------------\033[0m")
    print("\n\033[1;31mBye Bye QQ!!!\033[0m")
    print("\n\033[1;37m----------------------------\033[0m\n")
    sys.exit()

def first_round():
    print("\n\033[1;31mYou'll have to select two numbers to swap!!!\n(-1 to leave)\033[0m")
    while True:
        temp_input = int(input("First Number:"))
        if (temp_input == -1):
            ending()
        elif (temp_input >=10 or temp_input <= 0):
            print("\n\033[1;31mDat's the wrong number scope!!!\033[0m")
        else:
            recording_stack.append(find_pos(temp_input))
            choice_stack.append(temp_input)
            break
    while True:
        temp_input = int(input("Second Number:"))
        if (temp_input == -1):
            ending()
        elif (temp_input >=10 or temp_input <= 0):
            print("\n\033[1;31mDat's the wrong number scope!!!\033[0m")
            
        elif (shuffled[recording_stack[0]] == temp_input):
            print("\n\033[1;31mCan't select ZA same num!!!\033[0m")

        else:
            recording_stack.append(find_pos(temp_input))
            choice_stack.append(temp_input)
            break
    shuffled[recording_stack[0]],shuffled[recording_stack[1]] = shuffled[recording_stack[1]],shuffled[recording_stack[0]]

    global next_changer 
    next_changer = find_next(shuffled[recording_stack[0]],shuffled[recording_stack[1]])
    # print(recording_stack)

def other_round():
    global next_changer, choice_stack
    print(f"\n\033[1;31mYou'll have to select numbers to swap with \033[1;96m{next_changer} \033[1;31m!!!\n(-1 to escape, 0 to undo the previous move)\033[0m",)
    new_guy = int(input("A number: "))
    match new_guy:
        case 0:
            reversing()
            # print(recording_stack)
        case -1:
            ending()
        case 1|2|3|4|5|6|7|8|9:
            if (new_guy == next_changer):
                print("\n\033[1;31mCan't sway with the same one!!!\033[0m")
            else:
                choice_stack.append(new_guy)
                new_guy=find_pos(new_guy)
                naitei = find_pos(next_changer)
                shuffled[new_guy], shuffled[naitei] = shuffled[naitei],shuffled[new_guy]
                recording_stack.append(naitei)
                recording_stack.append(new_guy)
                next_changer = find_next(next_changer,shuffled[naitei])
            # print(recording_stack)
        case _:
            print("\n\033[1;31mDon't know what you're talking!\033[0m")

def winning():
    print_current()
    print_lolcat(cowsay.cowsay(f"Damnnn, You've WON with {len(choice_stack)} steps!!!",cow="tux"))
    print("Init order: ", end=" ")
    for i in temp_arr:
        print(i, end=" ")
    print("\nYour choices: ", end=" ")
    for i in choice_stack:
        print(i, end=" ")
    print()
    # print("\n\033[1;31mDamnnn, You've WON!!!\033[0m")

# main

seikai  = list(range(1,10))
shuffled = []
temp_arr = []

recording_stack=[]
choice_stack=[]
next_changer = -1

# main
starting()

first_time = True
while(shuffled != seikai):
    print("\n\033[1;37m----------------------------\033[0m")
    print_current()
    if (first_time):
        first_round()
        first_time = False
    else:
        other_round()
    print("\n\033[1;37m----------------------------\033[0m\n")

winning()
