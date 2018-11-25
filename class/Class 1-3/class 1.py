class Prog2():
    def add_numbers(self,x,y):
        return x+y

    def add_words(self,word1,word2):
        return word1 + " " + word2


sum = Prog2().add_numbers(10,200)
print(sum)
sentence = Prog2().add_words("Cobra","Kay")
print(sentence)

