

from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from constants import openai_key
import streamlit as st
from langchain.chains import LLMChain,SequentialChain

template='''I want you to act as a virtual doctor. I will describe my symptoms and you will provide a diagnosis. 
            You should only reply with your diagnosis. Do not write explanations. My first request is 
            {Symptoms}'''


st.title('Medical Bot')
text=st.text_input("Type symptoms")

#prompt template

first_input_prompt=PromptTemplate(
    input_variables=['Symptoms'],
    template=template
)

#we initialize the llm now
llm = ChatOpenAI(openai_api_key=openai_key)
chain=LLMChain(llm=llm,prompt=first_input_prompt,verbose=True,output_key='treatment')

template_2='''Based on the symptoms, you should only reply with your treatment plan. Do not write explanations. My request is 
            {treatment}'''

second_input_prompt=PromptTemplate(
    input_variables=['treatment'],
    template=template_2
)

chain2=LLMChain(llm=llm,prompt=second_input_prompt,verbose=True,output_key='Comments')

parent=SequentialChain(chains=[chain,chain2],input_variables=['Symptoms'],output_variables=['treatment','Comments'],verbose=True)

if text:
    st.write(parent({'Symptoms':text}))

    