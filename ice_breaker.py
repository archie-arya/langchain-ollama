from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama
from langchain.prompts import PromptTemplate
if __name__ == "__main__":
    llm = ChatOllama(model="deepseek-r1:1.5b")
    information = """
    elon musk is a businessman and investor he is the founder and a member of wealthy south african musk family. in 2022 he aquired paypal and the same year he bought twitter and renamed it to X
    """
    summary_template = """
    You are an AI assistant that provides factual summaries. Given the following information about a person:

    {information}

    Please provide:
    1. A short factual summary.
    2. Two verifiable facts about them.

    Do not create a fictional character. Use only the provided information.
    """

    summary_prompt_template = PromptTemplate(input_variables= ["information"], template=summary_template)

    chain = summary_prompt_template | llm | StrOutputParser()
    res = chain.invoke(input={"information": information})

    print(res)



