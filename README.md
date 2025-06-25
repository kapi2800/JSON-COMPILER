# JSON Compiler & Validator

This project is a **lightweight compiler and validator for JSON (JavaScript Object Notation)**, created as part of a **Project-Based Learning (PBL)** curriculum in my college. It applies compiler design concepts such as **Lexical Analysis**, **Parsing**, and **Semantic Validation** specifically tailored to JSON structures.

---

## Why I Made This

This project was built as my **college PBL (Project-Based Learning) submission**, carried out in **three progressive phases**:

1. **Phase 1 – Introduction**: Defined the project scope — to simulate a JSON validator using compiler stages.
2. **Phase 2 – Development**: Implemented core modules to parse and validate a single JSON object.
3. **Phase 3 – Final Update**: 
   - Extended support to **multiple JSON objects** (arrays of JSON).
   - Added a **Graphical User Interface (GUI)** using `Tkinter` for easier and more user-friendly operation.

All design, implementation, testing, and documentation were done independently.

---

## Demo

![Demo](./demo.gif)

---

## Objective

To build a compiler-inspired tool that can:
- Tokenize JSON strings
- Parse them into structured data
- Validate semantic correctness (e.g., duplicate keys, structure)

This tool is helpful in data validation scenarios where incorrect or malformed JSON can lead to failures in real systems.

---

## Features

- **Lexical Analyzer**: Extracts tokens (`{`, `:`, strings, numbers, etc.) using regular expressions.
- **Parser**: Implements **recursive descent** parsing to build Python dictionaries/lists.
- **Semantic Validator**:
  - Detects **duplicate keys** within objects.
  - Handles invalid structures or types.
- **Multi-JSON Support**: Accepts arrays of JSON objects and validates each individually.
- **Error Reporting**: Detailed, readable messages.
- **GUI (Tkinter)**: Simple UI to load and validate files without the command line.
    
---

## User Interface (UI)

Created a GUI using Tkinter for users who prefer clicking over command-line typing.

#### Run using:

 python src/ui.py 

---

## Features:

- File selector
- Scrollable output

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
- v2.0.0	Added GUI / Multi Json support

---

## Usage

#### CLI:
- python src/main.py examples/valid.json
  
#### GUI:
- python src/ui.py

---

## Project Outcome

- Developed full compiler simulation for JSON
- Validates both single and multiple JSON objects
- Modular and testable architecture
- Simple UI for non-technical users
- Uploaded and maintained as a final GitHub submission

---

## Final Note

This was a self-built, end-to-end academic project with no external collaboration.
Created and submitted as part of my college's PBL requirement to apply theoretical concepts in a practical environment.
