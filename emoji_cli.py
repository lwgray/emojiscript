#!/usr/bin/env python3
import sys
import os
import argparse
from prompt_toolkit import PromptSession
from prompt_toolkit.lexers import PygmentsLexer
from pygments.lexers import Python3Lexer
from termcolor import colored

from emoji import EmojiInterpreter

class EmojiScriptCLI:
    def __init__(self):
        self.interpreter = EmojiInterpreter()
        self.session = PromptSession()
        
    def run_file(self, filename):
        """Run an EmojiScript file"""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
                print(colored(f"🚀 Running {filename}...\n", 'cyan'))
                self.interpreter.run(content)
        except FileNotFoundError:
            print(colored(f"😱 File not found: {filename}", 'red'))
        except Exception as e:
            print(colored(f"😱 Error: {str(e)}", 'red'))

    def run_repl(self):
        """Run interactive REPL"""
        print(colored("""
🎮 Welcome to EmojiScript REPL! 🎮
Type your code (use Ctrl+D or Ctrl+C to exit)
Commands: help, examples, exit
Try: 📢 💭"Hello, World! 👋"
        """, 'cyan'))

        while True:
            try:
                code = self.session.prompt("emoji> ")
                
                # Skip empty lines
                if not code.strip():
                    continue
                
                # Handle special commands
                if code.strip() == 'exit':
                    break
                elif code.strip() == 'help':
                    self.print_help()
                    continue
                elif code.strip() == 'examples':
                    self.print_examples()
                    continue
                
                # Run the code
                self.interpreter.run(code)
                
            except KeyboardInterrupt:
                continue
            except EOFError:
                break
            except Exception as e:
                print(colored(f"😱 Error: {str(e)}", 'red'))
        
        print("\n👋 Goodbye!")

    def print_help(self):
        """Print help information"""
        help_text = """
📚 EmojiScript Quick Reference 📚

Output:
📢 - Print statement (e.g., 📢 💭"Hello!")

Variables:
📦 - Variable declaration (e.g., 📦x = 10)

Math Operations:
🤝 - Addition
💔 - Subtraction
💫 - Multiplication
✂️ - Division

Control Flow:
🤔 - If statement
🤷 - Else statement
🔁 - Loop

Comparisons:
📈 - Greater than
📉 - Less than

Data Types:
💭 - String (e.g., 💭"Hello")
🔢 - Numbers (just type them directly)

Lists:
📋 - Create list
📎 - Append to list
🎣 - Get from list

Special:
🎲 - Random number
💤 - Sleep/pause

Grouping:
🤜 - Left parenthesis
🤛 - Right parenthesis

Commands:
help     - Show this help
examples - Show example code
exit     - Exit REPL
"""
        print(colored(help_text, 'cyan'))

    def print_examples(self):
        """Print example code"""
        examples = """
📎 Example Programs 📎

1. Hello World:
   📢 💭"Hello, World! 👋"

2. Variables and Math:
   📦x = 10
   📦y = 5
   📢 🤜📦x 🤝 📦y🤛

3. If-Else Statement:
   📦num = 7
   🤔 🤜📦num 📈 5🤛 
       📢 💭"Big number!"
   🤷
       📢 💭"Small number!"

4. Loop:
   📦counter = 0
   🔁 3 {
       📦counter = 🤜📦counter 🤝 1🤛
       📢 📦counter
   }

5. Lists:
   📋 📦mylist
   📎 📦mylist 42
   📢 🎣 📦mylist 0

6. Random Numbers:
   📢 🎲 10
"""
        print(colored(examples, 'cyan'))

def main():
    parser = argparse.ArgumentParser(description='EmojiScript Interpreter')
    parser.add_argument('file', nargs='?', help='EmojiScript file to run')
    args = parser.parse_args()

    cli = EmojiScriptCLI()
    
    if args.file:
        cli.run_file(args.file)
    else:
        cli.run_repl()

if __name__ == '__main__':
    main()