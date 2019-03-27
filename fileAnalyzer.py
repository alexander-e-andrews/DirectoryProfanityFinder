from profanity_check import predict, predict_prob
import numpy as np

'''
In the future, plan to test different reading strategies
'''
def fileAnalyzer(path):
    readLines(path)

def lineByLine(path):
    pass

def allLines(path):
    pass

def readLines(path):
    lines = []
    try:
        with open(path) as fr:
            lines = fr.readlines()
    except UnicodeDecodeError:
        print(path + " is not an accepted file type, either remove extension for accepted.settings or check your file")
        return
    except Exception as e:
        print("Some unkown error occured")
        print(e)
    else:
        if len(lines) > 0:
            arr = predict(lines)
            profanLines = np.argwhere(arr == 1)
            numProfans = profanLines.size
            if numProfans > 0 :
                pIndex = 0
                pLine = profanLines[pIndex]
                print("Profanaties detected")
                with open(path) as fr:
                    for i, line in enumerate(fr):
                        if i == pLine:
                            #This format is for visual studio link connecting, Not my perferred view, but its a nice feature
                            print("File \"" + path + "\", line " + str(pLine[0] + 1) + "\n" + line)
                            pIndex = pIndex + 1
                            if pIndex >= numProfans:
                                break
                            else: #this is a uselesss else, but ohwell
                                pLine = profanLines[pIndex]

