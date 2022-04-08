from mpi4py import MPI
import string
import time
import sys
import numpy as np

#Getting information for nodes
comm = MPI.COMM_WORLD
size = MPI.COMM_WORLD.Get_size()
rank = MPI.COMM_WORLD.Get_rank()
name = MPI.Get_processor_name()

#Time for nodes
time_1 = 0
time_2 = 0
time_3 = 0
time_4 = 0

#Function for concatenate
def concatenate(lst):
    string = ""
    for ch in lst:
        string += ch
    return string

#Password cracking algorithm
def pass_crack(password_chunk):
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
            if theWord == password_chunk:
                print(name + " cracked the segment!")
                return
        passwordLen += 1

if(comm.rank == 0):
    chunkSize = 4
    word = input("Enter a password: ")
    lst = list(word)
    temp = np.array_split(lst, chunkSize)

    #Temp arrays for list
    temp1 = temp[0]
    temp2 = temp[1]
    temp3 = temp[2]
    temp4 = temp[3]

    #Converting array to list
    lst1 = temp1.tolist()
    lst2 = temp2.tolist()
    lst3 = temp3.tolist()
    lst4 = temp4.tolist()

    #Calling function to concatenate list together
    lst1 = concatenate(lst1)
    lst2 = concatenate(lst2)
    lst3 = concatenate(lst3)
    lst4 = concatenate(lst4)

    #Sending list segments to nodes
    req = comm.isend(lst2, dest=1, tag=11)
    req_1 = comm.isend(lst3, dest=2, tag=12)
    req_2 = comm.isend(lst4, dest=3, tag=13)
    
    print("-" * 30 + name + "-" * 30)

    #Calculating time
    start = time.perf_counter()
    pass_crack(lst1)
    end = time.perf_counter()

    #Printing time and segment
    time_1 = end - start
    print("Segment: " + lst1)
    print("Time for " + name + ": " + str(time_1) + "s")

elif(comm.rank == 1):
    #Recieving information from master node
    req = comm.irecv(source=0, tag=11)
    data = req.wait()

    print("-" * 30 + name + "-" * 30)

    #Calculating time
    start = time.perf_counter()
    pass_crack(data)
    end = time.perf_counter()

    #Printing time and segment
    time_2 = end - start
    print("Segment: " + data)
    print("Time for " + name + ": " + str(time_2) + "s")

elif(comm.rank == 2):
    #Recieving information from master node
    req_1 = comm.irecv(source=0, tag=12)
    data = req_1.wait()

    print("-" * 30 + name + "-" * 30)

    #Calculating time
    start = time.perf_counter()
    pass_crack(data)
    end = time.perf_counter()

    #Printing time and segment
    time_3 = end - start
    print("Segment: " + data)
    print("Time for " + name + ": " + str(time_3) + "s")

elif(comm.rank == 3):
    #Recieving information from master node
    req_2 = comm.irecv(source=0, tag=13)
    data = req_2.wait()

    print("-" * 30 + name + "-" * 30)

    #Calculating time
    start = time.perf_counter()
    pass_crack(data)
    end = time.perf_counter()

    #Printing time and segment
    time_4 = end - start
    print("Segment: " + data)
    print("Time for " + name + ": " + str(time_4) + "s")

"""
time.sleep(3)
if(comm.rank == 0):
    final_time = time_1 + time_2 + time_3 + time_4
    print("Password Cracked")
    print("Final Time Elapsed: " + " " + str(final_time) + "s")
"""
