#organizer

def add_event():
    print("Insert your memo and date:")
    memo = input()
    with open("dane.txt",'a') as file: #creates a file and adds a line
        file.write(memo+"\n")

def read_memos():
    with open("dane.txt") as f:
        lines = f.readlines()
        lines = [x.strip() for x in lines] #removed /n from the file, so the end of line doesn't show
        for line in lines:
            print(line)


print("This is your event planner: \n 1.Show your events \n 2.Add an event \n 3.Quit program")
option = input()

if option == "1":
    read_memos()
elif option == "2":
    add_event()

