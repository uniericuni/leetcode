class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.rootList=[False]*27

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        word=word.lower()
        list=self.rootList
        for i,c in enumerate(word):
            idx=ord(c)-ord('a')
            if not list[idx]:
                list[idx]=[False]*27
            if i==len(word)-1:
                list[idx][26]=True
            list=list[idx]

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        word=word.lower()
        return self.subsearch(word, self.rootList)
        
    def subsearch(self, word, list):
        if len(word)==0:
            if list[26]:
                return True
            else:
                return False
        idx=ord(word[0])-ord('a')
        if word[0]=='.':
            for subList in list[:26]:
                if subList and self.subsearch(word[1:], subList):
                    return True
        elif list[idx]:
            return self.subsearch(word[1:], list[idx])
        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
