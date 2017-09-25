# Author: William Hinz
# Assignment: CS320 A6

import sys
import json
import time
from collections import defaultdict, deque
from person import person
import generate_problems


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
        print('Please supply both an input and output filename.')
        exit(-1)


def WilleHinzley(j_father):
    men = deque()  # men are a
    women = {}  # women are b
    results = []
    for pairing in j_father:
        for guy in pairing[0]:
            # print(guy)
            men.append(person(guy, pairing[0][guy]))
        for girl in pairing[1]:
            # print(girl)
            women[girl] = (person(girl, pairing[1][girl]))
        while True:
            try:
                luckyGuy = men.popleft()
                for _ in luckyGuy.getPrefList():
                    Hottie = women[luckyGuy.getPrefList().pop(0)]
                    if Hottie.isPaired() == False:
                        Hottie.pair(luckyGuy)
                        break
                    else:
                        luckyGuyIndex = Hottie.getPrefList().index(luckyGuy.getName())
                        currGuyIndex = Hottie.getPrefList().index(Hottie.getPartner().getName())
                        if luckyGuyIndex < currGuyIndex:
                            unluckyGuy = Hottie.swap(luckyGuy)
                            men.append(unluckyGuy)
                            break # 9 HOURS AND YOU ELUDED ME WHHHYYYYYYYYYYYY
            except(IndexError):  # if all of the men have found a partner.
                break

        tempDict = defaultdict()
        for girl in women:
            tempDict[women[girl].getPartner().getName()] = girl
        results.append(tempDict)
        men.clear()
        women.clear()
    return results


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
