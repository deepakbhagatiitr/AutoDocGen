import ast
from typing import List, Dict

def parse_code(code: str) -> Dict:
    """
    Parse a Python codebase to extract API metadata (endpoints, methods, parameters).
    Args:
        code (str): Source code of the FastAPI app.
    
    Returns:
        Dict: Metadata with endpoints, methods, and parameters.
    """
    try:
        tree = ast.parse(code)
        endpoints = []

        # Walk through the AST to find function definitions
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                print(f"Function: {node.name}")  # Debug: Print function name

                for decorator in node.decorator_list:
                    print(f"  Decorator: {ast.dump(decorator)}")  # Debug: Print decorator details

                    # Handle decorators like @app.get, @app.post, etc.
                    if isinstance(decorator, ast.Call):
                        # We are looking for method like 'get', 'post', etc.
                        if isinstance(decorator.func, ast.Attribute):
                            method = decorator.func.attr.lower()  # e.g., 'get', 'post'
                            path = None

                            # Check if decorator has 'path' as a keyword argument
                            for kw in decorator.keywords:
                                if kw.arg == 'path' and isinstance(kw.value, ast.Constant):
                                    path = kw.value.value

                            # Handle decorators that have path as an argument (e.g., @app.get("/users"))
                            if not path and isinstance(decorator.args[0], ast.Constant):
                                path = decorator.args[0].value

                            if path and method in ['get', 'post', 'put', 'delete']:
                                # Extract parameters from function arguments
                                params = [arg.arg for arg in node.args.args if not arg.arg.startswith('__')]
                                print(f"  Endpoint: {method.upper()} {path} -> Params: {params}")  # Debug
                                endpoints.append({
                                    'path': path,
                                    'method': method.upper(),
                                    'parameters': params
                                })

        return {'endpoints': endpoints} if endpoints else {'endpoints': []}
    except Exception as e:
        return {'error': f'Parsing failed: {str(e)}'}

# Example usage (for testing)
if __name__ == "__main__":
    sample_code = """
from fastapi import FastAPI
app = FastAPI()

@app.get("/users")
async def list_users():
    return {"users": []}

@app.post("/items")
async def create_item(item_id: int):
    return {"item_id": item_id}
"""
    metadata = parse_code(sample_code)
    print(metadata)
