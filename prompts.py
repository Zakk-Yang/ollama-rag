# prompts.py

from llama_index.core import PromptTemplate

qa_prompt_tmpl_str = (
    "Context information is below.\n"
    "---------------------\n"
    "{context_str}\n"
    "---------------------\n"
    "Given the context information above I want you to think step by step to answer the query in a crisp manner, "
    "in case you don't know the answer say 'I don't know!'.\n"
    "Query: {query_str}\n"
    "Answer: "
)
qa_prompt_template = PromptTemplate(qa_prompt_tmpl_str)
