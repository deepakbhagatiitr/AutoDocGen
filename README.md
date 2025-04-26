# AutoDocGen – Automated Documentation Generator for APIs

This repository contains the experimental prototype for **AutoDocGen**, a tool that automatically generates API documentation from Python codebases (e.g., FastAPI).

## Overview

AutoDocGen scans API source code, extracts metadata (endpoints, HTTP methods, parameters), and generates documentation in OpenAPI JSON and Markdown formats. The prototype uses **FastAPI** for the API interface and includes placeholder logic for GenAI integration (e.g., Grok 3 via xAI API). Key features include:

- A `/generate-docs` POST endpoint to upload a Python codebase and receive documentation.
- Parsing of FastAPI code to extract endpoints, methods, and parameters.
- Generation of OpenAPI JSON and human-readable Markdown documentation.
- Unit and integration tests to verify functionality.

## Repository Structure

```
AutoDocGen/
├── src/
│   ├── __init__.py
│   ├── parser.py         # Code parsing logic (placeholder for GenAI)
│   ├── generator.py      # Documentation generation logic
│   ├── api.py            # FastAPI app with /generate-docs endpoint
├── tests/
│   ├── test_parser.py    # Unit tests for parser
│   ├── test_generator.py # Unit tests for generator
│   ├── test_api.py       # Integration tests for API
├── diagrams/
│   ├── architecture.png  # Mermaid flowchart (Solution Architecture)
│   ├── sequence_diagram.png # Mermaid sequence diagram (System Interaction)
│   ├── class_diagram.png # Mermaid class diagram (System Components)
├── screenshots/
│   ├── fastapi_swagger_ui.png # FastAPI Swagger UI
│   ├── openapi_json.png      # Generated OpenAPI JSON
│   ├── markdown_docs.png     # Generated Markdown documentation
├── README.md                # This file
├── requirements.txt         # Python dependencies
```

## Prerequisites

- **Python 3.8+**
- **pip** for installing dependencies
- **Git** for cloning the repository
- **VS Code** or another editor for viewing JSON/Markdown files
- A browser (e.g., Chrome) for accessing the FastAPI Swagger UI

## Setup

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/deepakbhagatiitr/AutoDocGen.git
   cd AutoDocGen
   ```

2. **Create a Virtual Environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   This installs `fastapi`, `uvicorn`, and `python-multipart` as specified in `requirements.txt`.

## Running the Prototype

1. **Start the FastAPI Server**:

   ```bash
   uvicorn src.api:app --reload
   ```

   The server will run at `http://localhost:8000`.

2. **Access the Swagger UI**:

   - Open `http://localhost:8000/docs` in a browser.
   - Use the `/generate-docs` POST endpoint to upload a Python codebase (e.g., a FastAPI app file).

3. **Test with a Sample Codebase**:
   Create a file named `sample.py` with the following content:

   ```python
   from fastapi import FastAPI
   app = FastAPI()

   @app.get(path="/users")
   async def list_users():
       return {"users": []}

   @app.post(path="/items")
   async def create_item(item_id: int):
       return {"item_id": item_id}
   ```

   - In the Swagger UI (`http://localhost:8000/docs`), select the `/generate-docs` endpoint.
   - Upload `sample.py` using the file input.
   - Execute the request to generate documentation.

4. **View Generated Documentation**:
   - The API response includes OpenAPI JSON and Markdown documentation in the JSON payload.
   - Files are saved in the `output/` folder as `openapi.json` and `docs.md`.
   - Check the `output/` folder (created automatically) for the generated files.

## Notes

- **GenAI Integration**: The `src/parser.py` file uses Python’s `ast` module as a placeholder for code parsing. To integrate Grok 3, replace the `parse_code` function with API calls to the xAI API (https://x.ai/api). Obtain an API key and access details from xAI, as referenced in the project report.
- **Scalability**: The prototype is designed for small codebases (<500 lines). For larger codebases, optimize the parsing logic or use a full GenAI model with a larger context window (e.g., 8k tokens, as specified in Section 6).
- **Diagrams**: The diagrams are generated using Mermaid for automation, as required by the project.
- **Screenshots**: The prototype generates the exact outputs needed for the screenshots.
- **FastAPI Familiarity**: The prototype leverages FastAPI, which aligns with your experience in Python and API development (e.g., FastAPI and Django REST Framework).

## Troubleshooting

- **Server Not Starting**: Ensure all dependencies are installed (`pip install -r requirements.txt`) and Python 3.8+ is used. Check for port conflicts (default: 8000).
- **Parsing Errors**: Verify the uploaded codebase is valid Python with FastAPI route decorators (e.g., `@app.get(path="/endpoint")`).
- **Screenshot Issues**: If the `output/` folder is empty, ensure the `/generate-docs` request was successful. Check the API response for errors.
- **Mermaid Rendering**: If diagrams fail to render, validate the Mermaid syntax in **Mermaid Live Editor** and ensure no typos in the code blocks.

For additional help, refer to the FastAPI documentation (https://fastapi.tiangolo.com/) or contact the API Innovators group.

## License

This project is for educational purposes and does not include a formal license.
