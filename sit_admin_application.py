# ICTPRG302 - Assessment Task 3: Application Development 
# Written by Braydon Pettit on "8/03/24 - 18/03/24"
# SIT have requested a menu as outlined in the "sit_specifications_v1.05.pdf"
# This is a simple menu which allows the user to print the Patient List, Add Patients, and Delete Patients from the List

__author__ = "Braydon Pettit"
__version__ = "0.1.3"
__date__ = "16/03/2024"

# importing json module allows us to be able to read our json file and open from it
# importing sys module allows us to call on the "sys.exit()" function which will close out program
# importing time module. this is the module that allows to call on "time.sleep" to allow us to introduce a delay into our menu

import json
import sys
import time

# defines "patient_list" as the "patients.json" file, and opens it in "read" mode

file = open("patients.json", 'r')
patient_list = json.load(file)
file.close()

# print_patient() function

def print_patient():
    
    # creates a variable "x = 1" to use as a counter to number the patient and "sorted" function to sort the patient alphabetically
    
    x = 1 
    sorted_patient = sorted(patient_list)
    print("\nPrinting Patient List...\n")
    time.sleep(1.5)
    
    # uses a "for loop" to iterate over the sorted list, prints the patient number and name "{x}. {patients}" and increases the counter by 1 for numbering the next patient "x +=1"
    
    for patients in sorted_patient:
        print(f"{x}. {patients}")
        time.sleep(0.2)
        x += 1
    print()
    
# add_patient function

def add_patient():
    
    # "while True:" loop asks user to input a string "lastname" and "firstname" 
    
    while True:
        print("\nEnter New Patient ->\n")
        lastname = str(input("Lastname: "))
        firstname = str(input("Firstname: "))
        
        # checks if lastname and firstname are alphabetic characters, combines {lastname} {firstname} to create a fullname and appends and writes the "patient_list" return will take us back to the menu
         
        if lastname.isalpha() and firstname.isalpha():
            print("\nAdding Patient...")
            time.sleep(1.5)
            print("\nPatient has been added to the patient list.\n")
            time.sleep(1.5)
            add_patient = f"{lastname} {firstname}"
            patient_list.append(add_patient)
            write()
            return
        
        # "isalpha" stops the user from entering numbers as the patient if they do they will recieve the else statement
        
        else:
            print("\nInvalid Input. Please enter alphabetic characters for both first and lastnames.")
            time.sleep(1.5)
            
# del_patient function

def del_patient():
    
    # "while True:" loop creates a variable "x = 1" to use as a counter to number the patient and "sorted" function to sort the patient alphabetically
    
    while True:
        x = 1 
        sorted_patient = sorted(patient_list)
        print("\nDelete Patient ->\n")
        time.sleep(1.5)
        
        # prints the patient number and name "{x}. {patients}" and increases the counter by 1 for numbering the next patient "x +=1"
        
        for patients in sorted_patient:
            print(f"{x}. {patients}")
            time.sleep(0.2)
            x +=1
            
        # creates a variable called "delete_patient" asks user to input the number of the patient they want to delete or "0 to cancel"    
            
        try:
            delete_patient = int(input("\nEnter the patient number you want to delete (0 to cancel): "))
            time.sleep(1.5)
            delete_patient = int(delete_patient)
            
            # if the index to delete is within a valid range of "patient" indexes, then it'll retrieve the patient, then removes the patient and lets the user know then updates the list and returns back to the menu
            
            if 1 <= delete_patient <= len(sorted_patient):
                print()
                print("Deleting Patient...")
                time.sleep(1.5)
                deleted_patient = sorted_patient[delete_patient - 1]
                patient_list.remove(deleted_patient) 
                write()
                print(f"\nPatient '{deleted_patient}' has been deleted.\n")
                time.sleep(1.5)
                return
            
            # allows the user to enter "0" returning them back to the "SIT Data Entry Menu" if they enter text they will get "ValueError"     
            
            else:
                print("\nReturning to SIT Data Entry Menu...\n")
                time.sleep(1.5)
                return
            
        except ValueError:
                print("\nInvalid Input. Please enter a valid number...")
                time.sleep(1.5)
        
# function that closes the menu with "sys.exit()" but also saves the patient file "write()" function, prints a saving message and exiting message.

def exit():
    write()
    print("\nSaving Patient List...")
    time.sleep(1.5)
    print("\nExiting SIT Data Entry Menu...\n")
    time.sleep(1.5)
    sys.exit()

# "menu" function will print to the console when called upon, prints a simple menu and options of what the user can the input.

def menu():
    print("SIT Data Entry Menu")
    print("=" * 27)
    print("1: Print Patient's List")
    print("2: Add Patient")
    print("3: Delete Patient")
    print("4: Exit")
    print("=" * 27)

# "select(option)" function which is the main menu input, user can input 1 - 4 or they will get an error message.

def select(option):
    if option == 1:
        print_patient()
        
    elif option == 2:
        add_patient()
        
    elif option == 3:
        del_patient()
        
    elif option == 4:
        exit()
        
    else:
        print("\nInvalid Input. Please enter a valid number...\n")
        time.sleep(1.5)

# "write()" function to update the patient list, this opens our file in "w" or "write" to be able to append the patient list or remove a patient.

def write():
    file = open("patients.json", "w")
    json.dump(patient_list, file)
    file.close()
   
# repeat equals true while repeat is true is loop code, we can use this to repeat our menu, this is our main program
    
repeat=True
while repeat == True:
    
    # calls on the menu() and asks user to input a number then it uses our "select(option)" function which is defined above,
    
    try:
        menu()
        option = int(input("Enter your menu selection: "))
        select(option)
    
    # if the user tries to enter text or a number outside of what there options are they will get a "ValueError"
        
    except ValueError:
        print("\nInvalid Input. Please enter a valid number...\n")
        time.sleep(1.5)