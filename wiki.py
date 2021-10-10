import wikipedia
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import summary

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

    # print(json.dumps(score_dict, indent=1))
    for i in score_dict:
        if score_dict[i] == max_score:
            return i

def get_page_data(user_keyword):
    final_keyword = get_final_keyword(user_keyword)
    print("=================", final_keyword, "===================")
    wiki_page = wikipedia.page(final_keyword)
    para = ""
    for i in wiki_page.content.splitlines():
        str = i
        if(len(str)>1):
            if(str[:4]=="===="):
                str = str.removeprefix('==== ')
                str = str.removesuffix(' ====')
                print(">>>      ", str)
            elif(str[:3]=="==="):
                str = str.removeprefix('=== ')
                str = str.removesuffix(' ===')
                print(">> ", str)
            elif(str[:2]=="=="):
                str = str.removeprefix('== ')
                str = str.removesuffix(' ==')
                print(">", str)
            else:
                para += str+"\n";
        else:
            if(len(para)>1):
                print(para)

            para = ""

def get_wiki_summary(user_keyword, n = 3, summarize = True):
    final_keyword = get_final_keyword(user_keyword)
    print("=================", final_keyword, "===================")
    wiki_summary = wikipedia.summary(final_keyword).splitlines()
    result = ""
    for i in wiki_summary:
        if(summarize):
            result += summary.get_summary_para(i, n) + "\n"
        else:
            result += i + "\n"

    return result


if __name__ == "__main__":
    # get_page_data("reptile")
    print(get_wiki_summary("The Humans"))


