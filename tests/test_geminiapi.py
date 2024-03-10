import os

from _pytest.fixtures import fixture
from dotenv import load_dotenv

from tests.assertions import assert_env
import google.generativeai as genai


@fixture(autouse=True)
def run_before_and_after_tests():
    load_dotenv("../.env")
    assert_env(["LANGCHAIN_API_KEY",
                "GEMINI_API_KEY", ])
    genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))


def test_gemini_api_has_models():
    existing_models = [m.name for m in genai.list_models() if "generateContent" in m.supported_generation_methods]
    assert set(existing_models) == {
        "models/gemini-1.0-pro",
        "models/gemini-1.0-pro-001",
        "models/gemini-1.0-pro-latest",
        "models/gemini-1.0-pro-vision-latest",
        "models/gemini-pro",
        "models/gemini-pro-vision"}

