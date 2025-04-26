import unittest
from src.parser import parse_code

class TestParser(unittest.TestCase):
    def test_parse_code(self):
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
        expected = {
            'endpoints': [
                {'path': '/users', 'method': 'GET', 'parameters': []},
                {'path': '/items', 'method': 'POST', 'parameters': ['item_id']}
            ]
        }
        self.assertEqual(metadata, expected)

if __name__ == '__main__':
    unittest.main()