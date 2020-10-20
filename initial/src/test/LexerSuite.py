import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    ''' 
    def test_lower_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",101))

    def test_lower_upper_id(self):
        self.assertTrue(TestLexer.checkLexeme("Var","Var,<EOF>",102))

    def test_wrong_token(self):
        self.assertTrue(TestLexer.checkLexeme("ab?svn","ab,Error Token ?",103))

    def test_integer(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme("Var x;","Var,x,;,<EOF>",104))

    def test_illegal_escape(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\h def"  ""","""Illegal Escape In String: abc\\h""",105))

    def test_unterminated_string(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc def  ""","""Unclosed String: abc def  """,106))

    def test_normal_string_with_escape(self):
        """test normal string with escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "ab'"c\\n def"  ""","""ab'"c\\n def,<EOF>""",107))
    '''

    def test_block_commment(self):
        #self.assertTrue(TestLexer.checkLexeme('""abc12z\'\]""""\[\[\]''""','""abc12z\'\]"",""\[\[\]''"",<EOF>',101))
        #self.assertTrue(TestLexer.checkLexeme("\"\'\"abcd\'\"\\\'\"","\"abcd\"\',<EOF>",101))
        #self.assertTrue(TestLexer.checkLexeme("{{1,2},{3,4},{5,6}}",",<EOF>",101))
        f = open('E:\\Principle of Programming Language\\assignment1\\initial\\src\\test\\test.txt','r')
        input = f.read()
        self.assertTrue(TestLexer.checkLexeme(input,"<EOF>",101))
