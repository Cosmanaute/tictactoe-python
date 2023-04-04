import os

bord = {'1': ' ' , '2': ' ' , '3': ' ' ,
        '4': ' ' , '5': ' ' , '6': ' ' ,
        '7': ' ' , '8': ' ' , '9': ' ' }

def run():
    
    os.system('cls') #clearer konsollen
    total_moves = 0 
    active_player = 'o'
    
    for i in range(10):
        printBord(bord) #printer bord og gir inn bord som argument
        print(f"Det er {active_player} sin tur: ")
        move_where = input('move: ') #spør etter plass på flytte
        if bord[move_where] == ' ': #sjekker om plassen er ledig
            bord[move_where] = active_player #plasserer på valgt plass
            total_moves +=1
        else:
            os.system('cls')
            print('Cannot move there!')
            continue

        if total_moves < 9: #sjekker hvem som vinner
            if bord['1'] == bord['2'] == bord['3'] and bord['1'] != ' ':
                print(f"{active_player} has won!")
                printBord(bord)
                break
            elif bord['4'] == bord['5'] == bord['6'] and bord['4'] != ' ':
                print(f"{active_player} has won!")
                printBord(bord)
                break
            elif bord['7'] == bord['8'] == bord['9'] and bord['7'] != ' ':
                print(f"{active_player} has won!")
                printBord(bord)
                break
            elif bord['1'] == bord['4'] == bord['7'] and bord['1'] != ' ':
                print(f"{active_player} has won!")
                printBord(bord)
                break
            elif bord['2'] == bord['5'] == bord['7'] and bord['2'] != ' ':
                print(f"{active_player} has won!")
                printBord(bord)
                break
            elif bord['3'] == bord['6'] == bord['9'] and bord['3'] != ' ':
                print(f"{active_player} has won!")
                printBord(bord)
                break
            elif bord['1'] == bord['5'] == bord['9'] and bord['1'] != ' ':
                print(f"{active_player} has won!")
                printBord(bord)
                break
            elif bord['3'] == bord['5'] == bord['7'] and bord['3'] != ' ':
                print(f"{active_player} has won!")
                printBord(bord)
                break
        else:
            print("Uavgjort!")
            printBord(bord)
            break
        if active_player == 'o': #bytter hvem sin tur det er 
            active_player = 'x'
            os.system('cls') #bruker os.system('cls') til å cleare terminalen mellom alle printene
        elif active_player == 'x':
            os.system('cls')
            active_player = 'o'    
        
def printBord(brett):
    
    print("---------")
    print(brett['1'] + ' | ' + brett['2'] + ' | ' + brett['3'])
    print("---------")
    print(brett['4'] + ' | ' + brett['5'] + ' | ' + brett['6'])
    print("---------")
    print(brett['7'] + ' | ' + brett['8'] + ' | ' + brett['9'])
    print("---------")

if __name__ == '__main__':
    run()