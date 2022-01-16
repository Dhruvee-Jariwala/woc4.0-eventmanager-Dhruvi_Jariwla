phoneBook ={}

def store():
    print("========================================")
    name = input("Enter the name : ")
    contact = []
    print("Enter contact number (if more than 1 contact number than give space between them) : ")
    contact = list(input(">>> ").strip(" ").split(" "))
    phoneBook[name] = contact
    print("Contact of " + name + " is SAVED")
    print("========================================")

def searchKeyword():
    print("========================================")
    key = input("Enter the keyword : ")
    flag = 0
    for name in phoneBook.keys():
        if key in name:
            flag = 1
            print(name + " --> " , end = " ")
            print(*phoneBook[name], sep=", ")

    if flag == 0:
        print("No Such Contact exist")
    print("========================================")

def getNumber():
    print("========================================")
    name = input("Enter the name whose contact you want : ")
    if name in phoneBook.keys():
        print(name + " --> ", end=" ")
        print(*phoneBook[name], sep=", ")
    else:
        print("No Such Contact exist")

    print("========================================")

def seeAllContacts():
    print("========================================")
    for contacts in phoneBook:
        print(contacts + " --> ", end=" ")
        print(*phoneBook[contacts], sep=", ")
    print("========================================")

if __name__ == '__main__':
    moreOperation = 1
    while(moreOperation):
        print("-----------------------------------------------------------------------------------")
        print("What operation do you want to perform?")
        print("1. Store contact")
        print("2. Search contact from a keyword")
        print("3. Get number of a person")
        print("4. See All Contacts")
        choice = int(input("Enter your choice >>>> "))

        if(choice == 1):
            moreData = 1
            while (moreData):
                store()
                moreData = int(input("Store more data? \n Press 1 for YES \n Press 0 for NO. >>>>>>>> "))
        elif(choice == 2):
            searchKeyword()
        elif(choice == 3):
            getNumber()
        elif(choice == 4):
            seeAllContacts()

        print("-----------------------------------------------------------------------------------")
        moreOperation = int(input("Want to perform more Operation? \n Press 1 for YES \n Press 0 for NO. >>>>>>>> "))





