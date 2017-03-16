# Generated from MySQL.g4 by ANTLR 4.6
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MySQLParser import MySQLParser
else:
    from MySQLParser import MySQLParser



# This class defines a complete listener for a parse tree produced by MySQLParser.
class MySQLListener(ParseTreeListener):

    # Enter a parse tree produced by MySQLParser#relational_op.
    def enterRelational_op(self, ctx:MySQLParser.Relational_opContext):
        pass

    # Exit a parse tree produced by MySQLParser#relational_op.
    def exitRelational_op(self, ctx:MySQLParser.Relational_opContext):
        pass


    # Enter a parse tree produced by MySQLParser#cast_data_type.
    def enterCast_data_type(self, ctx:MySQLParser.Cast_data_typeContext):
        pass

    # Exit a parse tree produced by MySQLParser#cast_data_type.
    def exitCast_data_type(self, ctx:MySQLParser.Cast_data_typeContext):
        pass


    # Enter a parse tree produced by MySQLParser#search_modifier.
    def enterSearch_modifier(self, ctx:MySQLParser.Search_modifierContext):
        pass

    # Exit a parse tree produced by MySQLParser#search_modifier.
    def exitSearch_modifier(self, ctx:MySQLParser.Search_modifierContext):
        pass


    # Enter a parse tree produced by MySQLParser#transcoding_name.
    def enterTranscoding_name(self, ctx:MySQLParser.Transcoding_nameContext):
        pass

    # Exit a parse tree produced by MySQLParser#transcoding_name.
    def exitTranscoding_name(self, ctx:MySQLParser.Transcoding_nameContext):
        pass


    # Enter a parse tree produced by MySQLParser#interval_unit.
    def enterInterval_unit(self, ctx:MySQLParser.Interval_unitContext):
        pass

    # Exit a parse tree produced by MySQLParser#interval_unit.
    def exitInterval_unit(self, ctx:MySQLParser.Interval_unitContext):
        pass


    # Enter a parse tree produced by MySQLParser#string_literal.
    def enterString_literal(self, ctx:MySQLParser.String_literalContext):
        pass

    # Exit a parse tree produced by MySQLParser#string_literal.
    def exitString_literal(self, ctx:MySQLParser.String_literalContext):
        pass


    # Enter a parse tree produced by MySQLParser#number_literal.
    def enterNumber_literal(self, ctx:MySQLParser.Number_literalContext):
        pass

    # Exit a parse tree produced by MySQLParser#number_literal.
    def exitNumber_literal(self, ctx:MySQLParser.Number_literalContext):
        pass


    # Enter a parse tree produced by MySQLParser#hex_literal.
    def enterHex_literal(self, ctx:MySQLParser.Hex_literalContext):
        pass

    # Exit a parse tree produced by MySQLParser#hex_literal.
    def exitHex_literal(self, ctx:MySQLParser.Hex_literalContext):
        pass


    # Enter a parse tree produced by MySQLParser#boolean_literal.
    def enterBoolean_literal(self, ctx:MySQLParser.Boolean_literalContext):
        pass

    # Exit a parse tree produced by MySQLParser#boolean_literal.
    def exitBoolean_literal(self, ctx:MySQLParser.Boolean_literalContext):
        pass


    # Enter a parse tree produced by MySQLParser#bit_literal.
    def enterBit_literal(self, ctx:MySQLParser.Bit_literalContext):
        pass

    # Exit a parse tree produced by MySQLParser#bit_literal.
    def exitBit_literal(self, ctx:MySQLParser.Bit_literalContext):
        pass


    # Enter a parse tree produced by MySQLParser#literal_value.
    def enterLiteral_value(self, ctx:MySQLParser.Literal_valueContext):
        pass

    # Exit a parse tree produced by MySQLParser#literal_value.
    def exitLiteral_value(self, ctx:MySQLParser.Literal_valueContext):
        pass


    # Enter a parse tree produced by MySQLParser#functionList.
    def enterFunctionList(self, ctx:MySQLParser.FunctionListContext):
        pass

    # Exit a parse tree produced by MySQLParser#functionList.
    def exitFunctionList(self, ctx:MySQLParser.FunctionListContext):
        pass


    # Enter a parse tree produced by MySQLParser#number_functions.
    def enterNumber_functions(self, ctx:MySQLParser.Number_functionsContext):
        pass

    # Exit a parse tree produced by MySQLParser#number_functions.
    def exitNumber_functions(self, ctx:MySQLParser.Number_functionsContext):
        pass


    # Enter a parse tree produced by MySQLParser#char_functions.
    def enterChar_functions(self, ctx:MySQLParser.Char_functionsContext):
        pass

    # Exit a parse tree produced by MySQLParser#char_functions.
    def exitChar_functions(self, ctx:MySQLParser.Char_functionsContext):
        pass


    # Enter a parse tree produced by MySQLParser#time_functions.
    def enterTime_functions(self, ctx:MySQLParser.Time_functionsContext):
        pass

    # Exit a parse tree produced by MySQLParser#time_functions.
    def exitTime_functions(self, ctx:MySQLParser.Time_functionsContext):
        pass


    # Enter a parse tree produced by MySQLParser#other_functions.
    def enterOther_functions(self, ctx:MySQLParser.Other_functionsContext):
        pass

    # Exit a parse tree produced by MySQLParser#other_functions.
    def exitOther_functions(self, ctx:MySQLParser.Other_functionsContext):
        pass


    # Enter a parse tree produced by MySQLParser#group_functions.
    def enterGroup_functions(self, ctx:MySQLParser.Group_functionsContext):
        pass

    # Exit a parse tree produced by MySQLParser#group_functions.
    def exitGroup_functions(self, ctx:MySQLParser.Group_functionsContext):
        pass


    # Enter a parse tree produced by MySQLParser#escape_id.
    def enterEscape_id(self, ctx:MySQLParser.Escape_idContext):
        pass

    # Exit a parse tree produced by MySQLParser#escape_id.
    def exitEscape_id(self, ctx:MySQLParser.Escape_idContext):
        pass


    # Enter a parse tree produced by MySQLParser#schema_name.
    def enterSchema_name(self, ctx:MySQLParser.Schema_nameContext):
        pass

    # Exit a parse tree produced by MySQLParser#schema_name.
    def exitSchema_name(self, ctx:MySQLParser.Schema_nameContext):
        pass


    # Enter a parse tree produced by MySQLParser#table_name.
    def enterTable_name(self, ctx:MySQLParser.Table_nameContext):
        pass

    # Exit a parse tree produced by MySQLParser#table_name.
    def exitTable_name(self, ctx:MySQLParser.Table_nameContext):
        pass


    # Enter a parse tree produced by MySQLParser#column_name.
    def enterColumn_name(self, ctx:MySQLParser.Column_nameContext):
        pass

    # Exit a parse tree produced by MySQLParser#column_name.
    def exitColumn_name(self, ctx:MySQLParser.Column_nameContext):
        pass


    # Enter a parse tree produced by MySQLParser#index_name.
    def enterIndex_name(self, ctx:MySQLParser.Index_nameContext):
        pass

    # Exit a parse tree produced by MySQLParser#index_name.
    def exitIndex_name(self, ctx:MySQLParser.Index_nameContext):
        pass


    # Enter a parse tree produced by MySQLParser#partition_name.
    def enterPartition_name(self, ctx:MySQLParser.Partition_nameContext):
        pass

    # Exit a parse tree produced by MySQLParser#partition_name.
    def exitPartition_name(self, ctx:MySQLParser.Partition_nameContext):
        pass


    # Enter a parse tree produced by MySQLParser#alias.
    def enterAlias(self, ctx:MySQLParser.AliasContext):
        pass

    # Exit a parse tree produced by MySQLParser#alias.
    def exitAlias(self, ctx:MySQLParser.AliasContext):
        pass


    # Enter a parse tree produced by MySQLParser#expression.
    def enterExpression(self, ctx:MySQLParser.ExpressionContext):
        pass

    # Exit a parse tree produced by MySQLParser#expression.
    def exitExpression(self, ctx:MySQLParser.ExpressionContext):
        pass


    # Enter a parse tree produced by MySQLParser#bool_primary.
    def enterBool_primary(self, ctx:MySQLParser.Bool_primaryContext):
        pass

    # Exit a parse tree produced by MySQLParser#bool_primary.
    def exitBool_primary(self, ctx:MySQLParser.Bool_primaryContext):
        pass


    # Enter a parse tree produced by MySQLParser#predicate.
    def enterPredicate(self, ctx:MySQLParser.PredicateContext):
        pass

    # Exit a parse tree produced by MySQLParser#predicate.
    def exitPredicate(self, ctx:MySQLParser.PredicateContext):
        pass


    # Enter a parse tree produced by MySQLParser#bit_expr.
    def enterBit_expr(self, ctx:MySQLParser.Bit_exprContext):
        pass

    # Exit a parse tree produced by MySQLParser#bit_expr.
    def exitBit_expr(self, ctx:MySQLParser.Bit_exprContext):
        pass


    # Enter a parse tree produced by MySQLParser#simple_expr.
    def enterSimple_expr(self, ctx:MySQLParser.Simple_exprContext):
        pass

    # Exit a parse tree produced by MySQLParser#simple_expr.
    def exitSimple_expr(self, ctx:MySQLParser.Simple_exprContext):
        pass


    # Enter a parse tree produced by MySQLParser#function_call.
    def enterFunction_call(self, ctx:MySQLParser.Function_callContext):
        pass

    # Exit a parse tree produced by MySQLParser#function_call.
    def exitFunction_call(self, ctx:MySQLParser.Function_callContext):
        pass


    # Enter a parse tree produced by MySQLParser#case_when_statement.
    def enterCase_when_statement(self, ctx:MySQLParser.Case_when_statementContext):
        pass

    # Exit a parse tree produced by MySQLParser#case_when_statement.
    def exitCase_when_statement(self, ctx:MySQLParser.Case_when_statementContext):
        pass


    # Enter a parse tree produced by MySQLParser#case_when_statement1.
    def enterCase_when_statement1(self, ctx:MySQLParser.Case_when_statement1Context):
        pass

    # Exit a parse tree produced by MySQLParser#case_when_statement1.
    def exitCase_when_statement1(self, ctx:MySQLParser.Case_when_statement1Context):
        pass


    # Enter a parse tree produced by MySQLParser#case_when_statement2.
    def enterCase_when_statement2(self, ctx:MySQLParser.Case_when_statement2Context):
        pass

    # Exit a parse tree produced by MySQLParser#case_when_statement2.
    def exitCase_when_statement2(self, ctx:MySQLParser.Case_when_statement2Context):
        pass


    # Enter a parse tree produced by MySQLParser#match_against_statement.
    def enterMatch_against_statement(self, ctx:MySQLParser.Match_against_statementContext):
        pass

    # Exit a parse tree produced by MySQLParser#match_against_statement.
    def exitMatch_against_statement(self, ctx:MySQLParser.Match_against_statementContext):
        pass


    # Enter a parse tree produced by MySQLParser#column_spec.
    def enterColumn_spec(self, ctx:MySQLParser.Column_specContext):
        pass

    # Exit a parse tree produced by MySQLParser#column_spec.
    def exitColumn_spec(self, ctx:MySQLParser.Column_specContext):
        pass


    # Enter a parse tree produced by MySQLParser#expression_list.
    def enterExpression_list(self, ctx:MySQLParser.Expression_listContext):
        pass

    # Exit a parse tree produced by MySQLParser#expression_list.
    def exitExpression_list(self, ctx:MySQLParser.Expression_listContext):
        pass


    # Enter a parse tree produced by MySQLParser#interval_expr.
    def enterInterval_expr(self, ctx:MySQLParser.Interval_exprContext):
        pass

    # Exit a parse tree produced by MySQLParser#interval_expr.
    def exitInterval_expr(self, ctx:MySQLParser.Interval_exprContext):
        pass


    # Enter a parse tree produced by MySQLParser#table_references.
    def enterTable_references(self, ctx:MySQLParser.Table_referencesContext):
        pass

    # Exit a parse tree produced by MySQLParser#table_references.
    def exitTable_references(self, ctx:MySQLParser.Table_referencesContext):
        pass


    # Enter a parse tree produced by MySQLParser#escaped_table_reference.
    def enterEscaped_table_reference(self, ctx:MySQLParser.Escaped_table_referenceContext):
        pass

    # Exit a parse tree produced by MySQLParser#escaped_table_reference.
    def exitEscaped_table_reference(self, ctx:MySQLParser.Escaped_table_referenceContext):
        pass


    # Enter a parse tree produced by MySQLParser#table_reference.
    def enterTable_reference(self, ctx:MySQLParser.Table_referenceContext):
        pass

    # Exit a parse tree produced by MySQLParser#table_reference.
    def exitTable_reference(self, ctx:MySQLParser.Table_referenceContext):
        pass


    # Enter a parse tree produced by MySQLParser#table_factor.
    def enterTable_factor(self, ctx:MySQLParser.Table_factorContext):
        pass

    # Exit a parse tree produced by MySQLParser#table_factor.
    def exitTable_factor(self, ctx:MySQLParser.Table_factorContext):
        pass


    # Enter a parse tree produced by MySQLParser#index_hint_list.
    def enterIndex_hint_list(self, ctx:MySQLParser.Index_hint_listContext):
        pass

    # Exit a parse tree produced by MySQLParser#index_hint_list.
    def exitIndex_hint_list(self, ctx:MySQLParser.Index_hint_listContext):
        pass


    # Enter a parse tree produced by MySQLParser#index_options.
    def enterIndex_options(self, ctx:MySQLParser.Index_optionsContext):
        pass

    # Exit a parse tree produced by MySQLParser#index_options.
    def exitIndex_options(self, ctx:MySQLParser.Index_optionsContext):
        pass


    # Enter a parse tree produced by MySQLParser#index_hint.
    def enterIndex_hint(self, ctx:MySQLParser.Index_hintContext):
        pass

    # Exit a parse tree produced by MySQLParser#index_hint.
    def exitIndex_hint(self, ctx:MySQLParser.Index_hintContext):
        pass


    # Enter a parse tree produced by MySQLParser#index_list.
    def enterIndex_list(self, ctx:MySQLParser.Index_listContext):
        pass

    # Exit a parse tree produced by MySQLParser#index_list.
    def exitIndex_list(self, ctx:MySQLParser.Index_listContext):
        pass


    # Enter a parse tree produced by MySQLParser#partition_clause.
    def enterPartition_clause(self, ctx:MySQLParser.Partition_clauseContext):
        pass

    # Exit a parse tree produced by MySQLParser#partition_clause.
    def exitPartition_clause(self, ctx:MySQLParser.Partition_clauseContext):
        pass


    # Enter a parse tree produced by MySQLParser#partition_names.
    def enterPartition_names(self, ctx:MySQLParser.Partition_namesContext):
        pass

    # Exit a parse tree produced by MySQLParser#partition_names.
    def exitPartition_names(self, ctx:MySQLParser.Partition_namesContext):
        pass


    # Enter a parse tree produced by MySQLParser#statement.
    def enterStatement(self, ctx:MySQLParser.StatementContext):
        pass

    # Exit a parse tree produced by MySQLParser#statement.
    def exitStatement(self, ctx:MySQLParser.StatementContext):
        pass


    # Enter a parse tree produced by MySQLParser#data_manipulation_statements.
    def enterData_manipulation_statements(self, ctx:MySQLParser.Data_manipulation_statementsContext):
        pass

    # Exit a parse tree produced by MySQLParser#data_manipulation_statements.
    def exitData_manipulation_statements(self, ctx:MySQLParser.Data_manipulation_statementsContext):
        pass


    # Enter a parse tree produced by MySQLParser#select_statement.
    def enterSelect_statement(self, ctx:MySQLParser.Select_statementContext):
        pass

    # Exit a parse tree produced by MySQLParser#select_statement.
    def exitSelect_statement(self, ctx:MySQLParser.Select_statementContext):
        pass


    # Enter a parse tree produced by MySQLParser#select_expression.
    def enterSelect_expression(self, ctx:MySQLParser.Select_expressionContext):
        pass

    # Exit a parse tree produced by MySQLParser#select_expression.
    def exitSelect_expression(self, ctx:MySQLParser.Select_expressionContext):
        pass


    # Enter a parse tree produced by MySQLParser#where_clause.
    def enterWhere_clause(self, ctx:MySQLParser.Where_clauseContext):
        pass

    # Exit a parse tree produced by MySQLParser#where_clause.
    def exitWhere_clause(self, ctx:MySQLParser.Where_clauseContext):
        pass


    # Enter a parse tree produced by MySQLParser#groupby_clause.
    def enterGroupby_clause(self, ctx:MySQLParser.Groupby_clauseContext):
        pass

    # Exit a parse tree produced by MySQLParser#groupby_clause.
    def exitGroupby_clause(self, ctx:MySQLParser.Groupby_clauseContext):
        pass


    # Enter a parse tree produced by MySQLParser#groupby_item.
    def enterGroupby_item(self, ctx:MySQLParser.Groupby_itemContext):
        pass

    # Exit a parse tree produced by MySQLParser#groupby_item.
    def exitGroupby_item(self, ctx:MySQLParser.Groupby_itemContext):
        pass


    # Enter a parse tree produced by MySQLParser#having_clause.
    def enterHaving_clause(self, ctx:MySQLParser.Having_clauseContext):
        pass

    # Exit a parse tree produced by MySQLParser#having_clause.
    def exitHaving_clause(self, ctx:MySQLParser.Having_clauseContext):
        pass


    # Enter a parse tree produced by MySQLParser#orderby_clause.
    def enterOrderby_clause(self, ctx:MySQLParser.Orderby_clauseContext):
        pass

    # Exit a parse tree produced by MySQLParser#orderby_clause.
    def exitOrderby_clause(self, ctx:MySQLParser.Orderby_clauseContext):
        pass


    # Enter a parse tree produced by MySQLParser#orderby_item.
    def enterOrderby_item(self, ctx:MySQLParser.Orderby_itemContext):
        pass

    # Exit a parse tree produced by MySQLParser#orderby_item.
    def exitOrderby_item(self, ctx:MySQLParser.Orderby_itemContext):
        pass


    # Enter a parse tree produced by MySQLParser#limit_clause.
    def enterLimit_clause(self, ctx:MySQLParser.Limit_clauseContext):
        pass

    # Exit a parse tree produced by MySQLParser#limit_clause.
    def exitLimit_clause(self, ctx:MySQLParser.Limit_clauseContext):
        pass


    # Enter a parse tree produced by MySQLParser#offset.
    def enterOffset(self, ctx:MySQLParser.OffsetContext):
        pass

    # Exit a parse tree produced by MySQLParser#offset.
    def exitOffset(self, ctx:MySQLParser.OffsetContext):
        pass


    # Enter a parse tree produced by MySQLParser#row_count.
    def enterRow_count(self, ctx:MySQLParser.Row_countContext):
        pass

    # Exit a parse tree produced by MySQLParser#row_count.
    def exitRow_count(self, ctx:MySQLParser.Row_countContext):
        pass


    # Enter a parse tree produced by MySQLParser#select_list.
    def enterSelect_list(self, ctx:MySQLParser.Select_listContext):
        pass

    # Exit a parse tree produced by MySQLParser#select_list.
    def exitSelect_list(self, ctx:MySQLParser.Select_listContext):
        pass


    # Enter a parse tree produced by MySQLParser#column_list.
    def enterColumn_list(self, ctx:MySQLParser.Column_listContext):
        pass

    # Exit a parse tree produced by MySQLParser#column_list.
    def exitColumn_list(self, ctx:MySQLParser.Column_listContext):
        pass


    # Enter a parse tree produced by MySQLParser#subquery.
    def enterSubquery(self, ctx:MySQLParser.SubqueryContext):
        pass

    # Exit a parse tree produced by MySQLParser#subquery.
    def exitSubquery(self, ctx:MySQLParser.SubqueryContext):
        pass


    # Enter a parse tree produced by MySQLParser#table_spec.
    def enterTable_spec(self, ctx:MySQLParser.Table_specContext):
        pass

    # Exit a parse tree produced by MySQLParser#table_spec.
    def exitTable_spec(self, ctx:MySQLParser.Table_specContext):
        pass


    # Enter a parse tree produced by MySQLParser#displayed_column.
    def enterDisplayed_column(self, ctx:MySQLParser.Displayed_columnContext):
        pass

    # Exit a parse tree produced by MySQLParser#displayed_column.
    def exitDisplayed_column(self, ctx:MySQLParser.Displayed_columnContext):
        pass


    # Enter a parse tree produced by MySQLParser#delete_statements.
    def enterDelete_statements(self, ctx:MySQLParser.Delete_statementsContext):
        pass

    # Exit a parse tree produced by MySQLParser#delete_statements.
    def exitDelete_statements(self, ctx:MySQLParser.Delete_statementsContext):
        pass


    # Enter a parse tree produced by MySQLParser#delete_single_table_statement.
    def enterDelete_single_table_statement(self, ctx:MySQLParser.Delete_single_table_statementContext):
        pass

    # Exit a parse tree produced by MySQLParser#delete_single_table_statement.
    def exitDelete_single_table_statement(self, ctx:MySQLParser.Delete_single_table_statementContext):
        pass


    # Enter a parse tree produced by MySQLParser#delete_multiple_table_statement1.
    def enterDelete_multiple_table_statement1(self, ctx:MySQLParser.Delete_multiple_table_statement1Context):
        pass

    # Exit a parse tree produced by MySQLParser#delete_multiple_table_statement1.
    def exitDelete_multiple_table_statement1(self, ctx:MySQLParser.Delete_multiple_table_statement1Context):
        pass


    # Enter a parse tree produced by MySQLParser#delete_multiple_table_statement2.
    def enterDelete_multiple_table_statement2(self, ctx:MySQLParser.Delete_multiple_table_statement2Context):
        pass

    # Exit a parse tree produced by MySQLParser#delete_multiple_table_statement2.
    def exitDelete_multiple_table_statement2(self, ctx:MySQLParser.Delete_multiple_table_statement2Context):
        pass


    # Enter a parse tree produced by MySQLParser#insert_statements.
    def enterInsert_statements(self, ctx:MySQLParser.Insert_statementsContext):
        pass

    # Exit a parse tree produced by MySQLParser#insert_statements.
    def exitInsert_statements(self, ctx:MySQLParser.Insert_statementsContext):
        pass


    # Enter a parse tree produced by MySQLParser#insert_header.
    def enterInsert_header(self, ctx:MySQLParser.Insert_headerContext):
        pass

    # Exit a parse tree produced by MySQLParser#insert_header.
    def exitInsert_header(self, ctx:MySQLParser.Insert_headerContext):
        pass


    # Enter a parse tree produced by MySQLParser#insert_subfix.
    def enterInsert_subfix(self, ctx:MySQLParser.Insert_subfixContext):
        pass

    # Exit a parse tree produced by MySQLParser#insert_subfix.
    def exitInsert_subfix(self, ctx:MySQLParser.Insert_subfixContext):
        pass


    # Enter a parse tree produced by MySQLParser#insert_statement1.
    def enterInsert_statement1(self, ctx:MySQLParser.Insert_statement1Context):
        pass

    # Exit a parse tree produced by MySQLParser#insert_statement1.
    def exitInsert_statement1(self, ctx:MySQLParser.Insert_statement1Context):
        pass


    # Enter a parse tree produced by MySQLParser#value_list_clause.
    def enterValue_list_clause(self, ctx:MySQLParser.Value_list_clauseContext):
        pass

    # Exit a parse tree produced by MySQLParser#value_list_clause.
    def exitValue_list_clause(self, ctx:MySQLParser.Value_list_clauseContext):
        pass


    # Enter a parse tree produced by MySQLParser#column_value_list.
    def enterColumn_value_list(self, ctx:MySQLParser.Column_value_listContext):
        pass

    # Exit a parse tree produced by MySQLParser#column_value_list.
    def exitColumn_value_list(self, ctx:MySQLParser.Column_value_listContext):
        pass


    # Enter a parse tree produced by MySQLParser#insert_statement2.
    def enterInsert_statement2(self, ctx:MySQLParser.Insert_statement2Context):
        pass

    # Exit a parse tree produced by MySQLParser#insert_statement2.
    def exitInsert_statement2(self, ctx:MySQLParser.Insert_statement2Context):
        pass


    # Enter a parse tree produced by MySQLParser#set_columns_cluase.
    def enterSet_columns_cluase(self, ctx:MySQLParser.Set_columns_cluaseContext):
        pass

    # Exit a parse tree produced by MySQLParser#set_columns_cluase.
    def exitSet_columns_cluase(self, ctx:MySQLParser.Set_columns_cluaseContext):
        pass


    # Enter a parse tree produced by MySQLParser#set_column_cluase.
    def enterSet_column_cluase(self, ctx:MySQLParser.Set_column_cluaseContext):
        pass

    # Exit a parse tree produced by MySQLParser#set_column_cluase.
    def exitSet_column_cluase(self, ctx:MySQLParser.Set_column_cluaseContext):
        pass


    # Enter a parse tree produced by MySQLParser#insert_statement3.
    def enterInsert_statement3(self, ctx:MySQLParser.Insert_statement3Context):
        pass

    # Exit a parse tree produced by MySQLParser#insert_statement3.
    def exitInsert_statement3(self, ctx:MySQLParser.Insert_statement3Context):
        pass


    # Enter a parse tree produced by MySQLParser#update_statements.
    def enterUpdate_statements(self, ctx:MySQLParser.Update_statementsContext):
        pass

    # Exit a parse tree produced by MySQLParser#update_statements.
    def exitUpdate_statements(self, ctx:MySQLParser.Update_statementsContext):
        pass


    # Enter a parse tree produced by MySQLParser#single_table_update_statement.
    def enterSingle_table_update_statement(self, ctx:MySQLParser.Single_table_update_statementContext):
        pass

    # Exit a parse tree produced by MySQLParser#single_table_update_statement.
    def exitSingle_table_update_statement(self, ctx:MySQLParser.Single_table_update_statementContext):
        pass


    # Enter a parse tree produced by MySQLParser#multiple_table_update_statement.
    def enterMultiple_table_update_statement(self, ctx:MySQLParser.Multiple_table_update_statementContext):
        pass

    # Exit a parse tree produced by MySQLParser#multiple_table_update_statement.
    def exitMultiple_table_update_statement(self, ctx:MySQLParser.Multiple_table_update_statementContext):
        pass


