# Python Project Template

A well-structured Python project template with best practices.

## Project Structure

```
.
├── src/
│   └── myproject/
│       ├── __init__.py
│       ├── main.py
│       └── utils.py
├── tests/
│   ├── __init__.py
│   ├── test_main.py
│   └── test_utils.py
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
└── pyproject.toml
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/LeonardoFariaPBi/Python.git
cd Python
```

2. (Optional) Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Install the package in development mode:
```bash
pip install -e .
```

## Running the Code

You can run the main module directly:
```bash
python src/myproject/main.py
```

## Running Tests

Run all tests:
```bash
python -m pytest tests/
```

Or run individual test files:
```bash
python tests/test_main.py
python tests/test_utils.py
```

## Development

To install development dependencies:
```bash
pip install -e ".[dev]"
```

This will install pytest and other development tools.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.