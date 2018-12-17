import AST
from AST import addToClass

@addToClass(AST.Node)
def thread(self, lastNode):
    for c in self.children:
        lastNode = c.thread(lastNode)
    lastNode.addNext(self)
    return self

@addToClass(AST.WhileNode)
def thread(self, lastNode):
    cond = self.children[0].thread(lastNode)
    cond.addNext(self)
    body = self.children[1].thread(self)
    body.addNext(lastNode.next[-1]) #Pour sortir de la boucle à l'endroit où on y est rentré
    return self

#useless for now because DateNode and Author node heritate from Node
@addToClass(AST.DateNode)
def thread(self, lastNode):
    for c in self.children:
        lastNode = c.thread(lastNode)
    lastNode.addNext(self)
    return self

@addToClass(AST.AuthorNode)
def thread(self, lastNode):
    for c in self.children:
        lastNode = c.thread(lastNode)
    lastNode.addNext(self)
    return self

@addToClass(AST.TitleNode)
def thread(self, lastNode):
    for c in self.children:
        lastNode = c.thread(lastNode)
    lastNode.addNext(self)
    return self

@addToClass(AST.DateNode)
def thread(self, lastNode):
    for c in self.children:
        lastNode = c.thread(lastNode)
    lastNode.addNext(self)
    return self


#@addToClass(AST.IfNode)
#def thread(self, lastNode):
#
#    return self

def thread(tree):
    entry = AST.EntryNode()
    tree.thread(entry)
    return entry

if __name__ == "__main__":
    from parser5 import parse
    import sys, os
    prog = open(sys.argv[1]).read()
    ast = parse(prog)
    entry = thread(ast)

    graph = ast.makegraphicaltree()
    entry.threadTree(graph)

    name = os.path.splitext(sys.argv[1])[0]+'-ast-threaded.pdf'
    graph.write_pdf(name)
    print ("wrote threaded ast to", name)