# EmojiScript 🎮

EmojiScript is a fun programming language that uses emojis as operators and keywords. It features a rich set of operations, an interactive REPL with syntax highlighting, and a file execution mode.

## Features ✨

- Interactive REPL with syntax highlighting
- File execution mode
- Rich set of operators and commands
- Colorful terminal output
- Helpful built-in examples and documentation

## Installation 🚀

1. Ensure you have Python 3.6+ installed
2. Install the required dependencies:
```bash
pip install prompt_toolkit pygments termcolor
```
3. Clone this repository:
```bash
git clone https://github.com/lwgray/emojiscript
cd emojiscript
```

## Usage 💻

### Interactive REPL
Start the interactive REPL by running:
```bash
python emoji_cli.py
```

In the REPL, you can:
- Type code directly
- Use `help` to see available commands
- Use `examples` to see example code
- Use `exit` to quit
- Use Ctrl+D or Ctrl+C to exit

### File Execution
Run an EmojiScript file:
```bash
python emoji_cli.py yourscript.ejs
```

## Language Reference 📚

### Output
- 📢 - Print statement
  ```
  📢 💭"Hello, World! 👋"
  ```

### Variables
- 📦 - Variable declaration
  ```
  📦x = 10
  ```

### Math Operations
- 🤝 - Addition
- 💔 - Subtraction
- 💫 - Multiplication
- ✂️ - Division

### Control Flow
- 🤔 - If statement
- 🤷 - Else statement
- 🔁 - Loop

### Comparisons
- 📈 - Greater than
- 📉 - Less than

### Data Types
- 💭 - String
- 🔢 - Numbers (direct input)

### Lists
- 📋 - Create list
- 📎 - Append to list
- 🎣 - Get from list

### Special Operations
- 🎲 - Random number
- 💤 - Sleep/pause

### Grouping
- 🤜 - Left parenthesis
- 🤛 - Right parenthesis

## Example Programs 📝

### Hello World
```
📢 💭"Hello, World! 👋"
```

### Variables and Math
```
📦x = 10
📦y = 5
📢 🤜📦x 🤝 📦y🤛
```

### If-Else Statement
```
📦num = 7
🤔 🤜📦num 📈 5🤛 📢 💭"Big number!" 🤷 📢 💭"Small number!"
```

### Loop
```
📦counter = 0
🔁 3 📦counter = 🤜📦counter 🤝 1🤛
📢 📦counter
```

### Lists
```
📋 📦mylist
📎 📦mylist 42
📎 📦mylist 42
📎 📦mylist 17
📢 🎣 📦mylist 2
```

### Random Numbers
```
📢 🎲 10
```

## Error Handling 🚨

EmojiScript provides clear, emoji-enhanced error messages for common issues:
- File not found errors
- Syntax errors
- Runtime errors

## Development 🛠️

### Project Structure
```
emojiscript/
├── emoji_cli.py     # CLI interface
├── emoji.py         # Core interpreter
├── README.md        # Documentation
└── test_emoji.py    # Unittests
```

### Running Tests
```bash
python -m unittest test_emoji.py
```

## Contributing 🤝

Contributions are welcome! Areas for improvement:
- Adding new emoji operators
- Improving error messages
- Adding more examples
- Enhancing the REPL
- Writing documentation

## License 📝

This project is licensed under the MIT License - see the LICENSE file for details.

## Credits 👏

EmojiScript was created as a fun way to learn about:
- Lexers and parsers
- Interpreter design
- REPL interfaces
- Command-line tools

## Version History 📅

- 1.0.0
  - Interactive REPL with syntax highlighting
  - File execution mode
  - Complete set of mathematical operators
  - Control flow statements
  - List operations
  - Built-in help and examples
