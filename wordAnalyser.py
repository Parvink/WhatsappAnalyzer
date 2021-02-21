class WordAnalyzer:
    def __init__(self, listMessages):
        self.listMessages = listMessages
        self.dictionary = {}
        self.fillDictionary(listMessages)

    def fillDictionary(self, listMessages):
        for i in listMessages:
            words = i.message.split(' ')
            for word in words:
                if word is not '':
                    if word in self.dictionary.keys():
                        self.dictionary[word] += 1
                    else:
                        self.dictionary[word] = 1
        sorted_tuples = sorted(self.dictionary.items(), key=lambda item: item[1], reverse=True)
        sortedDict = {k: v for k, v in sorted_tuples}
        self.dictionary = sortedDict

    def getTopWords(self, nb):
        if len(self.dictionary.items()) < nb:
            nb = len(self.dictionary)
        return list(self.dictionary.items())[:nb]