import datetime as dt
import mod_rule2
import mod_rule1

# statements
s1 = "enter a word which is not used before by either player or computer"
s2 = "player is disqualified due to rule 3"
s3 = "player has entered the word"
s4 = 'enter a word with in a seconds '
s5 = 'player is disqualified due to rule 4'
s6 = "No more English words in Computer's memory......\nCOMPUTER HAS LOST THE GAME"
s7 = 'player is disqualified due to rule 2'

output = mod_rule1.transform1('word2.txt')
comp_list = output
list4 = open('dictionary.txt', 'r')
list5 = list4.read().split('\n')
len5 = len(list5)
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
used = []
input2 = []
computer1 = 0
total1, player = 0, 0
total2, computer = 0, 0

print("**********WELCOME TO WORD GAME **********")
print("BEFORE YOU BEGIN THE GAME REMEMBER 4 RULES:\n1) Word should be an English word")
print("2) Starting letter should be same as ending letter of Player/Computer")
print("3) Word should not be repeated\n4) Word should be input before 30 seconds")
print("\n")

for i in range(0, len5, 1):
    # PLAYERS TURN
    # rule4
    timeout = 30
    today1 = dt.datetime.now()
    input1 = input(s4 + str(timeout) + " : ")
    today2 = dt.datetime.now()
    time1 = (today2 - today1).seconds
    if time1 > timeout:
        print(s5)
        break

    # rule1
    if input1 not in list5:
        print("WRONG SPELLING ..... TRY AGAIN")
        input1 = input()
        if input1 not in list5:
            print("WRONG SPELLING...DISQUALIFIED")
            break

    # rule2
    if i > 0:
        last_char = input2[-1]
        disqualified = mod_rule2.rule2(last_char, input1)
        if disqualified:
            print(s7)
            break

    # rule3
    if input1 in used:
        print(s1)
        input1 = input()
        if input1 in used:
            print(s2)
            break
        else:
            used.append(input1)
    else:
        used.append(input1)

    # COMPUTERS TURN
    # computers input which follows rule1 and rule2
    last_char = input1[-1]
    position1 = alpha.index(last_char)
    temp_list1 = comp_list[position1]
    input2 = temp_list1[0]
    first_char = input2[0:1]
    index1 = alpha.index(first_char)
    current_list = comp_list[index1]
    if input2 in used or (input1 == input2):
        if input2 in current_list:
            current_list.remove(input2)
            if current_list == []:
                computer1 = 1
                print(s6)
                break
            input2 = comp_list[position1][0]
            used.append(input2)
    else:
        used.append(input2)

    # print
    print(input1, "-", input2)

    # total point
    player = len(input1)
    total1 += player
    computer = len(input2)
    total2 += computer

# display result
print("SCORE OF PLAYERS")
print("PLAYER : ", total1)
print("COMPUTER : ", total2)
if computer1 == 1:
    print("\n PLAYER IS THE WINNER")
else:
    if total1 > total2:
        print("\n PLAYER IS THE WINNER")
    else:
        print("\n COMPUTER IS THE WINNER")
