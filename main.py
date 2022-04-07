from mpi4py import MPI
import string
import time
import sys
import numpy as np

chunkSize = 4;
word = input("Enter a password: ")
lst = list(word)
temp = np.array_split(lst, chunkSize)

temp1 = temp[0]
temp2 = temp[1]
temp3 = temp[2]
temp4 = temp[3]

lst1 = temp1.tolist()
lst2 = temp2.tolist()
lst3 = temp3.tolist()
lst4 = temp4.tolist()

def concatenate(lst):
    string = ""
    for ch in lst:
        string += ch
    return string

lst1 = concatenate(lst1)
lst2 = concatenate(lst2)
lst3 = concatenate(lst3)
lst4 = concatenate(lst4)

comm = MPI.COMM_WORLD

size = MPI.COMM_WORLD.Get_size()
rank = MPI.COMM_WORLD.Get_rank()
name = MPI.Get_processor_name()

def bfCrack(segment):
    letterList = string.ascii_letters + string.digits + string.punctuation
    cpuWord = ""
    pos = 0
    attempts = 0
    while cpuWord != segment:
        for letter in letterList:
            attempts = attempts + 1
            if letter == segment[pos]:
                cpuWord = cpuWord + letter
                pos = pos + 1
                break
    return attempts

startTime = time.perf_counter()
if(comm.rank == 0):
    r1 = bfCrack(lst1)
elif(comm.rank == 1):
    r2 = bfCrack(lst2)
elif(comm.rank == 2):
    r3 = bfCrack(lst3)
elif(comm.rank == 3):
    r4 = bfCrack(lst4)
endTime = time.perf_counter()

totalTime = endTime - startTime

print("Found it!")
print("Time to crack: " + str(totalTime) + " seconds.")