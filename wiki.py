import wikipedia

def get_jaccard_sim(str1, str2): 
    a = set(str1.split()) 
    b = set(str2.split())
    c = a.intersection(b)
    return float(len(c)) / (len(a) + len(b) - len(c))

keyword = "homo sapiens"
search_results = wikipedia.search(keyword)
score = dict()
for i in search_results:
    score[i] = get_jaccard_sim(keyword, i)

print(score)
