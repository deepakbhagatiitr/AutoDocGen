import ast
from typing import List, Dict

def parse_code(code: str) -> Dict:
    """
    Parse a Python codebase to extract API metadata (endpoints, methods, parameters).
    Placeholder for GenAI (e.g., Grok 3) integration.
    
    Args:
        code (str): Source code of the FastAPI app.
    
    Returns:
        Dict: Metadata with endpoints, methods, and parameters.
    """
    try:
        tree = ast.parse(code)
        endpoints = []

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                for decorator in node.decorator_list:
                    if isinstance(decorator, ast.Call):
                        # Check for FastAPI route decorators (e.g., @app.get, @app.post)
                        if isinstance(decorator.func, ast.Attribute):
                            method = decorator.func.attr  # e.g., 'get', 'post'
                            path = None
                            for kw in decorator.keywords:
                                if kw.arg == 'path':
                                    path = kw.value.s if isinstance(kw.value, ast.Str) else None
                            if path and method in ['get', 'post', 'put', 'delete']:
                                params = [arg.arg for arg in node.args.args]
                                endpoints.append({
                                    'path': path,
                                    'method': method.upper(),
                                    'parameters': params
                                })

        return {'endpoints': endpoints}
    except Exception as e:
        return {'error': f'Parsing failed: {str(e)}'}

# Example usage (for testing)
if __name__ == "__main__":
    sample_code = """
from fastapi import FastAPI
app = FastAPI()

@app.get(path="/users")
async def list_users():
    return {"users": []}

@app.post(path="/items")
async def create_item(item_id: int):
    return {"item_id": item_id}
"""
    metadata = parse_code(sample_code)
    print(metadata)