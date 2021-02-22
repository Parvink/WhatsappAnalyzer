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

    def displayDataText(self):
        print('Average words : ', self.getAverageWords())
        print('Number of total words : ', self.getNumberWords())
        print('Number of words from Aimée : ', self.getNbWordsByName("Aimée"))
        print('Number of words from Thomas : ', self.getNbWordsByName("Thomas"))
        print('Number of average words in a message from Aimée : ', self.getAverageWordsByName("Aimée"))
        print('Number of average words in a message from Thomas : ', self.getAverageWordsByName("Thomas"))
        print('Number of messages from Aimee : ', self.getNbMessageByName("Aimée"))
        print('Number of messages from Thomas : ', self.getNbMessageByName("Thomas"))
        print('Number of time ok appeared : ', self.messageContainsString("ok"))
        #print('Number of time ok appeared from Aimée : ', self.messageContainsStringByName("ok", "Aimée"))
        #print('Number of time ok appeared from Thomas : ', self.messageContainsStringByName("ok", "Thomas"))
        #print('Top 200 words Aimée : ', self.wordAnalyserAimee.getTopWords(200))
        #print('Top 200 words Thomas : ', self.wordAnalyserThomas.getTopWords(200))
        print('Top 200 words Thomas : ', self.wordAnalyserThomas.getFilteredTopWords(200))
        print('Top 200 words Aimee : ', self.wordAnalyserAimee.getFilteredTopWords(200))
    