from os import remove
from  utils.fileParser import FileParser

class WordAnalyzer:
    def __init__(self, listMessages):
        self.listMessages = listMessages
        self.dictionary = {}
        file = FileParser('english100words.data')
        file.readTextfile()
        self.mostUsed = file.content
        self.fillDictionary(listMessages)
        self.filteredDictionary = self.removeCommonWords()

    def fillDictionary(self, listMessages):
        for i in listMessages:
            words = i.message.split(' ')
            for word in words:
                if word != '':
                    if word in self.dictionary.keys():
                        self.dictionary[word] += 1
                    else:
                        self.dictionary[word] = 1
        sorted_tuples = sorted(self.dictionary.items(), key=lambda item: item[1], reverse=True)
        sortedDict = {k: v for k, v in sorted_tuples}
        self.dictionary = sortedDict

    def removeCommonWords(self):
        filteredDictionary = self.dictionary.copy()
        for word in self.mostUsed:
            try:
                del filteredDictionary[word.lower()]
            except Exception:
                pass
        return filteredDictionary

    def getTopWords(self, nb):
        if len(self.dictionary.items()) < nb:
            nb = len(self.dictionary)
        return list(self.dictionary.items())[:nb]

    def getFilteredTopWords(self, nb):
        if len(self.filteredDictionary.items()) < nb:
            nb = len(self.filteredDictionary)
        return list(self.filteredDictionary.items())[:nb]