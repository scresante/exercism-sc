from collections import defaultdict
import re
import pdb
def preproc(ph):
    ph = ph.lower()
    ignore = ':!@#$%^&*()".'
    ph = ''.join(list(filter(lambda a: a not in ignore, ph)))
    ph = re.sub(' +', ' ', ph)
    ph = re.split('\t|\n|,| |_', ph)
    ph = [ q.strip('\'') for q in ph ]
    return ph


def word_count(phrase):
    counts = defaultdict(int)
    # pdb.set_trace()
    for word in preproc(phrase):
        if word:
            counts[word] += 1
    return dict(counts)
