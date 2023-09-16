from lark import Tree, Lark
from lark.lexer import Token


class Lister():
    tabsPerSpace = 4
    
    indentableRules = {
        'center',
        'indented_content',
        'list_item'
    }
    
    def transform(self, tree):
        for child in tree.children:
            if isinstance(child, Tree):
                self.transform(child)
                
        listStack = []
        indentStack = []
        
        transformed = set() # to be removed from current children list
                
        for i, child in enumerate(tree.children):
            if self._indentable(child):
                indent = self._indent(child)
                
                if not self._isListItem(child):
                    indentOffset = 1
                
                else:
                    indentOffset = 0
                
                if self._isListItem(child) and (len(listStack) < 1 or indentStack[-1] < indent):                        
                    parentList = Tree('list', [child])
                    
                    if len(listStack) > 0:
                        listStack[-1].children.append(parentList)
                        parentList.indent = listStack[-1].indent + 1
                        transformed.add(i)

                    else:
                        # tree.children.append(parentList)
                        tree.children[i] = parentList
                        parentList.indent = 0
                        
                    child.indent = parentList.indent + 1

                    # print(f'listering list item: {child}\n with indent {indent}\n\n')
                    
                    listStack.append(parentList)
                    indentStack.append(indent)
                    
                else:
                    while len(listStack) > 0 and indentStack[-1] + indentOffset > indent:
                        listStack.pop()
                        indentStack.pop()

                    if len(listStack) > 0:
                        parentList = listStack[-1]

                        if self._isListItem(child):
                            parentList.children.append(child)
                            child.indent = parentList.indent + 1
                            
                        else:
                            parentList.children[-1].children.append(Token('NEWLINE', '\n'))
                            parentList.children[-1].children.append(child)
                            child.indent = parentList.children[-1].indent + 1

                        transformed.add(i)
                        
                    elif len(listStack) < 1 and self._isListItem(child):
                        parentList = Tree('list', [child])
                        # transformed.add(i)
                        
                        parentList.indent = 0
                        child.indent = 1
                        
                        listStack.append(parentList)
                        indentStack.append(indent)
                        
                        tree.children[i] = parentList

                    
            # if item was not indentable, it has probably ended previous lists so flush stacks
            # but an empty line should flush the stack
            elif not (isinstance(child, Token) and (child.type == 'NEWLINE' or child.type == 'INLINE_WHITESPACE' or child.type == 'WHITESPACE')):
                listStack = []
                indentStack = []     
           
        remainingChildren = []
            
        for i, child in enumerate(tree.children):
            if not i in transformed:
                remainingChildren.append(child)
                
        tree.children = remainingChildren
    
    
    def _indent(self, tree):
        token = tree.children[0]
        indent = 0
        
        if isinstance(token, Token) and token.type == 'INLINE_WHITESPACE':
            for c in token.value:
                if c == ' ':
                    indent += 1
                elif c == '\t':
                    indent += self.tabsPerSpace
            
            return indent
        
        return 0
    
    
    def _isListItem(self, tree):
        if isinstance(tree, Tree) and tree.data == 'list_item':
            return True
            
        return False
    
        
    def _indentable(self, tree):
        if isinstance(tree, Tree) and tree.data in self.indentableRules:
            return True
        
        return False   