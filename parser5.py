import ply.yacc as yacc

from lex5 import tokens
import AST

vars = {}

def p_programme_statement(p):
    ''' programme : statement NEWLINE'''
    p[0] = AST.ProgramNode(p[1])

def p_programme_recursive(p):
    ''' programme : statement NEWLINE programme '''
    p[0] = AST.ProgramNode([p[1]]+p[3].children)

def p_statement(p):
    ''' statement : expression SEMICOLON '''
    p[0] = p[1]

def p_expression_author(p):
    ''' expression : AUTHOR PARANTHESIS_OPEN IDENTIFIER PARANTHESIS_CLOSE '''
    p[0] = AST.AuthorNode(p[3])

def p_expression_date(p):
    ''' expression : DATE PARANTHESIS_OPEN IDENTIFIER PARANTHESIS_CLOSE '''
    p[0] = AST.DateNode(p[3])

def p_expression_title(p):
    ''' expression : TITLE PARANTHESIS_OPEN IDENTIFIER PARANTHESIS_CLOSE '''
    p[0] = AST.TitleNode(p[3])

def p_expression_image(p):
    ''' expression : IMG PARANTHESIS_OPEN IDENTIFIER PARANTHESIS_CLOSE '''
    p[0] = AST.ImageNode(p[3])

def p_error(p):
    if p:
        print ("Syntax error in line %d" % p.lineno)
        #yacc.errok()
    else:
        print ("Sytax error: unexpected end of file!")

def parse(program):
    return yacc.parse(program)

yacc.yacc(outputdir='generated')

if __name__ == "__main__":
    import sys
    prog = open(sys.argv[1]).read()
    result = yacc.parse(prog, debug=False)
    if result:
        print(result)
        import os
        graph = result.makegraphicaltree()
        name = os.path.splitext(sys.argv[1])[0]+'-ast.pdf'
        graph.write_pdf(name)
        print ("wrote ast to", name)
    else:
        print ("Parsing returned no result!")
