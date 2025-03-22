from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama
from langchain.prompts import PromptTemplate

from third_parties.linkedin import scrape_linkedin_profile

if __name__ == "__main__":
    llm_deepseek = ChatOllama(model="deepseek-r1:1.5b")
    llm_llama = ChatOllama(model="llama3.2")


    summary_template = """
    given the LinkedIn information {information} about a person I want you provide:
    1. A short summary.
    2. Two interesting facts about them.

    Do not create a fictional character. Use only the provided information.
    """

    summary_prompt_template = PromptTemplate(input_variables= ["information"], template=summary_template)

    chain = summary_prompt_template | llm_llama | StrOutputParser()
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url="https://gist.githubusercontent.com/archie-arya/ef7558bfa280bf140dd6d87315bca456/raw/16db15cec373393d12d84b0dab94dcd3d4ab49c6/eden-marco_linkedin.json")
    res = chain.invoke(input={"information": linkedin_data})

    print(res)



