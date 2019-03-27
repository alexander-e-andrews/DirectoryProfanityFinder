from profanity_check import predict, predict_prob
from directoryLoader import directoryFileListBuilder
from fileAnalyzer import fileAnalyzer

'''
Dev: Alexander Edward Andrews
Email: alexander.e.andrews.ce@gmail.com
'''
def main():
    fileNode = directoryFileListBuilder()
    recursiveCaller(fileNode)

def recursiveCaller(fileNode):
    for f in fileNode.files:
        fileAnalyzer(f)
    for n in fileNode.directories:
        recursiveCaller(n)

main()
