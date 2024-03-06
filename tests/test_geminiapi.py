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
    for m in genai.list_models():
        if "generateContent" in m.supported_generation_methods:
            print(m.name)
