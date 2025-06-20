# JSON Compiler – Parser & Validator

A lightweight JSON Parser and Validator built using core Python to simulate concepts from **Compiler Design** such as Lexical Analysis, Parsing, and Semantic Validation.

---

## Project Objective

To create a custom compiler-style tool that parses and validates JSON input, identifying both **syntax** and **semantic** errors (like duplicate keys), without relying on Python's built-in `json` library.

---

## Related to Compiler Design

- **Lexer (Lexical Analyzer)** – Breaks the raw input string into tokens.
- **Parser (Syntax Analyzer)** – Groups tokens into structured objects.
- **Validator (Semantic Analyzer)** – Ensures correctness like no duplicate keys.

---

## How to Run

```bash
# Example: run with valid JSON
python src/main.py examples/valid.json

# Example: run with invalid JSON
python src/main.py examples/invalid.json
```

---


## Features

- Tokenizes JSON into meaningful parts.
- Parses into Python objects (dict, list).
- Validates structure and detects duplicate keys.
- Error handling for malformed input.

---

## Technologies Used

---
- Python 3.12+
- unittest (for testing)

---

## Versioning

This project uses semantic versioning:

Version	Description
- v1.0.0	First working build: Parser + Validator
- v1.1.0	Enhanced error handling
- v2.0.0	Future: Add GUI / Partial parsing support

---

## Future Scope

- GUI interface using Tkinter or PyQt.
- Support for partial validation.
- Integration with web-based tools or APIs.

---

## What's New (v1.1.0)

- Added support for multiple JSON objects in one file.
- Parser now processes each object individually.
- Improved error reporting without stopping after first error.
