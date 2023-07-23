import random
#text files' names
DL = 'DailyList.txt'
C = 'Chores.txt'

#lists
daily_list = []
chores_list = []

def viewingChores():
    print('(Viewing Chores...)')
    print('\nChores:\n')
    for i in chores_list:
        print('> '+ i )

def singleChore():
    print('(Single Chore...)')
    print('\n' + random.choice(daily_list))

def generateList():
    print('(Generating New List...)')
    for h in daily_list:
        chores_list.append(h)
    daily_list.clear()
    n = int(input('\nHow many chores would you like? '))
    new = random.sample(chores_list, n)
    for i in new:
        daily_list.append(i)
        for j in chores_list:
            if i == j:
                chores_list.remove(j)

    rewriteTextFile(DL, daily_list)
    rewriteTextFile(C, chores_list)

def removeChore():
    print('(Removing Chore...)')
    c = input('\nEnter Chore to Delete: ')
    daily_list.remove(c.lower() + '\n')

def addChore():
    print('(Adding New Chore...)')
    c = input('\nEnter New Chore: ')
    daily_list.append(c.lower() + '\n')

def viewList():
    print('(Viewing List...)')
    print('\nList:\n')
    for i in daily_list:
        print('> '+ i )

def rewriteTextFile(filename, list):
    file = open(filename, 'w')
    for i in list:
        file.write(i)
    file.close()

def rewriteList(list, filename):
    file = open(filename, 'r')
    for i in file:
        list.append(i)
    file.close()

def main():
    flag = 1
    rewriteList(chores_list, C)
    rewriteList(daily_list, DL)

    while(flag!=0):
        print('\nHello! What would you like to do?\n------------------------------')
        print('0: Exit\n1: View List\n2: Add New Chore\n3: Remove Chore\n4: Generate New List\n5: Single Chore \n6: View Chores\n7: Move Chore')
        x = int(input('\nYou Selected: '))
    
        match x:
            case 0:
                print('(Exiting...)')
                flag = 0
                rewriteTextFile(DL, daily_list)
                rewriteTextFile(C, chores_list)
            case 1:
                viewList()
            case 2:
                addChore()
            case 3:
                removeChore()
            case 4:
                generateList()
            case 5:
                singleChore()
            case 6:
                viewingChores()
            case 7:
                print('(Moving Chore...)')
            case _:
                print('Error')


main()