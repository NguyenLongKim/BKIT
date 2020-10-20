# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2N")
        buf.write("\u0303\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\3\2\3\2\3\3\3\3\3\4\3\4\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23")
        buf.write("\3\24\3\24\3\25\3\25\3\26\3\26\3\27\6\27\u0147\n\27\r")
        buf.write("\27\16\27\u0148\3\27\7\27\u014c\n\27\f\27\16\27\u014f")
        buf.write("\13\27\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3")
        buf.write("\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33")
        buf.write("\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3 \3 \3 \3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3!")
        buf.write("\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3")
        buf.write("#\3#\3#\3$\3$\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3&\3&\3&\3")
        buf.write("&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3)\3")
        buf.write(")\3)\3*\3*\3*\3*\3*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3,\3,\3")
        buf.write(",\3,\3,\3,\3-\3-\3.\3.\3.\3/\3/\3\60\3\60\3\60\3\61\3")
        buf.write("\61\3\62\3\62\3\62\3\63\3\63\3\64\3\64\3\64\3\65\3\65")
        buf.write("\3\66\3\66\3\67\3\67\3\67\38\38\38\39\39\39\3:\3:\3:\3")
        buf.write(";\3;\3<\3<\3=\3=\3=\3>\3>\3>\3?\3?\3?\3?\3@\3@\3@\3A\3")
        buf.write("A\3A\3B\3B\3B\3B\3C\3C\3C\3C\3D\3D\6D\u0215\nD\rD\16D")
        buf.write("\u0216\3D\7D\u021a\nD\fD\16D\u021d\13D\3D\3D\3D\3D\5D")
        buf.write("\u0223\nD\3D\7D\u0226\nD\fD\16D\u0229\13D\3D\3D\3D\3D")
        buf.write("\5D\u022f\nD\3D\7D\u0232\nD\fD\16D\u0235\13D\5D\u0237")
        buf.write("\nD\3E\6E\u023a\nE\rE\16E\u023b\3E\3E\6E\u0240\nE\rE\16")
        buf.write("E\u0241\3E\3E\5E\u0246\nE\3E\6E\u0249\nE\rE\16E\u024a")
        buf.write("\3E\6E\u024e\nE\rE\16E\u024f\3E\3E\5E\u0254\nE\3E\6E\u0257")
        buf.write("\nE\rE\16E\u0258\5E\u025b\nE\3F\3F\3F\3F\5F\u0261\nF\3")
        buf.write("G\3G\3G\3H\3H\7H\u0268\nH\fH\16H\u026b\13H\3H\3H\3H\3")
        buf.write("I\3I\3I\3I\3I\7I\u0275\nI\fI\16I\u0278\13I\5I\u027a\n")
        buf.write("I\3I\3I\3I\3I\3I\3I\7I\u0282\nI\fI\16I\u0285\13I\5I\u0287")
        buf.write("\nI\3I\3I\3I\3I\3I\5I\u028e\nI\3I\3I\3I\5I\u0293\nI\7")
        buf.write("I\u0295\nI\fI\16I\u0298\13I\5I\u029a\nI\3I\3I\3I\3I\3")
        buf.write("I\3I\7I\u02a2\nI\fI\16I\u02a5\13I\5I\u02a7\nI\3I\3I\3")
        buf.write("I\3I\3I\3I\7I\u02af\nI\fI\16I\u02b2\13I\5I\u02b4\nI\3")
        buf.write("I\5I\u02b7\nI\3J\6J\u02ba\nJ\rJ\16J\u02bb\3J\3J\3K\3K")
        buf.write("\3K\3K\7K\u02c4\nK\fK\16K\u02c7\13K\3K\3K\3K\3K\3K\3L")
        buf.write("\3L\3L\3M\3M\7M\u02d3\nM\fM\16M\u02d6\13M\3M\5M\u02d9")
        buf.write("\nM\3M\3M\3N\3N\3N\3O\3O\7O\u02e2\nO\fO\16O\u02e5\13O")
        buf.write("\3O\3O\3O\3P\3P\3P\3P\7P\u02ee\nP\fP\16P\u02f1\13P\3P")
        buf.write("\3P\3P\6P\u02f6\nP\rP\16P\u02f7\7P\u02fa\nP\fP\16P\u02fd")
        buf.write("\13P\5P\u02ff\nP\3P\3P\3P\3\u02c5\2Q\3\3\5\4\7\5\t\6\13")
        buf.write("\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37")
        buf.write("\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34")
        buf.write("\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_")
        buf.write("\61a\62c\63e\64g\65i\66k\67m8o9q:s;u<w=y>{?}@\177A\u0081")
        buf.write("B\u0083C\u0085D\u0087E\u0089F\u008b\2\u008d\2\u008fG\u0091")
        buf.write("H\u0093I\u0095J\u0097K\u0099L\u009b\2\u009dM\u009fN\3")
        buf.write("\2\17\3\2c|\7\2))\62;C\\aac|\3\2\63;\3\2\62;\4\2\62;C")
        buf.write("H\3\2\629\4\2GGgg\4\2--//\7\2\n\f\16\17$$))^^\t\2))^^")
        buf.write("ddhhppttvv\5\2\13\f\16\17\"\"\7\3\n\f\16\17$$))^^\3\2")
        buf.write(",,\2\u032e\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2")
        buf.write("\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2")
        buf.write("\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2")
        buf.write("\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#")
        buf.write("\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2")
        buf.write("\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3")
        buf.write("\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e")
        buf.write("\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2")
        buf.write("o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2")
        buf.write("\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081")
        buf.write("\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2")
        buf.write("\2\2\u0089\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093")
        buf.write("\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2")
        buf.write("\2\2\u009d\3\2\2\2\2\u009f\3\2\2\2\3\u00a1\3\2\2\2\5\u00a3")
        buf.write("\3\2\2\2\7\u00a5\3\2\2\2\t\u00a7\3\2\2\2\13\u00b4\3\2")
        buf.write("\2\2\r\u00c1\3\2\2\2\17\u00cf\3\2\2\2\21\u00dd\3\2\2\2")
        buf.write("\23\u00ed\3\2\2\2\25\u00fd\3\2\2\2\27\u010c\3\2\2\2\31")
        buf.write("\u011b\3\2\2\2\33\u0123\3\2\2\2\35\u0129\3\2\2\2\37\u0134")
        buf.write("\3\2\2\2!\u0139\3\2\2\2#\u013b\3\2\2\2%\u013d\3\2\2\2")
        buf.write("\'\u013f\3\2\2\2)\u0141\3\2\2\2+\u0143\3\2\2\2-\u0146")
        buf.write("\3\2\2\2/\u0150\3\2\2\2\61\u0155\3\2\2\2\63\u015a\3\2")
        buf.write("\2\2\65\u0161\3\2\2\2\67\u0164\3\2\2\29\u0168\3\2\2\2")
        buf.write(";\u016e\3\2\2\2=\u0174\3\2\2\2?\u017b\3\2\2\2A\u0184\3")
        buf.write("\2\2\2C\u018e\3\2\2\2E\u0194\3\2\2\2G\u019d\3\2\2\2I\u01a5")
        buf.write("\3\2\2\2K\u01a9\3\2\2\2M\u01b0\3\2\2\2O\u01b5\3\2\2\2")
        buf.write("Q\u01b8\3\2\2\2S\u01be\3\2\2\2U\u01c7\3\2\2\2W\u01cc\3")
        buf.write("\2\2\2Y\u01d2\3\2\2\2[\u01d4\3\2\2\2]\u01d7\3\2\2\2_\u01d9")
        buf.write("\3\2\2\2a\u01dc\3\2\2\2c\u01de\3\2\2\2e\u01e1\3\2\2\2")
        buf.write("g\u01e3\3\2\2\2i\u01e6\3\2\2\2k\u01e8\3\2\2\2m\u01ea\3")
        buf.write("\2\2\2o\u01ed\3\2\2\2q\u01f0\3\2\2\2s\u01f3\3\2\2\2u\u01f6")
        buf.write("\3\2\2\2w\u01f8\3\2\2\2y\u01fa\3\2\2\2{\u01fd\3\2\2\2")
        buf.write("}\u0200\3\2\2\2\177\u0204\3\2\2\2\u0081\u0207\3\2\2\2")
        buf.write("\u0083\u020a\3\2\2\2\u0085\u020e\3\2\2\2\u0087\u0236\3")
        buf.write("\2\2\2\u0089\u0239\3\2\2\2\u008b\u0260\3\2\2\2\u008d\u0262")
        buf.write("\3\2\2\2\u008f\u0265\3\2\2\2\u0091\u02b6\3\2\2\2\u0093")
        buf.write("\u02b9\3\2\2\2\u0095\u02bf\3\2\2\2\u0097\u02cd\3\2\2\2")
        buf.write("\u0099\u02d0\3\2\2\2\u009b\u02dc\3\2\2\2\u009d\u02df\3")
        buf.write("\2\2\2\u009f\u02e9\3\2\2\2\u00a1\u00a2\7?\2\2\u00a2\4")
        buf.write("\3\2\2\2\u00a3\u00a4\7]\2\2\u00a4\6\3\2\2\2\u00a5\u00a6")
        buf.write("\7_\2\2\u00a6\b\3\2\2\2\u00a7\u00a8\7k\2\2\u00a8\u00a9")
        buf.write("\7p\2\2\u00a9\u00aa\7v\2\2\u00aa\u00ab\7a\2\2\u00ab\u00ac")
        buf.write("\7q\2\2\u00ac\u00ad\7h\2\2\u00ad\u00ae\7a\2\2\u00ae\u00af")
        buf.write("\7h\2\2\u00af\u00b0\7n\2\2\u00b0\u00b1\7q\2\2\u00b1\u00b2")
        buf.write("\7c\2\2\u00b2\u00b3\7v\2\2\u00b3\n\3\2\2\2\u00b4\u00b5")
        buf.write("\7h\2\2\u00b5\u00b6\7n\2\2\u00b6\u00b7\7q\2\2\u00b7\u00b8")
        buf.write("\7c\2\2\u00b8\u00b9\7v\2\2\u00b9\u00ba\7a\2\2\u00ba\u00bb")
        buf.write("\7q\2\2\u00bb\u00bc\7h\2\2\u00bc\u00bd\7a\2\2\u00bd\u00be")
        buf.write("\7k\2\2\u00be\u00bf\7p\2\2\u00bf\u00c0\7v\2\2\u00c0\f")
        buf.write("\3\2\2\2\u00c1\u00c2\7k\2\2\u00c2\u00c3\7p\2\2\u00c3\u00c4")
        buf.write("\7v\2\2\u00c4\u00c5\7a\2\2\u00c5\u00c6\7q\2\2\u00c6\u00c7")
        buf.write("\7h\2\2\u00c7\u00c8\7a\2\2\u00c8\u00c9\7u\2\2\u00c9\u00ca")
        buf.write("\7v\2\2\u00ca\u00cb\7t\2\2\u00cb\u00cc\7k\2\2\u00cc\u00cd")
        buf.write("\7p\2\2\u00cd\u00ce\7i\2\2\u00ce\16\3\2\2\2\u00cf\u00d0")
        buf.write("\7u\2\2\u00d0\u00d1\7v\2\2\u00d1\u00d2\7t\2\2\u00d2\u00d3")
        buf.write("\7k\2\2\u00d3\u00d4\7p\2\2\u00d4\u00d5\7i\2\2\u00d5\u00d6")
        buf.write("\7a\2\2\u00d6\u00d7\7q\2\2\u00d7\u00d8\7h\2\2\u00d8\u00d9")
        buf.write("\7a\2\2\u00d9\u00da\7k\2\2\u00da\u00db\7p\2\2\u00db\u00dc")
        buf.write("\7v\2\2\u00dc\20\3\2\2\2\u00dd\u00de\7h\2\2\u00de\u00df")
        buf.write("\7n\2\2\u00df\u00e0\7q\2\2\u00e0\u00e1\7c\2\2\u00e1\u00e2")
        buf.write("\7v\2\2\u00e2\u00e3\7a\2\2\u00e3\u00e4\7q\2\2\u00e4\u00e5")
        buf.write("\7h\2\2\u00e5\u00e6\7a\2\2\u00e6\u00e7\7u\2\2\u00e7\u00e8")
        buf.write("\7v\2\2\u00e8\u00e9\7t\2\2\u00e9\u00ea\7k\2\2\u00ea\u00eb")
        buf.write("\7p\2\2\u00eb\u00ec\7i\2\2\u00ec\22\3\2\2\2\u00ed\u00ee")
        buf.write("\7u\2\2\u00ee\u00ef\7v\2\2\u00ef\u00f0\7t\2\2\u00f0\u00f1")
        buf.write("\7k\2\2\u00f1\u00f2\7p\2\2\u00f2\u00f3\7i\2\2\u00f3\u00f4")
        buf.write("\7a\2\2\u00f4\u00f5\7q\2\2\u00f5\u00f6\7h\2\2\u00f6\u00f7")
        buf.write("\7a\2\2\u00f7\u00f8\7h\2\2\u00f8\u00f9\7n\2\2\u00f9\u00fa")
        buf.write("\7q\2\2\u00fa\u00fb\7c\2\2\u00fb\u00fc\7v\2\2\u00fc\24")
        buf.write("\3\2\2\2\u00fd\u00fe\7d\2\2\u00fe\u00ff\7q\2\2\u00ff\u0100")
        buf.write("\7q\2\2\u0100\u0101\7n\2\2\u0101\u0102\7a\2\2\u0102\u0103")
        buf.write("\7q\2\2\u0103\u0104\7h\2\2\u0104\u0105\7a\2\2\u0105\u0106")
        buf.write("\7u\2\2\u0106\u0107\7v\2\2\u0107\u0108\7t\2\2\u0108\u0109")
        buf.write("\7k\2\2\u0109\u010a\7p\2\2\u010a\u010b\7i\2\2\u010b\26")
        buf.write("\3\2\2\2\u010c\u010d\7u\2\2\u010d\u010e\7v\2\2\u010e\u010f")
        buf.write("\7t\2\2\u010f\u0110\7k\2\2\u0110\u0111\7p\2\2\u0111\u0112")
        buf.write("\7i\2\2\u0112\u0113\7a\2\2\u0113\u0114\7q\2\2\u0114\u0115")
        buf.write("\7h\2\2\u0115\u0116\7a\2\2\u0116\u0117\7d\2\2\u0117\u0118")
        buf.write("\7q\2\2\u0118\u0119\7q\2\2\u0119\u011a\7n\2\2\u011a\30")
        buf.write("\3\2\2\2\u011b\u011c\7r\2\2\u011c\u011d\7t\2\2\u011d\u011e")
        buf.write("\7k\2\2\u011e\u011f\7p\2\2\u011f\u0120\7v\2\2\u0120\u0121")
        buf.write("\7N\2\2\u0121\u0122\7p\2\2\u0122\32\3\2\2\2\u0123\u0124")
        buf.write("\7r\2\2\u0124\u0125\7t\2\2\u0125\u0126\7k\2\2\u0126\u0127")
        buf.write("\7p\2\2\u0127\u0128\7v\2\2\u0128\34\3\2\2\2\u0129\u012a")
        buf.write("\7r\2\2\u012a\u012b\7t\2\2\u012b\u012c\7k\2\2\u012c\u012d")
        buf.write("\7p\2\2\u012d\u012e\7v\2\2\u012e\u012f\7U\2\2\u012f\u0130")
        buf.write("\7v\2\2\u0130\u0131\7t\2\2\u0131\u0132\7N\2\2\u0132\u0133")
        buf.write("\7p\2\2\u0133\36\3\2\2\2\u0134\u0135\7t\2\2\u0135\u0136")
        buf.write("\7g\2\2\u0136\u0137\7c\2\2\u0137\u0138\7f\2\2\u0138 \3")
        buf.write("\2\2\2\u0139\u013a\7=\2\2\u013a\"\3\2\2\2\u013b\u013c")
        buf.write("\7.\2\2\u013c$\3\2\2\2\u013d\u013e\7<\2\2\u013e&\3\2\2")
        buf.write("\2\u013f\u0140\7\60\2\2\u0140(\3\2\2\2\u0141\u0142\7*")
        buf.write("\2\2\u0142*\3\2\2\2\u0143\u0144\7+\2\2\u0144,\3\2\2\2")
        buf.write("\u0145\u0147\t\2\2\2\u0146\u0145\3\2\2\2\u0147\u0148\3")
        buf.write("\2\2\2\u0148\u0146\3\2\2\2\u0148\u0149\3\2\2\2\u0149\u014d")
        buf.write("\3\2\2\2\u014a\u014c\t\3\2\2\u014b\u014a\3\2\2\2\u014c")
        buf.write("\u014f\3\2\2\2\u014d\u014b\3\2\2\2\u014d\u014e\3\2\2\2")
        buf.write("\u014e.\3\2\2\2\u014f\u014d\3\2\2\2\u0150\u0151\7D\2\2")
        buf.write("\u0151\u0152\7q\2\2\u0152\u0153\7f\2\2\u0153\u0154\7{")
        buf.write("\2\2\u0154\60\3\2\2\2\u0155\u0156\7G\2\2\u0156\u0157\7")
        buf.write("n\2\2\u0157\u0158\7u\2\2\u0158\u0159\7g\2\2\u0159\62\3")
        buf.write("\2\2\2\u015a\u015b\7G\2\2\u015b\u015c\7p\2\2\u015c\u015d")
        buf.write("\7f\2\2\u015d\u015e\7H\2\2\u015e\u015f\7q\2\2\u015f\u0160")
        buf.write("\7t\2\2\u0160\64\3\2\2\2\u0161\u0162\7K\2\2\u0162\u0163")
        buf.write("\7h\2\2\u0163\66\3\2\2\2\u0164\u0165\7X\2\2\u0165\u0166")
        buf.write("\7c\2\2\u0166\u0167\7t\2\2\u01678\3\2\2\2\u0168\u0169")
        buf.write("\7G\2\2\u0169\u016a\7p\2\2\u016a\u016b\7f\2\2\u016b\u016c")
        buf.write("\7F\2\2\u016c\u016d\7q\2\2\u016d:\3\2\2\2\u016e\u016f")
        buf.write("\7D\2\2\u016f\u0170\7t\2\2\u0170\u0171\7g\2\2\u0171\u0172")
        buf.write("\7c\2\2\u0172\u0173\7m\2\2\u0173<\3\2\2\2\u0174\u0175")
        buf.write("\7G\2\2\u0175\u0176\7n\2\2\u0176\u0177\7u\2\2\u0177\u0178")
        buf.write("\7g\2\2\u0178\u0179\7K\2\2\u0179\u017a\7h\2\2\u017a>\3")
        buf.write("\2\2\2\u017b\u017c\7G\2\2\u017c\u017d\7p\2\2\u017d\u017e")
        buf.write("\7f\2\2\u017e\u017f\7Y\2\2\u017f\u0180\7j\2\2\u0180\u0181")
        buf.write("\7k\2\2\u0181\u0182\7n\2\2\u0182\u0183\7g\2\2\u0183@\3")
        buf.write("\2\2\2\u0184\u0185\7R\2\2\u0185\u0186\7c\2\2\u0186\u0187")
        buf.write("\7t\2\2\u0187\u0188\7c\2\2\u0188\u0189\7o\2\2\u0189\u018a")
        buf.write("\7g\2\2\u018a\u018b\7v\2\2\u018b\u018c\7g\2\2\u018c\u018d")
        buf.write("\7t\2\2\u018dB\3\2\2\2\u018e\u018f\7Y\2\2\u018f\u0190")
        buf.write("\7j\2\2\u0190\u0191\7k\2\2\u0191\u0192\7n\2\2\u0192\u0193")
        buf.write("\7g\2\2\u0193D\3\2\2\2\u0194\u0195\7E\2\2\u0195\u0196")
        buf.write("\7q\2\2\u0196\u0197\7p\2\2\u0197\u0198\7v\2\2\u0198\u0199")
        buf.write("\7k\2\2\u0199\u019a\7p\2\2\u019a\u019b\7w\2\2\u019b\u019c")
        buf.write("\7g\2\2\u019cF\3\2\2\2\u019d\u019e\7G\2\2\u019e\u019f")
        buf.write("\7p\2\2\u019f\u01a0\7f\2\2\u01a0\u01a1\7D\2\2\u01a1\u01a2")
        buf.write("\7q\2\2\u01a2\u01a3\7f\2\2\u01a3\u01a4\7{\2\2\u01a4H\3")
        buf.write("\2\2\2\u01a5\u01a6\7H\2\2\u01a6\u01a7\7q\2\2\u01a7\u01a8")
        buf.write("\7t\2\2\u01a8J\3\2\2\2\u01a9\u01aa\7T\2\2\u01aa\u01ab")
        buf.write("\7g\2\2\u01ab\u01ac\7v\2\2\u01ac\u01ad\7w\2\2\u01ad\u01ae")
        buf.write("\7t\2\2\u01ae\u01af\7p\2\2\u01afL\3\2\2\2\u01b0\u01b1")
        buf.write("\7V\2\2\u01b1\u01b2\7t\2\2\u01b2\u01b3\7w\2\2\u01b3\u01b4")
        buf.write("\7g\2\2\u01b4N\3\2\2\2\u01b5\u01b6\7F\2\2\u01b6\u01b7")
        buf.write("\7q\2\2\u01b7P\3\2\2\2\u01b8\u01b9\7G\2\2\u01b9\u01ba")
        buf.write("\7p\2\2\u01ba\u01bb\7f\2\2\u01bb\u01bc\7K\2\2\u01bc\u01bd")
        buf.write("\7h\2\2\u01bdR\3\2\2\2\u01be\u01bf\7H\2\2\u01bf\u01c0")
        buf.write("\7w\2\2\u01c0\u01c1\7p\2\2\u01c1\u01c2\7e\2\2\u01c2\u01c3")
        buf.write("\7v\2\2\u01c3\u01c4\7k\2\2\u01c4\u01c5\7q\2\2\u01c5\u01c6")
        buf.write("\7p\2\2\u01c6T\3\2\2\2\u01c7\u01c8\7V\2\2\u01c8\u01c9")
        buf.write("\7j\2\2\u01c9\u01ca\7g\2\2\u01ca\u01cb\7p\2\2\u01cbV\3")
        buf.write("\2\2\2\u01cc\u01cd\7H\2\2\u01cd\u01ce\7c\2\2\u01ce\u01cf")
        buf.write("\7n\2\2\u01cf\u01d0\7u\2\2\u01d0\u01d1\7g\2\2\u01d1X\3")
        buf.write("\2\2\2\u01d2\u01d3\7-\2\2\u01d3Z\3\2\2\2\u01d4\u01d5\7")
        buf.write("-\2\2\u01d5\u01d6\7\60\2\2\u01d6\\\3\2\2\2\u01d7\u01d8")
        buf.write("\7/\2\2\u01d8^\3\2\2\2\u01d9\u01da\7/\2\2\u01da\u01db")
        buf.write("\7\60\2\2\u01db`\3\2\2\2\u01dc\u01dd\7,\2\2\u01ddb\3\2")
        buf.write("\2\2\u01de\u01df\7,\2\2\u01df\u01e0\7\60\2\2\u01e0d\3")
        buf.write("\2\2\2\u01e1\u01e2\7^\2\2\u01e2f\3\2\2\2\u01e3\u01e4\7")
        buf.write("^\2\2\u01e4\u01e5\7\60\2\2\u01e5h\3\2\2\2\u01e6\u01e7")
        buf.write("\7\'\2\2\u01e7j\3\2\2\2\u01e8\u01e9\7#\2\2\u01e9l\3\2")
        buf.write("\2\2\u01ea\u01eb\7(\2\2\u01eb\u01ec\7(\2\2\u01ecn\3\2")
        buf.write("\2\2\u01ed\u01ee\7~\2\2\u01ee\u01ef\7~\2\2\u01efp\3\2")
        buf.write("\2\2\u01f0\u01f1\7?\2\2\u01f1\u01f2\7?\2\2\u01f2r\3\2")
        buf.write("\2\2\u01f3\u01f4\7#\2\2\u01f4\u01f5\7?\2\2\u01f5t\3\2")
        buf.write("\2\2\u01f6\u01f7\7@\2\2\u01f7v\3\2\2\2\u01f8\u01f9\7>")
        buf.write("\2\2\u01f9x\3\2\2\2\u01fa\u01fb\7>\2\2\u01fb\u01fc\7?")
        buf.write("\2\2\u01fcz\3\2\2\2\u01fd\u01fe\7@\2\2\u01fe\u01ff\7?")
        buf.write("\2\2\u01ff|\3\2\2\2\u0200\u0201\7?\2\2\u0201\u0202\7\61")
        buf.write("\2\2\u0202\u0203\7?\2\2\u0203~\3\2\2\2\u0204\u0205\7@")
        buf.write("\2\2\u0205\u0206\7\60\2\2\u0206\u0080\3\2\2\2\u0207\u0208")
        buf.write("\7>\2\2\u0208\u0209\7\60\2\2\u0209\u0082\3\2\2\2\u020a")
        buf.write("\u020b\7>\2\2\u020b\u020c\7?\2\2\u020c\u020d\7\60\2\2")
        buf.write("\u020d\u0084\3\2\2\2\u020e\u020f\7@\2\2\u020f\u0210\7")
        buf.write("?\2\2\u0210\u0211\7\60\2\2\u0211\u0086\3\2\2\2\u0212\u0237")
        buf.write("\7\62\2\2\u0213\u0215\t\4\2\2\u0214\u0213\3\2\2\2\u0215")
        buf.write("\u0216\3\2\2\2\u0216\u0214\3\2\2\2\u0216\u0217\3\2\2\2")
        buf.write("\u0217\u021b\3\2\2\2\u0218\u021a\t\5\2\2\u0219\u0218\3")
        buf.write("\2\2\2\u021a\u021d\3\2\2\2\u021b\u0219\3\2\2\2\u021b\u021c")
        buf.write("\3\2\2\2\u021c\u0237\3\2\2\2\u021d\u021b\3\2\2\2\u021e")
        buf.write("\u021f\7\62\2\2\u021f\u0223\7z\2\2\u0220\u0221\7\62\2")
        buf.write("\2\u0221\u0223\7Z\2\2\u0222\u021e\3\2\2\2\u0222\u0220")
        buf.write("\3\2\2\2\u0223\u0227\3\2\2\2\u0224\u0226\t\6\2\2\u0225")
        buf.write("\u0224\3\2\2\2\u0226\u0229\3\2\2\2\u0227\u0225\3\2\2\2")
        buf.write("\u0227\u0228\3\2\2\2\u0228\u0237\3\2\2\2\u0229\u0227\3")
        buf.write("\2\2\2\u022a\u022b\7\62\2\2\u022b\u022f\7q\2\2\u022c\u022d")
        buf.write("\7\62\2\2\u022d\u022f\7Q\2\2\u022e\u022a\3\2\2\2\u022e")
        buf.write("\u022c\3\2\2\2\u022f\u0233\3\2\2\2\u0230\u0232\t\7\2\2")
        buf.write("\u0231\u0230\3\2\2\2\u0232\u0235\3\2\2\2\u0233\u0231\3")
        buf.write("\2\2\2\u0233\u0234\3\2\2\2\u0234\u0237\3\2\2\2\u0235\u0233")
        buf.write("\3\2\2\2\u0236\u0212\3\2\2\2\u0236\u0214\3\2\2\2\u0236")
        buf.write("\u0222\3\2\2\2\u0236\u022e\3\2\2\2\u0237\u0088\3\2\2\2")
        buf.write("\u0238\u023a\t\5\2\2\u0239\u0238\3\2\2\2\u023a\u023b\3")
        buf.write("\2\2\2\u023b\u0239\3\2\2\2\u023b\u023c\3\2\2\2\u023c\u023d")
        buf.write("\3\2\2\2\u023d\u025a\7\60\2\2\u023e\u0240\t\5\2\2\u023f")
        buf.write("\u023e\3\2\2\2\u0240\u0241\3\2\2\2\u0241\u023f\3\2\2\2")
        buf.write("\u0241\u0242\3\2\2\2\u0242\u0243\3\2\2\2\u0243\u0245\t")
        buf.write("\b\2\2\u0244\u0246\t\t\2\2\u0245\u0244\3\2\2\2\u0245\u0246")
        buf.write("\3\2\2\2\u0246\u0248\3\2\2\2\u0247\u0249\t\5\2\2\u0248")
        buf.write("\u0247\3\2\2\2\u0249\u024a\3\2\2\2\u024a\u0248\3\2\2\2")
        buf.write("\u024a\u024b\3\2\2\2\u024b\u025b\3\2\2\2\u024c\u024e\t")
        buf.write("\5\2\2\u024d\u024c\3\2\2\2\u024e\u024f\3\2\2\2\u024f\u024d")
        buf.write("\3\2\2\2\u024f\u0250\3\2\2\2\u0250\u025b\3\2\2\2\u0251")
        buf.write("\u0253\t\b\2\2\u0252\u0254\t\t\2\2\u0253\u0252\3\2\2\2")
        buf.write("\u0253\u0254\3\2\2\2\u0254\u0256\3\2\2\2\u0255\u0257\t")
        buf.write("\5\2\2\u0256\u0255\3\2\2\2\u0257\u0258\3\2\2\2\u0258\u0256")
        buf.write("\3\2\2\2\u0258\u0259\3\2\2\2\u0259\u025b\3\2\2\2\u025a")
        buf.write("\u023f\3\2\2\2\u025a\u024d\3\2\2\2\u025a\u0251\3\2\2\2")
        buf.write("\u025b\u008a\3\2\2\2\u025c\u0261\n\n\2\2\u025d\u0261\5")
        buf.write("\u008dG\2\u025e\u025f\7)\2\2\u025f\u0261\7$\2\2\u0260")
        buf.write("\u025c\3\2\2\2\u0260\u025d\3\2\2\2\u0260\u025e\3\2\2\2")
        buf.write("\u0261\u008c\3\2\2\2\u0262\u0263\7^\2\2\u0263\u0264\t")
        buf.write("\13\2\2\u0264\u008e\3\2\2\2\u0265\u0269\7$\2\2\u0266\u0268")
        buf.write("\5\u008bF\2\u0267\u0266\3\2\2\2\u0268\u026b\3\2\2\2\u0269")
        buf.write("\u0267\3\2\2\2\u0269\u026a\3\2\2\2\u026a\u026c\3\2\2\2")
        buf.write("\u026b\u0269\3\2\2\2\u026c\u026d\7$\2\2\u026d\u026e\b")
        buf.write("H\2\2\u026e\u0090\3\2\2\2\u026f\u0279\7}\2\2\u0270\u027a")
        buf.write("\3\2\2\2\u0271\u0276\5\u0087D\2\u0272\u0273\7.\2\2\u0273")
        buf.write("\u0275\5\u0087D\2\u0274\u0272\3\2\2\2\u0275\u0278\3\2")
        buf.write("\2\2\u0276\u0274\3\2\2\2\u0276\u0277\3\2\2\2\u0277\u027a")
        buf.write("\3\2\2\2\u0278\u0276\3\2\2\2\u0279\u0270\3\2\2\2\u0279")
        buf.write("\u0271\3\2\2\2\u027a\u027b\3\2\2\2\u027b\u02b7\7\177\2")
        buf.write("\2\u027c\u0286\7}\2\2\u027d\u0287\3\2\2\2\u027e\u0283")
        buf.write("\5\u0089E\2\u027f\u0280\7.\2\2\u0280\u0282\5\u0089E\2")
        buf.write("\u0281\u027f\3\2\2\2\u0282\u0285\3\2\2\2\u0283\u0281\3")
        buf.write("\2\2\2\u0283\u0284\3\2\2\2\u0284\u0287\3\2\2\2\u0285\u0283")
        buf.write("\3\2\2\2\u0286\u027d\3\2\2\2\u0286\u027e\3\2\2\2\u0287")
        buf.write("\u0288\3\2\2\2\u0288\u02b7\7\177\2\2\u0289\u0299\7}\2")
        buf.write("\2\u028a\u029a\3\2\2\2\u028b\u028e\5M\'\2\u028c\u028e")
        buf.write("\5W,\2\u028d\u028b\3\2\2\2\u028d\u028c\3\2\2\2\u028e\u0296")
        buf.write("\3\2\2\2\u028f\u0292\7.\2\2\u0290\u0293\5M\'\2\u0291\u0293")
        buf.write("\5W,\2\u0292\u0290\3\2\2\2\u0292\u0291\3\2\2\2\u0293\u0295")
        buf.write("\3\2\2\2\u0294\u028f\3\2\2\2\u0295\u0298\3\2\2\2\u0296")
        buf.write("\u0294\3\2\2\2\u0296\u0297\3\2\2\2\u0297\u029a\3\2\2\2")
        buf.write("\u0298\u0296\3\2\2\2\u0299\u028a\3\2\2\2\u0299\u028d\3")
        buf.write("\2\2\2\u029a\u029b\3\2\2\2\u029b\u02b7\7\177\2\2\u029c")
        buf.write("\u02a6\7}\2\2\u029d\u02a7\3\2\2\2\u029e\u02a3\5\u008f")
        buf.write("H\2\u029f\u02a0\7.\2\2\u02a0\u02a2\5\u008fH\2\u02a1\u029f")
        buf.write("\3\2\2\2\u02a2\u02a5\3\2\2\2\u02a3\u02a1\3\2\2\2\u02a3")
        buf.write("\u02a4\3\2\2\2\u02a4\u02a7\3\2\2\2\u02a5\u02a3\3\2\2\2")
        buf.write("\u02a6\u029d\3\2\2\2\u02a6\u029e\3\2\2\2\u02a7\u02a8\3")
        buf.write("\2\2\2\u02a8\u02b7\7\177\2\2\u02a9\u02b3\7}\2\2\u02aa")
        buf.write("\u02b4\3\2\2\2\u02ab\u02b0\5\u0091I\2\u02ac\u02ad\7.\2")
        buf.write("\2\u02ad\u02af\5\u0091I\2\u02ae\u02ac\3\2\2\2\u02af\u02b2")
        buf.write("\3\2\2\2\u02b0\u02ae\3\2\2\2\u02b0\u02b1\3\2\2\2\u02b1")
        buf.write("\u02b4\3\2\2\2\u02b2\u02b0\3\2\2\2\u02b3\u02aa\3\2\2\2")
        buf.write("\u02b3\u02ab\3\2\2\2\u02b4\u02b5\3\2\2\2\u02b5\u02b7\7")
        buf.write("\177\2\2\u02b6\u026f\3\2\2\2\u02b6\u027c\3\2\2\2\u02b6")
        buf.write("\u0289\3\2\2\2\u02b6\u029c\3\2\2\2\u02b6\u02a9\3\2\2\2")
        buf.write("\u02b7\u0092\3\2\2\2\u02b8\u02ba\t\f\2\2\u02b9\u02b8\3")
        buf.write("\2\2\2\u02ba\u02bb\3\2\2\2\u02bb\u02b9\3\2\2\2\u02bb\u02bc")
        buf.write("\3\2\2\2\u02bc\u02bd\3\2\2\2\u02bd\u02be\bJ\3\2\u02be")
        buf.write("\u0094\3\2\2\2\u02bf\u02c0\7,\2\2\u02c0\u02c1\7,\2\2\u02c1")
        buf.write("\u02c5\3\2\2\2\u02c2\u02c4\13\2\2\2\u02c3\u02c2\3\2\2")
        buf.write("\2\u02c4\u02c7\3\2\2\2\u02c5\u02c6\3\2\2\2\u02c5\u02c3")
        buf.write("\3\2\2\2\u02c6\u02c8\3\2\2\2\u02c7\u02c5\3\2\2\2\u02c8")
        buf.write("\u02c9\7,\2\2\u02c9\u02ca\7,\2\2\u02ca\u02cb\3\2\2\2\u02cb")
        buf.write("\u02cc\bK\3\2\u02cc\u0096\3\2\2\2\u02cd\u02ce\13\2\2\2")
        buf.write("\u02ce\u02cf\bL\4\2\u02cf\u0098\3\2\2\2\u02d0\u02d4\7")
        buf.write("$\2\2\u02d1\u02d3\5\u008bF\2\u02d2\u02d1\3\2\2\2\u02d3")
        buf.write("\u02d6\3\2\2\2\u02d4\u02d2\3\2\2\2\u02d4\u02d5\3\2\2\2")
        buf.write("\u02d5\u02d8\3\2\2\2\u02d6\u02d4\3\2\2\2\u02d7\u02d9\t")
        buf.write("\r\2\2\u02d8\u02d7\3\2\2\2\u02d9\u02da\3\2\2\2\u02da\u02db")
        buf.write("\bM\5\2\u02db\u009a\3\2\2\2\u02dc\u02dd\7^\2\2\u02dd\u02de")
        buf.write("\n\13\2\2\u02de\u009c\3\2\2\2\u02df\u02e3\7$\2\2\u02e0")
        buf.write("\u02e2\5\u008bF\2\u02e1\u02e0\3\2\2\2\u02e2\u02e5\3\2")
        buf.write("\2\2\u02e3\u02e1\3\2\2\2\u02e3\u02e4\3\2\2\2\u02e4\u02e6")
        buf.write("\3\2\2\2\u02e5\u02e3\3\2\2\2\u02e6\u02e7\5\u009bN\2\u02e7")
        buf.write("\u02e8\bO\6\2\u02e8\u009e\3\2\2\2\u02e9\u02ea\7,\2\2\u02ea")
        buf.write("\u02eb\7,\2\2\u02eb\u02ef\3\2\2\2\u02ec\u02ee\n\16\2\2")
        buf.write("\u02ed\u02ec\3\2\2\2\u02ee\u02f1\3\2\2\2\u02ef\u02ed\3")
        buf.write("\2\2\2\u02ef\u02f0\3\2\2\2\u02f0\u02fe\3\2\2\2\u02f1\u02ef")
        buf.write("\3\2\2\2\u02f2\u02ff\7,\2\2\u02f3\u02f5\7,\2\2\u02f4\u02f6")
        buf.write("\n\16\2\2\u02f5\u02f4\3\2\2\2\u02f6\u02f7\3\2\2\2\u02f7")
        buf.write("\u02f5\3\2\2\2\u02f7\u02f8\3\2\2\2\u02f8\u02fa\3\2\2\2")
        buf.write("\u02f9\u02f3\3\2\2\2\u02fa\u02fd\3\2\2\2\u02fb\u02f9\3")
        buf.write("\2\2\2\u02fb\u02fc\3\2\2\2\u02fc\u02ff\3\2\2\2\u02fd\u02fb")
        buf.write("\3\2\2\2\u02fe\u02f2\3\2\2\2\u02fe\u02fb\3\2\2\2\u02ff")
        buf.write("\u0300\3\2\2\2\u0300\u0301\7\2\2\3\u0301\u0302\bP\7\2")
        buf.write("\u0302\u00a0\3\2\2\2,\2\u0148\u014d\u0216\u021b\u0222")
        buf.write("\u0227\u022e\u0233\u0236\u023b\u0241\u0245\u024a\u024f")
        buf.write("\u0253\u0258\u025a\u0260\u0269\u0276\u0279\u0283\u0286")
        buf.write("\u028d\u0292\u0296\u0299\u02a3\u02a6\u02b0\u02b3\u02b6")
        buf.write("\u02bb\u02c5\u02d4\u02d8\u02e3\u02ef\u02f7\u02fb\u02fe")
        buf.write("\b\3H\2\b\2\2\3L\3\3M\4\3O\5\3P\6")
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
    INTEGER = 67
    FLOAT = 68
    STRING = 69
    ARRAY = 70
    WS = 71
    BLOCK_COMMENT = 72
    ERROR_CHAR = 73
    UNCLOSE_STRING = 74
    ILLEGAL_ESCAPE = 75
    UNTERMINATED_COMMENT = 76

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "'['", "']'", "'int_of_float'", "'float_of_int'", "'int_of_string'", 
            "'string_of_int'", "'float_of_string'", "'string_of_float'", 
            "'bool_of_string'", "'string_of_bool'", "'printLn'", "'print'", 
            "'printStrLn'", "'read'", "';'", "','", "':'", "'.'", "'('", 
            "')'", "'Body'", "'Else'", "'EndFor'", "'If'", "'Var'", "'EndDo'", 
            "'Break'", "'ElseIf'", "'EndWhile'", "'Parameter'", "'While'", 
            "'Continue'", "'EndBody'", "'For'", "'Return'", "'True'", "'Do'", 
            "'EndIf'", "'Function'", "'Then'", "'False'", "'+'", "'+.'", 
            "'-'", "'-.'", "'*'", "'*.'", "'\\'", "'\\.'", "'%'", "'!'", 
            "'&&'", "'||'", "'=='", "'!='", "'>'", "'<'", "'<='", "'>='", 
            "'=/='", "'>.'", "'<.'", "'<=.'", "'>=.'" ]

    symbolicNames = [ "<INVALID>",
            "SEMI", "COMMA", "COLON", "DOT", "LP", "RP", "ID", "BODY", "ELSE", 
            "ENDFOR", "IF", "VAR", "ENDDO", "BREAK", "ELSEIF", "ENDWHILE", 
            "PARAMETER", "WHILE", "CONTINUE", "ENDBODY", "FOR", "RETURN", 
            "TRUE", "DO", "ENDIF", "FUNCTION", "THEN", "FALSE", "ADD", "ADDDOT", 
            "SUB", "SUBDOT", "MUL", "MULDOT", "DIV", "DIVDOT", "MOD", "NEG", 
            "AND", "OR", "EQ", "NEI", "GT", "LT", "LTE", "GTE", "NEF", "GTDOT", 
            "LTDOT", "LTEDOT", "GTEDOT", "INTEGER", "FLOAT", "STRING", "ARRAY", 
            "WS", "BLOCK_COMMENT", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "UNTERMINATED_COMMENT" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "SEMI", "COMMA", "COLON", "DOT", "LP", "RP", 
                  "ID", "BODY", "ELSE", "ENDFOR", "IF", "VAR", "ENDDO", 
                  "BREAK", "ELSEIF", "ENDWHILE", "PARAMETER", "WHILE", "CONTINUE", 
                  "ENDBODY", "FOR", "RETURN", "TRUE", "DO", "ENDIF", "FUNCTION", 
                  "THEN", "FALSE", "ADD", "ADDDOT", "SUB", "SUBDOT", "MUL", 
                  "MULDOT", "DIV", "DIVDOT", "MOD", "NEG", "AND", "OR", 
                  "EQ", "NEI", "GT", "LT", "LTE", "GTE", "NEF", "GTDOT", 
                  "LTDOT", "LTEDOT", "GTEDOT", "INTEGER", "FLOAT", "STR_CHAR", 
                  "ESC_SEQ", "STRING", "ARRAY", "WS", "BLOCK_COMMENT", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ESC_ILLEGAL", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

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
            actions[70] = self.STRING_action 
            actions[74] = self.ERROR_CHAR_action 
            actions[75] = self.UNCLOSE_STRING_action 
            actions[77] = self.ILLEGAL_ESCAPE_action 
            actions[78] = self.UNTERMINATED_COMMENT_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                    y = str(self.text)
                    self.text = y[1:-1]
                
     

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
                
     


