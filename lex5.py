import ply.lex as lex

reserved_words = (
	'author',
	'date',
	'img',
	'title',
	'marge',
	'p', #paragraph
	'c', #chapter
	's', #section
	'ss', #subsection
	'sss', #subsubsection
	'filename',
	'bl', #bulletlist
	'table',
)

tokens = (
	'PARANTHESIS_OPEN',
    'PARANTHESIS_CLOSE',
	'IDENTIFIER',
	'NEWLINE',
	'EMPTY',
	'SEMICOLON'
) + tuple(map(lambda s:s.upper(),reserved_words))

literals = '();={}'

def t_IDENTIFIER(t):
	r'\w+(\s+\w+|,|\.\w+|\/\w+)*'
	if t.value in reserved_words:
		t.type = t.value.upper()
	return t

def t_NEWLINE(t):
	r'\n+'
	t.lexer.lineno += len(t.value)
	return t

def t_EMPTY(t):
	r'\#'
	return t

def t_PARANTHESIS_OPEN(t):
    r'\('
    return t

def t_PARANTHESIS_CLOSE(t):
    r'\)'
    return t

def t_SEMICOLON(t):
    r';'
    return t

t_ignore  = ' \t'

def t_error(t):
	print ("Illegal character '%s'" % repr(t.value[0]))
	t.lexer.skip(1)

lex.lex()

if __name__ == "__main__":
	import sys
	prog = open(sys.argv[1]).read()

	lex.input(prog)

	while 1:
		tok = lex.token()
		if not tok: break
		print ("line %d: %s(%s)" % (tok.lineno, tok.type, tok.value))
