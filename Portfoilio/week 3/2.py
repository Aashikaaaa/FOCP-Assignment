"""Write a program that simulates the way in which a user might choose a password.
The program should prompt for a new password, and then prompt again. If the two
passwords entered are the same the program should say "Password Set" or
similar, otherwise it should report an error"""

password1 = input("Enter a new password: ")
password2= input("Enter a password for conformation: ")

def set_password():
    
    if password1 == password2:
        print("Password Set")
    else:
        print("Error, Please try again.")    

set_password()