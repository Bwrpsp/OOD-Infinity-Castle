from AvlTree import AVLTree
from primegen import SieveOfEratosthenes,get_prime_nth,primenth
from room import process_room_number
from demon import generate_demon_id
import time
from ascii import muzan,logo,clear
from tqdm import tqdm
from performance_tracker import PerformanceTracker
from castle_export import export_castle_to_csv, import_castle_from_csv

clear()
logo()
initial = int(input("\nPlease enter the initial demons amount : "))
clear()
muzan()
logo()
print("\n======Building Castle======\n")
castle = AVLTree()
for i in tqdm(range(initial)):
    castle.insertRoom((i+1,generate_demon_id(0,0,i+1)))

print("\n=====Finish Building=====")
time.sleep(0.2)
clear()

# Initialize performance tracker
tracker = PerformanceTracker()

def help():
    logo()
    print("\n\nMuzan's infinity castle")
    print("key input:\n")
    print("1 Show all demons in castle")
    print("2 Add demon(s)")
    print("3 Remove demon")
    print("4 search demon by room number")
    print("5 Export castle data to CSV")
    print("6 Export performance metrics to CSV")
    print("7 View performance summary")
    print("\nHelp if you forget the key")
    print("quit if you want to exit program (all data would be lost)\n")




help()
key = input("\nplease enter you command to Nakime : ")
clear()
lot = 1
while(1):
    try:
        helped = False
        if key == '1':
            tracking = tracker.start_tracking("Show all demons")
            
            logo()
            print("\n==== Fetching data ====\n")
            lst = castle.get_all()
            clear()


            logo()
            print("\nAll demons in this castle are :\n\n")
            for demon in lst:
                print(f"Room: {demon.num}           Demon's ID : {demon.demon}")

            metric = tracker.end_tracking(tracking)
            print(f"\n[Performance] Time: {metric['execution_time']}s | RAM: {metric['end_ram_mb']}MB")
            
            tmp = input("\nPress enter to continue : ")
            clear()


        elif key=='2':
            logo()
            print("Please choose method of adding demon : ")
            print("1 : adding n demon(s)")
            print("2 : adding inf demons")
            print("3 : adding inf demons on n bus(es)")
            print("4 : adding inf demons on inf buses")
            print("5 : adding demon manually (assigned room number)")

            method = int(input("\nEnter input : "))
            clear()

            if method == 1:
                tracking = tracker.start_tracking("Add n demons")
                
                logo()
                n = int(input("Enter amount of demon : "))

                print("\nAdding demon . . .")

                castle.move_room(1,n)
                for i in tqdm(range(n)):
                    castle.insertRoom((i+1,generate_demon_id(lot,1,i+1)))

                lot+=1
                metric = tracker.end_tracking(tracking)
                print("\nAdding done!!")
                print(f"[Performance] Time: {metric['execution_time']}s | RAM Change: {metric['ram_change_mb']:+.2f}MB")
                cont = input("\nEnter to continue  : ")
                clear()


            elif method == 2:
                tracking = tracker.start_tracking("Add inf demons")
                
                logo()
                n = int(input("Enter amount of demon (inf) : "))

                print("\nAdding demon . . .")

                castle.move_room(2,1)
                for i in tqdm(range(n)):
                    castle.insertRoom((i*2+1,generate_demon_id(lot,2,i+1)))

                lot+=1
                metric = tracker.end_tracking(tracking)
                print("\nAdding done!!")
                print(f"[Performance] Time: {metric['execution_time']}s | RAM Change: {metric['ram_change_mb']:+.2f}MB")
                cont = input("\nEnter to continue  : ")
                clear()

            # /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

            elif method == 3:
                tracking = tracker.start_tracking("Add inf demons on n buses")
                
                logo()
                bus = int(input("Enter amount of bus : "))
                # n = int(input("Enter amount of demon (inf) : "))
                n = list(map(int,input('Enter amount of demon (inf) : ').split()))

                

                print("\nAdding demon . . .")

                castle.move_room(2,bus)
                # for i in tqdm(n):
                for i in tqdm(range(bus)):
                    for j in range(n[i]):
                        castle.insertRoom(((j*(bus+1))+i+1,generate_demon_id(lot,3,j+1,i+1)))

                lot+=1
                metric = tracker.end_tracking(tracking)
                print("\nAdding done!!")
                print(f"[Performance] Time: {metric['execution_time']}s | RAM Change: {metric['ram_change_mb']:+.2f}MB")
                cont = input("\nEnter to continue  : ")
                clear()

            # /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

            elif method == 4:
                tracking = tracker.start_tracking("Add inf demons on inf buses")
                
                logo()
                bus = int(input("Enter amount of bus (inf): "))
                # n = int(input("Enter amount of demon (inf) : "))
                n = list(map(int,input('Enter amount of demon (inf) : ').split()))

                print("\nAdding demon . . .")

                castle.move_room(3)
                for i in tqdm(range(bus)):
                    for j in range(n[i]):
                        castle.insertRoom((process_room_number(3,i+1,j+1),generate_demon_id(lot,4,j+1,i+1)))

                lot+=1
                metric = tracker.end_tracking(tracking)
                print("\nAdding done!!")
                print(f"[Performance] Time: {metric['execution_time']}s | RAM Change: {metric['ram_change_mb']:+.2f}MB")
                cont = input("\nEnter to continue  : ")
                clear()

            # /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

            elif method == 5:
                tracking = tracker.start_tracking("Add demon manually")
                
                logo()
                n = int(input("Enter room number : "))

                print("\nAdding demon . . .")

                if castle.search(n):
                    print("This room is occupied !!!!")
                else:
                    castle.insertRoom((n,generate_demon_id(lot,5,1)))

                lot+=1
                metric = tracker.end_tracking(tracking)
                print("\nAdding done!!")
                print(f"[Performance] Time: {metric['execution_time']}s | RAM Change: {metric['ram_change_mb']:+.2f}MB")
                cont = input("\nEnter to continue  : ")
                clear()
            else:
                logo()
                print("!!! Wrong command !!!")
                cont = input("\nEnter to continue  : ")
                clear()



        elif key=='3':
            tracking = tracker.start_tracking("Remove demon")
            
            logo()
            n = int(input("Enter room number to be remove : "))
            removed = castle.removeRoom(n)

            if removed:
                print(f"Success fully remove room {removed.num}. The demon inside is {removed.demon}")
            else:
                print("Error : Room not found!!")

            metric = tracker.end_tracking(tracking)
            print(f"[Performance] Time: {metric['execution_time']}s | RAM Change: {metric['ram_change_mb']:+.2f}MB")
            
            cont = input("\nEnter to continue  : ")
            clear()
    
        elif key=='4':
            tracking = tracker.start_tracking("Search demon")
            
            logo()
            n = int(input("Enter room number to be search : "))
            search = castle.search(n)

            if search:
                print(f"Found room {search.num}. The demon inside is {search.demon}")
            else:
                print("Error : Room not found!!")

            metric = tracker.end_tracking(tracking)
            print(f"[Performance] Time: {metric['execution_time']}s | RAM: {metric['end_ram_mb']}MB")
            
            cont = input("\nEnter to continue  : ")
            clear()

        elif key=='5':
            tracking = tracker.start_tracking("Export castle to CSV")
            
            logo()
            success, result = export_castle_to_csv(castle)
            
            if success:
                print(f"\n✓ Castle data exported successfully!")
                print(f"File saved as: {result}")
                print(f"Total rooms exported: {len(castle.get_all())}")
            else:
                print(f"\n✗ Export failed: {result}")
            
            metric = tracker.end_tracking(tracking)
            print(f"[Performance] Time: {metric['execution_time']}s")
            
            cont = input("\nPress enter to continue : ")
            clear()
        
        elif key=='6':
            logo()
            success, result = tracker.export_to_csv()
            
            if success:
                print(f"\n✓ Performance metrics exported successfully!")
                print(f"File saved as: {result}")
            else:
                print(f"\n✗ Export failed: {result}")
            
            cont = input("\nPress enter to continue : ")
            clear()
        
        elif key=='7':
            logo()
            print(tracker.get_summary())
            
            if tracker.metrics:
                print("\nRecent Commands:")
                print(f"{'Command':<30} {'Time (s)':<12} {'RAM Change (MB)':<15}")
                print("-" * 60)
                for metric in tracker.metrics[-10:]:  # Show last 10
                    print(f"{metric['command']:<30} {metric['execution_time']:<12.4f} {metric['ram_change_mb']:+15.2f}")
            
            cont = input("\nPress enter to continue : ")
            clear()

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
        clear()
    except:
        clear()
        print("Something went wrong !!")
        key = ""