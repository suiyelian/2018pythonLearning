# encoding: utf-8
import re


class CheckSql(object):

    def __init__(self):
        self._pattern = re.compile(r'\(\s*\"\s*call.*?\"', re.S)
        self._endSemicolon = re.compile(r'\(\s*\"\s*call.*?;\s*\"', re.S)
        pass

    def check_sentence(self):
        with open(r"Regular.txt") as codeFile:
            for line in codeFile:
                for matched in re.findall(self._pattern, line):
                    self.check_sem(matched)

    def check_sem(self, sentence):
        if not re.findall(self._endSemicolon, sentence):
            print("error")
        else:
            print("success")

test = CheckSql()

test.check_sentence()



