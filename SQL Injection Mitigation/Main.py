#Main file, calls different levels of mitigation from the Strong and Weak Mitigation files, 
#calls from constants according to needs. Can run automatic tests, iterating through each
#type of mitigation, and attack.

from Query import genQuery
from Weak_mitigation import genQueryWeak
from Strong_mitigation import genQueryStrong
import Constants

def main():
    #main function, functions as a director.
    print("Group 6 Lab SQL Injection Mitigation")
    print("For automatic test iteration, enter 0")
    print("For manual test iteration, enter 1")
    user_input = input("")
    if user_input == "0":
        AutomaticTests()
    elif user_input == "1":
        ManualTests()
    print("Tests Complete")

def AutomaticTests():
    #automatically iterates through the tests.
    print("Starting Automatic Tests")
    usernameList = [] #creates a username list which will be replaced for tests
    passwordList = [] #creates a password list which will be replaced for tests
    for attackNumber in range(0,5): #determine which attack, [valid, tautology, union, additional state, comment] to test.
        usernameList, passwordList = AttacksIteration(attackNumber) #generates matching lists by attack.
        for mitigation in range(0,3): #iterates through different mitigations, nothing, weak, then strong. 
            for instance in range(0,3): #iterates through three different test cases for each mitigation and attack combination.
                MitigationIteration(usernameList[instance], passwordList[instance], mitigation)

def ManualTests():
    #allows manual selection of tests
    Testing = True
    while Testing:
        print("Please select the test")
        print("1. Valid Tests")
        print("2. Tautology Tests")
        print("3. Union Tests")
        print("4. Additional Statement Tests")
        print("5. Comment Tests")
        print("6. Quit")
        attack = int(input())-1
        if attack < 5:
            print("Please select the level of mitigation")
            print("1. No Mitigation")
            print("2. Weak Mitigation")
            print("3. Strong Mitigation")
            mitigation = int(input()) -1
            usernameList, passwordList = AttacksIteration(attack)
            for instance in range(0,3):
                MitigationIteration(usernameList[instance], passwordList[instance], mitigation)
        else:
            Testing = False

def MitigationIteration(username, password, mitigation):
    #function that iterates through the types of tests, starting with no mitigation, 
    #then weak mitigation, and finally strong mitigation
    if mitigation == 1:
        print(f"---Using weak mitigation against Username: {username}, Password: {password}.")
        username, password = genQueryWeak(username, password)
    elif mitigation == 2:
        print(f"---Using strong mitigation against Username: {username}, Password: {password}.")
        username, password = genQueryStrong(username, password)
    else:
        print(f"---Using no mitigation against Username: {username}, Password: {password}.")
    genQuery(username, password)
    input("-------Push enter to continue. ")

def AttacksIteration(attack):
    #function that iterates through the types of attacks, starting with valid, then
    #tautology, then union, then additional state, and finally comments.
    if attack == 0:
        usernames = Constants.validUsernames
        passwords = Constants.validPasswords
        input("-Running Valid Tests, push enter to continue. ")
    elif attack == 1:
        usernames = Constants.tautologyUsernames
        passwords = Constants.tautologyPasswords
        input("-Running Tautology Tests, push enter to continue. ")
    elif attack == 2:
        usernames = Constants.unionUsernames
        passwords = Constants.unionPasswords
        input("-Running Union Tests, push enter to continue. ")
    elif attack == 3:
        usernames = Constants.addStateUsernames
        passwords = Constants.addStatePasswords
        input("-Running Additional Statement Tests, push enter to continue. ")
    elif attack == 4:
        usernames = Constants.commentUsernames
        passwords = Constants.commentPasswords
        input("-Running Comment Tests, push enter to continue. ")
    return usernames, passwords
main()