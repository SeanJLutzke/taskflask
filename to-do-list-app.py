#import sys so it's possible to quit the app
import sys

#Declare global variables
tasklist = []
choppingBlock = ""

#Define Functions
def addTask():
    task = str.upper(input("Add a task: "))
    tasklist.append(task)

def viewTasks():
    if not tasklist:
        print("You need to add a task first.")
    else:
        print(tasklist)

def deleteTask():
    x = 0
    if not tasklist:
        print("You need to add a task first.")
    else:
        while x < len(tasklist):
            print(f"{x}: {tasklist[x]}")
            x += 1 
        choppingBlock = input("Which task would you like to delete? (Enter the index number and press enter.)")
        try:
            tasklist.pop(int(choppingBlock))
        except IndexError:
            print("That number isn't valid.")
        except ValueError:
            print("That is not a number.")
        else:
            print("Task deleted.")
        finally:
            print("End of deletion.")

def quitApp():
    print("Then go away")
    sys.exit()

#Main loop so that the code actually runs
def main():
    while True:
        choice = str.upper(input("Welcome to TaskFlask. Press A to add a task, V to view tasks, D to delete a task, or Q to quit:"))
        if choice == "A":
            addTask()        
        elif choice == "V":
            viewTasks()        
        elif choice == "D":
            deleteTask()
        elif choice == "Q":
            quitApp()
        else:
            print("Invalid entry. Please try again.")

if __name__ == "__main__":
    main()