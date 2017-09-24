import sys
import json

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

if __name__ == '__main__':
    files = inputVerify()
    print(files[0] + " " + files[1])