from lark import Tree
from lark.visitors import Visitor_Recursive
from lark.lexer import Token



class Compiler(Visitor_Recursive):
    # blockMap = {
    #     'df' : 'definition',
    #     'th' : 'theorem',
    #     'ex' : 'example',
    #     'exc' : 'exercise',
    #     'exr' : 'exercise',
    #     'lm' : 'lemma',
    #     'ob' : 'observation',
    #     'pz' : 'pozorovani',
    #     'pp' : 'proposition',
    #     'cr' : 'corollary',
    #     'nt' : 'note',
    #     'pb' : 'problem',
    #     'alg' : 'algorithm',
    #     'blk' : 'block',
    #     'rmrk' : 'remark',
    #     'fact' : 'fact',
    #     'cv' : 'cviceni',
    #     'cj' : 'conjecture',
    #     'proof' : 'proof'
    # }
    blockMap = {
        'df' : 'definition',
        'th' : 'theorem',
        'ex' : 'example',
        'exc' : 'exercise',
        'exr' : 'exercise',
        'lm' : 'lemma',
        'ob' : 'observation',
        'pz' : 'pozorovani',
        'pp' : 'proposition',
        'cr' : 'corollary',
        'nt' : 'note',
        'pb' : 'problem',
        'alg' : 'algorithm',
        'blk' : 'block',
        'rmrk' : 'remark',
        'fact' : 'fact',
        'cv' : 'cviceni',
        'cj' : 'conjecture',
        'proof' : 'proof'
    }

    math_bb_symbol_map = {
        '𝔸' : '\\mathbb{A}',
        '𝔹' : '\\mathbb{B}',
        'ℂ' : '\\mathbb{C}',
        '𝔻' : '\\mathbb{D}',
        '𝔼' : '\\mathbb{E}',
        '𝔽' : '\\mathbb{F}',
        '𝔾' : '\\mathbb{G}',
        'ℍ' : '\\mathbb{H}',
        '𝕀' : '\\mathbb{I}',
        '𝕁' : '\\mathbb{J}',
        '𝕂' : '\\mathbb{K}',
        '𝕃' : '\\mathbb{L}',
        '𝕄' : '\\mathbb{M}',
        'ℕ' : '\\mathbb{N}',
        '𝕆' : '\\mathbb{O}',
        'ℙ' : '\\mathbb{P}',
        'ℚ' : '\\mathbb{Q}',
        'ℝ' : '\\mathbb{R}',
        '𝕊' : '\\mathbb{S}',
        '𝕋' : '\\mathbb{T}',
        '𝕌' : '\\mathbb{U}',
        '𝕍' : '\\mathbb{V}',
        '𝕎' : '\\mathbb{W}',
        '𝕏' : '\\mathbb{X}',
        '𝕐' : '\\mathbb{Y}',
        'ℤ' : '\\mathbb{Z}'
    }

    math_cal_symbol_map = {
        '𝓐' : '\\mathcal{A}',
        '𝓑' : '\\mathcal{B}',
        '𝓒' : '\\mathcal{C}',
        '𝓓' : '\\mathcal{D}',
        '𝓔' : '\\mathcal{E}',
        '𝓕' : '\\mathcal{F}',
        '𝓖' : '\\mathcal{G}',
        '𝓗' : '\\mathcal{H}',
        '𝓘' : '\\mathcal{I}',
        '𝓙' : '\\mathcal{J}',
        '𝓚' : '\\mathcal{K}',
        '𝓛' : '\\mathcal{L}',
        '𝓜' : '\\mathcal{M}',
        '𝓝' : '\\mathcal{N}',
        '𝓞' : '\\mathcal{O}',
        '𝓟' : '\\mathcal{P}',
        '𝓠' : '\\mathcal{Q}',
        '𝓡' : '\\mathcal{R}',
        '𝓢' : '\\mathcal{S}',
        '𝓣' : '\\mathcal{T}',
        '𝓤' : '\\mathcal{U}',
        '𝓥' : '\\mathcal{V}',
        '𝓦' : '\\mathcal{W}',
        '𝓧' : '\\mathcal{X}',
        '𝓨' : '\\mathcal{Y}',
        '𝓩' : '\\mathcal{Z}'
    }

    math_greek_symbol_map = {
        'α' : '\\alpha',
        'β' : '\\beta',
        'γ' : '\\gamma',
        'δ' : '\\delta',
        'ε' : '\\epsilon',
        'φ' : '\\varphi',
        'η' : '\\eta',
        'ι' : '\\iota',
        'κ' : '\\kappa',
        'λ' : '\\lambda',
        'μ' : '\\mu',
        'ν' : '\\nu',
        'ω' : '\\omega',
        'π' : '\\pi',
        'Θ' : '\\theta',
        'ψ' : '\\psi',
        '𝛝' : '\\vartheta',
        'ρ' : '\\rho',
        'σ' : '\\sigma',
        'τ' : '\\tau',
        'υ' : '\\vartheta',
        'χ' : '\\chi',
        'ψ' : '\\Psi',
        'Ψ' : '\\Psi',
        'ζ' : '\\zeta',
        'ξ' : '\\xi',
        'Ω' : '\\Omega',
        'Σ' : '\\Sigma',
        'Δ' : '\\Delta',
        'Φ' : '\\Phi',
        'Γ' : '\\Gamma',
        'Λ' : '\\Lambda',
        'Ξ' : '\\Xi'
    }

    math_symbol_map = {
        '∞' : '\\infty',
        '⟨' : '\\langle',
        '⟩' : '\\rangle',
        '⋱' : '\\ddots',
        '︙' : '\\vdots',
        '⠇' : '\\vdots',
        '∇' : '\\nabla',
        '⊥' : '\\bot',
        '∅' : '\\emptyset',
        '∝' : '\\varpropto',
        '◦' : '\\circ',
        '○' : '\\circ',
        '￮' : '\\circ',
        '↾' : '\\upharpoonright',
        '¶' : '{}',
        '✓' : '\\checkmark',
        '≼' : '\\preceq',
        '≺' : '\\prec',
        '⊀' : '\\nprec',
        '⇕' : '\\Updownarrow',
        '⇳' : '\\Updownarrow',
        '↓' : '\\downarrow',
        '↑' : '\\uparrow',
        '⇓' : '\\Downarrow',
        '⇑' : '\\Uparrow',
        '⊄' : '\\not\\subset',
        '⊅' : '\\not\\supset',
        '⋡' : '\\nsucc',
        '≽' : '\\succeq',
        '≻' : '\\succ',
        '∋' : '\\ni',
        '⊴' : '\\trianglelefteq',
        '⊵' : '\\trianglerighteq',
        '⊲' : '\\triangleleft',
        '⊳' : '\\triangleright',
        '⋪' : '\\not\\triangleleft',
        '⋫' : '\\not\\triangleright',
        '⋬' : '\\not\\trianglelefteq',
        '⋭' : '\\not\\trianglerighteq',
        '∦' : '\\nparallel',
        '⌈' : '\\lceil',
        '⌉' : '\\rceil',
        '⌊𝨨' : '\\lfloor',
        '⌋' : '\\rfloor',
        '⊊' : '\\subsetneq',
        '⊋' : '\\supsetneq'

    }

    shortcut_operator_map = {
        '<=>' : '\\iff',
        '=>' : '\\implies',
        '<=' : '\\impliedby',
        '<->' : '\\leftrightarrow',
        '|->' : '\\mapsto',
        '->' : '\\to',
        '<-' : '\\leftarrow',
        '<<' : '\\ll',
        '>>' : '\\gg',
        '\\Σ' : '\\sum\\limits',
        '\\π' : '\\prod\\limits',
        '\\∪' : '\\bigcup\\limits',
        '\\∩' : '\\bigcap\\limits',
        '\\∫' : '\\int\\limits', 
        '\\∨' : '\\bigvee\\limits',
        '\\∧' : '\\bigwedge\\limits',
        '\\⊕' : '\\bigoplus\\limits',
    }

    unicode_operator_map = {
        '∧' : '\\land',
        '∨' : '\\lor',
        '∩' : '\\cap',
        '∪' : '\\cup',
        '∀' : '\\forall',
        '∃' : '\\exists',
        '∄' : '\\nexists',
        '∂' : '\\partial',   
        '=' : '=',
        '≠' : '\\neq',
        '~' : '\\sim',
        '≡' : '\\equiv',
        '≢' : '\\not\\equiv',
        '≈' : '\\approx',
        '≉' : '\\not\\approx',
        '⊂' : '\\subset',
        '⊆' : '\\subseteq',
        '⊈' : '\\nsubseteq',
        '⊃' : '\\supset',
        '⊇' : '\\supseteq',
        '⊉' : '\\nsupseteq',
        '≠' : '\\neq',

        '\\' : '\\backslash',

        '=' : '=',
        '+' : '+',
        '-' : '-',
        '/' : '/',
        '*' : '*',

        '≤' : '\\leq',
        '≥' : '\\geq',
        '<' : '<',
        '>' : '>',
        '≪' : '\\ll',
        '≫' : '\\gg',
        '!' : '!',
        '|' : '|',
        ':' : ':',
        '∈' : '\\in',
        '∉' : '\\notin',
        '∙' : '\\cdot',
        '≆' : '\\not\\approxeq',
        '≅' : '\\approxeq',
        '≃' : '\\simeq',
        '×' : '\\times',
        '±' : '\\pm',
        '¬' : '\\neg',
        '∤' : '\\nmid',
        '⊍' : '\\uplus',
        '⨄' : '\\uplus',

        '⊤' : '\\top',
        '⊥' : '\\bot',
        '⊨' : '\\models',
        '⊢' : '\\vdash',

        '⌈' : '\\lceil',
        '⌉' : '\\rceil',
        '⌊' : '\\lfloor',
        '⌋' : '\\rfloor',
    }

    operator_map = {
        '<=>' : '\\iff',
        '=>' : '\\implies',
        '<=' : '\\impliedby',
        '<->' : '\\leftrightarrow',
        '|->' : '\\mapsto',
        '->' : '\\to',
        '<-' : '\\leftarrow',
        '<<' : '\\ll',
        '>>' : '\\gg',
        '~' : '\\sim',
        '≡' : '\\equiv',
        '≢' : '\\not\\equiv',
        '≈' : '\\approx',
        '≉' : '\\not\\approx',
        '⊂' : '\\subset',
        '⊆' : '\\subseteq',
        '⊃' : '\\supset',
        '⊇' : '\\supseteq',
        '≠' : '\\neq',
        '=' : '=',
        '+' : '+',
        '-' : '-',
        '/' : '/',
        '*' : '*',
        '^' : '^',
        '_' : '_',
        '\\' : '\\backslash',
        '∧' : '\\land',
        '∨' : '\\lor',
        '∩' : '\\cap',
        '∪' : '\\cup',
        '∀' : '\\forall',
        '∃' : '\\exists',
        '∄' : '\\nexists',
        '√' : '\\sqrt',
        '∂' : '\\partial',
        '∫' : '\\int', 
        '\\∫' : '\\int\\limits', 
        '≤' : '\\leq',
        '≥' : '\\geq',
        '<' : '<',
        '>' : '>',
        '!' : '!',
        '|' : '|',
        ':' : ':',
        '∈' : '\\in',
        '∉' : '\\notin',
        '∙' : '\\cdot',
        '≆' : '\\not\\approxeq',
        '≅' : '\\approxeq',
        '≃' : '\\simeq',
        '×' : '\\times',
        '±' : '\\pm',
        '¬' : '\\neg',
        '∤' : '\\nmid',
        '\\Σ' : '\\sum\\limits',
        '\\π' : '\\prod\\limits',
        '\\∪' : '\\bigcup\\limits',
        '\\∩' : '\\bigcap\\limits',
        '⊍' : '\\uplus',
    }

    keyword_operator_map = {
        'mod' : '\\mod',
        'min' : '\\min\\limits',
        'max' : '\\max\\limits',
        'argmin' : '\\argmin\\limits',
        'argmax' : '\\argmax\\limits',
        'sin' : '\\sin',
        'cos' : '\\cos',
        'tan' : '\\tan',
        'exp' : '\\exp',
        'log' : '\\log',
        'conv' : '\\conv',
        'cone' : '\\cone',
        'ln' : '\\ln',
        'diag' : '\\diag',
        'sup' : '\\sup\\limits',
        'inf' : '\\inf\\limits',
        'arccos' : '\\arccos\\limits',
        'arcsin' : '\\arcsin\\limits',
        'sgn' : '\\sgn',
        'lim' : '\\lim\\limits',
        'span' : '\\spn',
        'limsup' : '\\limsup\\limits',
        'liminf' : '\\liminf\\limits',
    }
    
    escapedCharacterMap = {
        '&' : '\\&',
        '#' : '\\#',
        '%' : '\\%'
        # '$' : '\\$'
    }
    
    commandSymbols = { 'MATH_GREEK_SYMBOLS', 'MATH_BB_SYMBOLS', 'MATH_CAL_SYMBOLS', 'MATH_SYMBOLS', 'MATH_OPERATOR_A', 'MATH_OPERATOR_B', 'UNICODE_OPERATOR', 'SHORTCUT_OPERATOR', 'KEYWORD_OPERATOR' }
    
    
    def __default__(self, tree):
        tree.result = ''
        tree.indent = 0
        
        self._gatherFromChildren(tree)

                
    def _gatherFromChildren(self, tree, startIndex = 0, endIndex = None, space = '', write = True):
        if endIndex == None:
            endIndex = len(tree.children)

        result = ''
        
        for i, child in enumerate(tree.children[startIndex:endIndex]):
            if i > 0 and not (isinstance(child, Tree) and (child.data.value == 'inline_whitespace' or tree.children[i - 1].data.value == 'inline_whitespace')):
                result += space

            if isinstance(child, Tree):
                # tree.result += self._escapeCharacters(child.result)
                result += child.result
                
            elif isinstance(child, Token):
                if child.type == 'INLINE_WHITESPACE':                    
                    child.value = child.value.replace('   ', '\\enskip')
                    child.value = child.value.replace('  ', '\\;')
                    child.value = child.value.replace('\t', '\\quad')

                result += self._escapeCharacters(child.value)
                
        if write:
            tree.result += result

        return result

    
    def _escapeCharacters(self, string):
        for original, escaped in self.escapedCharacterMap.items():
            string = string.replace(original, escaped)
        
        return string


    def image(self, tree):
        string = tree.children[0].value

        tree.result = '\\includegraphics'

        if '[' in string:
            string = string.split('[')[1]
            string = string.split(']')
            scale, string = string[0], string[1]
            tree.result += f'[scale={scale}]'

        path = string.split('{')[1][:-1]

        tree.result += f'{{{path}}}'



        # temp = tree.children[0].value.split('[')
        # scale 

        # tree.result = '\\includegraphics[scale=0.6]{'
        # tree.result += tree.children[0].value.split('{')[1][:-1]
        # tree.result += '}'

                
                
    def math_block(self, tree):
        tree.result = '$'
        
        self._gatherFromChildren(tree, startIndex = 1, endIndex = len(tree.children) - 1, space = ' ')
        
        tree.result += '$'
        
        
    def center(self, tree):
        tree.result = '\\begin{center}\n\n'

        startIndex = 1 + (tree.children[0].type != 'CENTER_OPEN')
        endIndex = len(tree.children) - 1
        
        content = '\t' + self._gatherFromChildren(tree, startIndex = startIndex, endIndex = endIndex, write = False).strip()
        
        tree.result += content.replace('\n', '\n\t')
        tree.result += '\n\n\\end{center}\n'
        
        
    def table(self, tree):
        # must also sort out column numbers, sepparators, etc.
        
        columnCount = 1
        
        rows = ''
        
        for child in tree.children:
            rows += child.result
            columnCount = max(child.columnCount, columnCount)

        columnSignature = ' ' + (columnCount * 'c ')
        tree.result = f'\n\\begin{{tabular}}{{{columnSignature}}}\n'
        tree.result += rows
        tree.result += '\n\\end{tabular}\n'
        
        
    def table_row(self, tree):
        tree.columnCount = 1
        
        if tree.children[0].type == 'TABLE_SEPPARATOR':
            tree.result = '\t\\hline\n'    

        else: 
            tree.result = '\t'
            
            for child in tree.children[1:len(tree.children) - 1]:
                if isinstance(child, Tree):
                    tree.result += child.result

                elif isinstance(child, Token):
                    if child.type == 'TABLE_DELIMITER':
                        tree.result += ' & '
                        tree.columnCount += 1

                    else:
                        tree.result += child.value
                
            tree.result += '\\\\\n'
        

    def chapter_header(self, tree):
        title = tree.children[0].result
        tree.result = f'\\chapter{{{title}}}\n'

        
    def section_header(self, tree):
        title = tree.children[0].result
        tree.result = f'\\section{{{title}}}\n'

        
    def subsection_header(self, tree):
        title = tree.children[0].result
        tree.result = f'\\subsection{{{title}}}\n'

        
    def subsubsection_header(self, tree):
        title = tree.children[0].result
        tree.result = f'\\subsubsection{{{title}}}\n'
        
        
    def comment(self, tree):
        tree.result = ''
    
    
    def block(self, tree):   
        titleChild = tree.children[0]

        if len(titleChild.children) < 1:
            blockType = 'block'
            tree.result = '\n\\begin{block}\n'


        elif len(titleChild.children) == 1:
            firstChild = titleChild.children[0]

            if isinstance(firstChild, Token):
                blockTag = firstChild.value.lower()
                blockType = self.blockMap[blockTag]

                tree.result = f'\n\\begin{{{blockType}}}\n'

            else:
                title = firstChild.result
                blockType = 'block'

                tree.result = f'\n\\begin{{block}}[{title}]\n'

        elif len(titleChild.children) > 1:
            blockTag = titleChild.children[0].value.lower()
            blockType = self.blockMap[blockTag]
            
            title = titleChild.children[1].result

            tree.result = f'\n\\begin{{{blockType}}}[{title}]\n'


        self._gatherFromChildren(tree, startIndex = 1)
        
        tree.result += f'\n\\end{{{blockType}}}\n'
        
        
    def list(self, tree):
        indent = '\t' * tree.indent
        
        tree.result = f'\\begin{{itemize}}\n'

        if tree.indent < 1:
            tree.result += '\n\t\\itemsep0em\n'
        
        content = '\t' + self._gatherFromChildren(tree, write = False)
        
        tree.result += content.replace('\n', '\n\t')
        tree.result += f'\n\\end{{itemize}}\n'


    def list_bullet(self, tree):
        tree.result = ''

        if tree.children[0].value == '-':
            self._gatherFromChildren(tree, startIndex = 1, endIndex = len(tree.children))
 
        elif tree.children[0].value == '-{':        
            self._gatherFromChildren(tree, startIndex = 1, endIndex = len(tree.children))

    
    def list_item(self, tree):
        indent = '\t' * tree.indent

        if isinstance(tree.children[0], Token):
            bullet = tree.children[1].result
            startIndex = 1

        else:
            bullet = tree.children[0].result
            startIndex = 0


        if len(bullet) > 0:
            tree.result = f'\n\\item[{bullet}]'        
            
        else:
            tree.result = f'\n\\item' 
            
        self._gatherFromChildren(tree, startIndex = 1 + startIndex)

        tree.result += '\n'

        
    def spacing(self, tree):
        token = tree.children[0].value
        tree.result = ''
        
        if token == 'DOUBLE_SPACE':
            tree.result = '\\; '
            
        if token == 'TRIPLE_SPACE':
            tree.result = '\\enskip '
            
        if token == 'TAB':
            tree.result = '\\t '
            
            
