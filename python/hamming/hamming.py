def distance(strand_a, strand_b):
    return count( [ (q,w) for q,w in zip(strand_a,strand_b) if q != w ])
