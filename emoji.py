from ply import lex, yacc
import random
import time
from termcolor import colored

# Define tokens at module level since PLY needs this
tokens = (
    'NUMBER',
    'PLUS',      # 🤝
    'MINUS',     # 💔
    'TIMES',     # 💫
    'DIVIDE',    # ✂️
    'PRINT',     # 📢
    'LPAREN',    # 🤜
    'RPAREN',    # 🤛
    'EQUALS',    # =
    'VARIABLE',  # 📦
    'STRING',    # 💭
    'IF',        # 🤔
    'LOOP',      # 🔁
    'RANDOM',    # 🎲
    'SLEEP',     # 💤
    'GT',        # 📈
    'LT',        # 📉
    'NEWLINE',   # Explicit newline handling
    'ELSE',      # 🤷
    'LIST',      # 📋
    'GET',       # 🎣
    'APPEND'     # 📎
)

class EmojiLexer:
    tokens = tokens  # Share tokens with the module level

    # Regular expression rules for tokens
    t_PLUS = r'🤝'
    t_MINUS = r'💔'
    t_TIMES = r'💫'
    t_DIVIDE = r'✂️'
    t_PRINT = r'📢'
    t_LPAREN = r'🤜'
    t_RPAREN = r'🤛'
    t_EQUALS = r'='
    t_IF = r'🤔'
    t_LOOP = r'🔁'
    t_RANDOM = r'🎲'
    t_SLEEP = r'💤'
    t_GT = r'📈'
    t_LT = r'📉'
    t_VARIABLE = r'📦[a-zA-Z_][a-zA-Z0-9_]*'
    t_LIST = r'📋'
    t_GET = r'🎣'
    t_APPEND = r'📎'
    t_ELSE = r'🤷'

    def t_STRING(self, t):
        r'💭"[^"]*"'
        t.value = t.value[2:-1]  # Remove the 💭" and "
        return t

    def t_NUMBER(self, t):
        r'\d+'
        t.value = int(t.value)
        return t

    def t_NEWLINE(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)
        return t

    def t_COMMENT(self, t):
        r'\#.*'
        pass  # Comments are ignored

    t_ignore = ' \t'

    def t_error(self, t):
        print(f"😱 Illegal character '{t.value[0]}'")
        t.lexer.skip(1)

    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
        return self.lexer

class EmojiParser:
    tokens = tokens  # Share tokens with the module level
    
    def __init__(self):
        self.lexer = EmojiLexer().build()
        
        # Define precedence
        self.precedence = (
            ('left', 'GET'),
            ('left', 'GT', 'LT'),
            ('left', 'PLUS', 'MINUS'),
            ('left', 'TIMES', 'DIVIDE'),
        )
        
        self.parser = yacc.yacc(module=self, start='program')

    def p_program(self, p):
        '''program : statement
                  | program NEWLINE statement'''
        if len(p) == 2:
            p[0] = [p[1]] if p[1] is not None else []
        else:
            p[0] = p[1] + [p[3]] if p[3] is not None else p[1]

    def p_statement(self, p):
        '''statement : print_stmt
                    | assignment_stmt
                    | if_stmt
                    | loop_stmt
                    | sleep_stmt
                    | list_stmt
                    | empty'''
        p[0] = p[1]

    def p_empty(self, p):
        '''empty :'''
        pass

    def p_print_stmt(self, p):
        '''print_stmt : PRINT expression'''
        p[0] = ('print', p[2])

    def p_assignment_stmt(self, p):
        '''assignment_stmt : VARIABLE EQUALS expression'''
        p[0] = ('assign', p[1], p[3])

    def p_if_stmt(self, p):
        '''if_stmt : IF expression statement
                  | IF expression statement ELSE statement'''
        if len(p) == 4:
            p[0] = ('if', p[2], p[3], None)
        else:
            p[0] = ('if', p[2], p[3], p[5])

    def p_expression_list_operation(self, p):
        '''expression : GET VARIABLE expression'''
        p[0] = ('get_list', p[2], p[3])

    def p_list_stmt(self, p):
        '''list_stmt : LIST VARIABLE
                    | APPEND VARIABLE expression
                    '''
        if p[1] == '📋':
            p[0] = ('create_list', p[2])
        else:
            p[0] = ('append_list', p[2], p[3])

    def p_loop_stmt(self, p):
        '''loop_stmt : LOOP expression statement'''
        p[0] = ('loop', p[2], p[3])

    def p_sleep_stmt(self, p):
        '''sleep_stmt : SLEEP expression'''
        p[0] = ('sleep', p[2])

    def p_expression(self, p):
        '''expression : expression PLUS expression
                     | expression MINUS expression
                     | expression TIMES expression
                     | expression DIVIDE expression
                     | expression GT expression
                     | expression LT expression
                     | RANDOM expression
                     | LPAREN expression RPAREN
                     | NUMBER
                     | STRING
                     | VARIABLE'''
        if len(p) == 4:
            if p[1] == '🤜':  # Parentheses
                p[0] = p[2]
            else:  # Binary operations
                p[0] = ('binop', p[2], p[1], p[3])
        elif len(p) == 3 and p[1] == '🎲':  # Random
            p[0] = ('random', p[2])
        elif len(p) == 2:  # Number, String, or Variable
            if isinstance(p[1], int):
                p[0] = ('literal', p[1])
            elif isinstance(p[1], str) and p[1].startswith('📦'):
                p[0] = ('var', p[1])
            else:
                p[0] = ('literal', p[1])

    def p_error(self, p):
        if p:
            print(f"😱 Syntax error at '{p.value}'")
        else:
            print("😱 Syntax error at EOF")

    def parse(self, code):
        return self.parser.parse(code, lexer=self.lexer)

