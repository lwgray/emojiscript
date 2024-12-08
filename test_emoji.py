import unittest
from emoji import EmojiInterpreter, EmojiParser, EmojiLexer
from io import StringIO
import sys
import time

class TestEmojiScript(unittest.TestCase):
    def setUp(self):
        self.interpreter = EmojiInterpreter()
        self.parser = EmojiParser()
        # Capture stdout for testing print statements
        self.held_output = StringIO()
        self.original_stdout = sys.stdout
        sys.stdout = self.held_output

    def tearDown(self):
        # Restore stdout
        sys.stdout = self.original_stdout
        self.held_output.close()

    def get_output(self):
        # Helper to get captured output
        return self.held_output.getvalue().strip()

    def test_basic_print(self):
        """Test basic print statement"""
        self.interpreter.run('📢 💭"Hello, World!"')
        self.assertIn("Hello, World!", self.get_output())

    def test_variable_assignment(self):
        """Test variable assignment and retrieval"""
        self.interpreter.run('📦x = 42\n📢 📦x')
        self.assertIn("42", self.get_output())

    def test_arithmetic_operations(self):
        """Test basic arithmetic operations"""
        # Addition
        self.interpreter.run('📢 🤜5 🤝 3🤛')
        self.assertIn("8", self.get_output())
        self.held_output.truncate(0)
        self.held_output.seek(0)

        # Subtraction
        self.interpreter.run('📢 🤜10 💔 4🤛')
        self.assertIn("6", self.get_output())
        self.held_output.truncate(0)
        self.held_output.seek(0)

        # Multiplication
        self.interpreter.run('📢 🤜6 💫 7🤛')
        self.assertIn("42", self.get_output())
        self.held_output.truncate(0)
        self.held_output.seek(0)

        # Division
        self.interpreter.run('📢 🤜15 ✂️ 3🤛')
        self.assertIn("5.0", self.get_output())

    def test_if_statement(self):
        """Test if-else control flow"""
        program = '''
        📦x = 10
        🤔 🤜📦x 📈 5🤛 📢 💭"Greater" 🤷 📢 💭"Lesser"
        '''
        self.interpreter.run(program)
        self.assertIn("Greater", self.get_output())

    def test_loop(self):
        """Test loop functionality"""
        program = '''
        📦counter = 0
        🔁 3 📦counter = 🤜📦counter 🤝 1🤛
        📢 📦counter
        '''
        self.interpreter.run(program)
        self.assertIn("3", self.get_output())

    def test_list_operations(self):
        """Test list creation, appending, and retrieval"""
        program = '''
        📋 📦mylist
        📎 📦mylist 42
        📎 📦mylist 17
        📢 🎣 📦mylist 1
        '''
        self.interpreter.run(program)
        self.assertIn("17", self.get_output())

    def test_string_concatenation(self):
        """Test string concatenation"""
        self.interpreter.run('📢 🤜💭"Hello" 🤝 💭" World"🤛')
        self.assertIn("Hello World", self.get_output())

    def test_random_number(self):
        """Test random number generation is within bounds"""
        program = '''
        📦num = 🎲 10
        📢 📦num
        '''
        self.interpreter.run(program)
        output = int(self.get_output().split()[-1])
        self.assertTrue(1 <= output <= 10)

    def test_comparison_operators(self):
        """Test comparison operators"""
        # Greater than
        self.interpreter.run('📢 🤜5 📈 3🤛')
        self.assertIn("True", self.get_output())
        self.held_output.truncate(0)
        self.held_output.seek(0)

        # Less than
        self.interpreter.run('📢 🤜2 📉 4🤛')
        self.assertIn("True", self.get_output())

    def test_sleep_operation(self):
        """Test sleep operation timing"""
        start_time = time.time()
        self.interpreter.run('💤 1')
        elapsed_time = time.time() - start_time
        self.assertTrue(0.9 <= elapsed_time <= 1.1)

    def test_error_handling(self):
        """Test error handling for various scenarios"""
        # Undefined variable
        self.interpreter.run('📢 📦undefined_var')
        self.assertIn("Undefined variable", self.get_output())
        self.held_output.truncate(0)
        self.held_output.seek(0)

        # Invalid list access
        program = '''
        📋 📦mylist
        📢 🎣 📦mylist 5
        '''
        self.interpreter.run(program)
        self.assertIn("Index 5 out of range", self.get_output())

    def test_lexer(self):
        """Test lexer token recognition"""
        lexer = EmojiLexer().build()
        lexer.input('📢 💭"Hello"')
        tokens = [t.type for t in lexer]
        expected = ['PRINT', 'STRING']
        self.assertEqual(tokens, expected)

    def test_parser(self):
        """Test parser AST generation"""
        parser = EmojiParser()
        ast = parser.parse('📢 42')
        self.assertEqual(ast[0][0], 'print')
        self.assertEqual(ast[0][1][0], 'literal')
        self.assertEqual(ast[0][1][1], 42)

if __name__ == '__main__':
    unittest.main()