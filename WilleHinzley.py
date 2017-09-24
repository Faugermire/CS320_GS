# Author: William Hinz
#Assignment: CS320 A6

import sys
import json
import time

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

def WilleHinzley(jFather):
    print('Yeah')

if __name__ == '__main__':
    # read in command line input
    files = inputVerify()
    # read in input file
    jFather = read_json(files[0])
    # start timer
    start_time = time.process_time()
    # run Gale-Shapley calculations
    WilleHinzley(jFather)
    # stop timer
    end_time = time.process_time()
    # write output file
    write_json(jFather, files[1])
    # print out execution time
    print("Ran in: {:.5f} secs".format(end_time - start_time))