def is_pangram(sentence):
    lets = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
    for l in lets:
        if sentence.find(l) == -1:
            return False
    return True


