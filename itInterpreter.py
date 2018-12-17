import AST


stack = []
vars = {}

titlePageVars = {
'Img'   : '',
'Title' : 'Title of the document',
'Author': '',
'Date'  : '\\today',
}

boolVars = {
'Img':False,
'Title':False,
'Author':False,
'Date':False,
}



def valueOfToken(t):
	if isinstance(t,str):
		try:
			return vars[t]
		except KeyError:
			print("*** Error: variable %s undefined!"%t)
	return t


def execute(node):
	global titlePageVars
	global boolVars
	while node:
		if node.__class__ == AST.AuthorNode:
			val = node.tok
			boolVars['Author'] = True
			titlePageVars['Author'] = str(val)
		if node.__class__ == AST.ImageNode:
			val = node.tok
			boolVars['Img'] = True
			titlePageVars['Img'] = str(val)
		elif node.__class__ == AST.TitleNode:
			val = node.tok
			boolVars['Title'] = True
			titlePageVars['Title'] = str(val)
		elif node.__class__ == AST.DateNode:
			val = node.tok
			boolVars['Date'] = True
			if val == 'today':
				titlePageVars['Date'] = '\\today'
			else:
				titlePageVars['Date'] = str(val)
		elif node.__class__ in [AST.EntryNode, AST.ProgramNode]:
			pass
		elif node.__class__ == AST.TokenNode:
			stack.append(node.tok)
		if node.next:
			node = node.next[0]
		else:
			node = None


if __name__ == "__main__":

	from parser5 import parse
	from threader import thread
	import sys
	prog = open(sys.argv[1]).read()
	ast = parse(prog)
	entry = thread(ast)

	execute(entry)
	stringOutput =  '\\begin{document}\n'
	stringOutput += '\\pagenumbering{gobble}\n'
	if(boolVars['Img']):
		stringOutput += '\\begin{figure}\n'
		stringOutput += '\\centering\n'
		stringOutput += '\\vspace*{1cm}\n'
		stringOutput += '\\includegraphics[width=0.7\\textwidth]{'+titlePageVars['Img']+'}\n'
		stringOutput += '\\end{figure}\n'
	stringOutput += '\\vspace*{3cm}\n'
	stringOutput += '\\begin{center}\n'
	stringOutput += '\\textbf{\\Huge{'+titlePageVars['Title']+'}} \\\\[1cm]\n'
	stringOutput += '{\\Large '+titlePageVars['Author']+'} \\\\[5cm]\n'
	stringOutput += titlePageVars['Date']+'\n'
	stringOutput += '\\end{center}\n'
	stringOutput += "\\end{document}\n"

	print(titlePageVars['Author'])

	print(stringOutput)
