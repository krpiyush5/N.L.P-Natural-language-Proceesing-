from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

#we are going to study stemming in nltk

ps=PorterStemmer()

example=["python","pythonista","pythoner","pythoned","pyth"]

#for w in example:
#    print(ps.stem(w))

new_txt="python is most commonly language used for machine learning . implementation is very easy, thats why python is my favorite."

words=word_tokenize(new_txt)

for w in words:
    print(ps.stem(w))