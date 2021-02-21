class StructureText:
    def __init__(self, text):
        self.text = text
        self.date = text[:10]
        self.hour = text[13:18]
        secondHalf = text[21:]
        self.name = secondHalf[:secondHalf.find(':')]
        self.message = secondHalf[secondHalf.find(': ') + 2:].lower()
        self.filterMessage('?!,:()_-\'')
        self.filterString('<médias omis>')

    def filterMessage(self, string):
        for char in string:
            self.message = self.message.replace(char, '')

    def filterString(self, string):
        self.message = self.message.replace(string, '')

    def countWords(self):
        return (len(self.message.split(' ')))

b = StructureText('22/01/2021 à 15:51 - Thomas K: I will')