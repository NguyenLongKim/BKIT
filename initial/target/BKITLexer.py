# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2P")
        buf.write("\u030a\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\3\2\3\2\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\17")
        buf.write("\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24")
        buf.write("\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\7\31")
        buf.write("\u0150\n\31\f\31\16\31\u0153\13\31\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\3!")
        buf.write("\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3")
        buf.write("#\3#\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3")
        buf.write("%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3(")
        buf.write("\3(\3(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3*\3*\3*\3+\3+\3+\3")
        buf.write("+\3+\3+\3,\3,\3,\3,\3,\3,\3,\3,\3,\3-\3-\3-\3-\3-\3.\3")
        buf.write(".\3.\3.\3.\3.\3/\3/\3\60\3\60\3\60\3\61\3\61\3\62\3\62")
        buf.write("\3\62\3\63\3\63\3\64\3\64\3\64\3\65\3\65\3\66\3\66\3\66")
        buf.write("\3\67\3\67\38\38\39\39\39\3:\3:\3:\3;\3;\3;\3<\3<\3<\3")
        buf.write("=\3=\3>\3>\3?\3?\3?\3@\3@\3@\3A\3A\3A\3A\3B\3B\3B\3C\3")
        buf.write("C\3C\3D\3D\3D\3D\3E\3E\3E\3E\3F\3F\6F\u0219\nF\rF\16F")
        buf.write("\u021a\3F\7F\u021e\nF\fF\16F\u0221\13F\3F\3F\3F\3F\5F")
        buf.write("\u0227\nF\3F\7F\u022a\nF\fF\16F\u022d\13F\3F\3F\3F\3F")
        buf.write("\5F\u0233\nF\3F\7F\u0236\nF\fF\16F\u0239\13F\5F\u023b")
        buf.write("\nF\3G\6G\u023e\nG\rG\16G\u023f\3G\3G\6G\u0244\nG\rG\16")
        buf.write("G\u0245\3G\3G\5G\u024a\nG\3G\6G\u024d\nG\rG\16G\u024e")
        buf.write("\3G\6G\u0252\nG\rG\16G\u0253\3G\3G\5G\u0258\nG\3G\6G\u025b")
        buf.write("\nG\rG\16G\u025c\7G\u025f\nG\fG\16G\u0262\13G\3H\3H\3")
        buf.write("H\3H\5H\u0268\nH\3I\3I\3I\3J\3J\7J\u026f\nJ\fJ\16J\u0272")
        buf.write("\13J\3J\3J\3J\3K\3K\3K\3K\3K\7K\u027c\nK\fK\16K\u027f")
        buf.write("\13K\5K\u0281\nK\3K\3K\3K\3K\3K\3K\7K\u0289\nK\fK\16K")
        buf.write("\u028c\13K\5K\u028e\nK\3K\3K\3K\3K\3K\5K\u0295\nK\3K\3")
        buf.write("K\3K\5K\u029a\nK\7K\u029c\nK\fK\16K\u029f\13K\5K\u02a1")
        buf.write("\nK\3K\3K\3K\3K\3K\3K\7K\u02a9\nK\fK\16K\u02ac\13K\5K")
        buf.write("\u02ae\nK\3K\3K\3K\3K\3K\3K\7K\u02b6\nK\fK\16K\u02b9\13")
        buf.write("K\5K\u02bb\nK\3K\5K\u02be\nK\3L\6L\u02c1\nL\rL\16L\u02c2")
        buf.write("\3L\3L\3M\3M\3M\3M\7M\u02cb\nM\fM\16M\u02ce\13M\3M\3M")
        buf.write("\3M\3M\3M\3N\3N\3N\3O\3O\7O\u02da\nO\fO\16O\u02dd\13O")
        buf.write("\3O\5O\u02e0\nO\3O\3O\3P\3P\3P\3Q\3Q\7Q\u02e9\nQ\fQ\16")
        buf.write("Q\u02ec\13Q\3Q\3Q\3Q\3R\3R\3R\3R\7R\u02f5\nR\fR\16R\u02f8")
        buf.write("\13R\3R\3R\3R\6R\u02fd\nR\rR\16R\u02fe\7R\u0301\nR\fR")
        buf.write("\16R\u0304\13R\5R\u0306\nR\3R\3R\3R\3\u02cc\2S\3\3\5\4")
        buf.write("\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63")
        buf.write("\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-")
        buf.write("Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q:s;u<w=y>{?}")
        buf.write("@\177A\u0081B\u0083C\u0085D\u0087E\u0089F\u008bG\u008d")
        buf.write("H\u008f\2\u0091\2\u0093I\u0095J\u0097K\u0099L\u009bM\u009d")
        buf.write("N\u009f\2\u00a1O\u00a3P\3\2\17\3\2c|\7\2))\62;C\\aac|")
        buf.write("\3\2\63;\3\2\62;\4\2\62;CH\3\2\629\4\2GGgg\4\2--//\7\2")
        buf.write("\n\f\16\17$$))^^\t\2))^^ddhhppttvv\5\2\13\f\16\17\"\"")
        buf.write("\7\3\n\f\16\17$$))^^\3\2,,\2\u0335\2\3\3\2\2\2\2\5\3\2")
        buf.write("\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2")
        buf.write("\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2")
        buf.write("\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37")
        buf.write("\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2")
        buf.write("\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2")
        buf.write("\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2")
        buf.write("\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2")
        buf.write("\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2")
        buf.write("\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3")
        buf.write("\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a")
        buf.write("\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2")
        buf.write("k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2")
        buf.write("\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2")
        buf.write("\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085")
        buf.write("\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2")
        buf.write("\2\2\u008d\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097")
        buf.write("\3\2\2\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d\3\2\2")
        buf.write("\2\2\u00a1\3\2\2\2\2\u00a3\3\2\2\2\3\u00a5\3\2\2\2\5\u00a7")
        buf.write("\3\2\2\2\7\u00b4\3\2\2\2\t\u00c2\3\2\2\2\13\u00cf\3\2")
        buf.write("\2\2\r\u00df\3\2\2\2\17\u00ed\3\2\2\2\21\u00fd\3\2\2\2")
        buf.write("\23\u010c\3\2\2\2\25\u011b\3\2\2\2\27\u0123\3\2\2\2\31")
        buf.write("\u0129\3\2\2\2\33\u0134\3\2\2\2\35\u0139\3\2\2\2\37\u013b")
        buf.write("\3\2\2\2!\u013d\3\2\2\2#\u013f\3\2\2\2%\u0141\3\2\2\2")
        buf.write("\'\u0143\3\2\2\2)\u0145\3\2\2\2+\u0147\3\2\2\2-\u0149")
        buf.write("\3\2\2\2/\u014b\3\2\2\2\61\u014d\3\2\2\2\63\u0154\3\2")
        buf.write("\2\2\65\u0159\3\2\2\2\67\u015e\3\2\2\29\u0165\3\2\2\2")
        buf.write(";\u0168\3\2\2\2=\u016c\3\2\2\2?\u0172\3\2\2\2A\u0178\3")
        buf.write("\2\2\2C\u017f\3\2\2\2E\u0188\3\2\2\2G\u0192\3\2\2\2I\u0198")
        buf.write("\3\2\2\2K\u01a1\3\2\2\2M\u01a9\3\2\2\2O\u01ad\3\2\2\2")
        buf.write("Q\u01b4\3\2\2\2S\u01b9\3\2\2\2U\u01bc\3\2\2\2W\u01c2\3")
        buf.write("\2\2\2Y\u01cb\3\2\2\2[\u01d0\3\2\2\2]\u01d6\3\2\2\2_\u01d8")
        buf.write("\3\2\2\2a\u01db\3\2\2\2c\u01dd\3\2\2\2e\u01e0\3\2\2\2")
        buf.write("g\u01e2\3\2\2\2i\u01e5\3\2\2\2k\u01e7\3\2\2\2m\u01ea\3")
        buf.write("\2\2\2o\u01ec\3\2\2\2q\u01ee\3\2\2\2s\u01f1\3\2\2\2u\u01f4")
        buf.write("\3\2\2\2w\u01f7\3\2\2\2y\u01fa\3\2\2\2{\u01fc\3\2\2\2")
        buf.write("}\u01fe\3\2\2\2\177\u0201\3\2\2\2\u0081\u0204\3\2\2\2")
        buf.write("\u0083\u0208\3\2\2\2\u0085\u020b\3\2\2\2\u0087\u020e\3")
        buf.write("\2\2\2\u0089\u0212\3\2\2\2\u008b\u023a\3\2\2\2\u008d\u023d")
        buf.write("\3\2\2\2\u008f\u0267\3\2\2\2\u0091\u0269\3\2\2\2\u0093")
        buf.write("\u026c\3\2\2\2\u0095\u02bd\3\2\2\2\u0097\u02c0\3\2\2\2")
        buf.write("\u0099\u02c6\3\2\2\2\u009b\u02d4\3\2\2\2\u009d\u02d7\3")
        buf.write("\2\2\2\u009f\u02e3\3\2\2\2\u00a1\u02e6\3\2\2\2\u00a3\u02f0")
        buf.write("\3\2\2\2\u00a5\u00a6\7?\2\2\u00a6\4\3\2\2\2\u00a7\u00a8")
        buf.write("\7k\2\2\u00a8\u00a9\7p\2\2\u00a9\u00aa\7v\2\2\u00aa\u00ab")
        buf.write("\7a\2\2\u00ab\u00ac\7q\2\2\u00ac\u00ad\7h\2\2\u00ad\u00ae")
        buf.write("\7a\2\2\u00ae\u00af\7h\2\2\u00af\u00b0\7n\2\2\u00b0\u00b1")
        buf.write("\7q\2\2\u00b1\u00b2\7c\2\2\u00b2\u00b3\7v\2\2\u00b3\6")
        buf.write("\3\2\2\2\u00b4\u00b5\7k\2\2\u00b5\u00b6\7p\2\2\u00b6\u00b7")
        buf.write("\7v\2\2\u00b7\u00b8\7a\2\2\u00b8\u00b9\7q\2\2\u00b9\u00ba")
        buf.write("\7h\2\2\u00ba\u00bb\7a\2\2\u00bb\u00bc\7u\2\2\u00bc\u00bd")
        buf.write("\7v\2\2\u00bd\u00be\7t\2\2\u00be\u00bf\7k\2\2\u00bf\u00c0")
        buf.write("\7p\2\2\u00c0\u00c1\7i\2\2\u00c1\b\3\2\2\2\u00c2\u00c3")
        buf.write("\7h\2\2\u00c3\u00c4\7n\2\2\u00c4\u00c5\7q\2\2\u00c5\u00c6")
        buf.write("\7c\2\2\u00c6\u00c7\7v\2\2\u00c7\u00c8\7a\2\2\u00c8\u00c9")
        buf.write("\7q\2\2\u00c9\u00ca\7h\2\2\u00ca\u00cb\7a\2\2\u00cb\u00cc")
        buf.write("\7k\2\2\u00cc\u00cd\7p\2\2\u00cd\u00ce\7v\2\2\u00ce\n")
        buf.write("\3\2\2\2\u00cf\u00d0\7h\2\2\u00d0\u00d1\7n\2\2\u00d1\u00d2")
        buf.write("\7q\2\2\u00d2\u00d3\7c\2\2\u00d3\u00d4\7v\2\2\u00d4\u00d5")
        buf.write("\7a\2\2\u00d5\u00d6\7q\2\2\u00d6\u00d7\7h\2\2\u00d7\u00d8")
        buf.write("\7a\2\2\u00d8\u00d9\7u\2\2\u00d9\u00da\7v\2\2\u00da\u00db")
        buf.write("\7t\2\2\u00db\u00dc\7k\2\2\u00dc\u00dd\7p\2\2\u00dd\u00de")
        buf.write("\7i\2\2\u00de\f\3\2\2\2\u00df\u00e0\7u\2\2\u00e0\u00e1")
        buf.write("\7v\2\2\u00e1\u00e2\7t\2\2\u00e2\u00e3\7k\2\2\u00e3\u00e4")
        buf.write("\7p\2\2\u00e4\u00e5\7i\2\2\u00e5\u00e6\7a\2\2\u00e6\u00e7")
        buf.write("\7q\2\2\u00e7\u00e8\7h\2\2\u00e8\u00e9\7a\2\2\u00e9\u00ea")
        buf.write("\7k\2\2\u00ea\u00eb\7p\2\2\u00eb\u00ec\7v\2\2\u00ec\16")
        buf.write("\3\2\2\2\u00ed\u00ee\7u\2\2\u00ee\u00ef\7v\2\2\u00ef\u00f0")
        buf.write("\7t\2\2\u00f0\u00f1\7k\2\2\u00f1\u00f2\7p\2\2\u00f2\u00f3")
        buf.write("\7i\2\2\u00f3\u00f4\7a\2\2\u00f4\u00f5\7q\2\2\u00f5\u00f6")
        buf.write("\7h\2\2\u00f6\u00f7\7a\2\2\u00f7\u00f8\7h\2\2\u00f8\u00f9")
        buf.write("\7n\2\2\u00f9\u00fa\7q\2\2\u00fa\u00fb\7c\2\2\u00fb\u00fc")
        buf.write("\7v\2\2\u00fc\20\3\2\2\2\u00fd\u00fe\7u\2\2\u00fe\u00ff")
        buf.write("\7v\2\2\u00ff\u0100\7t\2\2\u0100\u0101\7k\2\2\u0101\u0102")
        buf.write("\7p\2\2\u0102\u0103\7i\2\2\u0103\u0104\7a\2\2\u0104\u0105")
        buf.write("\7q\2\2\u0105\u0106\7h\2\2\u0106\u0107\7a\2\2\u0107\u0108")
        buf.write("\7d\2\2\u0108\u0109\7q\2\2\u0109\u010a\7q\2\2\u010a\u010b")
        buf.write("\7n\2\2\u010b\22\3\2\2\2\u010c\u010d\7d\2\2\u010d\u010e")
        buf.write("\7q\2\2\u010e\u010f\7q\2\2\u010f\u0110\7n\2\2\u0110\u0111")
        buf.write("\7a\2\2\u0111\u0112\7q\2\2\u0112\u0113\7h\2\2\u0113\u0114")
        buf.write("\7a\2\2\u0114\u0115\7u\2\2\u0115\u0116\7v\2\2\u0116\u0117")
        buf.write("\7t\2\2\u0117\u0118\7k\2\2\u0118\u0119\7p\2\2\u0119\u011a")
        buf.write("\7i\2\2\u011a\24\3\2\2\2\u011b\u011c\7r\2\2\u011c\u011d")
        buf.write("\7t\2\2\u011d\u011e\7k\2\2\u011e\u011f\7p\2\2\u011f\u0120")
        buf.write("\7v\2\2\u0120\u0121\7N\2\2\u0121\u0122\7p\2\2\u0122\26")
        buf.write("\3\2\2\2\u0123\u0124\7r\2\2\u0124\u0125\7t\2\2\u0125\u0126")
        buf.write("\7k\2\2\u0126\u0127\7p\2\2\u0127\u0128\7v\2\2\u0128\30")
        buf.write("\3\2\2\2\u0129\u012a\7r\2\2\u012a\u012b\7t\2\2\u012b\u012c")
        buf.write("\7k\2\2\u012c\u012d\7p\2\2\u012d\u012e\7v\2\2\u012e\u012f")
        buf.write("\7U\2\2\u012f\u0130\7v\2\2\u0130\u0131\7t\2\2\u0131\u0132")
        buf.write("\7N\2\2\u0132\u0133\7p\2\2\u0133\32\3\2\2\2\u0134\u0135")
        buf.write("\7t\2\2\u0135\u0136\7g\2\2\u0136\u0137\7c\2\2\u0137\u0138")
        buf.write("\7f\2\2\u0138\34\3\2\2\2\u0139\u013a\7=\2\2\u013a\36\3")
        buf.write("\2\2\2\u013b\u013c\7.\2\2\u013c \3\2\2\2\u013d\u013e\7")
        buf.write("<\2\2\u013e\"\3\2\2\2\u013f\u0140\7\60\2\2\u0140$\3\2")
        buf.write("\2\2\u0141\u0142\7*\2\2\u0142&\3\2\2\2\u0143\u0144\7+")
        buf.write("\2\2\u0144(\3\2\2\2\u0145\u0146\7}\2\2\u0146*\3\2\2\2")
        buf.write("\u0147\u0148\7\177\2\2\u0148,\3\2\2\2\u0149\u014a\7]\2")
        buf.write("\2\u014a.\3\2\2\2\u014b\u014c\7_\2\2\u014c\60\3\2\2\2")
        buf.write("\u014d\u0151\t\2\2\2\u014e\u0150\t\3\2\2\u014f\u014e\3")
        buf.write("\2\2\2\u0150\u0153\3\2\2\2\u0151\u014f\3\2\2\2\u0151\u0152")
        buf.write("\3\2\2\2\u0152\62\3\2\2\2\u0153\u0151\3\2\2\2\u0154\u0155")
        buf.write("\7D\2\2\u0155\u0156\7q\2\2\u0156\u0157\7f\2\2\u0157\u0158")
        buf.write("\7{\2\2\u0158\64\3\2\2\2\u0159\u015a\7G\2\2\u015a\u015b")
        buf.write("\7n\2\2\u015b\u015c\7u\2\2\u015c\u015d\7g\2\2\u015d\66")
        buf.write("\3\2\2\2\u015e\u015f\7G\2\2\u015f\u0160\7p\2\2\u0160\u0161")
        buf.write("\7f\2\2\u0161\u0162\7H\2\2\u0162\u0163\7q\2\2\u0163\u0164")
        buf.write("\7t\2\2\u01648\3\2\2\2\u0165\u0166\7K\2\2\u0166\u0167")
        buf.write("\7h\2\2\u0167:\3\2\2\2\u0168\u0169\7X\2\2\u0169\u016a")
        buf.write("\7c\2\2\u016a\u016b\7t\2\2\u016b<\3\2\2\2\u016c\u016d")
        buf.write("\7G\2\2\u016d\u016e\7p\2\2\u016e\u016f\7f\2\2\u016f\u0170")
        buf.write("\7F\2\2\u0170\u0171\7q\2\2\u0171>\3\2\2\2\u0172\u0173")
        buf.write("\7D\2\2\u0173\u0174\7t\2\2\u0174\u0175\7g\2\2\u0175\u0176")
        buf.write("\7c\2\2\u0176\u0177\7m\2\2\u0177@\3\2\2\2\u0178\u0179")
        buf.write("\7G\2\2\u0179\u017a\7n\2\2\u017a\u017b\7u\2\2\u017b\u017c")
        buf.write("\7g\2\2\u017c\u017d\7K\2\2\u017d\u017e\7h\2\2\u017eB\3")
        buf.write("\2\2\2\u017f\u0180\7G\2\2\u0180\u0181\7p\2\2\u0181\u0182")
        buf.write("\7f\2\2\u0182\u0183\7Y\2\2\u0183\u0184\7j\2\2\u0184\u0185")
        buf.write("\7k\2\2\u0185\u0186\7n\2\2\u0186\u0187\7g\2\2\u0187D\3")
        buf.write("\2\2\2\u0188\u0189\7R\2\2\u0189\u018a\7c\2\2\u018a\u018b")
        buf.write("\7t\2\2\u018b\u018c\7c\2\2\u018c\u018d\7o\2\2\u018d\u018e")
        buf.write("\7g\2\2\u018e\u018f\7v\2\2\u018f\u0190\7g\2\2\u0190\u0191")
        buf.write("\7t\2\2\u0191F\3\2\2\2\u0192\u0193\7Y\2\2\u0193\u0194")
        buf.write("\7j\2\2\u0194\u0195\7k\2\2\u0195\u0196\7n\2\2\u0196\u0197")
        buf.write("\7g\2\2\u0197H\3\2\2\2\u0198\u0199\7E\2\2\u0199\u019a")
        buf.write("\7q\2\2\u019a\u019b\7p\2\2\u019b\u019c\7v\2\2\u019c\u019d")
        buf.write("\7k\2\2\u019d\u019e\7p\2\2\u019e\u019f\7w\2\2\u019f\u01a0")
        buf.write("\7g\2\2\u01a0J\3\2\2\2\u01a1\u01a2\7G\2\2\u01a2\u01a3")
        buf.write("\7p\2\2\u01a3\u01a4\7f\2\2\u01a4\u01a5\7D\2\2\u01a5\u01a6")
        buf.write("\7q\2\2\u01a6\u01a7\7f\2\2\u01a7\u01a8\7{\2\2\u01a8L\3")
        buf.write("\2\2\2\u01a9\u01aa\7H\2\2\u01aa\u01ab\7q\2\2\u01ab\u01ac")
        buf.write("\7t\2\2\u01acN\3\2\2\2\u01ad\u01ae\7T\2\2\u01ae\u01af")
        buf.write("\7g\2\2\u01af\u01b0\7v\2\2\u01b0\u01b1\7w\2\2\u01b1\u01b2")
        buf.write("\7t\2\2\u01b2\u01b3\7p\2\2\u01b3P\3\2\2\2\u01b4\u01b5")
        buf.write("\7V\2\2\u01b5\u01b6\7t\2\2\u01b6\u01b7\7w\2\2\u01b7\u01b8")
        buf.write("\7g\2\2\u01b8R\3\2\2\2\u01b9\u01ba\7F\2\2\u01ba\u01bb")
        buf.write("\7q\2\2\u01bbT\3\2\2\2\u01bc\u01bd\7G\2\2\u01bd\u01be")
        buf.write("\7p\2\2\u01be\u01bf\7f\2\2\u01bf\u01c0\7K\2\2\u01c0\u01c1")
        buf.write("\7h\2\2\u01c1V\3\2\2\2\u01c2\u01c3\7H\2\2\u01c3\u01c4")
        buf.write("\7w\2\2\u01c4\u01c5\7p\2\2\u01c5\u01c6\7e\2\2\u01c6\u01c7")
        buf.write("\7v\2\2\u01c7\u01c8\7k\2\2\u01c8\u01c9\7q\2\2\u01c9\u01ca")
        buf.write("\7p\2\2\u01caX\3\2\2\2\u01cb\u01cc\7V\2\2\u01cc\u01cd")
        buf.write("\7j\2\2\u01cd\u01ce\7g\2\2\u01ce\u01cf\7p\2\2\u01cfZ\3")
        buf.write("\2\2\2\u01d0\u01d1\7H\2\2\u01d1\u01d2\7c\2\2\u01d2\u01d3")
        buf.write("\7n\2\2\u01d3\u01d4\7u\2\2\u01d4\u01d5\7g\2\2\u01d5\\")
        buf.write("\3\2\2\2\u01d6\u01d7\7-\2\2\u01d7^\3\2\2\2\u01d8\u01d9")
        buf.write("\7-\2\2\u01d9\u01da\7\60\2\2\u01da`\3\2\2\2\u01db\u01dc")
        buf.write("\7/\2\2\u01dcb\3\2\2\2\u01dd\u01de\7/\2\2\u01de\u01df")
        buf.write("\7\60\2\2\u01dfd\3\2\2\2\u01e0\u01e1\7,\2\2\u01e1f\3\2")
        buf.write("\2\2\u01e2\u01e3\7,\2\2\u01e3\u01e4\7\60\2\2\u01e4h\3")
        buf.write("\2\2\2\u01e5\u01e6\7^\2\2\u01e6j\3\2\2\2\u01e7\u01e8\7")
        buf.write("^\2\2\u01e8\u01e9\7\60\2\2\u01e9l\3\2\2\2\u01ea\u01eb")
        buf.write("\7\'\2\2\u01ebn\3\2\2\2\u01ec\u01ed\7#\2\2\u01edp\3\2")
        buf.write("\2\2\u01ee\u01ef\7(\2\2\u01ef\u01f0\7(\2\2\u01f0r\3\2")
        buf.write("\2\2\u01f1\u01f2\7~\2\2\u01f2\u01f3\7~\2\2\u01f3t\3\2")
        buf.write("\2\2\u01f4\u01f5\7?\2\2\u01f5\u01f6\7?\2\2\u01f6v\3\2")
        buf.write("\2\2\u01f7\u01f8\7#\2\2\u01f8\u01f9\7?\2\2\u01f9x\3\2")
        buf.write("\2\2\u01fa\u01fb\7@\2\2\u01fbz\3\2\2\2\u01fc\u01fd\7>")
        buf.write("\2\2\u01fd|\3\2\2\2\u01fe\u01ff\7>\2\2\u01ff\u0200\7?")
        buf.write("\2\2\u0200~\3\2\2\2\u0201\u0202\7@\2\2\u0202\u0203\7?")
        buf.write("\2\2\u0203\u0080\3\2\2\2\u0204\u0205\7?\2\2\u0205\u0206")
        buf.write("\7\61\2\2\u0206\u0207\7?\2\2\u0207\u0082\3\2\2\2\u0208")
        buf.write("\u0209\7@\2\2\u0209\u020a\7\60\2\2\u020a\u0084\3\2\2\2")
        buf.write("\u020b\u020c\7>\2\2\u020c\u020d\7\60\2\2\u020d\u0086\3")
        buf.write("\2\2\2\u020e\u020f\7>\2\2\u020f\u0210\7?\2\2\u0210\u0211")
        buf.write("\7\60\2\2\u0211\u0088\3\2\2\2\u0212\u0213\7@\2\2\u0213")
        buf.write("\u0214\7?\2\2\u0214\u0215\7\60\2\2\u0215\u008a\3\2\2\2")
        buf.write("\u0216\u023b\7\62\2\2\u0217\u0219\t\4\2\2\u0218\u0217")
        buf.write("\3\2\2\2\u0219\u021a\3\2\2\2\u021a\u0218\3\2\2\2\u021a")
        buf.write("\u021b\3\2\2\2\u021b\u021f\3\2\2\2\u021c\u021e\t\5\2\2")
        buf.write("\u021d\u021c\3\2\2\2\u021e\u0221\3\2\2\2\u021f\u021d\3")
        buf.write("\2\2\2\u021f\u0220\3\2\2\2\u0220\u023b\3\2\2\2\u0221\u021f")
        buf.write("\3\2\2\2\u0222\u0223\7\62\2\2\u0223\u0227\7z\2\2\u0224")
        buf.write("\u0225\7\62\2\2\u0225\u0227\7Z\2\2\u0226\u0222\3\2\2\2")
        buf.write("\u0226\u0224\3\2\2\2\u0227\u022b\3\2\2\2\u0228\u022a\t")
        buf.write("\6\2\2\u0229\u0228\3\2\2\2\u022a\u022d\3\2\2\2\u022b\u0229")
        buf.write("\3\2\2\2\u022b\u022c\3\2\2\2\u022c\u023b\3\2\2\2\u022d")
        buf.write("\u022b\3\2\2\2\u022e\u022f\7\62\2\2\u022f\u0233\7q\2\2")
        buf.write("\u0230\u0231\7\62\2\2\u0231\u0233\7Q\2\2\u0232\u022e\3")
        buf.write("\2\2\2\u0232\u0230\3\2\2\2\u0233\u0237\3\2\2\2\u0234\u0236")
        buf.write("\t\7\2\2\u0235\u0234\3\2\2\2\u0236\u0239\3\2\2\2\u0237")
        buf.write("\u0235\3\2\2\2\u0237\u0238\3\2\2\2\u0238\u023b\3\2\2\2")
        buf.write("\u0239\u0237\3\2\2\2\u023a\u0216\3\2\2\2\u023a\u0218\3")
        buf.write("\2\2\2\u023a\u0226\3\2\2\2\u023a\u0232\3\2\2\2\u023b\u008c")
        buf.write("\3\2\2\2\u023c\u023e\t\5\2\2\u023d\u023c\3\2\2\2\u023e")
        buf.write("\u023f\3\2\2\2\u023f\u023d\3\2\2\2\u023f\u0240\3\2\2\2")
        buf.write("\u0240\u0241\3\2\2\2\u0241\u0260\7\60\2\2\u0242\u0244")
        buf.write("\t\5\2\2\u0243\u0242\3\2\2\2\u0244\u0245\3\2\2\2\u0245")
        buf.write("\u0243\3\2\2\2\u0245\u0246\3\2\2\2\u0246\u0247\3\2\2\2")
        buf.write("\u0247\u0249\t\b\2\2\u0248\u024a\t\t\2\2\u0249\u0248\3")
        buf.write("\2\2\2\u0249\u024a\3\2\2\2\u024a\u024c\3\2\2\2\u024b\u024d")
        buf.write("\t\5\2\2\u024c\u024b\3\2\2\2\u024d\u024e\3\2\2\2\u024e")
        buf.write("\u024c\3\2\2\2\u024e\u024f\3\2\2\2\u024f\u025f\3\2\2\2")
        buf.write("\u0250\u0252\t\5\2\2\u0251\u0250\3\2\2\2\u0252\u0253\3")
        buf.write("\2\2\2\u0253\u0251\3\2\2\2\u0253\u0254\3\2\2\2\u0254\u025f")
        buf.write("\3\2\2\2\u0255\u0257\t\b\2\2\u0256\u0258\t\t\2\2\u0257")
        buf.write("\u0256\3\2\2\2\u0257\u0258\3\2\2\2\u0258\u025a\3\2\2\2")
        buf.write("\u0259\u025b\t\5\2\2\u025a\u0259\3\2\2\2\u025b\u025c\3")
        buf.write("\2\2\2\u025c\u025a\3\2\2\2\u025c\u025d\3\2\2\2\u025d\u025f")
        buf.write("\3\2\2\2\u025e\u0243\3\2\2\2\u025e\u0251\3\2\2\2\u025e")
        buf.write("\u0255\3\2\2\2\u025f\u0262\3\2\2\2\u0260\u025e\3\2\2\2")
        buf.write("\u0260\u0261\3\2\2\2\u0261\u008e\3\2\2\2\u0262\u0260\3")
        buf.write("\2\2\2\u0263\u0268\n\n\2\2\u0264\u0268\5\u0091I\2\u0265")
        buf.write("\u0266\7)\2\2\u0266\u0268\7$\2\2\u0267\u0263\3\2\2\2\u0267")
        buf.write("\u0264\3\2\2\2\u0267\u0265\3\2\2\2\u0268\u0090\3\2\2\2")
        buf.write("\u0269\u026a\7^\2\2\u026a\u026b\t\13\2\2\u026b\u0092\3")
        buf.write("\2\2\2\u026c\u0270\7$\2\2\u026d\u026f\5\u008fH\2\u026e")
        buf.write("\u026d\3\2\2\2\u026f\u0272\3\2\2\2\u0270\u026e\3\2\2\2")
        buf.write("\u0270\u0271\3\2\2\2\u0271\u0273\3\2\2\2\u0272\u0270\3")
        buf.write("\2\2\2\u0273\u0274\7$\2\2\u0274\u0275\bJ\2\2\u0275\u0094")
        buf.write("\3\2\2\2\u0276\u0280\7}\2\2\u0277\u0281\3\2\2\2\u0278")
        buf.write("\u027d\5\u008bF\2\u0279\u027a\7.\2\2\u027a\u027c\5\u008b")
        buf.write("F\2\u027b\u0279\3\2\2\2\u027c\u027f\3\2\2\2\u027d\u027b")
        buf.write("\3\2\2\2\u027d\u027e\3\2\2\2\u027e\u0281\3\2\2\2\u027f")
        buf.write("\u027d\3\2\2\2\u0280\u0277\3\2\2\2\u0280\u0278\3\2\2\2")
        buf.write("\u0281\u0282\3\2\2\2\u0282\u02be\7\177\2\2\u0283\u028d")
        buf.write("\7}\2\2\u0284\u028e\3\2\2\2\u0285\u028a\5\u008dG\2\u0286")
        buf.write("\u0287\7.\2\2\u0287\u0289\5\u008dG\2\u0288\u0286\3\2\2")
        buf.write("\2\u0289\u028c\3\2\2\2\u028a\u0288\3\2\2\2\u028a\u028b")
        buf.write("\3\2\2\2\u028b\u028e\3\2\2\2\u028c\u028a\3\2\2\2\u028d")
        buf.write("\u0284\3\2\2\2\u028d\u0285\3\2\2\2\u028e\u028f\3\2\2\2")
        buf.write("\u028f\u02be\7\177\2\2\u0290\u02a0\7}\2\2\u0291\u02a1")
        buf.write("\3\2\2\2\u0292\u0295\5Q)\2\u0293\u0295\5[.\2\u0294\u0292")
        buf.write("\3\2\2\2\u0294\u0293\3\2\2\2\u0295\u029d\3\2\2\2\u0296")
        buf.write("\u0299\7.\2\2\u0297\u029a\5Q)\2\u0298\u029a\5[.\2\u0299")
        buf.write("\u0297\3\2\2\2\u0299\u0298\3\2\2\2\u029a\u029c\3\2\2\2")
        buf.write("\u029b\u0296\3\2\2\2\u029c\u029f\3\2\2\2\u029d\u029b\3")
        buf.write("\2\2\2\u029d\u029e\3\2\2\2\u029e\u02a1\3\2\2\2\u029f\u029d")
        buf.write("\3\2\2\2\u02a0\u0291\3\2\2\2\u02a0\u0294\3\2\2\2\u02a1")
        buf.write("\u02a2\3\2\2\2\u02a2\u02be\7\177\2\2\u02a3\u02ad\7}\2")
        buf.write("\2\u02a4\u02ae\3\2\2\2\u02a5\u02aa\5\u0093J\2\u02a6\u02a7")
        buf.write("\7.\2\2\u02a7\u02a9\5\u0093J\2\u02a8\u02a6\3\2\2\2\u02a9")
        buf.write("\u02ac\3\2\2\2\u02aa\u02a8\3\2\2\2\u02aa\u02ab\3\2\2\2")
        buf.write("\u02ab\u02ae\3\2\2\2\u02ac\u02aa\3\2\2\2\u02ad\u02a4\3")
        buf.write("\2\2\2\u02ad\u02a5\3\2\2\2\u02ae\u02af\3\2\2\2\u02af\u02be")
        buf.write("\7\177\2\2\u02b0\u02ba\7}\2\2\u02b1\u02bb\3\2\2\2\u02b2")
        buf.write("\u02b7\5\u0095K\2\u02b3\u02b4\7.\2\2\u02b4\u02b6\5\u0095")
        buf.write("K\2\u02b5\u02b3\3\2\2\2\u02b6\u02b9\3\2\2\2\u02b7\u02b5")
        buf.write("\3\2\2\2\u02b7\u02b8\3\2\2\2\u02b8\u02bb\3\2\2\2\u02b9")
        buf.write("\u02b7\3\2\2\2\u02ba\u02b1\3\2\2\2\u02ba\u02b2\3\2\2\2")
        buf.write("\u02bb\u02bc\3\2\2\2\u02bc\u02be\7\177\2\2\u02bd\u0276")
        buf.write("\3\2\2\2\u02bd\u0283\3\2\2\2\u02bd\u0290\3\2\2\2\u02bd")
        buf.write("\u02a3\3\2\2\2\u02bd\u02b0\3\2\2\2\u02be\u0096\3\2\2\2")
        buf.write("\u02bf\u02c1\t\f\2\2\u02c0\u02bf\3\2\2\2\u02c1\u02c2\3")
        buf.write("\2\2\2\u02c2\u02c0\3\2\2\2\u02c2\u02c3\3\2\2\2\u02c3\u02c4")
        buf.write("\3\2\2\2\u02c4\u02c5\bL\3\2\u02c5\u0098\3\2\2\2\u02c6")
        buf.write("\u02c7\7,\2\2\u02c7\u02c8\7,\2\2\u02c8\u02cc\3\2\2\2\u02c9")
        buf.write("\u02cb\13\2\2\2\u02ca\u02c9\3\2\2\2\u02cb\u02ce\3\2\2")
        buf.write("\2\u02cc\u02cd\3\2\2\2\u02cc\u02ca\3\2\2\2\u02cd\u02cf")
        buf.write("\3\2\2\2\u02ce\u02cc\3\2\2\2\u02cf\u02d0\7,\2\2\u02d0")
        buf.write("\u02d1\7,\2\2\u02d1\u02d2\3\2\2\2\u02d2\u02d3\bM\3\2\u02d3")
        buf.write("\u009a\3\2\2\2\u02d4\u02d5\13\2\2\2\u02d5\u02d6\bN\4\2")
        buf.write("\u02d6\u009c\3\2\2\2\u02d7\u02db\7$\2\2\u02d8\u02da\5")
        buf.write("\u008fH\2\u02d9\u02d8\3\2\2\2\u02da\u02dd\3\2\2\2\u02db")
        buf.write("\u02d9\3\2\2\2\u02db\u02dc\3\2\2\2\u02dc\u02df\3\2\2\2")
        buf.write("\u02dd\u02db\3\2\2\2\u02de\u02e0\t\r\2\2\u02df\u02de\3")
        buf.write("\2\2\2\u02e0\u02e1\3\2\2\2\u02e1\u02e2\bO\5\2\u02e2\u009e")
        buf.write("\3\2\2\2\u02e3\u02e4\7^\2\2\u02e4\u02e5\n\13\2\2\u02e5")
        buf.write("\u00a0\3\2\2\2\u02e6\u02ea\7$\2\2\u02e7\u02e9\5\u008f")
        buf.write("H\2\u02e8\u02e7\3\2\2\2\u02e9\u02ec\3\2\2\2\u02ea\u02e8")
        buf.write("\3\2\2\2\u02ea\u02eb\3\2\2\2\u02eb\u02ed\3\2\2\2\u02ec")
        buf.write("\u02ea\3\2\2\2\u02ed\u02ee\5\u009fP\2\u02ee\u02ef\bQ\6")
        buf.write("\2\u02ef\u00a2\3\2\2\2\u02f0\u02f1\7,\2\2\u02f1\u02f2")
        buf.write("\7,\2\2\u02f2\u02f6\3\2\2\2\u02f3\u02f5\n\16\2\2\u02f4")
        buf.write("\u02f3\3\2\2\2\u02f5\u02f8\3\2\2\2\u02f6\u02f4\3\2\2\2")
        buf.write("\u02f6\u02f7\3\2\2\2\u02f7\u0305\3\2\2\2\u02f8\u02f6\3")
        buf.write("\2\2\2\u02f9\u0306\7,\2\2\u02fa\u02fc\7,\2\2\u02fb\u02fd")
        buf.write("\n\16\2\2\u02fc\u02fb\3\2\2\2\u02fd\u02fe\3\2\2\2\u02fe")
        buf.write("\u02fc\3\2\2\2\u02fe\u02ff\3\2\2\2\u02ff\u0301\3\2\2\2")
        buf.write("\u0300\u02fa\3\2\2\2\u0301\u0304\3\2\2\2\u0302\u0300\3")
        buf.write("\2\2\2\u0302\u0303\3\2\2\2\u0303\u0306\3\2\2\2\u0304\u0302")
        buf.write("\3\2\2\2\u0305\u02f9\3\2\2\2\u0305\u0302\3\2\2\2\u0306")
        buf.write("\u0307\3\2\2\2\u0307\u0308\7\2\2\3\u0308\u0309\bR\7\2")
        buf.write("\u0309\u00a4\3\2\2\2,\2\u0151\u021a\u021f\u0226\u022b")
        buf.write("\u0232\u0237\u023a\u023f\u0245\u0249\u024e\u0253\u0257")
        buf.write("\u025c\u025e\u0260\u0267\u0270\u027d\u0280\u028a\u028d")
        buf.write("\u0294\u0299\u029d\u02a0\u02aa\u02ad\u02b7\u02ba\u02bd")
        buf.write("\u02c2\u02cc\u02db\u02df\u02ea\u02f6\u02fe\u0302\u0305")
        buf.write("\b\3J\2\b\2\2\3N\3\3O\4\3Q\5\3R\6")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    INT_OF_FLOAT = 2
    INT_OF_STRING = 3
    FLOAT_OF_INT = 4
    FLOAT_OF_STRING = 5
    STRING_OF_INT = 6
    STRING_OF_FLOAT = 7
    STRING_OF_BOOL = 8
    BOOL_OF_STRING = 9
    PRINTLN = 10
    PRINT = 11
    PRINTSTRLN = 12
    READ = 13
    SEMI = 14
    COMMA = 15
    COLON = 16
    DOT = 17
    LP = 18
    RP = 19
    LCB = 20
    RCB = 21
    LSB = 22
    RSB = 23
    ID = 24
    BODY = 25
    ELSE = 26
    ENDFOR = 27
    IF = 28
    VAR = 29
    ENDDO = 30
    BREAK = 31
    ELSEIF = 32
    ENDWHILE = 33
    PARAMETER = 34
    WHILE = 35
    CONTINUE = 36
    ENDBODY = 37
    FOR = 38
    RETURN = 39
    TRUE = 40
    DO = 41
    ENDIF = 42
    FUNCTION = 43
    THEN = 44
    FALSE = 45
    ADD = 46
    ADDDOT = 47
    SUB = 48
    SUBDOT = 49
    MUL = 50
    MULDOT = 51
    DIV = 52
    DIVDOT = 53
    MOD = 54
    NEG = 55
    AND = 56
    OR = 57
    EQ = 58
    NEI = 59
    GT = 60
    LT = 61
    LTE = 62
    GTE = 63
    NEF = 64
    GTDOT = 65
    LTDOT = 66
    LTEDOT = 67
    GTEDOT = 68
    INTEGER = 69
    FLOAT = 70
    STRING = 71
    ARRAY = 72
    WS = 73
    BLOCK_COMMENT = 74
    ERROR_CHAR = 75
    UNCLOSE_STRING = 76
    ILLEGAL_ESCAPE = 77
    UNTERMINATED_COMMENT = 78

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "'int_of_float'", "'int_of_string'", "'float_of_int'", 
            "'float_of_string'", "'string_of_int'", "'string_of_float'", 
            "'string_of_bool'", "'bool_of_string'", "'printLn'", "'print'", 
            "'printStrLn'", "'read'", "';'", "','", "':'", "'.'", "'('", 
            "')'", "'{'", "'}'", "'['", "']'", "'Body'", "'Else'", "'EndFor'", 
            "'If'", "'Var'", "'EndDo'", "'Break'", "'ElseIf'", "'EndWhile'", 
            "'Parameter'", "'While'", "'Continue'", "'EndBody'", "'For'", 
            "'Return'", "'True'", "'Do'", "'EndIf'", "'Function'", "'Then'", 
            "'False'", "'+'", "'+.'", "'-'", "'-.'", "'*'", "'*.'", "'\\'", 
            "'\\.'", "'%'", "'!'", "'&&'", "'||'", "'=='", "'!='", "'>'", 
            "'<'", "'<='", "'>='", "'=/='", "'>.'", "'<.'", "'<=.'", "'>=.'" ]

    symbolicNames = [ "<INVALID>",
            "INT_OF_FLOAT", "INT_OF_STRING", "FLOAT_OF_INT", "FLOAT_OF_STRING", 
            "STRING_OF_INT", "STRING_OF_FLOAT", "STRING_OF_BOOL", "BOOL_OF_STRING", 
            "PRINTLN", "PRINT", "PRINTSTRLN", "READ", "SEMI", "COMMA", "COLON", 
            "DOT", "LP", "RP", "LCB", "RCB", "LSB", "RSB", "ID", "BODY", 
            "ELSE", "ENDFOR", "IF", "VAR", "ENDDO", "BREAK", "ELSEIF", "ENDWHILE", 
            "PARAMETER", "WHILE", "CONTINUE", "ENDBODY", "FOR", "RETURN", 
            "TRUE", "DO", "ENDIF", "FUNCTION", "THEN", "FALSE", "ADD", "ADDDOT", 
            "SUB", "SUBDOT", "MUL", "MULDOT", "DIV", "DIVDOT", "MOD", "NEG", 
            "AND", "OR", "EQ", "NEI", "GT", "LT", "LTE", "GTE", "NEF", "GTDOT", 
            "LTDOT", "LTEDOT", "GTEDOT", "INTEGER", "FLOAT", "STRING", "ARRAY", 
            "WS", "BLOCK_COMMENT", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "UNTERMINATED_COMMENT" ]

    ruleNames = [ "T__0", "INT_OF_FLOAT", "INT_OF_STRING", "FLOAT_OF_INT", 
                  "FLOAT_OF_STRING", "STRING_OF_INT", "STRING_OF_FLOAT", 
                  "STRING_OF_BOOL", "BOOL_OF_STRING", "PRINTLN", "PRINT", 
                  "PRINTSTRLN", "READ", "SEMI", "COMMA", "COLON", "DOT", 
                  "LP", "RP", "LCB", "RCB", "LSB", "RSB", "ID", "BODY", 
                  "ELSE", "ENDFOR", "IF", "VAR", "ENDDO", "BREAK", "ELSEIF", 
                  "ENDWHILE", "PARAMETER", "WHILE", "CONTINUE", "ENDBODY", 
                  "FOR", "RETURN", "TRUE", "DO", "ENDIF", "FUNCTION", "THEN", 
                  "FALSE", "ADD", "ADDDOT", "SUB", "SUBDOT", "MUL", "MULDOT", 
                  "DIV", "DIVDOT", "MOD", "NEG", "AND", "OR", "EQ", "NEI", 
                  "GT", "LT", "LTE", "GTE", "NEF", "GTDOT", "LTDOT", "LTEDOT", 
                  "GTEDOT", "INTEGER", "FLOAT", "STR_CHAR", "ESC_SEQ", "STRING", 
                  "ARRAY", "WS", "BLOCK_COMMENT", "ERROR_CHAR", "UNCLOSE_STRING", 
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
            actions[72] = self.STRING_action 
            actions[76] = self.ERROR_CHAR_action 
            actions[77] = self.UNCLOSE_STRING_action 
            actions[79] = self.ILLEGAL_ESCAPE_action 
            actions[80] = self.UNTERMINATED_COMMENT_action 
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
                
     


