import script_constructor
import util
from sklearn.metrics import accuracy_score
import tf_idf
import numpy as np
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import nltk
import numpy as math
import util
import script_constructor as sc
# import nltk
# import ssl

# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context = _create_unverified_https_context
# nltk.download('wordnet')

def main():
    # # TEMPORARY, NEED SOME SORT OF CONTROLLER INPUT
    # script_name = "Bennie"
    # # script_name = 'Hunt'
    # script = script_constructor.initialize_script(script_name)
    # # print(script.action_lines)
    # # print(script.characters) 
    

    # data_train = util.readAndCleanDataFromTxt('./resource/aclimdb/movie_data/full_train.txt')
    # data_test =  util.readAndCleanDataFromTxt('./resource/aclimdb/movie_data/full_test.txt')

    script_obj = sc.initialize_script('Bennie')
    char = script_obj.characters['ruth']

    data_train = nltk.sent_tokenize(tf_idf.consolidateLines(char.dialogue))
    
    # string = 'It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of light, it was the season of darkness, it was the spring of hope, it was the winter of despair'
    # data_train = string.split(', ')

    # data_test = util.remove_stop_words(data_test)
    # data_train = util.remove_stop_words(data_train)

    # data_test = util.get_lemmatized_text(data_test)
    # data_train = util.get_lemmatized_text(data_train)

    stop_words = ['in', 'of', 'at', 'a', 'the']

    vectorizer = util.getVectorizer('tfidf')
    vectorizer.fit(data_train)
    X = vectorizer.transform(data_train)
    sentenceValue = tf_idf._score_sentences(X.toarray().tolist(), data_train, vectorizer.vocabulary_.keys())
    av = tf_idf._find_average_score(sentenceValue)
    summary = tf_idf._generate_summary(data_train, sentenceValue, av*3)
    print(summary)
    # # X_test = vectorizer.transform(data_test)

    # print(X)

    # target = [1 if i < 12500 else 0 for i in range(25000)]

    # # for c in [0.001, 0.005, 0.01, 0.05, 0.1]:
    # #     model = util.handleClassification(target, X, c, 'svm')

    # #     print ("Final Accuracy: %s" 
    # #         % accuracy_score(target, model.predict(X_test)))

    # model = util.handleClassification(target, X, .1, 'svm')

    # print ("Final Accuracy: %s" 
    #    % accuracy_score(target, model.predict(X_test)))


if __name__ == '__main__':
    main()