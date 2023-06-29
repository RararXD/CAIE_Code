
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'statementsleftPLUSMINUSleftMULDIVleftLESSGREATERLESS_EQUALGREATER_EQUALEQUALNOT_EQUALleftANDleftORleftNOTrightUMINUSrightUPLUSAND ARRAY ASSIGN BOOLEAN CALL CASE CHAR CLASS COLON COMMA CONNECT CONSTANT DECLARE DIV DOT ELSE ENDCASE ENDFUNCTION ENDIF ENDPROCEDURE ENDTYPE ENDWHILE EQUAL FOR FUNCTION GREATER GREATER_EQUAL ID IF INHERITS INPUT INTEGER LEFT_BRACE LEFT_PAREN LEFT_SQUARE LESS LESS_EQUAL MINUS MUL NEW NEXT NOT NOT_EQUAL OF OR OTHERWISE OUTPUT PLUS POINTER PRIVATE PROCEDURE PUBLIC REAL REPEAT RETURN RETURNS RIGHT_BRACE RIGHT_PAREN RIGHT_SQUARE SEMICOLON STRING THEN TO TYPE UNTIL WHILEstatements : statements statement\n            | statementstatement : DECLARE ID COLON IDstatement : CONSTANT ID EQUAL expressionstatement : DECLARE ID COLON ARRAY LEFT_SQUARE dimensions RIGHT_SQUARE OF IDdimensions : dimensions COMMA dimension\n        | dimensiondimension : expression COLON expressionstatement : ID ASSIGN expressionstatement : ID LEFT_SQUARE indexes RIGHT_SQUARE ASSIGN expressionindexes : indexes COMMA expression\n            | expressionstatement : INPUT IDstatement : INPUT ID LEFT_SQUARE indexes RIGHT_SQUAREstatement : OUTPUT output_expressionoutput_expression : output_expression COMMA expression\n            | expressionstatement : IF expression THEN statements ELSE statements ENDIF\n            | IF expression THEN statements ENDIFstatement : CASE OF ID cases ENDCASEcases : cases case\n            | casecase : case_expression COLON statements SEMICOLON\n            | otherwise_statement SEMICOLONcase_expression : expression TO expression\n            | expressionotherwise_statement : OTHERWISE COLON statementsstatement : FOR ID ASSIGN expression TO expression statements NEXT IDstatement : REPEAT statements UNTIL expressionstatement : WHILE expression statements ENDWHILEstatement : expressionexpression : IDexpression : ID LEFT_SQUARE indexes RIGHT_SQUAREexpression : expression OR expressionexpression : expression AND expressionexpression : NOT expressionexpression : expression EQUAL expressionexpression : expression NOT_EQUAL expressionexpression : expression LESS expressionexpression : expression GREATER expressionexpression : expression LESS_EQUAL expressionexpression : expression GREATER_EQUAL expressionexpression : expression MUL expressionexpression : expression DIV expressionexpression : MINUS expression %prec UMINUSexpression : PLUS expression %prec UPLUSexpression : expression PLUS expressionexpression : expression MINUS expressionexpression : expression CONNECT expressionexpression : LEFT_PAREN expression RIGHT_PARENexpression : BOOLEANexpression : CHARexpression : STRINGexpression : REALexpression : INTEGERdeclare_parameters : declare_parameters COMMA declare_parameter\n            | declare_parameterdeclare_parameter : ID COLON IDparameters : parameters COMMA expression\n            | expressionstatement : PROCEDURE ID LEFT_PAREN declare_parameters RIGHT_PAREN statements ENDPROCEDURE\n            | PROCEDURE ID statements ENDPROCEDUREstatement : CALL ID LEFT_PAREN parameters RIGHT_PAREN\n            | CALL IDstatement : FUNCTION ID LEFT_PAREN declare_parameters RIGHT_PAREN RETURNS ID statements ENDFUNCTION\n            | FUNCTION ID LEFT_PAREN declare_parameters RIGHT_PAREN RETURNS ARRAY statements ENDFUNCTION\n            | FUNCTION ID RETURNS ID statements ENDFUNCTION\n            | FUNCTION ID RETURNS ARRAY statements ENDFUNCTIONexpression : ID LEFT_PAREN parameters RIGHT_PAREN\n            | ID LEFT_PAREN RIGHT_PARENstatement : RETURN expression'
    
