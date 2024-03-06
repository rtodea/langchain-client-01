from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from pytest import fixture

from tests.assertions import assert_env


@fixture(autouse=True)
def run_before_and_after_tests():
    load_dotenv("../.env")
    assert_env(["LANGCHAIN_API_KEY",
                "OPENAI_API_KEY", ])


def test_openai():
    llm = ChatOpenAI()
    assert llm is not None


def test_composition():
    llm = ChatOpenAI()
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are world class technical documentation writer."),
        ("user", "{input}")])
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    response = chain.invoke({"input": "how can langsmith help with testing?"})
    assert str is type(response)
