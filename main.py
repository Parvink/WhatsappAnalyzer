#!/usr/bin/env python3

from utils.fileParser import FileParser
from structureText import StructureText
from analyzer import Analyzer

def displayDataText(analyzed):
    print('Average words : ', analyzed.getAverageWords())
    print('Number of total words : ', analyzed.getNumberWords())
    print('Number of words from Aimée : ', analyzed.getNbWordsByName("Aimée"))
    print('Number of words from Thomas : ', analyzed.getNbWordsByName("Thomas"))
    print('Number of average words in a message from Aimée : ', analyzed.getAverageWordsByName("Aimée"))
    print('Number of average words in a message from Thomas : ', analyzed.getAverageWordsByName("Thomas"))
    print('Number of messages from Aimee : ', analyzed.getNbMessageByName("Aimée"))
    print('Number of messages from Thomas : ', analyzed.getNbMessageByName("Thomas"))
    print('Number of time ok appeared : ', analyzed.messageContainsString("ok"))
    #print('Number of time ok appeared from Aimée : ', analyzed.messageContainsStringByName("ok", "Aimée"))
    #print('Number of time ok appeared from Thomas : ', analyzed.messageContainsStringByName("ok", "Thomas"))
    print('Top 20 words Aimée : ', analyzed.wordAnalyserAimee.getTopWords(200))
    print('Top 20 words Thomas : ', analyzed.wordAnalyserThomas.getTopWords(200))

def main():
    p = FileParser('whatsAppAimee.txt')
    p.readTextfile()
    parsedMessage = []
    for messages in p.content:
        tmpMessage = StructureText(messages)
        if len(tmpMessage.message) != 0:
            parsedMessage.append(tmpMessage)
    analyzed = Analyzer(parsedMessage)
    displayDataText(analyzed)




if __name__ == "__main__":
        # execute only if run as a script
        main()