_lr_action_items = {'DECLARE':([0,1,2,4,6,12,22,23,24,25,26,27,46,47,48,49,53,54,55,57,59,60,61,62,64,68,71,72,73,74,75,76,77,78,79,80,81,82,83,87,91,95,96,100,102,104,106,108,110,118,119,120,121,125,129,130,135,136,137,138,139,141,144,147,149,151,152,156,157,158,160,161,163,166,167,171,173,174,175,176,181,182,183,184,185,186,],[3,3,-2,-32,-31,3,-51,-52,-53,-54,-55,-1,-13,-15,-17,-32,3,3,3,-64,-71,-36,-45,-46,-9,-70,-34,-35,-37,-38,-39,-40,-41,-42,-43,-44,-47,-48,-49,3,3,3,-50,-3,-33,-69,-4,-16,3,-29,-30,-46,-45,-62,3,3,-14,-33,3,-19,-20,3,3,3,-63,3,3,-10,3,3,3,3,3,-67,-68,-18,3,-61,3,3,3,3,-5,-28,-65,-66,]),'CONSTANT':([0,1,2,4,6,12,22,23,24,25,26,27,46,47,48,49,53,54,55,57,59,60,61,62,64,68,71,72,73,74,75,76,77,78,79,80,81,82,83,87,91,95,96,100,102,104,106,108,110,118,119,120,121,125,129,130,135,136,137,138,139,141,144,147,149,151,152,156,157,158,160,161,163,166,167,171,173,174,175,176,181,182,183,184,185,186,],[5,5,-2,-32,-31,5,-51,-52,-53,-54,-55,-1,-13,-15,-17,-32,5,5,5,-64,-71,-36,-45,-46,-9,-70,-34,-35,-37,-38,-39,-40,-41,-42,-43,-44,-47,-48,-49,5,5,5,-50,-3,-33,-69,-4,-16,5,-29,-30,-46,-45,-62,5,5,-14,-33,5,-19,-20,5,5,5,-63,5,5,-10,5,5,5,5,5,-67,-68,-18,5,-61,5,5,5,5,-5,-28,-65,-66,]),'ID':([0,1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,29,30,31,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,51,53,54,55,57,59,60,61,62,63,64,68,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,102,103,104,105,106,108,110,111,112,118,119,120,121,125,129,130,131,132,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,151,152,156,157,158,160,161,163,165,166,167,169,170,171,172,173,174,175,176,177,180,181,182,183,184,185,186,],[4,4,-2,28,-32,32,-31,46,49,49,52,4,49,55,49,57,58,49,49,49,49,-51,-52,-53,-54,-55,-1,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,-13,-15,-17,-32,88,4,4,4,-64,-71,-36,-45,-46,100,-9,-70,49,-34,-35,-37,-38,-39,-40,-41,-42,-43,-44,-47,-48,-49,49,49,49,4,49,49,49,4,49,49,122,4,-50,49,127,129,-3,-33,49,-69,49,-4,-16,4,49,-22,-29,-30,-46,-45,-62,4,4,49,49,-14,-33,4,-19,-20,-21,4,-24,49,4,49,162,4,127,-63,4,4,-10,4,4,4,4,4,175,-67,-68,49,49,-18,-23,4,-61,4,4,183,184,4,4,-5,-28,-65,-66,]),'INPUT':([0,1,2,4,6,12,22,23,24,25,26,27,46,47,48,49,53,54,55,57,59,60,61,62,64,68,71,72,73,74,75,76,77,78,79,80,81,82,83,87,91,95,96,100,102,104,106,108,110,118,119,120,121,125,129,130,135,136,137,138,139,141,144,147,149,151,152,156,157,158,160,161,163,166,167,171,173,174,175,176,181,182,183,184,185,186,],[7,7,-2,-32,-31,7,-51,-52,-53,-54,-55,-1,-13,-15,-17,-32,7,7,7,-64,-71,-36,-45,-46,-9,-70,-34,-35,-37,-38,-39,-40,-41,-42,-43,-44,-47,-48,-49,7,7,7,-50,-3,-33,-69,-4,-16,7,-29,-30,-46,-45,-62,7,7,-14,-33,7,-19,-20,7,7,7,-63,7,7,-10,7,7,7,7,7,-67,-68,-18,7,-61,7,7,7,7,-5,-28,-65,-66,]),'OUTPUT':([0,1,2,4,6,12,22,23,24,25,26,27,46,47,48,49,53,54,55,57,59,60,61,62,64,68,71,72,73,74,75,76,77,78,79,80,81,82,83,87,91,95,96,100,102,104,106,108,110,118,119,120,121,125,129,130,135,136,137,138,139,141,144,147,149,151,152,156,157,158,160,161,163,166,167,171,173,174,175,176,181,182,183,184,185,186,],[8,8,-2,-32,-31,8,-51,-52,-53,-54,-55,-1,-13,-15,-17,-32,8,8,8,-64,-71,-36,-45,-46,-9,-70,-34,-35,-37,-38,-39,-40,-41,-42,-43,-44,-47,-48,-49,8,8,8,-50,-3,-33,-69,-4,-16,8,-29,-30,-46,-45,-62,8,8,-14,-33,8,-19,-20,8,8,8,-63,8,8,-10,8,8,8,8,8,-67,-68,-18,8,-61,8,8,8,8,-5,-28,-65,-66,]),'IF':([0,1,2,4,6,12,22,23,24,25,26,27,46,47,48,49,53,54,55,57,59,60,61,62,64,68,71,72,73,74,75,76,77,78,79,80,81,82,83,87,91,95,96,100,102,104,106,108,110,118,119,120,121,125,129,130,135,136,137,138,139,141,144,147,149,151,152,156,157,158,160,161,163,166,167,171,173,174,175,176,181,182,183,184,185,186,],[9,9,-2,-32,-31,9,-51,-52,-53,-54,-55,-1,-13,-15,-17,-32,9,9,9,-64,-71,-36,-45,-46,-9,-70,-34,-35,-37,-38,-39,-40,-41,-42,-43,-44,-47,-48,-49,9,9,9,-50,-3,-33,-69,-4,-16,9,-29,-30,-46,-45,-62,9,9,-14,-33,9,-19,-20,9,9,9,-63,9,9,-10,9,9,9,9,9,-67,-68,-18,9,-61,9,9,9,9,-5,-28,-65,-66,]),'CASE':([0,1,2,4,6,12,22,23,24,25,26,27,46,47,48,49,53,54,55,57,59,60,61,62,64,68,71,72,73,74,75,76,77,78,79,80,81,82,83,87,91,95,96,100,102,104,106,108,110,118,119,120,121,125,129,130,135,136,137,138,139,141,144,147,149,151,152,156,157,158,160,161,163,166,167,171,173,174,175,176,181,182,183,184,185,186,],[10,10,-2,-32,-31,10,-51,-52,-53,-54,-55,-1,-13,-15,-17,-32,10,10,10,-64,-71,-36,-45,-46,-9,-70,-34,-35,-37,-38,-39,-40,-41,-42,-43,-44,-47,-48,-49,10,10,10,-50,-3,-33,-69,-4,-16,10,-29,-30,-46,-45,-62,10,10,-14,-33,10,-19,-20,10,10,10,-63,10,10,-10,10,10,10,10,10,-67,-68,-18,10,-61,10,10,10,10,-5,-28,-65,-66,]),'FOR':([0,1,2,4,6,12,22,23,24,25,26,27,46,47,48,49,53,54,55,57,59,60,61,62,64,68,71,72,73,74,75,76,77,78,79,80,81,82,83,87,91,95,96,100,102,104,106,108,110,118,119,120,121,125,129,130,135,136,137,138,139,141,144,147,149,151,152,156,157,158,160,161,163,166,167,171,173,174,175,176,181,182,183,184,185,186,],[11,11,-2,-32,-31,11,-51,-52,-53,-54,-55,-1,-13,-15,-17,-32,11,11,11,-64,-71,-36,-45,-46,-9,-70,-34,-35,-37,-38,-39,-40,-41,-42,-43,-44,-47,-48,-49,11,11,11,-50,-3,-33,-69,-4,-16,11,-29,-30,-46,-45,-62,11,11,-14,-33,11,-19,-20,11,11,11,-63,11,11,-10,11,11,11,11,11,-67,-68,-18,11,-61,11,11,11,11,-5,-28,-65,-66,]),'REPEAT':([0,1,2,4,6,12,22,23,24,25,26,27,46,47,48,49,53,54,55,57,59,60,61,62,64,68,71,72,73,74,75,76,77,78,79,80,81,82,83,87,91,95,96,100,102,104,106,108,110,118,119,120,121,125,129,130,135,136,137,138,139,141,144,147,149,151,152,156,157,158,160,161,163,166,167,171,173,174,175,176,181,182,183,184,185,186,],[12,12,-2,-32,-31,12,-51,-52,-53,-54,-55,-1,-13,-15,-17,-32,12,12,12,-64,-71,-36,-45,-46,-9,-70,-34,-35,-37,-38,-39,-40,-41,-42,-43,-44,-47,-48,-49,12,12,12,-50,-3,-33,-69,-4,-16,12,-29,-30,-46,-45,-62,12,12,-14,-33,12,-19,-20,12,12,12,-63,12,12,-10,12,12,12,12,12,-67,-68,-18,12,-61,12,12,12,12,-5,-28,-65,-66,]),'WHILE':([0,1,2,4,6,12,22,23,24,25,26,27,46,47,48,49,53,54,55,57,59,60,61,62,64,68,71,72,73,74,75,76,77,78,79,80,81,82,83,87,91,95,96,100,102,104,106,108,110,118,119,120,121,125,129,130,135,136,137,138,139,141,144,147,149,151,152,156,157,158,160,161,163,166,167,171,173,174,175,176,181,182,183,184,185,186,],[13,13,-2,-32,-31,13,-51,-52,-53,-54,-55,-1,-13,-15,-17,-32,13,13,13,-64,-71,-36,-45,-46,-9,-70,-34,-35,-37,-38,-39,-40,-41,-42,-43,-44,-47,-48,-49,13,13,13,-50,-3,-33,-69,-4,-16,13,-29,-30,-46,-45,-62,13,13,-14,-33,13,-19,-20,13,13,13,-63,13,13,-10,13,13,13,13,13,-67,-68,-18,13,-61,13,13,13,13,-5,-28,-65,-66,]),'PROCEDURE':([0,1,2,4,6,12,22,23,24,25,26,27,46,47,48,49,53,54,55,57,59,60,61,62,64,68,71,72,73,74,75,76,77,78,79,80,81,82,83,87,91,95,96,100,102,104,106,108,110,118,119,120,121,125,129,130,135,136,137,138,139,141,144,147,149,151,152,156,157,158,160,161,163,166,167,171,173,174,175,176,181,182,183,184,185,186,],[14,14,-2,-32,-31,14,-51,-52,-53,-54,-55,-1,-13,-15,-17,-32,14,14,14,-64,-71,-36,-45,-46,-9,-70,-34,-35,-37,-38,-39,-40,-41,-42,-43,-44,-47,-48,-49,14,14,14,-50,-3,-33,-69,-4,-16,14,-29,-30,-46,-45,-62,14,14,-14,-33,14,-19,-20,14,14,14,-63,14,14,-10,14,14,14,14,14,-67,-68,-18,14,-61,14,14,14,14,-5,-28,-65,-66,]),'CALL':([0,1,2,4,6,12,22,23,24,25,26,27,46,47,48,49,53,54,55,57,59,60,61,62,64,68,71,72,73,74,75,76,77,78,79,80,81,82,83,87,91,95,96,100,102,104,106,108,110,118,119,120,121,125,129,130,135,136,137,138,139,141,144,147,149,151,152,156,157,158,160,161,163,166,167,171,173,174,175,176,181,182,183,184,185,186,],[16,16,-2,-32,-31,16,-51,-52,-53,-54,-55,-1,-13,-15,-17,-32,16,16,16,-64,-71,-36,-45,-46,-9,-70,-34,-35,-37,-38,-39,-40,-41,-42,-43,-44,-47,-48,-49,16,16,16,-50,-3,-33,-69,-4,-16,16,-29,-30,-46,-45,-62,16,16,-14,-33,16,-19,-20,16,16,16,-63,16,16,-10,16,16,16,16,16,-67,-68,-18,16,-61,16,16,16,16,-5,-28,-65,-66,]),'FUNCTION':([0,1,2,4,6,12,22,23,24,25,26,27,46,47,48,49,53,54,55,57,59,60,61,62,64,68,71,72,73,74,75,76,77,78,79,80,81,82,83,87,91,95,96,100,102,104,106,108,110,118,119,120,121,125,129,130,135,136,137,138,139,141,144,147,149,151,152,156,157,158,160,161,163,166,167,171,173,174,175,176,181,182,183,184,185,186,],[17,17,-2,-32,-31,17,-51,-52,-53,-54,-55,-1,-13,-15,-17,-32,17,17,17,-64,-71,-36,-45,-46,-9,-70,-34,-35,-37,-38,-39,-40,-41,-42,-43,-44,-47,-48,-49,17,17,17,-50,-3,-33,-69,-4,-16,17,-29,-30,-46,-45,-62,17,17,-14,-33,17,-19,-20,17,17,17,-63,17,17,-10,17,17,17,17,17,-67,-68,-18,17,-61,17,17,17,17,-5,-28,-65,-66,]),'RETURN':([0,1,2,4,6,12,22,23,24,25,26,27,46,47,48,49,53,54,55,57,59,60,61,62,64,68,71,72,73,74,75,76,77,78,79,80,81,82,83,87,91,95,96,100,102,104,106,108,110,118,119,120,121,125,129,130,135,136,137,138,139,141,144,147,149,151,152,156,157,158,160,161,163,166,167,171,173,174,175,176,181,182,183,184,185,186,],[18,18,-2,-32,-31,18,-51,-52,-53,-54,-55,-1,-13,-15,-17,-32,18,18,18,-64,-71,-36,-45,-46,-9,-70,-34,-35,-37,-38,-39,-40,-41,-42,-43,-44,-47,-48,-49,18,18,18,-50,-3,-33,-69,-4,-16,18,-29,-30,-46,-45,-62,18,18,-14,-33,18,-19,-20,18,18,18,-63,18,18,-10,18,18,18,18,18,-67,-68,-18,18,-61,18,18,18,18,-5,-28,-65,-66,]),'NOT':([0,1,2,4,6,8,9,12,13,15,18,19,20,21,22,23,24,25,26,27,29,30,31,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,53,54,55,57,59,60,61,62,64,68,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,100,102,103,104,105,106,108,110,111,112,118,119,120,121,125,129,130,131,132,135,136,137,138,139,140,141,142,143,144,145,147,149,151,152,156,157,158,160,161,163,166,167,169,170,171,172,173,174,175,176,181,182,183,184,185,186,],[19,19,-2,-32,-31,19,19,19,19,19,19,19,19,19,-51,-52,-53,-54,-55,-1,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,-13,-15,-17,-32,19,19,19,-64,-71,-36,-45,-46,-9,-70,19,-34,-35,-37,-38,-39,-40,-41,-42,-43,-44,-47,-48,-49,19,19,19,19,19,19,19,19,19,19,19,19,-50,19,-3,-33,19,-69,19,-4,-16,19,19,-22,-29,-30,-46,-45,-62,19,19,19,19,-14,-33,19,-19,-20,-21,19,-24,19,19,19,19,-63,19,19,-10,19,19,19,19,19,-67,-68,19,19,-18,-23,19,-61,19,19,19,19,-5,-28,-65,-66,]),'MINUS':([0,1,2,4,6,8,9,12,13,15,18,19,20,21,22,23,24,25,26,27,29,30,31,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,53,54,55,56,57,59,60,61,62,64,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,100,102,103,104,105,106,108,110,111,112,115,117,118,119,120,121,122,125,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,147,149,151,152,155,156,157,158,159,160,161,163,166,167,169,170,171,172,173,174,175,176,179,181,182,183,184,185,186,],[20,20,-2,-32,44,20,20,20,20,20,20,20,20,20,-51,-52,-53,-54,-55,-1,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,-13,-15,44,-32,44,20,93,20,44,-64,44,-36,-45,-46,44,44,-70,44,20,-34,-35,-37,-38,-39,-40,-41,-42,-43,-44,-47,-48,44,20,20,20,20,20,20,20,20,20,20,20,20,-50,20,-3,-33,20,-69,20,-4,44,20,20,-22,44,44,44,-30,-46,-45,-32,-62,20,20,20,20,44,44,-14,-33,20,-19,-20,-21,20,-24,20,20,20,20,-63,20,20,44,44,20,20,44,20,93,20,-67,-68,20,20,-18,-23,20,-61,20,20,44,20,20,-5,-28,-65,-66,]),'PLUS':([0,1,2,4,6,8,9,12,13,15,18,19,20,21,22,23,24,25,26,27,29,30,31,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,53,54,55,56,57,59,60,61,62,64,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,100,102,103,104,105,106,108,110,111,112,115,117,118,119,120,121,122,125,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,147,149,151,152,155,156,157,158,159,160,161,163,166,167,169,170,171,172,173,174,175,176,179,181,182,183,184,185,186,],[21,21,-2,-32,43,21,21,21,21,21,21,21,21,21,-51,-52,-53,-54,-55,-1,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,-13,-15,43,-32,43,21,92,21,43,-64,43,-36,-45,-46,43,43,-70,43,21,-34,-35,-37,-38,-39,-40,-41,-42,-43,-44,-47,-48,43,21,21,21,21,21,21,21,21,21,21,21,21,-50,21,-3,-33,21,-69,21,-4,43,21,21,-22,43,43,43,-30,-46,-45,-32,-62,21,21,21,21,43,43,-14,-33,21,-19,-20,-21,21,-24,21,21,21,21,-63,21,21,43,43,21,21,43,21,92,21,-67,-68,21,21,-18,-23,21,-61,21,21,43,21,21,-5,-28,-65,-66,]),'LEFT_PAREN':([0,1,2,4,6,8,9,12,13,15,18,19,20,21,22,23,24,25,26,27,29,30,31,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,53,54,55,57,58,59,60,61,62,64,68,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,100,102,103,104,105,106,108,110,111,112,118,119,120,121,122,125,129,130,131,132,135,136,137,138,139,140,141,142,143,144,145,147,149,151,152,156,157,158,160,161,163,166,167,169,170,171,172,173,174,175,176,181,182,183,184,185,186,],[15,15,-2,31,-31,15,15,15,15,15,15,15,15,15,-51,-52,-53,-54,-55,-1,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,-13,-15,-17,31,15,15,94,97,98,-71,-36,-45,-46,-9,-70,15,-34,-35,-37,-38,-39,-40,-41,-42,-43,-44,-47,-48,-49,15,15,15,15,15,15,15,15,15,15,15,15,-50,15,-3,-33,15,-69,15,-4,-16,15,15,-22,-29,-30,-46,-45,31,-62,15,15,15,15,-14,-33,15,-19,-20,-21,15,-24,15,15,15,15,-63,15,15,-10,15,15,15,15,15,-67,-68,15,15,-18,-23,15,-61,15,15,15,15,-5,-28,-65,-66,]),'BOOLEAN':([0,1,2,4,6,8,9,12,13,15,18,19,20,21,22,23,24,25,26,27,29,30,31,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,53,54,55,57,59,60,61,62,64,68,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,100,102,103,104,105,106,108,110,111,112,118,119,120,121,125,129,130,131,132,135,136,137,138,139,140,141,142,143,144,145,147,149,151,152,156,157,158,160,161,163,166,167,169,170,171,172,173,174,175,176,181,182,183,184,185,186,],[22,22,-2,-32,-31,22,22,22,22,22,22,22,22,22,-51,-52,-53,-54,-55,-1,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,-13,-15,-17,-32,22,22,22,-64,-71,-36,-45,-46,-9,-70,22,-34,-35,-37,-38,-39,-40,-41,-42,-43,-44,-47,-48,-49,22,22,22,22,22,22,22,22,22,22,22,22,-50,22,-3,-33,22,-69,22,-4,-16,22,22,-22,-29,-30,-46,-45,-62,22,22,22,22,-14,-33,22,-19,-20,-21,22,-24,22,22,22,22,-63,22,22,-10,22,22,22,22,22,-67,-68,22,22,-18,-23,22,-61,22,22,22,22,-5,-28,-65,-66,]),'CHAR':([0,1,2,4,6,8,9,12,13,15,18,19,20,21,22,23,24,25,26,27,29,30,31,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,53,54,55,57,59,60,61,62,64,68,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,100,102,103,104,105,106,108,110,111,112,118,119,120,121,125,129,130,131,132,135,136,137,138,139,140,141,142,143,144,145,147,149,151,152,156,157,158,160,161,163,166,167,169,170,171,172,173,174,175,176,181,182,183,184,185,186,],[23,23,-2,-32,-31,23,23,23,23,23,23,23,23,23,-51,-52,-53,-54,-55,-1,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,-13,-15,-17,-32,23,23,23,-64,-71,-36,-45,-46,-9,-70,23,-34,-35,-37,-38,-39,-40,-41,-42,-43,-44,-47,-48,-49,23,23,23,23,23,23,23,23,23,23,23,23,-50,23,-3,-33,23,-69,23,-4,-16,23,23,-22,-29,-30,-46,-45,-62,23,23,23,23,-14,-33,23,-19,-20,-21,23,-24,23,23,23,23,-63,23,23,-10,23,23,23,23,23,-67,-68,23,23,-18,-23,23,-61,23,23,23,23,-5,-28,-65,-66,]),'STRING':([0,1,2,4,6,8,9,12,13,15,18,19,20,21,22,23,24,25,26,27,29,30,31,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,53,54,55,57,59,60,61,62,64,68,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,100,102,103,104,105,106,108,110,111,112,118,119,120,121,125,129,130,131,132,135,136,137,138,139,140,141,142,143,144,145,147,149,151,152,156,157,158,160,161,163,166,167,169,170,171,172,173,174,175,176,181,182,183,184,185,186,],[24,24,-2,-32,-31,24,24,24,24,24,24,24,24,24,-51,-52,-53,-54,-55,-1,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,-13,-15,-17,-32,24,24,24,-64,-71,-36,-45,-46,-9,-70,24,-34,-35,-37,-38,-39,-40,-41,-42,-43,-44,-47,-48,-49,24,24,24,24,24,24,24,24,24,24,24,24,-50,24,-3,-33,24,-69,24,-4,-16,24,24,-22,-29,-30,-46,-45,-62,24,24,24,24,-14,-33,24,-19,-20,-21,24,-24,24,24,24,24,-63,24,24,-10,24,24,24,24,24,-67,-68,24,24,-18,-23,24,-61,24,24,24,24,-5,-28,-65,-66,]),'REAL':([0,1,2,4,6,8,9,12,13,15,18,19,20,21,22,23,24,25,26,27,29,30,31,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,53,54,55,57,59,60,61,62,64,68,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,100,102,103,104,105,106,108,110,111,112,118,119,120,121,125,129,130,131,132,135,136,137,138,139,140,141,142,143,144,145,147,149,151,152,156,157,158,160,161,163,166,167,169,170,171,172,173,174,175,176,181,182,183,184,185,186,],[25,25,-2,-32,-31,25,25,25,25,25,25,25,25,25,-51,-52,-53,-54,-55,-1,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,-13,-15,-17,-32,25,25,25,-64,-71,-36,-45,-46,-9,-70,25,-34,-35,-37,-38,-39,-40,-41,-42,-43,-44,-47,-48,-49,25,25,25,25,25,25,25,25,25,25,25,25,-50,25,-3,-33,25,-69,25,-4,-16,25,25,-22,-29,-30,-46,-45,-62,25,25,25,25,-14,-33,25,-19,-20,-21,25,-24,25,25,25,25,-63,25,25,-10,25,25,25,25,25,-67,-68,25,25,-18,-23,25,-61,25,25,25,25,-5,-28,-65,-66,]),'INTEGER':([0,1,2,4,6,8,9,12,13,15,18,19,20,21,22,23,24,25,26,27,29,30,31,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,53,54,55,57,59,60,61,62,64,68,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,100,102,103,104,105,106,108,110,111,112,118,119,120,121,125,129,130,131,132,135,136,137,138,139,140,141,142,143,144,145,147,149,151,152,156,157,158,160,161,163,166,167,169,170,171,172,173,174,175,176,181,182,183,184,185,186,],[26,26,-2,-32,-31,26,26,26,26,26,26,26,26,26,-51,-52,-53,-54,-55,-1,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,-13,-15,-17,-32,26,26,26,-64,-71,-36,-45,-46,-9,-70,26,-34,-35,-37,-38,-39,-40,-41,-42,-43,-44,-47,-48,-49,26,26,26,26,26,26,26,26,26,26,26,26,-50,26,-3,-33,26,-69,26,-4,-16,26,26,-22,-29,-30,-46,-45,-62,26,26,26,26,-14,-33,26,-19,-20,-21,26,-24,26,26,26,26,-63,26,26,-10,26,26,26,26,26,-67,-68,26,26,-18,-23,26,-61,26,26,26,26,-5,-28,-65,-66,]),'$end':([1,2,4,6,22,23,24,25,26,27,46,47,48,49,57,59,60,61,62,64,68,71,72,73,74,75,76,77,78,79,80,81,82,83,96,100,102,104,106,108,118,119,125,135,136,138,139,149,156,166,167,171,174,183,184,185,186,],[0,-2,-32,-31,-51,-52,-53,-54,-55,-1,-13,-15,-17,-32,-64,-71,-36,-45,-46,-9,-70,-34,-35,-37,-38,-39,-40,-41,-42,-43,-44,-47,-48,-49,-50,-3,-33,-69,-4,-16,-29,-30,-62,-14,-33,-19,-20,-63,-10,-67,-68,-18,-61,-5,-28,-65,-66,]),'UNTIL':([2,4,6,22,23,24,25,26,27,46,47,48,49,53,57,59,60,61,62,64,68,71,72,73,74,75,76,77,78,79,80,81,82,83,96,100,102,104,106,108,118,119,125,135,136,138,139,149,156,166,167,171,174,183,184,185,186,],[-2,-32,-31,-51,-52,-53,-54,-55,-1,-13,-15,-17,-32,90,-64,-71,-36,-45,-46,-9,-70,-34,-35,-37,-38,-39,-40,-41,-42,-43,-44,-47,-48,-49,-50,-3,-33,-69,-4,-16,-29,-30,-62,-14,-33,-19,-20,-63,-10,-67,-68,-18,-61,-5,-28,-65,-66,]),'ENDWHILE':([2,4,6,22,23,24,25,26,27,46,47,48,49,57,59,60,61,62,64,68,71,72,73,74,75,76,77,78,79,80,81,82,83,91,96,100,102,104,106,108,118,119,120,121,125,135,136,138,139,149,156,166,167,171,174,183,184,185,186,],[-2,-32,-31,-51,-52,-53,-54,-55,-1,-13,-15,-17,-32,-64,-71,-36,-45,-46,-9,-70,-34,-35,-37,-38,-39,-40,-41,-42,-43,-44,-47,-48,-49,119,-50,-3,-33,-69,-4,-16,-29,-30,-46,-45,-62,-14,-33,-19,-20,-63,-10,-67,-68,-18,-61,-5,-28,-65,-66,]),'ENDPROCEDURE':([2,4,6,22,23,24,25,26,27,46,47,48,49,57,59,60,61,62,64,68,71,72,73,74,75,76,77,78,79,80,81,82,83,95,96,100,102,104,106,108,118,119,125,135,136,138,139,149,156,163,166,167,171,174,183,184,185,186,],[-2,-32,-31,-51,-52,-53,-54,-55,-1,-13,-15,-17,-32,-64,-71,-36,-45,-46,-9,-70,-34,-35,-37,-38,-39,-40,-41,-42,-43,-44,-47,-48,-49,125,-50,-3,-33,-69,-4,-16,-29,-30,-62,-14,-33,-19,-20,-63,-10,174,-67,-68,-18,-61,-5,-28,-65,-66,]),'ELSE':([2,4,6,22,23,24,25,26,27,46,47,48,49,57,59,60,61,62,64,68,71,72,73,74,75,76,77,78,79,80,81,82,83,96,100,102,104,106,108,110,118,119,125,135,136,138,139,149,156,166,167,171,174,183,184,185,186,],[-2,-32,-31,-51,-52,-53,-54,-55,-1,-13,-15,-17,-32,-64,-71,-36,-45,-46,-9,-70,-34,-35,-37,-38,-39,-40,-41,-42,-43,-44,-47,-48,-49,-50,-3,-33,-69,-4,-16,137,-29,-30,-62,-14,-33,-19,-20,-63,-10,-67,-68,-18,-61,-5,-28,-65,-66,]),'ENDIF':([2,4,6,22,23,24,25,26,27,46,47,48,49,57,59,60,61,62,64,68,71,72,73,74,75,76,77,78,79,80,81,82,83,96,100,102,104,106,108,110,118,119,125,135,136,138,139,149,156,157,166,167,171,174,183,184,185,186,],[-2,-32,-31,-51,-52,-53,-54,-55,-1,-13,-15,-17,-32,-64,-71,-36,-45,-46,-9,-70,-34,-35,-37,-38,-39,-40,-41,-42,-43,-44,-47,-48,-49,-50,-3,-33,-69,-4,-16,138,-29,-30,-62,-14,-33,-19,-20,-63,-10,171,-67,-68,-18,-61,-5,-28,-65,-66,]),'ENDFUNCTION':([2,4,6,22,23,24,25,26,27,46,47,48,49,57,59,60,61,62,64,68,71,72,73,74,75,76,77,78,79,80,81,82,83,96,100,102,104,106,108,118,119,125,135,136,138,139,149,151,152,156,166,167,171,174,181,182,183,184,185,186,],[-2,-32,-31,-51,-52,-53,-54,-55,-1,-13,-15,-17,-32,-64,-71,-36,-45,-46,-9,-70,-34,-35,-37,-38,-39,-40,-41,-42,-43,-44,-47,-48,-49,-50,-3,-33,-69,-4,-16,-29,-30,-62,-14,-33,-19,-20,-63,166,167,-10,-67,-68,-18,-61,185,186,-5,-28,-65,-66,]),'SEMICOLON':([2,4,6,22,23,24,25,26,27,46,47,48,49,57,59,60,61,62,64,68,71,72,73,74,75,76,77,78,79,80,81,82,83,96,100,102,104,106,108,114,118,119,125,135,136,138,139,149,156,158,160,166,167,171,174,183,184,185,186,],[-2,-32,-31,-51,-52,-53,-54,-55,-1,-13,-15,-17,-32,-64,-71,-36,-45,-46,-9,-70,-34,-35,-37,-38,-39,-40,-41,-42,-43,-44,-47,-48,-49,-50,-3,-33,-69,-4,-16,142,-29,-30,-62,-14,-33,-19,-20,-63,-10,172,-27,-67,-68,-18,-61,-5,-28,-65,-66,]),'NEXT':([2,4,6,22,23,24,25,26,27,46,47,48,49,57,59,60,61,62,64,68,71,72,73,74,75,76,77,78,79,80,81,82,83,96,100,102,104,106,108,118,119,120,121,125,135,136,138,139,149,156,166,167,171,173,174,183,184,185,186,],[-2,-32,-31,-51,-52,-53,-54,-55,-1,-13,-15,-17,-32,-64,-71,-36,-45,-46,-9,-70,-34,-35,-37,-38,-39,-40,-41,-42,-43,-44,-47,-48,-49,-50,-3,-33,-69,-4,-16,-29,-30,-46,-45,-62,-14,-33,-19,-20,-63,-10,-67,-68,-18,180,-61,-5,-28,-65,-66,]),'ASSIGN':([4,52,102,],[29,89,132,]),'LEFT_SQUARE':([4,46,49,101,122,],[30,84,86,131,86,]),'OR':([4,6,22,23,24,25,26,48,49,50,54,56,59,60,61,62,64,66,68,69,71,72,73,74,75,76,77,78,79,80,81,82,83,96,102,104,106,108,115,117,118,120,121,122,133,134,136,155,156,159,161,179,],[-32,33,-51,-52,-53,-54,-55,33,-32,33,33,33,33,-36,-45,-46,33,33,-70,33,-34,33,33,33,33,33,33,33,33,33,33,33,33,-50,-33,-69,33,33,33,33,33,-46,-45,-32,33,33,-33,33,33,33,33,33,]),'AND':([4,6,22,23,24,25,26,48,49,50,54,56,59,60,61,62,64,66,68,69,71,72,73,74,75,76,77,78,79,80,81,82,83,96,102,104,106,108,115,117,118,120,121,122,133,134,136,155,156,159,161,179,],[-32,34,-51,-52,-53,-54,-55,34,-32,34,34,34,34,-36,-45,-46,34,34,-70,34,-34,-35,34,34,34,34,34,34,34,34,34,34,34,-50,-33,-69,34,34,34,34,34,-46,-45,-32,34,34,-33,34,34,34,34,34,]),'EQUAL':([4,6,22,23,24,25,26,32,48,49,50,54,56,59,60,61,62,64,66,68,69,71,72,73,74,75,76,77,78,79,80,81,82,83,96,102,104,106,108,115,117,118,120,121,122,133,134,136,155,156,159,161,179,],[-32,35,-51,-52,-53,-54,-55,70,35,-32,35,35,35,35,-36,-45,-46,35,35,-70,35,-34,-35,-37,-38,-39,-40,-41,-42,35,35,35,35,35,-50,-33,-69,35,35,35,35,35,-46,-45,-32,35,35,-33,35,35,35,35,35,]),'NOT_EQUAL':([4,6,22,23,24,25,26,48,49,50,54,56,59,60,61,62,64,66,68,69,71,72,73,74,75,76,77,78,79,80,81,82,83,96,102,104,106,108,115,117,118,120,121,122,133,134,136,155,156,159,161,179,],[-32,36,-51,-52,-53,-54,-55,36,-32,36,36,36,36,-36,-45,-46,36,36,-70,36,-34,-35,-37,-38,-39,-40,-41,-42,36,36,36,36,36,-50,-33,-69,36,36,36,36,36,-46,-45,-32,36,36,-33,36,36,36,36,36,]),'LESS':([4,6,22,23,24,25,26,48,49,50,54,56,59,60,61,62,64,66,68,69,71,72,73,74,75,76,77,78,79,80,81,82,83,96,102,104,106,108,115,117,118,120,121,122,133,134,136,155,156,159,161,179,],[-32,37,-51,-52,-53,-54,-55,37,-32,37,37,37,37,-36,-45,-46,37,37,-70,37,-34,-35,-37,-38,-39,-40,-41,-42,37,37,37,37,37,-50,-33,-69,37,37,37,37,37,-46,-45,-32,37,37,-33,37,37,37,37,37,]),'GREATER':([4,6,22,23,24,25,26,48,49,50,54,56,59,60,61,62,64,66,68,69,71,72,73,74,75,76,77,78,79,80,81,82,83,96,102,104,106,108,115,117,118,120,121,122,133,134,136,155,156,159,161,179,],[-32,38,-51,-52,-53,-54,-55,38,-32,38,38,38,38,-36,-45,-46,38,38,-70,38,-34,-35,-37,-38,-39,-40,-41,-42,38,38,38,38,38,-50,-33,-69,38,38,38,38,38,-46,-45,-32,38,38,-33,38,38,38,38,38,]),'LESS_EQUAL':([4,6,22,23,24,25,26,48,49,50,54,56,59,60,61,62,64,66,68,69,71,72,73,74,75,76,77,78,79,80,81,82,83,96,102,104,106,108,115,117,118,120,121,122,133,134,136,155,156,159,161,179,],[-32,39,-51,-52,-53,-54,-55,39,-32,39,39,39,39,-36,-45,-46,39,39,-70,39,-34,-35,-37,-38,-39,-40,-41,-42,39,39,39,39,39,-50,-33,-69,39,39,39,39,39,-46,-45,-32,39,39,-33,39,39,39,39,39,]),'GREATER_EQUAL':([4,6,22,23,24,25,26,48,49,50,54,56,59,60,61,62,64,66,68,69,71,72,73,74,75,76,77,78,79,80,81,82,83,96,102,104,106,108,115,117,118,120,121,122,133,134,136,155,156,159,161,179,],[-32,40,-51,-52,-53,-54,-55,40,-32,40,40,40,40,-36,-45,-46,40,40,-70,40,-34,-35,-37,-38,-39,-40,-41,-42,40,40,40,40,40,-50,-33,-69,40,40,40,40,40,-46,-45,-32,40,40,-33,40,40,40,40,40,]),'MUL':([4,6,22,23,24,25,26,48,49,50,54,56,59,60,61,62,64,66,68,69,71,72,73,74,75,76,77,78,79,80,81,82,83,96,102,104,106,108,115,117,118,120,121,122,133,134,136,155,156,159,161,179,],[-32,41,-51,-52,-53,-54,-55,41,-32,41,41,41,41,-36,-45,-46,41,41,-70,41,-34,-35,-37,-38,-39,-40,-41,-42,-43,-44,41,41,41,-50,-33,-69,41,41,41,41,41,-46,-45,-32,41,41,-33,41,41,41,41,41,]),'DIV':([4,6,22,23,24,25,26,48,49,50,54,56,59,60,61,62,64,66,68,69,71,72,73,74,75,76,77,78,79,80,81,82,83,96,102,104,106,108,115,117,118,120,121,122,133,134,136,155,156,159,161,179,],[-32,42,-51,-52,-53,-54,-55,42,-32,42,42,42,42,-36,-45,-46,42,42,-70,42,-34,-35,-37,-38,-39,-40,-41,-42,-43,-44,42,42,42,-50,-33,-69,42,42,42,42,42,-46,-45,-32,42,42,-33,42,42,42,42,42,]),'CONNECT':([4,6,22,23,24,25,26,48,49,50,54,56,59,60,61,62,64,66,68,69,71,72,73,74,75,76,77,78,79,80,81,82,83,96,102,104,106,108,115,117,118,120,121,122,133,134,136,155,156,159,161,179,],[-32,45,-51,-52,-53,-54,-55,45,-32,45,45,45,45,-36,-45,-46,45,45,-70,45,-34,-35,-37,-38,-39,-40,-41,-42,-43,-44,-47,-48,45,-50,-33,-69,45,45,45,45,45,-46,-45,-32,45,45,-33,45,45,45,45,45,]),'OF':([10,168,],[51,177,]),'COMMA':([22,23,24,25,26,47,48,49,60,61,62,65,66,67,68,69,71,72,73,74,75,76,77,78,79,80,81,82,83,96,104,107,108,109,123,124,126,128,133,134,136,153,154,162,164,178,179,],[-51,-52,-53,-54,-55,85,-17,-32,-36,-45,-46,103,-12,105,-70,-60,-34,-35,-37,-38,-39,-40,-41,-42,-43,-44,-47,-48,-49,-50,-69,103,-16,103,148,-57,105,148,-11,-59,-33,169,-7,-58,-56,-6,-8,]),'THEN':([22,23,24,25,26,49,50,60,61,62,68,71,72,73,74,75,76,77,78,79,80,81,82,83,96,104,136,],[-51,-52,-53,-54,-55,-32,87,-36,-45,-46,-70,-34,-35,-37,-38,-39,-40,-41,-42,-43,-44,-47,-48,-49,-50,-69,-33,]),'RIGHT_PAREN':([22,23,24,25,26,31,49,56,60,61,62,67,68,69,71,72,73,74,75,76,77,78,79,80,81,82,83,96,104,122,123,124,126,128,134,136,162,164,],[-51,-52,-53,-54,-55,68,-32,96,-36,-45,-46,104,-70,-60,-34,-35,-37,-38,-39,-40,-41,-42,-43,-44,-47,-48,-49,-50,-69,-32,147,-57,149,150,-59,-33,-58,-56,]),'RIGHT_SQUARE':([22,23,24,25,26,49,60,61,62,65,66,68,71,72,73,74,75,76,77,78,79,80,81,82,83,96,104,107,109,133,136,153,154,178,179,],[-51,-52,-53,-54,-55,-32,-36,-45,-46,102,-12,-70,-34,-35,-37,-38,-39,-40,-41,-42,-43,-44,-47,-48,-49,-50,-69,135,136,-11,-33,168,-7,-6,-8,]),'TO':([22,23,24,25,26,49,60,61,62,68,71,72,73,74,75,76,77,78,79,80,81,82,83,96,104,115,117,136,],[-51,-52,-53,-54,-55,-32,-36,-45,-46,-70,-34,-35,-37,-38,-39,-40,-41,-42,-43,-44,-47,-48,-49,-50,-69,143,145,-33,]),'COLON':([22,23,24,25,26,28,49,60,61,62,68,71,72,73,74,75,76,77,78,79,80,81,82,83,96,104,113,115,116,122,127,136,155,159,],[-51,-52,-53,-54,-55,63,-32,-36,-45,-46,-70,-34,-35,-37,-38,-39,-40,-41,-42,-43,-44,-47,-48,-49,-50,-69,141,-26,144,146,146,-33,170,-25,]),'RETURNS':([58,150,],[99,165,]),'ARRAY':([63,99,165,],[101,130,176,]),'OTHERWISE':([88,111,112,140,142,172,],[116,116,-22,-21,-24,-23,]),'ENDCASE':([111,112,140,142,172,],[139,-22,-21,-24,-23,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statements':([0,12,54,55,87,129,130,137,141,144,147,161,175,176,],[1,53,91,95,110,151,152,157,158,160,163,173,181,182,]),'statement':([0,1,12,53,54,55,87,91,95,110,129,130,137,141,144,147,151,152,157,158,160,161,163,173,175,176,181,182,],[2,27,2,27,2,2,2,27,27,27,2,2,2,2,2,2,27,27,27,27,27,2,27,27,2,2,27,27,]),'expression':([0,1,8,9,12,13,15,18,19,20,21,29,30,31,33,34,35,36,37,38,39,40,41,42,43,44,45,53,54,55,70,84,85,86,87,88,89,90,91,92,93,94,95,97,103,105,110,111,129,130,131,132,137,141,143,144,145,147,151,152,157,158,160,161,163,169,170,173,175,176,181,182,],[6,6,48,50,6,54,56,59,60,61,62,64,66,69,71,72,73,74,75,76,77,78,79,80,81,82,83,6,6,6,106,66,108,66,6,115,117,118,6,120,121,56,6,69,133,134,6,115,6,6,155,156,6,6,159,6,161,6,6,6,6,6,6,6,6,155,179,6,6,6,6,6,]),'output_expression':([8,],[47,]),'indexes':([30,84,86,],[65,107,109,]),'parameters':([31,97,],[67,126,]),'cases':([88,],[111,]),'case':([88,111,],[112,140,]),'case_expression':([88,111,],[113,113,]),'otherwise_statement':([88,111,],[114,114,]),'declare_parameters':([94,98,],[123,128,]),'declare_parameter':([94,98,148,],[124,124,164,]),'dimensions':([131,],[153,]),'dimension':([131,169,],[154,178,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statements","S'",1,None,None,None),
  ('statements -> statements statement','statements',2,'p_statements','parse.py',31),
  ('statements -> statement','statements',1,'p_statements','parse.py',32),
  ('statement -> DECLARE ID COLON ID','statement',4,'p_declare_statement','parse.py',41),
  ('statement -> CONSTANT ID EQUAL expression','statement',4,'p_const_declare_statement','parse.py',45),
  ('statement -> DECLARE ID COLON ARRAY LEFT_SQUARE dimensions RIGHT_SQUARE OF ID','statement',9,'p_array_declare_statement','parse.py',49),
  ('dimensions -> dimensions COMMA dimension','dimensions',3,'p_dimensions_expression','parse.py',53),
  ('dimensions -> dimension','dimensions',1,'p_dimensions_expression','parse.py',54),
  ('dimension -> expression COLON expression','dimension',3,'p_dimension_expression','parse.py',63),
  ('statement -> ID ASSIGN expression','statement',3,'p_assign_statement','parse.py',67),
  ('statement -> ID LEFT_SQUARE indexes RIGHT_SQUARE ASSIGN expression','statement',6,'p_array_assign_statement','parse.py',71),
  ('indexes -> indexes COMMA expression','indexes',3,'p_indexes','parse.py',75),
  ('indexes -> expression','indexes',1,'p_indexes','parse.py',76),
  ('statement -> INPUT ID','statement',2,'p_input_statement','parse.py',85),
  ('statement -> INPUT ID LEFT_SQUARE indexes RIGHT_SQUARE','statement',5,'p_array_input','parse.py',89),
  ('statement -> OUTPUT output_expression','statement',2,'p_output_statement','parse.py',93),
  ('output_expression -> output_expression COMMA expression','output_expression',3,'p_output_expression','parse.py',97),
  ('output_expression -> expression','output_expression',1,'p_output_expression','parse.py',98),
  ('statement -> IF expression THEN statements ELSE statements ENDIF','statement',7,'p_if_statement','parse.py',107),
  ('statement -> IF expression THEN statements ENDIF','statement',5,'p_if_statement','parse.py',108),
  ('statement -> CASE OF ID cases ENDCASE','statement',5,'p_case_statement','parse.py',115),
  ('cases -> cases case','cases',2,'p_cases','parse.py',119),
  ('cases -> case','cases',1,'p_cases','parse.py',120),
  ('case -> case_expression COLON statements SEMICOLON','case',4,'p_case','parse.py',129),
  ('case -> otherwise_statement SEMICOLON','case',2,'p_case','parse.py',130),
  ('case_expression -> expression TO expression','case_expression',3,'p_case_expression','parse.py',137),
  ('case_expression -> expression','case_expression',1,'p_case_expression','parse.py',138),
  ('otherwise_statement -> OTHERWISE COLON statements','otherwise_statement',3,'p_otherwise_statement','parse.py',145),
  ('statement -> FOR ID ASSIGN expression TO expression statements NEXT ID','statement',9,'p_for_statement','parse.py',149),
  ('statement -> REPEAT statements UNTIL expression','statement',4,'p_repeat_statement','parse.py',153),
  ('statement -> WHILE expression statements ENDWHILE','statement',4,'p_while_statement','parse.py',157),
  ('statement -> expression','statement',1,'p_expression_statement','parse.py',161),
  ('expression -> ID','expression',1,'p_id_expression','parse.py',165),
  ('expression -> ID LEFT_SQUARE indexes RIGHT_SQUARE','expression',4,'p_array_id_expression','parse.py',169),
  ('expression -> expression OR expression','expression',3,'p_or_expression','parse.py',173),
  ('expression -> expression AND expression','expression',3,'p_and_expression','parse.py',177),
  ('expression -> NOT expression','expression',2,'p_not_expression','parse.py',181),
  ('expression -> expression EQUAL expression','expression',3,'p_equal_expression','parse.py',185),
  ('expression -> expression NOT_EQUAL expression','expression',3,'p_not_equal_expression','parse.py',189),
  ('expression -> expression LESS expression','expression',3,'p_less_expression','parse.py',193),
  ('expression -> expression GREATER expression','expression',3,'p_greater_expression','parse.py',197),
  ('expression -> expression LESS_EQUAL expression','expression',3,'p_less_equal_expression','parse.py',201),
  ('expression -> expression GREATER_EQUAL expression','expression',3,'p_greater_equal_expression','parse.py',205),
  ('expression -> expression MUL expression','expression',3,'p_mul_expression','parse.py',209),
  ('expression -> expression DIV expression','expression',3,'p_div_expression','parse.py',213),
  ('expression -> MINUS expression','expression',2,'p_uminus_expression','parse.py',217),
  ('expression -> PLUS expression','expression',2,'p_uplus_expression','parse.py',221),
  ('expression -> expression PLUS expression','expression',3,'p_plus_expression','parse.py',225),
  ('expression -> expression MINUS expression','expression',3,'p_minus_expression','parse.py',229),
  ('expression -> expression CONNECT expression','expression',3,'p_connect_expression','parse.py',233),
  ('expression -> LEFT_PAREN expression RIGHT_PAREN','expression',3,'p_paren_expression','parse.py',238),
  ('expression -> BOOLEAN','expression',1,'p_boolean_expression','parse.py',243),
  ('expression -> CHAR','expression',1,'p_char_expression','parse.py',247),
  ('expression -> STRING','expression',1,'p_string_expression','parse.py',251),
  ('expression -> REAL','expression',1,'p_real_expression','parse.py',255),
  ('expression -> INTEGER','expression',1,'p_int_expression','parse.py',259),
  ('declare_parameters -> declare_parameters COMMA declare_parameter','declare_parameters',3,'p_declare_parameters','parse.py',265),
  ('declare_parameters -> declare_parameter','declare_parameters',1,'p_declare_parameters','parse.py',266),
  ('declare_parameter -> ID COLON ID','declare_parameter',3,'p_declare_parameter','parse.py',275),
  ('parameters -> parameters COMMA expression','parameters',3,'p_parameters','parse.py',279),
  ('parameters -> expression','parameters',1,'p_parameters','parse.py',280),
  ('statement -> PROCEDURE ID LEFT_PAREN declare_parameters RIGHT_PAREN statements ENDPROCEDURE','statement',7,'p_procedure_statement','parse.py',289),
  ('statement -> PROCEDURE ID statements ENDPROCEDURE','statement',4,'p_procedure_statement','parse.py',290),
  ('statement -> CALL ID LEFT_PAREN parameters RIGHT_PAREN','statement',5,'p_call_procedure_statement','parse.py',297),
  ('statement -> CALL ID','statement',2,'p_call_procedure_statement','parse.py',298),
  ('statement -> FUNCTION ID LEFT_PAREN declare_parameters RIGHT_PAREN RETURNS ID statements ENDFUNCTION','statement',9,'p_function_statement','parse.py',305),
  ('statement -> FUNCTION ID LEFT_PAREN declare_parameters RIGHT_PAREN RETURNS ARRAY statements ENDFUNCTION','statement',9,'p_function_statement','parse.py',306),
  ('statement -> FUNCTION ID RETURNS ID statements ENDFUNCTION','statement',6,'p_function_statement','parse.py',307),
  ('statement -> FUNCTION ID RETURNS ARRAY statements ENDFUNCTION','statement',6,'p_function_statement','parse.py',308),
  ('expression -> ID LEFT_PAREN parameters RIGHT_PAREN','expression',4,'p_call_function_expression','parse.py',315),
  ('expression -> ID LEFT_PAREN RIGHT_PAREN','expression',3,'p_call_function_expression','parse.py',316),
  ('statement -> RETURN expression','statement',2,'p_return_statement','parse.py',326),
]
