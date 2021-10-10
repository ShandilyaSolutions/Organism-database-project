import wikipedia
from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json

def get_cosine_sim(*strs): 
    vectors = [t for t in get_vectors(*strs)]
    return cosine_similarity(vectors)
    
def get_vectors(*strs):
    text = [t for t in strs]
    vectorizer = CountVectorizer()
    vectorizer.fit(text)
    return vectorizer.transform(text).toarray()

def get_final_keyword(keyword):
    search_results = wikipedia.search(keyword)
    score_dict = dict()
    score_list = list()
    max_score = 0
    for i in search_results:
        score = get_cosine_sim(i, keyword)[0][1]
        score_dict[i] = score
        score_list.append(score)
        max_score = max(max_score, score)

    print(json.dumps(score_dict, indent=1))
    for i in score_dict:
        if score_dict[i] == max_score:
            return i

    
print(get_final_keyword("naja naja"))

