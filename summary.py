from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import numpy as np
import networkx as nx
 

def read_article(paragraph):
    article = paragraph.split(". ")
    sentences = []

    for sentence in article:
        sentences.append(sentence.replace("[^a-zA-Z]", " ").split(" "))
    sentences.pop() 
    return sentences


def sentence_similarity(sent1, sent2, stopwords=None):
    if stopwords is None:
        stopwords = []
 
    sent1 = [w.lower() for w in sent1]
    sent2 = [w.lower() for w in sent2]
 
    all_words = list(set(sent1 + sent2))
 
    vector1 = [0] * len(all_words)
    vector2 = [0] * len(all_words)
 
    # build the vector for the first sentence
    for w in sent1:
        if w in stopwords:
            continue
        vector1[all_words.index(w)] += 1
 
    # build the vector for the second sentence
    for w in sent2:
        if w in stopwords:
            continue
        vector2[all_words.index(w)] += 1
    return 1 - cosine_distance(vector1, vector2)

 
def build_similarity_matrix(sentences, stop_words):
    # Create an empty similarity matrix
    similarity_matrix = np.zeros((len(sentences), len(sentences)))
 
    for idx1 in range(len(sentences)):
        for idx2 in range(len(sentences)):
            if idx1 == idx2: #ignore if both are same sentences
                continue 
            similarity_matrix[idx1][idx2] = sentence_similarity(sentences[idx1], sentences[idx2], stop_words)

    return similarity_matrix


# This is the requred function, just pass a paragrah of text in form of string with no new line character
# And the second argunet is no of top summarized sentences you wanna added in the final summary.
def get_summary_para(paragraph, top_n=5):
    stop_words = stopwords.words('english')
    summarize_text = []
    sentences =  read_article(paragraph)
    sentence_similarity_martix = build_similarity_matrix(sentences, stop_words)
    sentence_similarity_graph = nx.from_numpy_array(sentence_similarity_martix)
    scores = nx.pagerank(sentence_similarity_graph)

    ranked_sentence = sorted(((scores[i],s) for i,s in enumerate(sentences)), reverse=True)    
    for i in range(min(top_n, len(ranked_sentence))):
      summarize_text.append(" ".join(ranked_sentence[i][1]))
    return ". ".join(summarize_text)


def get_summary_file(file, n):
    f = open(file)
    for i in f:
        print("********************** Original Text: ***********************")
        print(i)
        print("********************* Summarize Text: ***********************")
        print(get_summary_para(i.strip(), n))
        print("\n\n")

if __name__ == "__main__":
    get_summary_file("tests/human_per_para.txt", 3)
