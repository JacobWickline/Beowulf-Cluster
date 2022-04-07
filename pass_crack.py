import string
import time
password = input("Please enter a password: ")
file = ("rockyou.txt")

def iterative(password):
    alphabet = string.ascii_letters + string.punctuation + string.digits
    passwordLen = 1

    while True:
        possibilities = len(alphabet) ** passwordLen
        #print(possibilities)
        #input()
        for i in range(possibilities):
            theWord = ""
            val = i
            for j in range(passwordLen):
                ch = val % len(alphabet)
                theWord += alphabet[ch]
                val = val // len(alphabet)
            #print(theWord)
            if theWord == password:
                print("Found it!")
                return
        passwordLen += 1

def search(file):
    file_open = open(file, "r", encoding = "latin-1")
    password_found = False
    start1 = time.perf_counter()

    for i in file_open:
        if i == password:
            password_found = True
            end1 = time.perf_counter()
    end2 = time.perf_counter()

    if password_found == True:
        time1 = end1 - start1
        print("Password was found in the list")
        print("Time Elapsed: ", time1)

    else:
        time2 = end2 - start1
        print("Password was not found in the list")
        print("Time Elapsed: ", time2)

    file_open.close()

start = time.perf_counter()
iterative(password)
end = time.perf_counter()
time = end - start

print("Time Elapsed: ", time)

search(file)
