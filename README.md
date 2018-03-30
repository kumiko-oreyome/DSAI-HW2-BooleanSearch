# DSAI-HW2-BooleanSearch

### Construct Index
- Using python dict data structure as index , key is word,value is set of document ids
- Build the index by bigram+trigram  
- Because english word may contain more than 3 characters ,I extract english word by regular expression,then add to the index
- Without using word segmentation tool because some word in query like 蔡英文 cannot segmented by jieba ,it produce "蔡","英文" (both cut_all=true/False)
- After I find out the problem of jieba(蔡英文),I using trigram&bigram directly
- word segmentation also consume some time,I just implement the 100% accuracy baseline model first 

### Query
- if or , using set union  --> current_result = index[word]|current_result
- if and, using set join --> current_result = index[word]&current_result
- if not , using set difference --> current_result = index[word]-current_result