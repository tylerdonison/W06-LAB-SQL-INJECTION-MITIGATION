#Main file, calls different levels of mitigation from the Strong and Weak Mitigation files, 
#calls from constants according to needs. Can run automatic tests, iterating through each
#type of mitigation, and attack.

from Query import genQuery
from Weak_mitigation import genQueryWeak
from Strong_mitigation import genQueryStrong
import Constants

def main():
    #main function, iterates through tests.
    usernameList = [] #creates a username list which will be replaced for tests
    passwordList = [] #creates a password list which will be replaced for tests
    for attackNumber in range(0,5): #determine which attack, [valid, tautology, union, additional state, comment] to test.
        usernameList, passwordList = AttacksInteration(attackNumber) #generates matching lists by attack.
        for mitigation in range(0,3): #iterates through different mitigations, nothing, weak, then strong. 
            for instance in range(0,3): #iterates through three different test cases for each mitigation and attack combination.
                MitigationIteration(usernameList[instance], passwordList[instance], mitigation)


def MitigationIteration(username, password, mitigation):
    #function that iterates through the types of tests, starting with no mitigation, 
    #then weak mitigation, and finally strong mitigation
    if mitigation == 1:
        username, password = genQueryWeak(username, password)
        print("---Using weak mitigation.")
    elif mitigation == 2:
        username, password = genQueryStrong(username, password)
        print("---Using strong mitigation.")
    else:
        print("---Using no mitigation")
    genQuery(username, password)
    input("Push enter to continue. ")

def AttacksInteration(attack):
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