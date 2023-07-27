import os
import streamlit as st
from dotenv import load_dotenv
import uuid
from langchain import PromptTemplate
from langchain.llms import OpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

def load_openai_key():
    load_dotenv()
    openai_key = os.getenv('OPENAI_API_KEY')
    return openai_key

def initialize_llm(openai_key):
    llm = OpenAI(openai_api_key=openai_key)
    return llm

def main():
    openai_key = load_openai_key()
    llm = initialize_llm(openai_key)
    
    st.header("GHOSTWRITEIT.AI")
    

    #input_text = st.text_area(label="Enter idea for your book", placeholder="What is your idea?", key=uuid.uuid4())
    input_text = st.text_area(label="Enter idea for your book", placeholder="What is your idea?", key="text_area1")

    if input_text:
        st.write("You entered: ", input_text)
    
    # Add the "Generate" button
    if st.button("Generate"):
        if input_text:
            # Set up the chat prompt
            template = f"""
            You are a helpful writing assistant called ghostwriteIt.ai. 
            User is going to tell you what they want to write i.e., book, Journal, Article, Academic document. 
            Acknowledge their choice and ask them for extra information so you can 
            formulate titles for what they wantt to write about.
            User: {input_text}"""
            system_message_prompt = SystemMessagePromptTemplate.from_template(template)
            human_template = input_text
            human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

            #chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

            # Format the messages
            #formatted_messages = chat_prompt.format_messages(input_text)

            output = llm.predict(template, max_tokens=100, temperature=0.9)
            print(output)
            st.write(output)
        else:
            st.error("Please enter some text to generate")

if __name__ == "__main__":
    main()
