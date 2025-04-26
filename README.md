# AutoDocGen – Automated Documentation Generator for APIs

This repository contains the experimental prototype for **AutoDocGen**, a tool that automatically generates API documentation from Python codebases (e.g., FastAPI).

## Overview

AutoDocGen scans API source code, extracts metadata (endpoints, HTTP methods, parameters), and generates documentation in OpenAPI JSON and Markdown formats. The prototype uses **FastAPI** for the API interface and includes placeholder logic for GenAI integration (e.g., Grok 3 via xAI API). Key features include:

- A `/generate-docs` POST endpoint to upload a Python codebase and receive documentation.
- Parsing of FastAPI code to extract endpoints, methods, and parameters.
- Generation of OpenAPI JSON and human-readable Markdown documentation.
- Unit and integration tests to verify functionality.

This repository supports the COT6930 project report by providing the prototype implementation, Mermaid diagrams, and screenshots for Sections 4, 5, and 7.

## Repository Structure

```
AutoDocGen/
├── src/
│   ├── __init__.py
│   ├── parser.py         # Code parsing logic (placeholder for GenAI)
│   ├── generator.py      # Documentation generation logic
│   ├── api.py            # FastAPI app with /generate-docs endpoint
├── tests/
│   ├── __init__.py
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
- **Mermaid Live Editor** (https://mermaid.live/) for rendering diagrams
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

## Generating Screenshots

The COT6930 project report requires three screenshots in **Section 7: Experimental Prototype**. Follow these steps to create them:

1. **FastAPI Endpoint Interface**:

   - Run the server: `uvicorn src.api:app --reload`.
   - Open `http://localhost:8000/docs` in a browser.
   - Navigate to the `/generate-docs` POST endpoint in the Swagger UI.
   - Capture the Swagger UI interface showing the endpoint.
   - Save as `screenshots/fastapi_swagger_ui.png`.

2. **Generated OpenAPI JSON**:

   - Upload `sample.py` via the Swagger UI (see “Test with a Sample Codebase”).
   - Open the generated `output/openapi.json` in VS Code or another code editor.
   - Capture the editor window showing the JSON content (e.g., endpoints like `/users` and `/items`).
   - Save as `screenshots/openapi_json.png`.

3. **Markdown Documentation**:
   - Upload `sample.py` via the Swagger UI.
   - Open the generated `output/docs.md` in a Markdown viewer (e.g., VS Code with Markdown Preview, or paste into GitHub’s Markdown renderer).
   - Capture the rendered Markdown view, showing sections like “Endpoints,” “Parameters,” and “Responses.”
   - Save as `screenshots/markdown_docs.png`.

**Embedding in the Report**:

- **Word Document**: Use **Insert > Pictures** to embed each PNG in Section 7 with captions (e.g., “Figure 4: Uploading a FastAPI codebase to trigger documentation generation”).
- **Markdown**: Use syntax like `![FastAPI Endpoint Interface](screenshots/fastapi_swagger_ui.png)`.

## Rendering Diagrams

The project report includes three Mermaid diagrams in **Sections 4 (Solution Architecture)**, **5.1 (Sequence Diagram)**, and **5.3 (Class Diagram)**. To render them:

1. **Extract Mermaid Code**:

   - Locate the Mermaid code blocks in the project report (e.g., in a Markdown file or Word document provided by the API Innovators group).
   - The code is found under the respective sections:
     - Section 4: Flowchart for Solution Architecture
     - Section 5.1: Sequence Diagram for System Interaction
     - Section 5.3: Class Diagram for System Components

2. **Render in Mermaid Live Editor**:

   - Copy each Mermaid code block into **Mermaid Live Editor** (https://mermaid.live/).
   - Export as PNG files:
     - Section 4: Save as `diagrams/architecture.png`
     - Section 5.1: Save as `diagrams/sequence_diagram.png`
     - Section 5.3: Save as `diagrams/class_diagram.png`

3. **Save to Repository**:
   - Place the PNG files in the `diagrams/` folder.
   - Commit and push to GitHub.

**Embedding in the Report**:

- **Word Document**: Use **Insert > Pictures** to embed each PNG in the respective section with captions (e.g., “Figure 1: Solution Architecture”).
- **Markdown**: Use syntax like `![Solution Architecture](diagrams/architecture.png)`.

## Running Tests

The prototype includes unit and integration tests to verify functionality. To run them:

```bash
python -m unittest discover tests
```

This executes:

- `test_parser.py`: Tests the code parsing logic.
- `test_generator.py`: Tests the OpenAPI JSON and Markdown generation.
- `test_api.py`: Tests the `/generate-docs` endpoint.

## Notes

- **GenAI Integration**: The `src/parser.py` file uses Python’s `ast` module as a placeholder for code parsing. To integrate Grok 3, replace the `parse_code` function with API calls to the xAI API (https://x.ai/api). Obtain an API key and access details from xAI, as referenced in the project report.
- **Scalability**: The prototype is designed for small codebases (<500 lines). For larger codebases, optimize the parsing logic or use a full GenAI model with a larger context window (e.g., 8k tokens, as specified in Section 6).
- **Diagrams**: The diagrams are generated using Mermaid for automation, as required by the project. They are labeled as Mermaid diagrams (flowchart, sequence, class) to align with the project’s automation focus.
- **Screenshots**: The prototype generates the exact outputs needed for the screenshots. Follow the instructions above to capture them consistently with the report’s requirements.
- **FastAPI Familiarity**: The prototype leverages FastAPI, which aligns with your experience in Python and API development (e.g., FastAPI and Django REST Framework).
- **OwlMind Framework**: The prototype supports the multi-agent architecture (Parser Agent, Generator Agent) described in Section 6, with `parser.py` and `generator.py` representing the agents.

## Troubleshooting

- **Server Not Starting**: Ensure all dependencies are installed (`pip install -r requirements.txt`) and Python 3.8+ is used. Check for port conflicts (default: 8000).
- **Parsing Errors**: Verify the uploaded codebase is valid Python with FastAPI route decorators (e.g., `@app.get(path="/endpoint")`).
- **Screenshot Issues**: If the `output/` folder is empty, ensure the `/generate-docs` request was successful. Check the API response for errors.
- **Mermaid Rendering**: If diagrams fail to render, validate the Mermaid syntax in **Mermaid Live Editor** and ensure no typos in the code blocks.

For additional help, refer to the FastAPI documentation (https://fastapi.tiangolo.com/) or contact the API Innovators group.

## License

This project is for educational purposes and does not include a formal license.
