from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import numpy as np
import pandas

#nltk.download()


example="My name is Kumar Piyush ,You can call me Data scientist"
words=word_tokenize(example)

stop_words=set(stopwords.words("english"))
arr=[w for w in words if not w in stop_words]

print(arr)