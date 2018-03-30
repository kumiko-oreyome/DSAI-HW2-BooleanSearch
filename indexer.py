import re
from util import elapsed_time

@elapsed_time('bulid index...')
def build_index(titles,index):
    bigrams = get_titles_ngram(titles, 2)
    trigrams = get_titles_ngram(titles, 3)
    en = get_english_words_per_title(titles)
    assert len(bigrams) == len(trigrams)
    assert len(bigrams) == len(en)
    for i in range(len(bigrams)):
        for word in bigrams[i]:
            update_index(i+1, word, index)
        for word in trigrams[i]:
            update_index(i+1, word, index)  
        for word in en[i]:
            update_index(i+1, word, index)  
    
def update_index(doc_id,word,index):
    if word not in index :
        index[word] = set()
    doc_set = index[word]
    if doc_id not in doc_set:
        index[word].add(doc_id)


def get_english_words_per_title(titles):
    englishs = [] 
    for title in titles:
        english = get_english_words(title)
        englishs.append(english)
    return englishs


def get_english_words(s):
    english_words = re.findall(r"[a-zA-Z]+",s)
    return english_words


def get_titles_ngram(titles,n):
    ngrams_per_title = [] 
    for title in titles:
        ngrams = ngram(title, n)
        ngrams_per_title.append(ngrams)
    return ngrams_per_title


def ngram(s,n):
    ngrams = []
    for i in range(len(s)-n+1):
        gram = s[i:i+n]
        ngrams.append(gram)
    return ngrams

        