###################################################



    def array(self, tree):
        openBracket = tree.children[0][-1]
        closeBracket = tree.children[-1][-1]
        
        columnCount = 0
            
        if openBracket == '\\':
            tree.result = '\n\\left. '
        
        elif openBracket == '{':
            tree.result = '\n\\left\\{ '
        
        else:
            tree.result = f'\n\\left{openBracket} '
            
        rows = ''
                
        for child in tree.children[1:-2]:
            rows += '\t' + child.result + '\\\\\n'
            columnCount = max(columnCount, child.columnCount)

        # add last row sepparately without a latex newline at the end
        rows += '\t' + tree.children[-2].result + '\n'
        columnCount = max(columnCount, tree.children[-2].columnCount)

        columnSignature = columnCount * 'c'
        tree.result += f'\\begin{{array}}{{{columnSignature}}}\n'
        tree.result += rows
        tree.result += '\\end{array}'
            
        if closeBracket == '\\':
            tree.result += ' \\right. '
        
        elif closeBracket == '}':
            tree.result += ' \\right\\} '
        
        else:
            tree.result += f' \\right{closeBracket} '
            
    
    def array_row(self, tree):
        tree.result = ''
        tree.columnCount = 1
        
        for child in tree.children:
            if isinstance(child, Token) and child.type == 'ARRAY_COLUMN_DIVIDER':
                tree.result += ' & '
                tree.columnCount += 1
            
            else:
                tree.result += child.result
            
        
    def symbol(self, tree):
        child = tree.children[0]

        if child.type == 'NUMBER' or child.type == 'LETTER':
            tree.result = tree.children[0].value
            
        elif child.type == 'MATH_GREEK_SYMBOLS':
            tree.result = f'{self.math_greek_symbol_map[tree.children[0].value]}'

        elif child.type == 'MATH_BB_SYMBOLS':
            tree.result = f'{self.math_bb_symbol_map[tree.children[0].value]}'
            
        elif child.type == 'MATH_CAL_SYMBOLS':
            tree.result = f'{self.math_cal_symbol_map[tree.children[0].value]}'
            
        elif child.type == 'MATH_SYMBOLS':
            tree.result = f'{self.math_symbol_map[tree.children[0].value]}'
            
        elif child.type == 'MATH_OPWORD':
            tree.result = f'{self.operator_word_map[tree.children[0].value]}'

        elif child.type == 'PUNCTUATION' or child.type == 'PARENTHESES':
            content = f'{tree.children[0].value}'
        
            if content == '{{' or content == '}}':
                content = '\\' + content[0]
            
            tree.result = content   

        elif child.type == 'UNICODE_OPERATOR':         
            tree.result = f'{self.unicode_operator_map[tree.children[0].value]}'

        elif child.type == 'SHORTCUT_OPERATOR':         
            tree.result = f'{self.shortcut_operator_map[tree.children[0].value]}'

        elif child.type == 'KEYWORD_OPERATOR':
            tree.result = f'{self.keyword_operator_map[tree.children[0].value]}'


            
    def fraction(self, tree):    
        tree.result = f'\\frac{{{tree.children[0].result}}}{{{tree.children[-1].result}}}'
            

    def root(self, tree):    
        child = tree.children[0]

        if isinstance(child, Token) and child.type == 'ROOT_OPERATOR':
            tree.result = f'\\sqrt{{{tree.children[-1].result}}}'

        else:
            tree.result = f'\\sqrt[{tree.children[0].result}]{{{tree.children[-1].result}}}'
                 
        
    def inline_whitespace(self, tree):
        child = tree.children[0]
        
        if child.type == 'TRIPLE_SPACE':
            tree.result = ' \\enskip '
            
        elif child.type == 'DOUBLE_SPACE':
            tree.result = ' \\; '
            
        elif child.type == 'SPACE':
            tree.result = ' '
            
        elif child.type == 'TAB':
            tree.result = ' \\quad '
        
        
    def term(self, tree):
        tree.result = ''
        
        for i, child in enumerate(tree.children):
            if isinstance(child, Tree):
                if i > 0 and child.children[0].type in self.commandSymbols:
                    tree.result += ' '

                tree.result += child.result
                
            elif isinstance(child, Token):
                if i > 0 and child.type in self.commandSymbols:
                    tree.result += ' '      

                if child.value == '{{':
                    tree.result += r' \{ '
                    
                elif child.value == '}}':
                    tree.result += r' \} '

                else:
                    tree.result += child.value    

  

                
    def text_block(self, tree):
        tree.result = f'\\enskip \\text{{{tree.children[0].value}}} \\enskip '
                        
    
    def structural(self, tree):
        content = f'{tree.children[0].value}'
        
        if content == '{{' or content == '}}':
            content = '\\' + content[0]
            
        tree.result = content


    def math_content(self, tree):
        tree.result = ''
        tree.indent = 0
        
        self._gatherFromChildren(tree, space = ' ')
        
        
    def sub_expression(self, tree):
        if len(tree.children) > 1:
            tree.result = ''
            
            for child in tree.children:
                # if isinstance(child, Token) and (child.type == 'SINGLE_OPEN_BRACKET' or child.type == 'OPEN_BRACKET'):
                #     tree.result += r'{'
                    
                # elif isinstance(child, Token) and (child.type == 'SINGLE_CLOSE_BRACKET' or child.type == 'CLOSE_BRACKET'):
                #     tree.result += r'}'
                    
                if hasattr(child, 'result'):
                    tree.result += child.result
   
        else:
            child = tree.children[0]
                
            if hasattr(child, 'result'):
                tree.result = child.result
                            
        
    def expression(self, tree):
        tree.result = ''
        
        for i, child in enumerate(tree.children):
            if hasattr(child, 'result'):
                tree.result += child.result
        
                    
    def underline_overline(self, tree):        
        if isinstance(tree.children[1], Token): # nothing before subexpression
            result = tree.children[0].result
            operation = tree.children[1]
            
        else:
            result = tree.children[1].result
            operation = tree.children[2]      
        
        if operation.type == 'UNDERLINE_OPERATOR':
            result = f'\\underline{{{result}}}'
            
        elif operation.type == 'OVERLINE_OPERATOR':
            result = f'\\overline{{{result}}}'            
            
        tree.result = result
        
                
    def sub_super_script_term(self, tree):
        tree.result = tree.children[0].result
        
        for child in tree.children[1:]:
            if isinstance(child, Token) and (child.type == 'SUPERSCRIPT_OPERATOR' or child.type == 'SUBSCRIPT_OPERATOR'):
                tree.result += child.value
                
            else:
                if isinstance(child, Tree):
                    result = child.result
                    
                    # print(f'tesing child: {child}')
                    if len(result) > 1:
                        result = f'{{{result}}}'
                    
                    tree.result += result