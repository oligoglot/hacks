import json
import re
from collections import Counter, defaultdict
stops = set(['the', 'is', 'are'])
def remove_stops(words):
    for w in words:
        if w not in stops:
            yield w

suffix = re.compile('(acy|al|ance|ence|dom|er|or|ism|ist|ity|ty|ment|ness|ship|sion|tion|ate|en|ify|fy|ize|ise|able|ible|al|esque|ful|ic|ical|ious|ous|ish|ive|less|y|s|es)$')
def stem(w):
    return suffix.sub('', w)

docs = 0
docspace = {}
class Entity:
    def __init__(self, doctext, did):
        self.doc = json.loads(doctext.lower())
        self.did = str(did)

    def vectorise(self):
        self.vector = {}
        self.vector['bow'] = set()
        self.vector['tf'] = Counter()
        for w in remove_stops(re.split('\W+', self.doc['name'])):
            w = stem(w) 
            self.vector['bow'].add(w)
            self.vector['tf'][w] += 1
        return self.vector

    def __repr__(self):
        return repr(self.did)

def search(q):
    q = q.lower().strip()
    print "The query is", q
    score = defaultdict(float)
    for w in remove_stops(re.split('\W+', q)):
        w = stem(w)
        for did in index[w]:
            doc = docspace[did]
            score[doc] = score[doc] + float(doc.vector['tf'][w])/len(index[w])
    for doc in sorted(score, key=lambda doc:score[doc], reverse = True):
        print doc.vector['bow'], doc.vector['tf'], score[doc]

import sys
index = defaultdict(set)
with open(sys.argv[1], 'r') as df:
    for line in df:
        e = Entity(line.strip(), docs)
        docspace[str(docs)] = e
        docs += 1
        e.vectorise()
        for w in e.vector['bow']:
            index[w].add(e.did)
'''
for w in index:
    print w, str.join(',', index[w])
'''
search(sys.argv[2])
