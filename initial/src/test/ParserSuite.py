import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    '''
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = "Var: x=1.2,y=1.e10,z=\"kim\";Var: t=True,b[2][3] = {{2,3,4},{4,5,6}};"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))
    
    def test_wrong_miss_close(self):
        """Miss variable"""
        input = "Var: ;"
        expect = "Error on line 1 col 5: ;"
        self.assertTrue(TestParser.checkParser(input,expect,202))
    '''
    def test_simple_program(self):
        """Simple program: int main() {} """
        f = open('E:\\Principle of Programming Language\\assignment1\\initial\\src\\test\\test.txt','r')
        input = f.read()
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))