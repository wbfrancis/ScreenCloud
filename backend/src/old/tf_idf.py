from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import nltk
import numpy as math
import util
import script_constructor as sc
# import ssl

# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context = _create_unverified_https_context
# nltk.download('stopwords')

def consolidateLines(lines):
    string = ""
    for l in lines:
        string += l.text + ' '
    return string

def _create_frequency_matrix(sentences):
    frequency_matrix = {}
    stopWords = set(stopwords.words("english"))
    ps = nltk.PorterStemmer()

    for sent in sentences:
        freq_table = {}
        words = word_tokenize(sent)
        for word in words:
            word = word.lower()
            word = ps.stem(word)
            if word in stopWords:
                continue

            if word in freq_table:
                freq_table[word] += 1
            else:
                freq_table[word] = 1
        
        frequency_matrix[sent[:15]] = freq_table

    return frequency_matrix

def _create_tf_matrix(freq_matrix):
    tf_matrix = {}

    for sent, f_table in freq_matrix.items():
        tf_table = {}

        count_words_in_sentence = len(f_table)
        for word, count in f_table.items():
            tf_table[word] = count / count_words_in_sentence

        tf_matrix[sent] = tf_table

    return tf_matrix

def _create_documents_per_words(freq_matrix):
    word_per_doc_table = {}

    for sent, f_table in freq_matrix.items():
        for word, count in f_table.items():
            if word in word_per_doc_table:
                word_per_doc_table[word] += 1
            else:
                word_per_doc_table[word] = 1

    return word_per_doc_table

def _create_idf_matrix(freq_matrix, count_doc_per_words, total_documents):
    idf_matrix = {}

    for sent, f_table in freq_matrix.items():
        idf_table = {}

        for word in f_table.keys():
            idf_table[word] = math.log10(total_documents / float(count_doc_per_words[word]))

        idf_matrix[sent] = idf_table

    return idf_matrix

def _create_tf_idf_matrix(tf_matrix, idf_matrix):
    tf_idf_matrix = {}

    for (sent1, f_table1), (sent2, f_table2) in zip(tf_matrix.items(), idf_matrix.items()):

        tf_idf_table = {}

        for (word1, value1), (word2, value2) in zip(f_table1.items(),
                                                    f_table2.items()):  # here, keys are the same in both the table
            tf_idf_table[word1] = float(value1 * value2)

        tf_idf_matrix[sent1] = tf_idf_table

    return tf_idf_matrix

def _score_sentences(tf_idf_matrix) -> dict:
    """
    score a sentence by its word's TF
    Basic algorithm: adding the TF frequency of every non-stop word in a sentence divided by total no of words in a sentence.
    :rtype: dict
    """

    sentenceValue = {}

    for sent, f_table in tf_idf_matrix.items():
        total_score_per_sentence = 0

        count_words_in_sentence = len(f_table)
        for word, score in f_table.items():
            # doesn't count punctuation
            if word.isalnum():
                total_score_per_sentence += score

        sentenceValue[sent] = total_score_per_sentence / count_words_in_sentence

    return sentenceValue

# corpus is a list of sentences, vocabulary is a list of unique words in the corpus
def _score_sentences(tf_idf_matrix_as_list, corpus, vocabulary) -> dict:
    """
    score a sentence by its word's TF
    Basic algorithm: adding the TF frequency of every non-stop word in a sentence divided by total no of words in a sentence.
    :rtype: dict
    """

    sentenceValue = {}
    
    for docIndex in range(len(tf_idf_matrix_as_list)):
        count_words_in_sentence = 0
        total_score_per_sentence = 0

        for wordIndex in range(len(tf_idf_matrix_as_list[docIndex])):
            data = tf_idf_matrix_as_list[docIndex][wordIndex]
            if (data is not 0):
                count_words_in_sentence += 1
                total_score_per_sentence += data

        sentenceValue[corpus[docIndex]] = total_score_per_sentence / count_words_in_sentence
    
    return sentenceValue

def _generate_summary(sentences, sentenceValue, threshold):
    sentence_count = 0
    summary = ''

    for sentence in sentences:
        if sentence in sentenceValue and sentenceValue[sentence] >= (threshold):
            summary += " " + sentence
            
    return summary


# script_obj = sc.initialize_script('Bennie')
# char = script_obj.characters['ruth']

# sentences = nltk.sent_tokenize(consolidateLines(char.dialogue)) # NLTK function

# # vectorizer = util.getVectorizer('tf_idf')
# # tf_idf_matrix = vectorizer.fit_transform(sentences)
# # print(tf_idf_matrix.toarray())

# total_documents = len(sentences)
# f_matrix = _create_frequency_matrix(sentences)
# tf_matrix = _create_tf_matrix(f_matrix)
# dpw_matrix = _create_documents_per_words(f_matrix)
# idf_matrix = _create_idf_matrix(f_matrix, dpw_matrix, total_documents)
# tf_idf_matrix = _create_tf_idf_matrix(tf_matrix, idf_matrix)

# sentenceValue = _score_sentences(tf_idf_matrix)
# av = util._find_average_score(sentenceValue)
# summary = _generate_summary(sentences, sentenceValue, 1.3*av)
# print(summary)



