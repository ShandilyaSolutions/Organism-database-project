from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

text = "Humans (Homo sapiens) are the most abundant and widespread species of primate, characterized by bipedality, large and complex brains enabling the development of advanced tools, culture and language. Humans are highly social beings and tend to live in complex social structures composed of many cooperating and competing groups, from families and kinship networks to political states. Social interactions between humans have established a wide variety of values, social norms, and rituals, which bolster human society. Curiosity and the human desire to understand and influence the environment and to explain and manipulate phenomena have motivated humanity's development of science, philosophy, mythology, religion, and other fields of knowledge."

stopWords = set(stopwords.words("english"))
words = word_tokenize(text)

freqTable = dict()

for word in words:
    word = word.lower()
    if word in stopWords:
        continue
    if word in freqTable:
        freqTable[word]+=1
    else:
        freqTable[word] = 1

sentences = sent_tokenize(text)
senteceValue = dict()
for sen in sentences:
    for word, freq in freqTable.items():
        if word in sen.lower():
            if sen in senteceValue:
                senteceValue[sen] += 1
            else:
                senteceValue[sen] = 1
sumValue = 0
for sen in senteceValue:
    sumValue += senteceValue[sen]

average = int(sumValue/len(senteceValue))

summary = ''

for sen in sentences:
    if(sen in senteceValue) and (senteceValue[sen]>(1.2*average)):
        summary += " " + sen

print(summary)
    
