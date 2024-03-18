from langchain.llms import OpenAI
from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv() #take environment variable from .env file

#function to load OpenAi model and get response
def get_openai_response(question):
    llm=OpenAI(openai_api_key = os.getenv('OPEN_API_KEY'),model_name = "gpt-3.5-turbo-instruct", temperature = 0.5)
    response = llm(question)
    return response

#intialize streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("MyLangchain application")
input=  st.text_input("Input:", key="input")
response = get_openai_response(input)
submit = st.button("Enter your question")

if submit:
    st.subheader("Result")
    st.write(response)

