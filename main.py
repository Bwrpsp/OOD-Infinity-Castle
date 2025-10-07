from AvlTree import AVLTree
from primegen import SieveOfEratosthenes,get_prime_nth,primenth
from room import process_room_number
from demon import generate_demon_id
import os
import time
from ascii import muzan,logo

os.system("cls")
logo()
initial = int(input("\nPlease enter the initial demons amount : "))
os.system('cls')
muzan()
logo()
print("\n======Building Castle======\n")
castle = AVLTree()
for i in range(initial):
    castle.insertRoom((i+1,generate_demon_id(0,0,i+1)))

time.sleep(1)
print("\n=====Finish Building=====")
time.sleep(0.2)
os.system("cls")


def help():
    logo()
    print("\n\nMuzan's infinity castle")
    print("key input:\n")
    print("1 Show all demons in castle")
    print("2 Add demon(s)")
    print("3 Remove demon")
    print("4 search demon by room number")
    print("5 search room number of demon's id")
    print("\nHelp if you forget the key")
    print("quit if you want to exit program (all data would be lost)\n")




help()
key = input("\nplease enter you command to Nakime : ")
os.system('cls')
lot = 1
while(1):
    helped = False
    if key == '1':
        logo()
        print("\n==== Fetching data ====\n")
        lst = castle.get_all()
        os.system("cls")


        logo()
        print("\nAll demons in this castle are :\n\n")
        for demon in lst:
            print(f"Room: {demon.num}           Demon's ID : {demon.demon}")
        
        tmp = input("\nPress enter to continue : ")
        os.system("cls")


    elif key=='2':
        logo()
        print("Please choose method of adding demon : ")
        print("1 : adding n demon(s)")
        print("2 : adding inf demons")
        print("3 : adding inf demons on n bus(es)")
        print("4 : adding inf demons on inf buses")

        method = int(input("\nEnter input : "))
        os.system("cls")

        if method == 1:
            logo()
            n = int(input("Enter amount of demon : "))

            print("\nAdding demon . . .")

            castle.move_room(1,n)
            for i in range(n):
                castle.insertRoom((i+1,generate_demon_id(lot,1,i+1)))

            lot+=1
            print("\nAdding done!!")
            cont = input("\nEnter to continue  : ")
            os.system("cls")
            

        elif method == 2:
            logo()
            n = int(input("Enter amount of demon (inf) : "))

            print("\nAdding demon . . .")

            castle.move_room(2,1)
            for i in range(n):
                castle.insertRoom((i*2+1,generate_demon_id(lot,2,i+1)))

            lot+=1
            print("\nAdding done!!")
            cont = input("\nEnter to continue  : ")
            os.system("cls")


        elif method == 3:
            logo()
            bus = int(input("Enter amount of bus : "))
            n = int(input("Enter amount of demon (inf) : "))

            print("\nAdding demon . . .")

            castle.move_room(2,bus)
            for i in range(n):
                for j in range(bus):
                    castle.insertRoom(((i*(bus+1))+j+1,generate_demon_id(lot,3,i+1,j+1)))
            
            lot+=1
            print("\nAdding done!!")
            cont = input("\nEnter to continue  : ")
            os.system("cls")
        elif method == 4:
            logo()
            bus = int(input("Enter amount of bus (inf): "))
            n = int(input("Enter amount of demon (inf) : "))

            print("\nAdding demon . . .")

            castle.move_room(3)
            for i in range(n):
                for j in range(bus):
                    castle.insertRoom((process_room_number(3,j+1,i+1),generate_demon_id(lot,4,i+1,j+1)))

            lot+=1
            print("\nAdding done!!")
            cont = input("\nEnter to continue  : ")
            os.system("cls")
        else:
            logo()
            print("!!! Wrong command !!!")
            cont = input("\nEnter to continue  : ")
            os.system("cls")



    elif key=='3':
        pass
    elif key=='4':
        pass

    elif key.lower()=='quit':
        logo()
        confirm = input("\nWarnig Quiting mean all data would be lost do u want to preceed [y/N] : ")
        if confirm.lower() == 'y':
            break
    elif key == "Muzan":
        muzan()
    else:
        help()
        helped = True


    
    if not helped:
        logo()
    key = input("\nplease enter you command to Nakime : ")
    os.system('cls')