class EmojiInterpreter:
    def __init__(self):
        self.variables = {}
        self.lists = {}
        self.parser = EmojiParser()

    def to_string(self, value):
        """Convert any value to string representation"""
        return str(value)

    def evaluate(self, node):
        if node is None:
            return None
            
        if isinstance(node, tuple):
            operation = node[0]
            
            if operation == 'print':
                value = self.evaluate(node[1])
                print(f"🎯 Output:", value)
                return None
                
            elif operation == 'assign':
                var_name = node[1]
                value = self.evaluate(node[2])
                self.variables[var_name] = value
                return None
                
            elif operation == 'binop':
                op = node[1]
                left = self.evaluate(node[2])
                right = self.evaluate(node[3])
                

                # Convert operands to strings if either operand is a string
                if op == '🤝' and (isinstance(left, str) or isinstance(right, str)):
                    left = self.to_string(left)
                    right = self.to_string(right)
 
                if op == '🤝': return left + right
                elif op == '💔': return left - right
                elif op == '💫': return left * right
                elif op == '✂️': return left / right
                elif op == '📈': return left > right
                elif op == '📉': return left < right
                
            elif operation == 'random':
                max_val = self.evaluate(node[1])
                return random.randint(1, max_val)
                
            elif operation == 'if':
                condition = self.evaluate(node[1])
                if condition:
                    return self.evaluate(node[2])
                elif node[3]:  # else block
                    return self.evaluate(node[3])
                    
            elif operation == 'create_list':
                self.lists[node[1]] = []
                return None
                
            elif operation == 'append_list':
                if node[1] in self.lists:
                    value = self.evaluate(node[2])
                    self.lists[node[1]].append(value)
                else:
                    print(colored(f"😱 List {node[1]} not found!", 'red'))
                return None
                
            elif operation == 'get_list':
                var_name = node[1]
                if var_name in self.lists:
                    index = self.evaluate(node[2])
                    try:
                        return self.lists[var_name][index]
                    except IndexError:
                        print(colored(f"😱 Index {index} out of range!", 'red'))
                        return None
                else:
                    print(colored(f"😱 List {node[1]} not found!", 'red'))
                return None
                    
            elif operation == 'loop':
                times = self.evaluate(node[1])
                result = None
                for _ in range(times):
                    result = self.evaluate(node[2])
                return result
                
            elif operation == 'sleep':
                seconds = self.evaluate(node[1])
                time.sleep(seconds)
                return None
                
            elif operation == 'literal':
                return node[1]
                
            elif operation == 'var':
                var_name = node[1]
                if var_name in self.variables:
                    return self.variables[var_name]
                else:
                    print(f"😱 Undefined variable: {var_name}")
                    return 0

    def run(self, code):
        program = self.parser.parse(code)
        if program:
            for statement in program:
                self.evaluate(statement)

def run_demo():
    interpreter = EmojiInterpreter()
    
    print("🎮 Welcome to EmojiScript 2.0! 🎮")
    print("\nRunning demo program...")
    
    program = """
📢 💭"Welcome to EmojiScript! 🌟"


📦counter = 1
📢 💭"Starting loop:"
🔁 5 📦counter = 🤜📦counter 🤝 1🤛
📢 📦counter


📢 💭"Generating random number between 1 and 10..."
📦random_num = 🎲 10
📢 📦random_num

🤔 🤜📦random_num 📈 5🤛 📢 💭"That's a big number! 🎉"

💤 1
📢 💭"Done! 👋"
"""
    
    print("\nProgram source:")
    print(program)
    print("\nProgram output:")
    interpreter.run(program)

if __name__ == '__main__':
    run_demo()
