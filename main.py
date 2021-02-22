#!/usr/bin/env python3

from utils.fileParser import FileParser
from utils.plotter import Plotter
from structureText import StructureText
from analyzer import Analyzer

import sys


def main():
    try:
        p = FileParser(sys.argv[1])
    except Exception:
        print('Usage: You must give a text file from the Whatsapp export feature ')
        sys.exit(84)
    p.readTextfile()
    parsedMessage = []
    for messages in p.content:
        tmpMessage = StructureText(messages)
        if len(tmpMessage.message) != 0:
            parsedMessage.append(tmpMessage)
    analyzed = Analyzer(parsedMessage)
    analyzed.displayDataText()
    plotter = Plotter(analyzed.wordAnalyserAimee.getFilteredTopWords(25))
    plotter.displayBubblePlot('Aimée top 25 words', "Word", "Number of occurences")
    plotter = Plotter(analyzed.wordAnalyserThomas.getFilteredTopWords(25))
    plotter.displayBubblePlot('Thomas top 25 words', "Word", "Number of occurences")


if __name__ == "__main__":
        main()