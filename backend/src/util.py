import re
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC

from nltk.corpus import stopwords

def preprocess_corpus(corpus, REPLACE_NO_SPACE, REPLACE_WITH_SPACE):
    corpus = [REPLACE_NO_SPACE.sub("", document.lower()) for document in corpus]
    corpus = [REPLACE_WITH_SPACE.sub(" ", document) for document in corpus]
    
    return corpus

def readAndCleanDataFromTxt(path, REPLACE_NO_SPACE="", REPLACE_WITH_SPACE=""):
    # REPLACE_NO_SPACE = re.compile("[.;:!\'?,\"()\[\]]")
    REPLACE_WITH_SPACE = re.compile("(<br\s*/><br\s*/>)|(\-)|(\/)")

    data = []
    for line in open(path, 'r'):
        # print(line)
        data.append(line.strip())

    return preprocess_corpus(data, REPLACE_NO_SPACE, REPLACE_WITH_SPACE)



def remove_stop_words(corpus, stop_words=stopwords.words('english')):
    removed_stop_words = []
    for review in corpus:
        removed_stop_words.append(
            ' '.join([word for word in review.split() 
                      if word not in stop_words])
        )
    return removed_stop_words



def get_stemmed_text(corpus):
    from nltk.stem.porter import PorterStemmer
    stemmer = PorterStemmer()
    return [' '.join([stemmer.stem(word) for word in document.split()]) for document in corpus]

def get_lemmatized_text(corpus):
    from nltk.stem import WordNetLemmatizer
    lemmatizer = WordNetLemmatizer()
    return [' '.join([lemmatizer.lemmatize(word) for word in document.split()]) for document in corpus]


#  matrix is (docIndex, wordIndex)=data
def getVectorizer(vType, ngram_minmax=(1,2), stop_words=[]):
    if vType is 'one_hot':
        return CountVectorizer(binary=True, stop_words=stop_words)
    elif vType is 'word_count':
        return CountVectorizer(binary=False, stop_words=stop_words)
    elif vType is 'n_gram':
        return CountVectorizer(binary=True, ngram_range=ngram_minmax, stop_words=stop_words)
    elif vType is 'tfidf':
        return TfidfVectorizer(stop_words=stop_words)


def getClassifier(name, c):
    if name is 'lr':
        return LogisticRegression(C=c)
    elif name is 'svm':
        return LinearSVC(C=c)

def handleClassification(target, data, c, classifierName):
    

    X_train, X_val, y_train, y_val = train_test_split(
        data, target, train_size = 0.75
    )

    model = getClassifier(classifierName, c)
        
    model = LogisticRegression(C=c)
    model.fit(data, target)
    return model



def _find_average_score(sentenceValue) -> int:
    """
    Find the average score from the sentence value dictionary
    :rtype: int
    """
    sumValues = 0
    for entry in sentenceValue:
        sumValues += sentenceValue[entry]

    # Average value of a sentence from original summary_text
    average = (sumValues / len(sentenceValue))

    return average


def printMostPositiveAndNegative(LR_model, vectorizer):
    feature_to_coef = {
        word: coef for word, coef in zip(
            vectorizer.get_feature_names(), LR_model.coef_[0]
        )
    }

    for best_positive in sorted(
        feature_to_coef.items(), 
        key=lambda x: x[1], 
        reverse=True)[:5]:
        print (best_positive)

    for best_negative in sorted(
        feature_to_coef.items(), 
        key=lambda x: x[1])[:5]:
        print (best_negative)

