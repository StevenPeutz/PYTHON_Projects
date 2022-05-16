import nltk
#nltk.download()
#dir(nltk)
import pandas as pd
from pandas.core.algorithms import value_counts
messages = pd.read_csv('/Users/steven/Documents/GitLocal/NLP-SentimentAnalysis-BTC/NLTK_code/Practice/data/spam.csv', encoding='latin-1')

#drop the 3 extra empty colums
messages = messages.drop(labels= ["Unnamed: 2","Unnamed: 3", "Unnamed: 4" ], axis=1)

#given the remaining two columns descriptive names
# use .rename instead of .columns, .columns for name change no longer supprted/allowed
messages = messages.rename(columns={'v1': 'label', 'v2': 'text'})

#checking the balance or target var
messages['label'].value_counts()

# #checking for missing values
#messages['label'].isnull().sum()
#messages['text'].isnull().sum()
messages.isnull().sum(axis = 0)



####################################
# #cleaning text
####################################

# # 1 removing punctuation using the punctuation list within string package
##############################
# import string
# def remove_punctuation(text):
#     text = "".join([char for char in text if char not in string.punctuation])
#     return text
# messages['text_clean'] = messages['text'].apply (lambda x: remove_punctuation(x))


# #tokenize
################
# import re
# def tokenize(text):
#     tokens = re.split('\W+', text)
#     return tokens
# messages['text_tokenized'] = messages['text_clean'].apply(lambda x: tokenize(x.lower()))


# #remove stopwords
######################
# stopwords = nltk.corpus.stopwords.words('english')  # has 179 words (len(stopwards))
# def remove_stopwords(tokenized_text):
#     text = [word for word in tokenized_text if word not in stopwords]
#     return text
# messages['text_tokenNoStop'] = messages['text_tokenized'].apply(lambda x: remove_stopwords(x))

###############################
###############################


#all above in one, before getting to vectorization with tf-idf
import string
import re
stopwords = nltk.corpus.stopwords.words('english')  # has 179 words (len(stopwards))

def clean_text(text):
    text = "".join([char for char in text if char not in string.punctuation])
    tokenized_text = re.split('\W+', text)
    text = [word for word in tokenized_text if word not in stopwords]
    return text

new_text_list = clean_text(messages['text'])
#new_text_list[:10]
len(new_text_list)

from sklearn.feature_extraction.text import TfidfVectorizer

tfidf_vect = TfidfVectorizer(analyzer=clean_text)
x_tfidf = tfidf_vect.fit_transform(messages['text'])

#print(tfidf_vect.get_feature_names())
x_tfidf.shape
type(x_tfidf)

x_features = pd.DataFrame(x_tfidf.toarray())
x_features.head()


from sklearn.ensemble import RandomForestClassifier
print(RandomForestClassifier())

# Import the methods that will be needed to evaluate a basic model
from sklearn.metrics import precision_score, recall_score
from sklearn.model_selection import train_test_split

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(x_features,
                                                    messages['label'],
                                                    test_size=0.2)


# Fit a basic Random Forest model
rf = RandomForestClassifier()
rf_model = rf.fit(X_train, y_train)

# Make predictions on the test set using the fit model
y_pred = rf_model.predict(X_test)

# Evalute model predictions using precision and recall
precision = precision_score(y_test, y_pred, pos_label='spam')
recall = recall_score(y_test, y_pred, pos_label='spam')
print('Precision: {} / Recall: {}'.format(round(precision, 3), round(recall, 3)))
                                                    