# python3

import sys
import threading
import numpy as np

def compute_height(n, parents):
    koka_garums = 0
    augstumi = [0] * n
    for i in range(n):
        if augstumi[i] != 0:
            continue
        augstums = 0
        j = i
        while parents[j] != -1:
            if augstumi[j] != 0:
                augstums += augstumi[j]
                break
            augstums += 1
            j = parents[j]
        augstumi[i] = augstums
        if augstums > koka_garums:
            koka_garums = augstums
    return koka_garums


def main():
    # implement input form keyboard and from files
    izvele = input()
    if izvele == 'I':
        # input number of elements
        n = int(input("Enter the number of nodes: "))
        # input values in one variable, separate with space, split these values in an array
        parents = np.asarray(list(map(int, input("Enter the parent nodes separated by spaces: ").split())))
    elif izvele == 'F':
        # let user input file name to use, don't allow file names with letter a
        faila_nosaukums = input("Enter the file name: ")
        if 'a'in faila_nosaukums:
            return
        else:    
            with open(F"./test/{faila_nosaukums}") as f:
                n = int(f.readline())
                parents = np.asarray(list(map(int, f.readline().split())))
    else:
        print("Invalid choice.")
        return
    # call the function and output it's result
    koka_garums = compute_height(n, parents) + 1
    print(koka_garums)

#In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)# max depth of recursion
threading.stack_size(2**27)# new thread will get stack of such size
threading.Thread(target=main).start()