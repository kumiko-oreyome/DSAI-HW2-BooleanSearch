import jieba
from util import elapsed_time

# titles : list of strings
# return vocab : {word:set([]),....}
@elapsed_time('segmentation')
def get_vocab_by_word_seg(titles):
    index = {}

    for i,title in enumerate(titles):
        seg_list = jieba.cut( title,cut_all=True)
        for word in seg_list:
            if len(word) > 3:
                continue
            if word not in index:
                index[word] = set()
    return index

