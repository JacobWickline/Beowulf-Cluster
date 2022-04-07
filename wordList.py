import time

class wordlistAttack:
    def __init__(self, hPassword): #initialize and get user password
        self.h = hPassword
        
    def crack(self):
        timeStart = time.perf_counter() #start time
        f = open("rockyou.txt", "r") #open wordlist
        try: #catch UnicodeDecodeError
            for line in f: #for each word in the wordlist
                cPassword = line.rstrip("\n") #strip new line characters
                if self.h == cPassword: #if user password is the same as the word in list
                    timeEnd = time.perf_counter() #end timer
                    totalTime = timeEnd - timeStart #calculate total time to crack
                    print("Time to wordlist crack: " + str(totalTime)) #print total time
                    return True #tell main password is cracked
            return False #otherwise tell main password is not cracked
        except UnicodeDecodeError: #if UnicodeDecodeError is caught
            timeEnd = time.perf_counter() #end timer
            totalTime = timeEnd - timeStart #calculate total time to failure
            print("Time to wordlist failure: " + str(totalTime)) #print total time
            return False #tell main password is not cracked