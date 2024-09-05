# this code gives the user some context as to what this application is.
print("\nThis program is a Password Manager.")

#This is my decryption function that I have imported.
import decryptionfunction



#My encryption function.
def encryptionf(value):

    charSet="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`~!@#$%^&*()_-=|\}]{[\"':;?/>.<,"
    encText = "".join([charSet[(charSet.find(c)+3)%95] for c in value])
    return encText



choice = ''

# V starts a loop that runs until the user enters the value for quit.
while choice != 'q':
    # giving the user choices so that they can choose what they want to do/ quit the program.
    print("\n[1] Enter 1 to enter username.")
    print("[2] Enter 2 to enter password.")
    print("[3] Enter 3 to enter URL.")
    print("[q] Enter q to quit.")
    
    # asks for users choice
    choice = input("\nMake your choice ")
    
    # V requests user input.
    
    if choice == '1':
        username = input("\nEnter the username.\n")
        password= input("\nEnter password.\n")
        website= input("\nEnter the website.\n")
        encrypted_password=encryptionf(password) 
        with open ('testing.txt', 'a') as file:
            file.write(f"{username},{encrypted_password},{website}\n")

            


            
    elif choice == '2':
        print("option 2 selected.")
        with open("testing.txt","r") as file:
            for line in file:
                username, encrypted_password, website = line.strip().split(',')
                decrypted_password = decryptionfunction.my_decryption(encrypted_password)
                print(f"{username:<20}{website:<30}{decrypted_password}")
                
        


 
    elif choice == 'q':
        print("\nExiting the menu\n")
    else:
        print("\nInvalid option, please try again.\n")
        
# exiting program message.
print("Program exit.")







