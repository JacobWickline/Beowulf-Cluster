from bruteForce import bruteForceAttack
from wordList import wordlistAttack

# Sources:
# https://www.kite.com/python/answers/how-to-import-a-class-from-another-file-in-python for re-learning how to import classes
# https://docs.python.org/3/tutorial/classes.html for documentation on classes
# https://docs.python.org/3/tutorial/inputoutput.html for documentation on I/O and file manipulation

userPassword = str(input("Enter your password: ")) #get user password
bfAttack = bruteForceAttack(userPassword) #initialize brute-force attack
attempts = bfAttack.crack() #start brute-force crack, return number of attempts.

print("Password brute-force cracked in " + str(attempts) + " attempts using brute-force.") #print number of attempts

wlAttack = wordlistAttack(userPassword) #initialize wordlist attack
isFound = wlAttack.crack() #start wordlist crack, return whether password is cracked

if isFound == True:
    print("Password was found in wordlist.")
else:
    print("Could not find password in wordlist.")

#times for brute-force attacks of different password lengths
#2 (6T): 1.5499999999946112e-05
#4 (7%jL): 2.3999999999801958e-05
#8 (6DKBrVL#): 3.829999999993561e-05
    
#time for word list attack using chocolate as password
#0.0002681999999998297