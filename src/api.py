from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from src.parser import parse_code
from src.generator import generate_openapi, generate_markdown
import os

app = FastAPI(title="AutoDocGen API")

@app.post("/generate-docs")
async def generate_docs(file: UploadFile = File(...)):
    """
    Upload a Python codebase and generate API documentation.
    
    Args:
        file (UploadFile): Python source code file.
    
    Returns:
        JSONResponse: Generated OpenAPI JSON and Markdown documentation.
    """
    try:
        # Read uploaded file
        code = (await file.read()).decode('utf-8')
        
        # Parse code to extract metadata
        metadata = parse_code(code)
        if 'error' in metadata:
            return JSONResponse(status_code=400, content={"error": metadata['error']})
        
        # Generate documentation
        openapi_json = generate_openapi(metadata)
        markdown_docs = generate_markdown(metadata)
        
        # Save outputs for screenshots
        output_dir = "output"
        os.makedirs(output_dir, exist_ok=True)
        with open(os.path.join(output_dir, "openapi.json"), "w") as f:
            f.write(openapi_json)
        with open(os.path.join(output_dir, "docs.md"), "w") as f:
            f.write(markdown_docs)
        
        return {
            "message": "Documentation generated",
            "openapi_json": openapi_json,
            "markdown_docs": markdown_docs
        }
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": f"Failed to generate documentation: {str(e)}"})
