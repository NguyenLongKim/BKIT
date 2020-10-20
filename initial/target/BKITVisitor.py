# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKITParser import BKITParser
else:
    from BKITParser import BKITParser

# This class defines a complete generic visitor for a parse tree produced by BKITParser.

class BKITVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKITParser#program.
    def visitProgram(self, ctx:BKITParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_declare.
    def visitVar_declare(self, ctx:BKITParser.Var_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#vars_list.
    def visitVars_list(self, ctx:BKITParser.Vars_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#scalar_var.
    def visitScalar_var(self, ctx:BKITParser.Scalar_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#literal.
    def visitLiteral(self, ctx:BKITParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#composite_var.
    def visitComposite_var(self, ctx:BKITParser.Composite_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#dimension.
    def visitDimension(self, ctx:BKITParser.DimensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#func_declare.
    def visitFunc_declare(self, ctx:BKITParser.Func_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#params_list.
    def visitParams_list(self, ctx:BKITParser.Params_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#stms_list.
    def visitStms_list(self, ctx:BKITParser.Stms_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expr.
    def visitExpr(self, ctx:BKITParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#int_expr.
    def visitInt_expr(self, ctx:BKITParser.Int_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#float_expr.
    def visitFloat_expr(self, ctx:BKITParser.Float_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#relational_expr.
    def visitRelational_expr(self, ctx:BKITParser.Relational_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#bool_expr.
    def visitBool_expr(self, ctx:BKITParser.Bool_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#element_expr.
    def visitElement_expr(self, ctx:BKITParser.Element_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#index_operators.
    def visitIndex_operators(self, ctx:BKITParser.Index_operatorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#int_of_float.
    def visitInt_of_float(self, ctx:BKITParser.Int_of_floatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#float_of_int.
    def visitFloat_of_int(self, ctx:BKITParser.Float_of_intContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#int_of_string.
    def visitInt_of_string(self, ctx:BKITParser.Int_of_stringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#string_of_int.
    def visitString_of_int(self, ctx:BKITParser.String_of_intContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#float_of_string.
    def visitFloat_of_string(self, ctx:BKITParser.Float_of_stringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#string_of_float.
    def visitString_of_float(self, ctx:BKITParser.String_of_floatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#bool_of_string.
    def visitBool_of_string(self, ctx:BKITParser.Bool_of_stringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#string_of_bool.
    def visitString_of_bool(self, ctx:BKITParser.String_of_boolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#type_coercion_func.
    def visitType_coercion_func(self, ctx:BKITParser.Type_coercion_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_delcare_stm.
    def visitVar_delcare_stm(self, ctx:BKITParser.Var_delcare_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#asm_stm.
    def visitAsm_stm(self, ctx:BKITParser.Asm_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#if_stm.
    def visitIf_stm(self, ctx:BKITParser.If_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#for_stm.
    def visitFor_stm(self, ctx:BKITParser.For_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#initExpr.
    def visitInitExpr(self, ctx:BKITParser.InitExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#conditionExpr.
    def visitConditionExpr(self, ctx:BKITParser.ConditionExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#updateExpr.
    def visitUpdateExpr(self, ctx:BKITParser.UpdateExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#while_stm.
    def visitWhile_stm(self, ctx:BKITParser.While_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#do_while_stm.
    def visitDo_while_stm(self, ctx:BKITParser.Do_while_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#break_stm.
    def visitBreak_stm(self, ctx:BKITParser.Break_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#coninue_stm.
    def visitConinue_stm(self, ctx:BKITParser.Coninue_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#call_stm.
    def visitCall_stm(self, ctx:BKITParser.Call_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#return_stm.
    def visitReturn_stm(self, ctx:BKITParser.Return_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#func_call.
    def visitFunc_call(self, ctx:BKITParser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#params_func_call.
    def visitParams_func_call(self, ctx:BKITParser.Params_func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#printLn_func.
    def visitPrintLn_func(self, ctx:BKITParser.PrintLn_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#print_func.
    def visitPrint_func(self, ctx:BKITParser.Print_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#printStrLn_func.
    def visitPrintStrLn_func(self, ctx:BKITParser.PrintStrLn_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#read_func.
    def visitRead_func(self, ctx:BKITParser.Read_funcContext):
        return self.visitChildren(ctx)



del BKITParser