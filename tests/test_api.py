import unittest
from fastapi.testclient import TestClient
from src.api import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_generate_docs(self):
        sample_code = """
from fastapi import FastAPI
app = FastAPI()

@app.get(path="/test")
async def test_endpoint():
    return {"test": "ok"}
"""
        with open("test.py", "w") as f:
            f.write(sample_code)
        
        with open("test.py", "rb") as f:
            response = self.client.post("/generate-docs", files={"file": f})
        
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response.json())
        self.assertIn("openapi_json", response.json())
        self.assertIn("markdown_docs", response.json())

if __name__ == '__main__':
    unittest.main()