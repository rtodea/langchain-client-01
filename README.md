# LangChain-Client

A personal project to learn about LLMs.


## Tutorial Pages

1. [LangChain Quick Start](https://python.langchain.com/docs/get_started/quickstart)
2. [Gemini API: Quickstart with Python](https://ai.google.dev/tutorials/python_quickstart)

## Gotchas

### Gemini is not accessible in your region
```
google.api_core.exceptions.FailedPrecondition: 400 User location is not supported for the API use.
```

We are using a [`Colab` instance](https://colab.research.google.com/github/google/generative-ai-docs/blob/main/site/en/tutorials/python_quickstart.ipynb#scrollTo=QvvWFy08e5c5)
running behind Opera's VPN.
