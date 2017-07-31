import nltk
import pandas as pd
import numpy as np
import itertools
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import sys  
reload(sys)  # to set ASCII encoding 
sys.setdefaultencoding('utf8')

df = pd.read_csv('user-sent_quoted-coach_msg_postman_message_Jan18.csv')

#sort to group by userID
df_sorted = df.sort_values('sender_id')

dicty_word_tokenize = {}
stop_words = set(stopwords.words('english')) # list of stop words

for index, row in df.iterrows():
	dicty_word_tokenize[row['sender_id']] = word_tokenize(row['body']) #break the Msg string into words and dump it into a Dictionery

dicty_word_filt = {}
for key,value in dicty_word_tokenize.iteritems():
	filtered_sentence = [w for w in value if not w in stop_words]
	dicty_word_filt[key] = filtered_sentence

print dicty_word_filt



