# Contributing to AI Chatbot

We welcome contributions! Please follow these guidelines to ensure code quality.

## Development Setup

1. **Fork** the repository.
2. **Clone** your fork.
3. **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    python -m nltk.downloader punkt stopwords
    ```

4. **Create a Branch**: `git checkout -b feature/amazing-feature`

## Coding Standards

* **Style**: Follow PEP 8.
* **Type Hints**: Use type hints for function arguments and return values.
* **Docstrings**: All public functions and classes must have docstrings.
* **Testing**: Add unit tests for new logic in `tests/`.

## Pull Request Process

1. Ensure all tests pass: `python -m pytest`.
2. Update `README.md` if you change functionality.
3. Submit a PR with a clear description of changes.

## License

By contributing, you agree that your code will be licensed under the project's MIT License.
