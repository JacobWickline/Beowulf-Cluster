import string
import time

class bruteForceAttack:
    def __init__(self, hPassword): #initialize and get user password
        self.h = hPassword
        
    def crack(self):
        timeStart = time.perf_counter() #start time
        letterList = string.ascii_letters + string.digits + string.punctuation #create letter list
        c = "" #c refers to cpu password
        pos = 0 #start at first character in user's password
        attempts = 0 #count number of attempts
        while c != self.h: #until the cpu's password is the same as the user's
            for letter in letterList: #select 1 letter from the list at a time
                attempts = attempts + 1 #increase the number of attempts by 1
                if letter == self.h[pos]: #if the letter selected is the same as the first letter in the user's password
                    c = c + letter #add letter to result
                    pos = pos + 1 #move to next character in user's password
                    break #restart the for loop
        timeEnd = time.perf_counter() #end time
        totalTime = timeEnd - timeStart #calculate total time it took
        print("Time to brute-force crack: " + str(totalTime)) #print total time
        return attempts #return number of attempts to main
