from mpi4py import MPI
import string
import time
import sys
import numpy as np

comm = MPI.COMM_WORLD
size = MPI.COMM_WORLD.Get_size()
rank = MPI.COMM_WORLD.Get_rank()
name = MPI.Get_processor_name()

time_1 = 0
time_2 = 0
time_3 = 0
time_4 = 0

def concatenate(lst):
    string = ""
    for ch in lst:
        string += ch
    return string

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
                print(str(rank) + " cracked the segment!")
                return
        passwordLen += 1

if(comm.rank == 0):
    chunkSize = 4
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

    lst1 = concatenate(lst1)
    lst2 = concatenate(lst2)
    lst3 = concatenate(lst3)
    lst4 = concatenate(lst4)

    req = comm.isend(lst2, dest=1, tag=11)
    req_1 = comm.isend(lst3, dest=2, tag=12)
    req_2 = comm.isend(lst4, dest=3, tag=13)
    
    start = time.perf_counter()
    pass_crack(lst1)
    end = time.perf_counter()
    time_1 = end - start

elif(comm.rank == 1):
    req = comm.irecv(source=0, tag=11)
    data = req.wait()

    start = time.perf_counter()
    pass_crack(data)
    end = time.perf_counter()
    time_2 = end - start

elif(comm.rank == 2):
    req_1 = comm.irecv(source=0, tag=12)
    data = req_1.wait()

    start = time.perf_counter()
    pass_crack(data)
    end = time.perf_counter()
    time_3 = end - start

elif(comm.rank == 3):
    req_2 = comm.irecv(source=0, tag=13)
    data = req_2.wait()

    start = time.perf_counter()
    pass_crack(data)
    end = time.perf_counter()
    time_4 = end - start


if(comm.rank == 0):
    final_time = time_1 + time_2 + time_3 + time_4
    print("Password Cracked")
    print("Time Elapsed: ", final_time)
