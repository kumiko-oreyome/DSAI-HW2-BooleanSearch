#return sorted doc_id list
def parse_query(query,index):
    
    terms = query.split()
    op = 'or'
    res = set()
    for term in terms:
        if term == 'or' or term == 'and' \
                        or term == 'not':
            op = term
            continue

        relavent_docs = None
        if term not in index:
            relavent_docs = set() 
        else:
            relavent_docs = index[term]
        if op == 'or':
            res = res |  relavent_docs
        elif op == 'and':
             res = res &  relavent_docs
        else :
             res = res -  relavent_docs
    if len(res) == 0:
        return [0] 
    return sorted(list(res))