
from os import path
import re


class testFaker():
    """ """
    def __init__(self, inFun):
        self.wanted_string = ''
        self.fun_name = inFun.__code__.co_name
        self.file_name = inFun.__code__.co_filename
        self.test_file = self.guess_test_name()
        self.fake_mod_name = path.basename(path.splitext(self.file_name)[0])
        self.search = ''


    def get_test_string(self):
        self.search = '%s.%s()' % (self.fake_mod_name, self.fun_name)
        print('self.searching %s for %s' % (self.test_file, self.search))
        i = 0
        with open(self.test_file, 'r') as infile:
            for line in infile:
                i += 1
                # print('search: %s | line: %s...' % (self.search, line[30]))
                sPat = ".*self.assertEqual\(.*, '(.*)'\)"
                mObj = re.match(sPat, line)
                if mObj:
                    return mObj.groups()
                # if line.find(self.search) > 4:
                    # print('match found on line %s' % i)
                    # return line
        raise Exception('could not find a line')


    def guess_test_name(self):
        parts = path.splitext(self.file_name)
        return ''.join((parts[0], '_test', parts[1]))


def hello(name=''):
    def hello(): pass
    q = testFaker(hello)
    print(q.get_test_string()[0])
