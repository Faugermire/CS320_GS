# Author: William Hinz
# Assignment: CS320 A6

import sys
import json
import time
from collections import defaultdict, deque
from person import person


def write_json(obj, filename):
    with open(filename, mode='w') as f:
        json.dump(obj, f)


def read_json(filename):
    with open(filename) as f:
        return json.load(f)


def inputVerify():
    files = []
    if len(sys.argv) >= 2:
        files.append(sys.argv[1])
        files.append(sys.argv[2])
        return files
    else:
        print('Please, input both an input and output filename.')
        exit(-1)

def propose(man, woman):
    if woman.prefs.index(woman.currPartner) > woman.prefs.index(man):
        return False
    else:
        return True

def WilleHinzley(j_father):
    bachelors = deque()# men are a
    bachelorettes = [] # women are b
    result = []
    for pairing in j_father:
        for man in pairing[0]:
            #print(man)
            bachelors.append(person(man, pairing[0][man]))
        for woman in pairing[1]:
            #print(woman)
            bachelorettes.append(person(woman, pairing[1][woman]))

        while True:
            try:
                luckyGuy = bachelors.popleft()
                index = 0
                for i in range(len(bachelorettes)):
                    if bachelorettes[i].isPaired() == False: # if available
                        bachelorettes[i].pair(luckyGuy)
                        break
                    else: # if paired
                        newPartner = bachelorettes[i].getPrefList().index(luckyGuy.getName())
                        currPartner = bachelorettes[i].getPrefList().index(bachelorettes[i].getPartner().getName())
                        if newPartner < currPartner:
                            unluckyGuy = bachelorettes[i].swap(luckyGuy)
                            bachelors.append(unluckyGuy)
            except(IndexError):
                break
        for i in range(len(bachelorettes)):
            print(bachelorettes[i])
        bachelors.clear()
        bachelorettes.clear()

    # for _ in range(len(bachelors)):
    #     print(bachelors.popleft())
    #






    return result


if __name__ == '__main__':
    # read in command line input
    files = inputVerify()
    # read in input file
    j_father = read_json(files[0])
    # start timer
    start_time = time.process_time()
    # run Gale-Shapley calculations
    j_father = WilleHinzley(j_father)
    # stop timer
    end_time = time.process_time()
    # write output file
    write_json(j_father, files[1])
    # print out execution time
    print("Ran in: {:.5f} secs".format(end_time - start_time))
