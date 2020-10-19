# Generated from e:\Principle of Programming Language\assignment1\initial\src\main\bkit\parser\BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2R")
        buf.write("\u0300\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\3\2")
        buf.write("\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27")
        buf.write("\6\27\u014f\n\27\r\27\16\27\u0150\3\27\7\27\u0154\n\27")
        buf.write("\f\27\16\27\u0157\13\27\3\30\3\30\3\30\3\30\3\30\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3 \3 \3!\3!")
        buf.write("\3!\3!\3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3#\3")
        buf.write("#\3#\3#\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3$\3$\3%\3%\3")
        buf.write("%\3%\3&\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3(\3(\3")
        buf.write("(\3)\3)\3)\3)\3)\3)\3*\3*\3*\3*\3*\3*\3*\3*\3*\3+\3+\3")
        buf.write("+\3+\3+\3,\3,\3,\3,\3,\3,\3-\3-\3.\3.\3.\3/\3/\3\60\3")
        buf.write("\60\3\60\3\61\3\61\3\62\3\62\3\62\3\63\3\63\3\64\3\64")
        buf.write("\3\64\3\65\3\65\3\66\3\66\3\67\3\67\3\67\38\38\38\39\3")
        buf.write("9\39\3:\3:\3:\3;\3;\3<\3<\3=\3=\3=\3>\3>\3>\3?\3?\3?\3")
        buf.write("?\3@\3@\3@\3A\3A\3A\3B\3B\3B\3B\3C\3C\3C\3C\3D\3D\3E\3")
        buf.write("E\3E\3E\5E\u0221\nE\3F\3F\6F\u0225\nF\rF\16F\u0226\3F")
        buf.write("\7F\u022a\nF\fF\16F\u022d\13F\3F\3F\3F\3F\5F\u0233\nF")
        buf.write("\3F\7F\u0236\nF\fF\16F\u0239\13F\3F\3F\3F\3F\5F\u023f")
        buf.write("\nF\3F\7F\u0242\nF\fF\16F\u0245\13F\5F\u0247\nF\3G\6G")
        buf.write("\u024a\nG\rG\16G\u024b\3G\3G\6G\u0250\nG\rG\16G\u0251")
        buf.write("\3G\3G\5G\u0256\nG\3G\6G\u0259\nG\rG\16G\u025a\3G\6G\u025e")
        buf.write("\nG\rG\16G\u025f\3G\3G\5G\u0264\nG\3G\6G\u0267\nG\rG\16")
        buf.write("G\u0268\5G\u026b\nG\3H\3H\5H\u026f\nH\3I\3I\3I\3I\5I\u0275")
        buf.write("\nI\3J\3J\3J\3K\3K\7K\u027c\nK\fK\16K\u027f\13K\3K\3K")
        buf.write("\3K\3L\3L\3L\3L\3L\7L\u0289\nL\fL\16L\u028c\13L\5L\u028e")
        buf.write("\nL\3L\3L\3L\3L\3L\3L\7L\u0296\nL\fL\16L\u0299\13L\5L")
        buf.write("\u029b\nL\3L\3L\3L\3L\3L\3L\7L\u02a3\nL\fL\16L\u02a6\13")
        buf.write("L\5L\u02a8\nL\3L\3L\3L\3L\3L\3L\7L\u02b0\nL\fL\16L\u02b3")
        buf.write("\13L\5L\u02b5\nL\3L\3L\3L\3L\3L\3L\7L\u02bd\nL\fL\16L")
        buf.write("\u02c0\13L\5L\u02c2\nL\3L\5L\u02c5\nL\3M\6M\u02c8\nM\r")
        buf.write("M\16M\u02c9\3M\3M\3N\3N\3O\3O\3O\3O\7O\u02d4\nO\fO\16")
        buf.write("O\u02d7\13O\3O\3O\3O\3P\3P\3P\3Q\3Q\7Q\u02e1\nQ\fQ\16")
        buf.write("Q\u02e4\13Q\3Q\3Q\3Q\3R\3R\3R\3S\3S\7S\u02ee\nS\fS\16")
        buf.write("S\u02f1\13S\3S\3S\3S\3T\3T\3T\3T\7T\u02fa\nT\fT\16T\u02fd")
        buf.write("\13T\3T\3T\3\u02d5\2U\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24")
        buf.write("\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37")
        buf.write("= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64")
        buf.write("g\65i\66k\67m8o9q:s;u<w=y>{?}@\177A\u0081B\u0083C\u0085")
        buf.write("D\u0087E\u0089F\u008bG\u008dH\u008fI\u0091\2\u0093\2\u0095")
        buf.write("J\u0097K\u0099L\u009bM\u009dN\u009fO\u00a1P\u00a3\2\u00a5")
        buf.write("Q\u00a7R\3\2\17\3\2c|\7\2))\62;C\\aac|\n\2*+..\60\60<")
        buf.write("=]]__}}\177\177\3\2\63;\3\2\62;\4\2\62;CH\3\2\629\4\2")
        buf.write("GGgg\4\2--//\7\2\n\f\16\17$$))^^\t\2))^^ddhhppttvv\5\2")
        buf.write("\13\f\16\17\"\"\3\2$$\2\u032a\2\3\3\2\2\2\2\5\3\2\2\2")
        buf.write("\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17")
        buf.write("\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3")
        buf.write("\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2")
        buf.write("\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3")
        buf.write("\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2")
        buf.write("\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3")
        buf.write("\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E")
        buf.write("\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2")
        buf.write("O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2")
        buf.write("\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2")
        buf.write("\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2")
        buf.write("\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3")
        buf.write("\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177")
        buf.write("\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2")
        buf.write("\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d")
        buf.write("\3\2\2\2\2\u008f\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2")
        buf.write("\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d\3\2\2\2\2\u009f")
        buf.write("\3\2\2\2\2\u00a1\3\2\2\2\2\u00a5\3\2\2\2\2\u00a7\3\2\2")
        buf.write("\2\3\u00a9\3\2\2\2\5\u00ab\3\2\2\2\7\u00ad\3\2\2\2\t\u00af")
        buf.write("\3\2\2\2\13\u00bc\3\2\2\2\r\u00c9\3\2\2\2\17\u00d7\3\2")
        buf.write("\2\2\21\u00e5\3\2\2\2\23\u00f5\3\2\2\2\25\u0105\3\2\2")
        buf.write("\2\27\u0114\3\2\2\2\31\u0123\3\2\2\2\33\u012b\3\2\2\2")
        buf.write("\35\u0131\3\2\2\2\37\u013c\3\2\2\2!\u0141\3\2\2\2#\u0143")
        buf.write("\3\2\2\2%\u0145\3\2\2\2\'\u0147\3\2\2\2)\u0149\3\2\2\2")
        buf.write("+\u014b\3\2\2\2-\u014e\3\2\2\2/\u0158\3\2\2\2\61\u015d")
        buf.write("\3\2\2\2\63\u0162\3\2\2\2\65\u0169\3\2\2\2\67\u016c\3")
        buf.write("\2\2\29\u0170\3\2\2\2;\u0176\3\2\2\2=\u017c\3\2\2\2?\u0183")
        buf.write("\3\2\2\2A\u018c\3\2\2\2C\u0196\3\2\2\2E\u019c\3\2\2\2")
        buf.write("G\u01a5\3\2\2\2I\u01ad\3\2\2\2K\u01b1\3\2\2\2M\u01b8\3")
        buf.write("\2\2\2O\u01bd\3\2\2\2Q\u01c0\3\2\2\2S\u01c6\3\2\2\2U\u01cf")
        buf.write("\3\2\2\2W\u01d4\3\2\2\2Y\u01da\3\2\2\2[\u01dc\3\2\2\2")
        buf.write("]\u01df\3\2\2\2_\u01e1\3\2\2\2a\u01e4\3\2\2\2c\u01e6\3")
        buf.write("\2\2\2e\u01e9\3\2\2\2g\u01eb\3\2\2\2i\u01ee\3\2\2\2k\u01f0")
        buf.write("\3\2\2\2m\u01f2\3\2\2\2o\u01f5\3\2\2\2q\u01f8\3\2\2\2")
        buf.write("s\u01fb\3\2\2\2u\u01fe\3\2\2\2w\u0200\3\2\2\2y\u0202\3")
        buf.write("\2\2\2{\u0205\3\2\2\2}\u0208\3\2\2\2\177\u020c\3\2\2\2")
        buf.write("\u0081\u020f\3\2\2\2\u0083\u0212\3\2\2\2\u0085\u0216\3")
        buf.write("\2\2\2\u0087\u021a\3\2\2\2\u0089\u0220\3\2\2\2\u008b\u0246")
        buf.write("\3\2\2\2\u008d\u0249\3\2\2\2\u008f\u026e\3\2\2\2\u0091")
        buf.write("\u0274\3\2\2\2\u0093\u0276\3\2\2\2\u0095\u0279\3\2\2\2")
        buf.write("\u0097\u02c4\3\2\2\2\u0099\u02c7\3\2\2\2\u009b\u02cd\3")
        buf.write("\2\2\2\u009d\u02cf\3\2\2\2\u009f\u02db\3\2\2\2\u00a1\u02de")
        buf.write("\3\2\2\2\u00a3\u02e8\3\2\2\2\u00a5\u02eb\3\2\2\2\u00a7")
        buf.write("\u02f5\3\2\2\2\u00a9\u00aa\7?\2\2\u00aa\4\3\2\2\2\u00ab")
        buf.write("\u00ac\7]\2\2\u00ac\6\3\2\2\2\u00ad\u00ae\7_\2\2\u00ae")
        buf.write("\b\3\2\2\2\u00af\u00b0\7k\2\2\u00b0\u00b1\7p\2\2\u00b1")
        buf.write("\u00b2\7v\2\2\u00b2\u00b3\7a\2\2\u00b3\u00b4\7q\2\2\u00b4")
        buf.write("\u00b5\7h\2\2\u00b5\u00b6\7a\2\2\u00b6\u00b7\7h\2\2\u00b7")
        buf.write("\u00b8\7n\2\2\u00b8\u00b9\7q\2\2\u00b9\u00ba\7c\2\2\u00ba")
        buf.write("\u00bb\7v\2\2\u00bb\n\3\2\2\2\u00bc\u00bd\7h\2\2\u00bd")
        buf.write("\u00be\7n\2\2\u00be\u00bf\7q\2\2\u00bf\u00c0\7c\2\2\u00c0")
        buf.write("\u00c1\7v\2\2\u00c1\u00c2\7a\2\2\u00c2\u00c3\7v\2\2\u00c3")
        buf.write("\u00c4\7q\2\2\u00c4\u00c5\7a\2\2\u00c5\u00c6\7k\2\2\u00c6")
        buf.write("\u00c7\7p\2\2\u00c7\u00c8\7v\2\2\u00c8\f\3\2\2\2\u00c9")
        buf.write("\u00ca\7k\2\2\u00ca\u00cb\7p\2\2\u00cb\u00cc\7v\2\2\u00cc")
        buf.write("\u00cd\7a\2\2\u00cd\u00ce\7q\2\2\u00ce\u00cf\7h\2\2\u00cf")
        buf.write("\u00d0\7a\2\2\u00d0\u00d1\7u\2\2\u00d1\u00d2\7v\2\2\u00d2")
        buf.write("\u00d3\7t\2\2\u00d3\u00d4\7k\2\2\u00d4\u00d5\7p\2\2\u00d5")
        buf.write("\u00d6\7i\2\2\u00d6\16\3\2\2\2\u00d7\u00d8\7u\2\2\u00d8")
        buf.write("\u00d9\7v\2\2\u00d9\u00da\7t\2\2\u00da\u00db\7k\2\2\u00db")
        buf.write("\u00dc\7p\2\2\u00dc\u00dd\7i\2\2\u00dd\u00de\7a\2\2\u00de")
        buf.write("\u00df\7q\2\2\u00df\u00e0\7h\2\2\u00e0\u00e1\7a\2\2\u00e1")
        buf.write("\u00e2\7k\2\2\u00e2\u00e3\7p\2\2\u00e3\u00e4\7v\2\2\u00e4")
        buf.write("\20\3\2\2\2\u00e5\u00e6\7h\2\2\u00e6\u00e7\7n\2\2\u00e7")
        buf.write("\u00e8\7q\2\2\u00e8\u00e9\7c\2\2\u00e9\u00ea\7v\2\2\u00ea")
        buf.write("\u00eb\7a\2\2\u00eb\u00ec\7q\2\2\u00ec\u00ed\7h\2\2\u00ed")
        buf.write("\u00ee\7a\2\2\u00ee\u00ef\7u\2\2\u00ef\u00f0\7v\2\2\u00f0")
        buf.write("\u00f1\7t\2\2\u00f1\u00f2\7k\2\2\u00f2\u00f3\7p\2\2\u00f3")
        buf.write("\u00f4\7i\2\2\u00f4\22\3\2\2\2\u00f5\u00f6\7u\2\2\u00f6")
        buf.write("\u00f7\7v\2\2\u00f7\u00f8\7t\2\2\u00f8\u00f9\7k\2\2\u00f9")
        buf.write("\u00fa\7p\2\2\u00fa\u00fb\7i\2\2\u00fb\u00fc\7a\2\2\u00fc")
        buf.write("\u00fd\7q\2\2\u00fd\u00fe\7h\2\2\u00fe\u00ff\7a\2\2\u00ff")
        buf.write("\u0100\7h\2\2\u0100\u0101\7n\2\2\u0101\u0102\7q\2\2\u0102")
        buf.write("\u0103\7c\2\2\u0103\u0104\7v\2\2\u0104\24\3\2\2\2\u0105")
        buf.write("\u0106\7d\2\2\u0106\u0107\7q\2\2\u0107\u0108\7q\2\2\u0108")
        buf.write("\u0109\7n\2\2\u0109\u010a\7a\2\2\u010a\u010b\7q\2\2\u010b")
        buf.write("\u010c\7h\2\2\u010c\u010d\7a\2\2\u010d\u010e\7u\2\2\u010e")
        buf.write("\u010f\7v\2\2\u010f\u0110\7t\2\2\u0110\u0111\7k\2\2\u0111")
        buf.write("\u0112\7p\2\2\u0112\u0113\7i\2\2\u0113\26\3\2\2\2\u0114")
        buf.write("\u0115\7u\2\2\u0115\u0116\7v\2\2\u0116\u0117\7t\2\2\u0117")
        buf.write("\u0118\7k\2\2\u0118\u0119\7p\2\2\u0119\u011a\7i\2\2\u011a")
        buf.write("\u011b\7a\2\2\u011b\u011c\7q\2\2\u011c\u011d\7h\2\2\u011d")
        buf.write("\u011e\7a\2\2\u011e\u011f\7d\2\2\u011f\u0120\7q\2\2\u0120")
        buf.write("\u0121\7q\2\2\u0121\u0122\7n\2\2\u0122\30\3\2\2\2\u0123")
        buf.write("\u0124\7r\2\2\u0124\u0125\7t\2\2\u0125\u0126\7k\2\2\u0126")
        buf.write("\u0127\7p\2\2\u0127\u0128\7v\2\2\u0128\u0129\7N\2\2\u0129")
        buf.write("\u012a\7p\2\2\u012a\32\3\2\2\2\u012b\u012c\7r\2\2\u012c")
        buf.write("\u012d\7t\2\2\u012d\u012e\7k\2\2\u012e\u012f\7p\2\2\u012f")
        buf.write("\u0130\7v\2\2\u0130\34\3\2\2\2\u0131\u0132\7r\2\2\u0132")
        buf.write("\u0133\7t\2\2\u0133\u0134\7k\2\2\u0134\u0135\7p\2\2\u0135")
        buf.write("\u0136\7v\2\2\u0136\u0137\7U\2\2\u0137\u0138\7v\2\2\u0138")
        buf.write("\u0139\7t\2\2\u0139\u013a\7N\2\2\u013a\u013b\7p\2\2\u013b")
        buf.write("\36\3\2\2\2\u013c\u013d\7t\2\2\u013d\u013e\7g\2\2\u013e")
        buf.write("\u013f\7c\2\2\u013f\u0140\7f\2\2\u0140 \3\2\2\2\u0141")
        buf.write("\u0142\7=\2\2\u0142\"\3\2\2\2\u0143\u0144\7.\2\2\u0144")
        buf.write("$\3\2\2\2\u0145\u0146\7<\2\2\u0146&\3\2\2\2\u0147\u0148")
        buf.write("\7\60\2\2\u0148(\3\2\2\2\u0149\u014a\7*\2\2\u014a*\3\2")
        buf.write("\2\2\u014b\u014c\7+\2\2\u014c,\3\2\2\2\u014d\u014f\t\2")
        buf.write("\2\2\u014e\u014d\3\2\2\2\u014f\u0150\3\2\2\2\u0150\u014e")
        buf.write("\3\2\2\2\u0150\u0151\3\2\2\2\u0151\u0155\3\2\2\2\u0152")
        buf.write("\u0154\t\3\2\2\u0153\u0152\3\2\2\2\u0154\u0157\3\2\2\2")
        buf.write("\u0155\u0153\3\2\2\2\u0155\u0156\3\2\2\2\u0156.\3\2\2")
        buf.write("\2\u0157\u0155\3\2\2\2\u0158\u0159\7D\2\2\u0159\u015a")
        buf.write("\7q\2\2\u015a\u015b\7f\2\2\u015b\u015c\7{\2\2\u015c\60")
        buf.write("\3\2\2\2\u015d\u015e\7G\2\2\u015e\u015f\7n\2\2\u015f\u0160")
        buf.write("\7u\2\2\u0160\u0161\7g\2\2\u0161\62\3\2\2\2\u0162\u0163")
        buf.write("\7G\2\2\u0163\u0164\7p\2\2\u0164\u0165\7f\2\2\u0165\u0166")
        buf.write("\7H\2\2\u0166\u0167\7q\2\2\u0167\u0168\7t\2\2\u0168\64")
        buf.write("\3\2\2\2\u0169\u016a\7K\2\2\u016a\u016b\7h\2\2\u016b\66")
        buf.write("\3\2\2\2\u016c\u016d\7X\2\2\u016d\u016e\7c\2\2\u016e\u016f")
        buf.write("\7t\2\2\u016f8\3\2\2\2\u0170\u0171\7G\2\2\u0171\u0172")
        buf.write("\7p\2\2\u0172\u0173\7f\2\2\u0173\u0174\7F\2\2\u0174\u0175")
        buf.write("\7q\2\2\u0175:\3\2\2\2\u0176\u0177\7D\2\2\u0177\u0178")
        buf.write("\7t\2\2\u0178\u0179\7g\2\2\u0179\u017a\7c\2\2\u017a\u017b")
        buf.write("\7m\2\2\u017b<\3\2\2\2\u017c\u017d\7G\2\2\u017d\u017e")
        buf.write("\7n\2\2\u017e\u017f\7u\2\2\u017f\u0180\7g\2\2\u0180\u0181")
        buf.write("\7K\2\2\u0181\u0182\7h\2\2\u0182>\3\2\2\2\u0183\u0184")
        buf.write("\7G\2\2\u0184\u0185\7p\2\2\u0185\u0186\7f\2\2\u0186\u0187")
        buf.write("\7Y\2\2\u0187\u0188\7j\2\2\u0188\u0189\7k\2\2\u0189\u018a")
        buf.write("\7n\2\2\u018a\u018b\7g\2\2\u018b@\3\2\2\2\u018c\u018d")
        buf.write("\7R\2\2\u018d\u018e\7c\2\2\u018e\u018f\7t\2\2\u018f\u0190")
        buf.write("\7c\2\2\u0190\u0191\7o\2\2\u0191\u0192\7g\2\2\u0192\u0193")
        buf.write("\7v\2\2\u0193\u0194\7g\2\2\u0194\u0195\7t\2\2\u0195B\3")
        buf.write("\2\2\2\u0196\u0197\7Y\2\2\u0197\u0198\7j\2\2\u0198\u0199")
        buf.write("\7k\2\2\u0199\u019a\7n\2\2\u019a\u019b\7g\2\2\u019bD\3")
        buf.write("\2\2\2\u019c\u019d\7E\2\2\u019d\u019e\7q\2\2\u019e\u019f")
        buf.write("\7p\2\2\u019f\u01a0\7v\2\2\u01a0\u01a1\7k\2\2\u01a1\u01a2")
        buf.write("\7p\2\2\u01a2\u01a3\7w\2\2\u01a3\u01a4\7g\2\2\u01a4F\3")
        buf.write("\2\2\2\u01a5\u01a6\7G\2\2\u01a6\u01a7\7p\2\2\u01a7\u01a8")
        buf.write("\7f\2\2\u01a8\u01a9\7D\2\2\u01a9\u01aa\7q\2\2\u01aa\u01ab")
        buf.write("\7f\2\2\u01ab\u01ac\7{\2\2\u01acH\3\2\2\2\u01ad\u01ae")
        buf.write("\7H\2\2\u01ae\u01af\7q\2\2\u01af\u01b0\7t\2\2\u01b0J\3")
        buf.write("\2\2\2\u01b1\u01b2\7T\2\2\u01b2\u01b3\7g\2\2\u01b3\u01b4")
        buf.write("\7v\2\2\u01b4\u01b5\7w\2\2\u01b5\u01b6\7t\2\2\u01b6\u01b7")
        buf.write("\7p\2\2\u01b7L\3\2\2\2\u01b8\u01b9\7V\2\2\u01b9\u01ba")
        buf.write("\7t\2\2\u01ba\u01bb\7w\2\2\u01bb\u01bc\7g\2\2\u01bcN\3")
        buf.write("\2\2\2\u01bd\u01be\7F\2\2\u01be\u01bf\7q\2\2\u01bfP\3")
        buf.write("\2\2\2\u01c0\u01c1\7G\2\2\u01c1\u01c2\7p\2\2\u01c2\u01c3")
        buf.write("\7f\2\2\u01c3\u01c4\7K\2\2\u01c4\u01c5\7h\2\2\u01c5R\3")
        buf.write("\2\2\2\u01c6\u01c7\7H\2\2\u01c7\u01c8\7w\2\2\u01c8\u01c9")
        buf.write("\7p\2\2\u01c9\u01ca\7e\2\2\u01ca\u01cb\7v\2\2\u01cb\u01cc")
        buf.write("\7k\2\2\u01cc\u01cd\7q\2\2\u01cd\u01ce\7p\2\2\u01ceT\3")
        buf.write("\2\2\2\u01cf\u01d0\7V\2\2\u01d0\u01d1\7j\2\2\u01d1\u01d2")
        buf.write("\7g\2\2\u01d2\u01d3\7p\2\2\u01d3V\3\2\2\2\u01d4\u01d5")
        buf.write("\7H\2\2\u01d5\u01d6\7c\2\2\u01d6\u01d7\7n\2\2\u01d7\u01d8")
        buf.write("\7u\2\2\u01d8\u01d9\7g\2\2\u01d9X\3\2\2\2\u01da\u01db")
        buf.write("\7-\2\2\u01dbZ\3\2\2\2\u01dc\u01dd\7-\2\2\u01dd\u01de")
        buf.write("\7\60\2\2\u01de\\\3\2\2\2\u01df\u01e0\7/\2\2\u01e0^\3")
        buf.write("\2\2\2\u01e1\u01e2\7/\2\2\u01e2\u01e3\7\60\2\2\u01e3`")
        buf.write("\3\2\2\2\u01e4\u01e5\7,\2\2\u01e5b\3\2\2\2\u01e6\u01e7")
        buf.write("\7,\2\2\u01e7\u01e8\7\60\2\2\u01e8d\3\2\2\2\u01e9\u01ea")
        buf.write("\7^\2\2\u01eaf\3\2\2\2\u01eb\u01ec\7^\2\2\u01ec\u01ed")
        buf.write("\7\60\2\2\u01edh\3\2\2\2\u01ee\u01ef\7\'\2\2\u01efj\3")
        buf.write("\2\2\2\u01f0\u01f1\7#\2\2\u01f1l\3\2\2\2\u01f2\u01f3\7")
        buf.write("(\2\2\u01f3\u01f4\7(\2\2\u01f4n\3\2\2\2\u01f5\u01f6\7")
        buf.write("~\2\2\u01f6\u01f7\7~\2\2\u01f7p\3\2\2\2\u01f8\u01f9\7")
        buf.write("?\2\2\u01f9\u01fa\7?\2\2\u01far\3\2\2\2\u01fb\u01fc\7")
        buf.write("#\2\2\u01fc\u01fd\7?\2\2\u01fdt\3\2\2\2\u01fe\u01ff\7")
        buf.write("@\2\2\u01ffv\3\2\2\2\u0200\u0201\7>\2\2\u0201x\3\2\2\2")
        buf.write("\u0202\u0203\7>\2\2\u0203\u0204\7?\2\2\u0204z\3\2\2\2")
        buf.write("\u0205\u0206\7@\2\2\u0206\u0207\7?\2\2\u0207|\3\2\2\2")
        buf.write("\u0208\u0209\7?\2\2\u0209\u020a\7\61\2\2\u020a\u020b\7")
        buf.write("?\2\2\u020b~\3\2\2\2\u020c\u020d\7@\2\2\u020d\u020e\7")
        buf.write("\60\2\2\u020e\u0080\3\2\2\2\u020f\u0210\7>\2\2\u0210\u0211")
        buf.write("\7\60\2\2\u0211\u0082\3\2\2\2\u0212\u0213\7>\2\2\u0213")
        buf.write("\u0214\7?\2\2\u0214\u0215\7\60\2\2\u0215\u0084\3\2\2\2")
        buf.write("\u0216\u0217\7@\2\2\u0217\u0218\7?\2\2\u0218\u0219\7\60")
        buf.write("\2\2\u0219\u0086\3\2\2\2\u021a\u021b\t\4\2\2\u021b\u0088")
        buf.write("\3\2\2\2\u021c\u0221\5\u008bF\2\u021d\u0221\5\u008dG\2")
        buf.write("\u021e\u0221\5\u0095K\2\u021f\u0221\5\u008fH\2\u0220\u021c")
        buf.write("\3\2\2\2\u0220\u021d\3\2\2\2\u0220\u021e\3\2\2\2\u0220")
        buf.write("\u021f\3\2\2\2\u0221\u008a\3\2\2\2\u0222\u0247\7\62\2")
        buf.write("\2\u0223\u0225\t\5\2\2\u0224\u0223\3\2\2\2\u0225\u0226")
        buf.write("\3\2\2\2\u0226\u0224\3\2\2\2\u0226\u0227\3\2\2\2\u0227")
        buf.write("\u022b\3\2\2\2\u0228\u022a\t\6\2\2\u0229\u0228\3\2\2\2")
        buf.write("\u022a\u022d\3\2\2\2\u022b\u0229\3\2\2\2\u022b\u022c\3")
        buf.write("\2\2\2\u022c\u0247\3\2\2\2\u022d\u022b\3\2\2\2\u022e\u022f")
        buf.write("\7\62\2\2\u022f\u0233\7z\2\2\u0230\u0231\7\62\2\2\u0231")
        buf.write("\u0233\7Z\2\2\u0232\u022e\3\2\2\2\u0232\u0230\3\2\2\2")
        buf.write("\u0233\u0237\3\2\2\2\u0234\u0236\t\7\2\2\u0235\u0234\3")
        buf.write("\2\2\2\u0236\u0239\3\2\2\2\u0237\u0235\3\2\2\2\u0237\u0238")
        buf.write("\3\2\2\2\u0238\u0247\3\2\2\2\u0239\u0237\3\2\2\2\u023a")
        buf.write("\u023b\7\62\2\2\u023b\u023f\7q\2\2\u023c\u023d\7\62\2")
        buf.write("\2\u023d\u023f\7Q\2\2\u023e\u023a\3\2\2\2\u023e\u023c")
        buf.write("\3\2\2\2\u023f\u0243\3\2\2\2\u0240\u0242\t\b\2\2\u0241")
        buf.write("\u0240\3\2\2\2\u0242\u0245\3\2\2\2\u0243\u0241\3\2\2\2")
        buf.write("\u0243\u0244\3\2\2\2\u0244\u0247\3\2\2\2\u0245\u0243\3")
        buf.write("\2\2\2\u0246\u0222\3\2\2\2\u0246\u0224\3\2\2\2\u0246\u0232")
        buf.write("\3\2\2\2\u0246\u023e\3\2\2\2\u0247\u008c\3\2\2\2\u0248")
        buf.write("\u024a\t\6\2\2\u0249\u0248\3\2\2\2\u024a\u024b\3\2\2\2")
        buf.write("\u024b\u0249\3\2\2\2\u024b\u024c\3\2\2\2\u024c\u024d\3")
        buf.write("\2\2\2\u024d\u026a\7\60\2\2\u024e\u0250\t\6\2\2\u024f")
        buf.write("\u024e\3\2\2\2\u0250\u0251\3\2\2\2\u0251\u024f\3\2\2\2")
        buf.write("\u0251\u0252\3\2\2\2\u0252\u0253\3\2\2\2\u0253\u0255\t")
        buf.write("\t\2\2\u0254\u0256\t\n\2\2\u0255\u0254\3\2\2\2\u0255\u0256")
        buf.write("\3\2\2\2\u0256\u0258\3\2\2\2\u0257\u0259\t\6\2\2\u0258")
        buf.write("\u0257\3\2\2\2\u0259\u025a\3\2\2\2\u025a\u0258\3\2\2\2")
        buf.write("\u025a\u025b\3\2\2\2\u025b\u026b\3\2\2\2\u025c\u025e\t")
        buf.write("\6\2\2\u025d\u025c\3\2\2\2\u025e\u025f\3\2\2\2\u025f\u025d")
        buf.write("\3\2\2\2\u025f\u0260\3\2\2\2\u0260\u026b\3\2\2\2\u0261")
        buf.write("\u0263\t\t\2\2\u0262\u0264\t\n\2\2\u0263\u0262\3\2\2\2")
        buf.write("\u0263\u0264\3\2\2\2\u0264\u0266\3\2\2\2\u0265\u0267\t")
        buf.write("\6\2\2\u0266\u0265\3\2\2\2\u0267\u0268\3\2\2\2\u0268\u0266")
        buf.write("\3\2\2\2\u0268\u0269\3\2\2\2\u0269\u026b\3\2\2\2\u026a")
        buf.write("\u024f\3\2\2\2\u026a\u025d\3\2\2\2\u026a\u0261\3\2\2\2")
        buf.write("\u026b\u008e\3\2\2\2\u026c\u026f\5M\'\2\u026d\u026f\5")
        buf.write("W,\2\u026e\u026c\3\2\2\2\u026e\u026d\3\2\2\2\u026f\u0090")
        buf.write("\3\2\2\2\u0270\u0275\n\13\2\2\u0271\u0275\5\u0093J\2\u0272")
        buf.write("\u0273\7)\2\2\u0273\u0275\7$\2\2\u0274\u0270\3\2\2\2\u0274")
        buf.write("\u0271\3\2\2\2\u0274\u0272\3\2\2\2\u0275\u0092\3\2\2\2")
        buf.write("\u0276\u0277\7^\2\2\u0277\u0278\t\f\2\2\u0278\u0094\3")
        buf.write("\2\2\2\u0279\u027d\7$\2\2\u027a\u027c\5\u0091I\2\u027b")
        buf.write("\u027a\3\2\2\2\u027c\u027f\3\2\2\2\u027d\u027b\3\2\2\2")
        buf.write("\u027d\u027e\3\2\2\2\u027e\u0280\3\2\2\2\u027f\u027d\3")
        buf.write("\2\2\2\u0280\u0281\7$\2\2\u0281\u0282\bK\2\2\u0282\u0096")
        buf.write("\3\2\2\2\u0283\u028d\7}\2\2\u0284\u028e\3\2\2\2\u0285")
        buf.write("\u028a\5\u008bF\2\u0286\u0287\7.\2\2\u0287\u0289\5\u008b")
        buf.write("F\2\u0288\u0286\3\2\2\2\u0289\u028c\3\2\2\2\u028a\u0288")
        buf.write("\3\2\2\2\u028a\u028b\3\2\2\2\u028b\u028e\3\2\2\2\u028c")
        buf.write("\u028a\3\2\2\2\u028d\u0284\3\2\2\2\u028d\u0285\3\2\2\2")
        buf.write("\u028e\u028f\3\2\2\2\u028f\u02c5\7\177\2\2\u0290\u029a")
        buf.write("\7}\2\2\u0291\u029b\3\2\2\2\u0292\u0297\5\u008dG\2\u0293")
        buf.write("\u0294\7.\2\2\u0294\u0296\5\u008dG\2\u0295\u0293\3\2\2")
        buf.write("\2\u0296\u0299\3\2\2\2\u0297\u0295\3\2\2\2\u0297\u0298")
        buf.write("\3\2\2\2\u0298\u029b\3\2\2\2\u0299\u0297\3\2\2\2\u029a")
        buf.write("\u0291\3\2\2\2\u029a\u0292\3\2\2\2\u029b\u029c\3\2\2\2")
        buf.write("\u029c\u02c5\7\177\2\2\u029d\u02a7\7}\2\2\u029e\u02a8")
        buf.write("\3\2\2\2\u029f\u02a4\5\u008fH\2\u02a0\u02a1\7.\2\2\u02a1")
        buf.write("\u02a3\5\u008fH\2\u02a2\u02a0\3\2\2\2\u02a3\u02a6\3\2")
        buf.write("\2\2\u02a4\u02a2\3\2\2\2\u02a4\u02a5\3\2\2\2\u02a5\u02a8")
        buf.write("\3\2\2\2\u02a6\u02a4\3\2\2\2\u02a7\u029e\3\2\2\2\u02a7")
        buf.write("\u029f\3\2\2\2\u02a8\u02a9\3\2\2\2\u02a9\u02c5\7\177\2")
        buf.write("\2\u02aa\u02b4\7}\2\2\u02ab\u02b5\3\2\2\2\u02ac\u02b1")
        buf.write("\5\u0095K\2\u02ad\u02ae\7.\2\2\u02ae\u02b0\5\u0095K\2")
        buf.write("\u02af\u02ad\3\2\2\2\u02b0\u02b3\3\2\2\2\u02b1\u02af\3")
        buf.write("\2\2\2\u02b1\u02b2\3\2\2\2\u02b2\u02b5\3\2\2\2\u02b3\u02b1")
        buf.write("\3\2\2\2\u02b4\u02ab\3\2\2\2\u02b4\u02ac\3\2\2\2\u02b5")
        buf.write("\u02b6\3\2\2\2\u02b6\u02c5\7\177\2\2\u02b7\u02c1\7}\2")
        buf.write("\2\u02b8\u02c2\3\2\2\2\u02b9\u02be\5\u0097L\2\u02ba\u02bb")
        buf.write("\7.\2\2\u02bb\u02bd\5\u0097L\2\u02bc\u02ba\3\2\2\2\u02bd")
        buf.write("\u02c0\3\2\2\2\u02be\u02bc\3\2\2\2\u02be\u02bf\3\2\2\2")
        buf.write("\u02bf\u02c2\3\2\2\2\u02c0\u02be\3\2\2\2\u02c1\u02b8\3")
        buf.write("\2\2\2\u02c1\u02b9\3\2\2\2\u02c2\u02c3\3\2\2\2\u02c3\u02c5")
        buf.write("\7\177\2\2\u02c4\u0283\3\2\2\2\u02c4\u0290\3\2\2\2\u02c4")
        buf.write("\u029d\3\2\2\2\u02c4\u02aa\3\2\2\2\u02c4\u02b7\3\2\2\2")
        buf.write("\u02c5\u0098\3\2\2\2\u02c6\u02c8\t\r\2\2\u02c7\u02c6\3")
        buf.write("\2\2\2\u02c8\u02c9\3\2\2\2\u02c9\u02c7\3\2\2\2\u02c9\u02ca")
        buf.write("\3\2\2\2\u02ca\u02cb\3\2\2\2\u02cb\u02cc\bM\3\2\u02cc")
        buf.write("\u009a\3\2\2\2\u02cd\u02ce\7\f\2\2\u02ce\u009c\3\2\2\2")
        buf.write("\u02cf\u02d0\7$\2\2\u02d0\u02d1\7$\2\2\u02d1\u02d5\3\2")
        buf.write("\2\2\u02d2\u02d4\13\2\2\2\u02d3\u02d2\3\2\2\2\u02d4\u02d7")
        buf.write("\3\2\2\2\u02d5\u02d6\3\2\2\2\u02d5\u02d3\3\2\2\2\u02d6")
        buf.write("\u02d8\3\2\2\2\u02d7\u02d5\3\2\2\2\u02d8\u02d9\7$\2\2")
        buf.write("\u02d9\u02da\7$\2\2\u02da\u009e\3\2\2\2\u02db\u02dc\13")
        buf.write("\2\2\2\u02dc\u02dd\bP\4\2\u02dd\u00a0\3\2\2\2\u02de\u02e2")
        buf.write("\7$\2\2\u02df\u02e1\5\u0091I\2\u02e0\u02df\3\2\2\2\u02e1")
        buf.write("\u02e4\3\2\2\2\u02e2\u02e0\3\2\2\2\u02e2\u02e3\3\2\2\2")
        buf.write("\u02e3\u02e5\3\2\2\2\u02e4\u02e2\3\2\2\2\u02e5\u02e6\n")
        buf.write("\16\2\2\u02e6\u02e7\bQ\5\2\u02e7\u00a2\3\2\2\2\u02e8\u02e9")
        buf.write("\7^\2\2\u02e9\u02ea\n\f\2\2\u02ea\u00a4\3\2\2\2\u02eb")
        buf.write("\u02ef\7$\2\2\u02ec\u02ee\5\u0091I\2\u02ed\u02ec\3\2\2")
        buf.write("\2\u02ee\u02f1\3\2\2\2\u02ef\u02ed\3\2\2\2\u02ef\u02f0")
        buf.write("\3\2\2\2\u02f0\u02f2\3\2\2\2\u02f1\u02ef\3\2\2\2\u02f2")
        buf.write("\u02f3\5\u00a3R\2\u02f3\u02f4\bS\6\2\u02f4\u00a6\3\2\2")
        buf.write("\2\u02f5\u02f6\7$\2\2\u02f6\u02f7\7$\2\2\u02f7\u02fb\3")
        buf.write("\2\2\2\u02f8\u02fa\13\2\2\2\u02f9\u02f8\3\2\2\2\u02fa")
        buf.write("\u02fd\3\2\2\2\u02fb\u02f9\3\2\2\2\u02fb\u02fc\3\2\2\2")
        buf.write("\u02fc\u02fe\3\2\2\2\u02fd\u02fb\3\2\2\2\u02fe\u02ff\b")
        buf.write("T\7\2\u02ff\u00a8\3\2\2\2(\2\u0150\u0155\u0220\u0226\u022b")
        buf.write("\u0232\u0237\u023e\u0243\u0246\u024b\u0251\u0255\u025a")
        buf.write("\u025f\u0263\u0268\u026a\u026e\u0274\u027d\u028a\u028d")
        buf.write("\u0297\u029a\u02a4\u02a7\u02b1\u02b4\u02be\u02c1\u02c4")
        buf.write("\u02c9\u02d5\u02e2\u02ef\u02fb\b\3K\2\b\2\2\3P\3\3Q\4")
        buf.write("\3S\5\3T\6")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    SEMI = 16
    COMMA = 17
    COLON = 18
    DOT = 19
    LP = 20
    RP = 21
    ID = 22
    BODY = 23
    ELSE = 24
    ENDFOR = 25
    IF = 26
    VAR = 27
    ENDDO = 28
    BREAK = 29
    ELSEIF = 30
    ENDWHILE = 31
    PARAMETER = 32
    WHILE = 33
    CONTINUE = 34
    ENDBODY = 35
    FOR = 36
    RETURN = 37
    TRUE = 38
    DO = 39
    ENDIF = 40
    FUNCTION = 41
    THEN = 42
    FALSE = 43
    ADD = 44
    ADDDOT = 45
    SUB = 46
    SUBDOT = 47
    MUL = 48
    MULDOT = 49
    DIV = 50
    DIVDOT = 51
    MOD = 52
    NEG = 53
    AND = 54
    OR = 55
    EQ = 56
    NEI = 57
    GT = 58
    LT = 59
    LTE = 60
    GTE = 61
    NEF = 62
    GTDOT = 63
    LTDOT = 64
    LTEDOT = 65
    GTEDOT = 66
    SEPERATOR = 67
    LITERAL = 68
    INTEGER = 69
    FLOAT = 70
    BOOLEAN = 71
    STRING = 72
    ARRAY = 73
    WS = 74
    NEW_LINE = 75
    BLOCK_COMMENT = 76
    ERROR_CHAR = 77
    UNCLOSE_STRING = 78
    ILLEGAL_ESCAPE = 79
    UNTERMINATED_COMMENT = 80

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "'['", "']'", "'int_of_float'", "'float_to_int'", "'int_of_string'", 
            "'string_of_int'", "'float_of_string'", "'string_of_float'", 
            "'bool_of_string'", "'string_of_bool'", "'printLn'", "'print'", 
            "'printStrLn'", "'read'", "';'", "','", "':'", "'.'", "'('", 
            "')'", "'Body'", "'Else'", "'EndFor'", "'If'", "'Var'", "'EndDo'", 
            "'Break'", "'ElseIf'", "'EndWhile'", "'Parameter'", "'While'", 
            "'Continue'", "'EndBody'", "'For'", "'Return'", "'True'", "'Do'", 
            "'EndIf'", "'Function'", "'Then'", "'False'", "'+'", "'+.'", 
            "'-'", "'-.'", "'*'", "'*.'", "'\\'", "'\\.'", "'%'", "'!'", 
            "'&&'", "'||'", "'=='", "'!='", "'>'", "'<'", "'<='", "'>='", 
            "'=/='", "'>.'", "'<.'", "'<=.'", "'>=.'", "'\n'" ]

    symbolicNames = [ "<INVALID>",
            "SEMI", "COMMA", "COLON", "DOT", "LP", "RP", "ID", "BODY", "ELSE", 
            "ENDFOR", "IF", "VAR", "ENDDO", "BREAK", "ELSEIF", "ENDWHILE", 
            "PARAMETER", "WHILE", "CONTINUE", "ENDBODY", "FOR", "RETURN", 
            "TRUE", "DO", "ENDIF", "FUNCTION", "THEN", "FALSE", "ADD", "ADDDOT", 
            "SUB", "SUBDOT", "MUL", "MULDOT", "DIV", "DIVDOT", "MOD", "NEG", 
            "AND", "OR", "EQ", "NEI", "GT", "LT", "LTE", "GTE", "NEF", "GTDOT", 
            "LTDOT", "LTEDOT", "GTEDOT", "SEPERATOR", "LITERAL", "INTEGER", 
            "FLOAT", "BOOLEAN", "STRING", "ARRAY", "WS", "NEW_LINE", "BLOCK_COMMENT", 
            "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "SEMI", "COMMA", "COLON", "DOT", "LP", "RP", 
                  "ID", "BODY", "ELSE", "ENDFOR", "IF", "VAR", "ENDDO", 
                  "BREAK", "ELSEIF", "ENDWHILE", "PARAMETER", "WHILE", "CONTINUE", 
                  "ENDBODY", "FOR", "RETURN", "TRUE", "DO", "ENDIF", "FUNCTION", 
                  "THEN", "FALSE", "ADD", "ADDDOT", "SUB", "SUBDOT", "MUL", 
                  "MULDOT", "DIV", "DIVDOT", "MOD", "NEG", "AND", "OR", 
                  "EQ", "NEI", "GT", "LT", "LTE", "GTE", "NEF", "GTDOT", 
                  "LTDOT", "LTEDOT", "GTEDOT", "SEPERATOR", "LITERAL", "INTEGER", 
                  "FLOAT", "BOOLEAN", "STR_CHAR", "ESC_SEQ", "STRING", "ARRAY", 
                  "WS", "NEW_LINE", "BLOCK_COMMENT", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ESC_ILLEGAL", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()
        if tk == self.UNCLOSE_STRING:       
            raise UncloseString(result.text)
        elif tk == self.ILLEGAL_ESCAPE:
            raise IllegalEscape(result.text)
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        elif tk == self.UNTERMINATED_COMMENT:
            raise UnterminatedComment()
        else:
            return result;


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[73] = self.STRING_action 
            actions[78] = self.ERROR_CHAR_action 
            actions[79] = self.UNCLOSE_STRING_action 
            actions[81] = self.ILLEGAL_ESCAPE_action 
            actions[82] = self.UNTERMINATED_COMMENT_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            		y = str(self.text)
            		self.text = y[1:-1].replace("\'\"","\"").replace("\\b","\b").replace("\\f","\f").replace("\\r","\r").replace("\\n","\n").replace("\\t","\t").replace("\\'","\'").replace("\\\\","\\")   
            	
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            		raise ErrorToken(str(self.text))
            	
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            		y = str(self.text)
            		raise UncloseString(y[1:])
            	
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            		y = str(self.text)
            		raise IllegalEscape(y[1:])
            	
     

    def UNTERMINATED_COMMENT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

                    raise UnterminatedComment()
                
     


