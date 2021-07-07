import numpy as np
import random as rng

def getData():
    data = []
    filenames = ['features.csv', 'class.csv']
    try:
        filedata  = {filename:open(filename, 'r') for filename in filenames}
        classdata = []
        for row in filedata[filenames[0]].read().split('\n'):
            row       = row.split(',')
            data      += [[float(f) for f in row if not f =='' ]]
        for row in filedata[filenames[1]].read().split('\n'):
            if not row == '': classdata.append(int(row)) 
        data = list(zip(data, classdata))
    finally:
        for file in filedata.values():
            file.close()
    return data

def selectData(data, trainsize):
    size = len(data)
    rng.shuffle(data)
    trainData = data[:int(size * trainsize)]
    testData = data[int(size * trainsize):]

    return (trainData, testData)

def getMu(trainData):
    mu = 1
    return mu

def main():
    data = getData()
    (trainData, testData) = selectData(data, 1/2)
    # print(len(data1))
    # print(*data1, sep = '\n')
    # print("------------------------||-----------------------")
    # print(len(data2))
    # print(*data2, sep = '\n')

    my = getMu(trainData)
    sigma_k = []


if __name__ == "__main__":
    main()