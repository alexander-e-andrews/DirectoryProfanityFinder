from profanity_check import predict, predict_prob
from directoryLoader import directoryFileListBuilder
from fileAnalyzer import fileAnalyzer


def main():
    #print(predict(['Fucking cunts rabbit orange cheese cold hot red']))
    fileNode = directoryFileListBuilder()
    recursiveCaller(fileNode)

def recursiveCaller(fileNode):
    for f in fileNode.files:
        fileAnalyzer(f)
    for n in fileNode.directories:
        recursiveCaller(n)

main()
