import AST


stack = []
vars = {}

titlePageVars = {
'frontpageimg' : '',
'abstract' : '',
'language' : 'english',
'title' : 'Title of the document',
'author': 'by its authors',
'date'  : '\\today',
'margin' : 'auto',
'fileName' : 'PerfectDocument',
}

boolVars = {
'abstract' : False,
'frontpageimg':False,
'language':False,
'numbering':False,
'title':False,
'author':False,
'date':False,
'toc':False,
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
	global miscVars
	global boolVars
	body = ""
	while node:
		if node.__class__ == AST.FileNameNode:
			val = node.tok
			boolVars['fileName'] = True
			titlePageVars['fileName'] = str(val)
		elif node.__class__ == AST.AuthorNode:
			val = node.tok
			boolVars['author'] = True
			titlePageVars['author'] = str(val)
		elif node.__class__ == AST.LanguageNode:
			val = node.tok
			boolVars['language'] = True
			titlePageVars['language'] = str(val)
		elif node.__class__ == AST.FrontPageImageNode:
			val = node.tok
			boolVars['frontpageimg'] = True
			titlePageVars['frontpageimg'] = str(val)
		elif node.__class__ == AST.ImageNode:
			val = node.tok
			body += '\n%image : '+val+'\n\\begin{figure}[ht]\n'
			body += '\t\\centering\n'
			body += '\t\\vspace*{1cm}\n'
			body += '\t\\includegraphics[width=0.7\\textwidth]{'+val+'}\n'
			body += '\t\\caption{\label{}'+(val.split('/')[-1]).split('.')[0]+'}\n'
			body += '\\end{figure}\n'
		elif node.__class__ == AST.TitleNode:
			val = node.tok
			boolVars['title'] = True
			titlePageVars['title'] = str(val)
		elif node.__class__ == AST.NumberingNode:
			boolVars['numbering'] = (not boolVars['numbering'])
		elif node.__class__ == AST.DateNode:
			val = node.tok
			boolVars['date'] = True
			if val == 'today':
				titlePageVars['date'] = '\\today'
			else:
				titlePageVars['date'] = str(val)
		elif node.__class__ == AST.MarginNode:
			val = node.tok
			boolVars['margin'] = True
			titlePageVars['margin'] = str(val)
		elif node.__class__ == AST.AbstractNode:
			val = node.tok
			boolVars['abstract'] = True
			titlePageVars['abstract'] = str(val)
		elif node.__class__ == AST.TocNode:
			boolVars['toc'] = True
		elif node.__class__ == AST.ChapterNode:
			val = node.tok
			body += '\n\\chapter'+('' if boolVars['numbering'] else '*')+'{'+val+'}\n'
		elif node.__class__ == AST.SectionNode:
			val = node.tok
			body += '\n\\section'+('' if boolVars['numbering'] else '*')+'{'+val+'}\n'
		elif node.__class__ == AST.SubSectionNode:
			val = node.tok
			body += '\n\\subsection'+('' if boolVars['numbering'] else '*')+'{'+val+'}\n'
		elif node.__class__ == AST.SubSubSectionNode:
			val = node.tok
			body += '\n\\subsubsection'+('' if boolVars['numbering'] else '*')+'{'+val+'}\n'
		elif node.__class__ == AST.ParagraphNode:
			val = node.tok
			body += '\\paragraph{}\n'+val+'\n'
		elif node.__class__ == AST.BulletListNode:
			val = node.tok
			#print(val[1])
			for v in val[1].tok.children:
				print(v.tok)
		elif node.__class__ in [AST.EntryNode, AST.ProgramNode]:
			pass
		elif node.__class__ == AST.TokenNode:
			stack.append(node.tok)
		if node.next:
			node = node.next[0]
		else:
			node = None
	return body

def generate_pdf(filename,stringOutput):
	"""
	Genertates the pdf from string
	"""
	import subprocess
	import os
	import tempfile
	import shutil
	rootDir = os.getcwd()
	pdfname = filename+'.pdf'
	texname = filename+'.tex'
	outputFolder = 'output'
	outputPath = os.path.join(os.getcwd(),outputFolder)
	if not os.path.exists(outputPath):
	    os.makedirs(outputPath)
	filePath = os.path.join(outputPath, texname)
	f = open(filePath,'w')
	f.write(stringOutput)
	f.close()
	rootDir = os.getcwd()
	os.chdir(outputPath)
	try:
		os.remove(filename+'.log')
		os.remove(filename+'.aux')
		os.remove(filename+'.toc')
	except FileNotFoundError:
		pass
	# LateX Compilation is done twice in order to avoid the "Table of contents not displaying itself" bug.
	# https://stackoverflow.com/questions/3863630/latex-tableofcontents-command-always-shows-blank-contents-on-first-build
	# As this script will not neceserally be launched from a linux distribution. We can't call "rubber" command here which seems to fix this problem
	os.system('pdflatex -interaction=nonstopmode -file-line-error --shell-escape -halt-on-error'+' '+filePath)
	os.system('pdflatex -interaction=nonstopmode -file-line-error --shell-escape -halt-on-error'+' '+filePath)
	try:
		os.remove(filename+'.aux')
		os.remove(filename+'.log')
		os.remove(filename+'.toc')
	except FileNotFoundError:
		pass
	os.chdir(rootDir)

if __name__ == "__main__":
	from parser5 import parse
	from threader import thread
	import sys
	prog = open(sys.argv[1]).read()
	ast = parse(prog)
	entry = thread(ast)
	body = execute(entry)

	stringOutput = '\\documentclass[a4paper,10pt,openany,oneside]{report}\n'
	stringOutput += '\n% - PACKAGES -\n'
	if titlePageVars['margin'] == 'auto':
		stringOutput += '\\usepackage[left=2cm,right=2cm,top=2cm,includefoot]{geometry}\n'
	else:
		margin=titlePageVars['margin']
		stringOutput += '\\usepackage[left='+margin+'cm,right='+margin+'cm,top='+margin+'cm,includefoot]{geometry}\n'
	if boolVars['language']:
		stringOutput += '\\usepackage['+titlePageVars['language']+']{babel}\n'
	stringOutput += '\\usepackage{graphicx}\n'
	stringOutput += '\\usepackage{tabularx}\n'
	stringOutput += '\n% - DOCUMENT -\n'
	stringOutput += '\\begin{document}\n'
	stringOutput += '\\pagenumbering{gobble}\n'
	stringOutput += '\n% - FRONT PAGE -\n'
	stringOutput += '\\thispagestyle{empty}\n'
	if boolVars['frontpageimg']:
		stringOutput += '\\begin{figure}\n'
		stringOutput += '\t\\centering\n'
		stringOutput += '\t\\vspace*{1cm}\n'
		stringOutput += '\t\\includegraphics[width=0.6\\textwidth]{'+titlePageVars['frontpageimg']+'}\n'
		stringOutput += '\\end{figure}\n'
	stringOutput += '\\vspace*{3cm}\n'
	stringOutput += '\\begin{center}\n'
	stringOutput += '\\textbf{\\Huge{'+titlePageVars['title']+'}} \\\\[1cm]\n'
	stringOutput += '{\\Large '+titlePageVars['author']+'} \\\\[5cm]\n'
	stringOutput += titlePageVars['date']+'\n'
	stringOutput += '\\end{center}\n'
	if boolVars['abstract']:
		stringOutput += '\n% - ABSTRACT -\n'
		stringOutput += '\\chapter*{Abstract}\n'
		stringOutput += '\\paragraph{}'+titlePageVars['abstract']+'\n'
		stringOutput += '\\pagebreak\n'
	if boolVars['toc']:
		stringOutput += '\n% - TABLE OF CONTENTS -\n'
		stringOutput += '\\tableofcontents\n'
		stringOutput += '\\pagebreak\n'
	else:
		stringOutput += '\\pagebreak\n'
	stringOutput += "\\setcounter{page}{0}\n"
	stringOutput += '\n% - BODY -\n'
	stringOutput += body
	stringOutput += "\\end{document}\n"
	filename = titlePageVars['fileName']
	generate_pdf(filename, stringOutput)

	# commande :
	# pdflatex -synctex=1 -interaction=nonstopmode  --shell-escape testDocument.tex

# Problem : If images are needed into the document, they must be moved where the temporary file will be created.
