from util import load_titles,load_querys
from indexer import build_index
from query import parse_query

if __name__ == '__main__':
    # You should not modify this part.
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--source',
                       default='source.csv',

                       help='input source data file name')
    parser.add_argument('--query',
                        default='query.txt',
                        help='query file name')
    parser.add_argument('--output',
                        default='output.txt',
                        help='output file name')
    args = parser.parse_args()
    
    titles = load_titles(args.source)
    querys = load_querys(args.query)
     
    index = {}
    # build index by ngram & extract english word by regular expression
    # didn't use word segmentation because some word in query like 蔡英文 cannot segmented by jieba
    # and segmentation also consume time , I just implement the 100% accuracy baseline model first 
    build_index(titles,index)

    print('output result')
    #output results
    
    with open(args.output,'w') as f:
        for i,query in enumerate(querys):
            res = parse_query(query,index)
            line = [str(n) for n in res]
            line = ','.join(line)+'\n'
            f.write(line)