from wordAnalyser import WordAnalyzer 

class Analyzer:
    def __init__(self, parsedList):
        self.list = parsedList
        self.length = len(parsedList)
        self.wordAnalyser = WordAnalyzer(parsedList)
        self.wordAnalyserThomas = WordAnalyzer(self.getWordsByName('Thomas'))
        self.wordAnalyserAimee = WordAnalyzer(self.getWordsByName('Aimée'))

    def getNbMessageByName(self, name):
        sum = 0
        for messages in self.list:
            if name in messages.name:
                sum += 1
        return sum

    def getNumberWords(self):
        sum = 0
        for messages in self.list:
            sum += messages.countWords()
        return sum

    def getNbWordsByName(self, name):
        sum = 0
        for messages in self.list:
            if name in messages.name:
                sum += messages.countWords()
        return sum

    def getWordsByName(self, name):
        resultArray = []
        for messages in self.list:
            if name in messages.name:
                resultArray.append(messages)
        return resultArray

    def getAverageWords(self):
        average = 0.0
        for messages in self.list:
            average += messages.countWords()
        return average / self.length

    def getAverageWordsByName(self, name):
        average = 0.0
        for messages in self.list:
            if name in messages.name:
                average += messages.countWords()
        return average / self.getNbMessageByName(name)

    def messageContainsString(self, string):
        sum = 0
        for messages in self.list:
            if string in messages.message:
                sum += 1
        return sum

    def messageContainsStringByName(self, string, name):
        sum = 0
        for messages in self.list:
            if string in messages.message:
                if name in messages.name:
                    sum += 1
        return sum

    