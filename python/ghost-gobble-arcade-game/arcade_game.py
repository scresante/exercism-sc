def q(b):
    if b==1: return True
    return False

def eat_ghost(p,t): return q(p&t)

def score(t,d): return q(t|d)

def lose(p,t): return q(~p&t)

def win(h,p,t): return q(h&~(~p&t))
