import json
from typing import Dict

def generate_openapi(metadata: Dict) -> str:
    """
    Generate OpenAPI JSON from parsed metadata.
    
    Args:
        metadata (Dict): Extracted endpoints and parameters.
    
    Returns:
        str: OpenAPI JSON as a string.
    """
    openapi = {
        "openapi": "3.0.0",
        "info": {"title": "AutoDocGen API", "version": "1.0"},
        "paths": {}
    }

    for endpoint in metadata.get('endpoints', []):
        path = endpoint['path']
        method = endpoint['method'].lower()
        openapi['paths'][path] = openapi['paths'].get(path, {})
        openapi['paths'][path][method] = {
            "summary": f"{method.upper()} endpoint for {path}",
            "parameters": [
                {"name": param, "in": "query", "required": False, "schema": {"type": "string"}}
                for param in endpoint.get('parameters', [])
            ],
            "responses": {
                "200": {"description": "Success" if method != 'post' else "Created"}
            }
        }

    return json.dumps(openapi, indent=2)

def generate_markdown(metadata: Dict) -> str:
    """
    Generate Markdown documentation from parsed metadata.
    
    Args:
        metadata (Dict): Extracted endpoints and parameters.
    
    Returns:
        str: Markdown documentation as a string.
    """
    markdown = "# API Documentation\n\n## Endpoints\n\n"
    for endpoint in metadata.get('endpoints', []):
        markdown += f"### {endpoint['method']} {endpoint['path']}\n"
        markdown += f"- **Description**: {endpoint['method']} endpoint for {endpoint['path']}\n"
        markdown += f"- **Parameters**: {', '.join(endpoint.get('parameters', [])) or 'None'}\n"
        markdown += f"- **Responses**: 200 {'Created' if endpoint['method'] == 'POST' else 'OK'}\n\n"
    return markdown

# Example usage (for testing)
if __name__ == "__main__":
    sample_metadata = {
        'endpoints': [
            {'path': '/users', 'method': 'GET', 'parameters': []},
            {'path': '/items', 'method': 'POST', 'parameters': ['item_id']}
        ]
    }
    openapi_json = generate_openapi(sample_metadata)
    markdown_docs = generate_markdown(sample_metadata)
    with open("openapi.json", "w") as f:
        f.write(openapi_json)
    with open("docs.md", "w") as f:
        f.write(markdown_docs)
    print("Generated openapi.json and docs.md")