from util import load_titles,load_querys
from indexer import build_index
from query import parse_query





titles = load_titles()
querys = load_querys()
index_ini = {}
build_index(titles,index_ini)
index = index_ini

#evaluation
golds = []
with open('output.txt','r') as f:
    lines = f.readlines()
    for line in lines:
        nums = [int(num_str) for num_str in line.split(",")]
        golds.append(nums)

for i,query in enumerate(querys):
    res = parse_query(query,index)
    print(i)
    try:
        assert res == golds[i]
    except :
        print(res)
        print(golds[i])
        break


#res = parse_query('電玩 and 宅男',index)
#print(res)



#print(index_ini)
#print(len(index_ini))
#
#s1 = "Kelly Talk：關穎充藝術總監 拍時尚全家福"
#s2 = "貼心又討喜 NISSAN MARCH寵愛女性車主"
#titles = [s1,s2]

#print(get_english_words_per_title(titles))
#print(get_titles_ngram(titles,2))
#print(get_titles_ngram(titles,3))

#print(len(index_ini))