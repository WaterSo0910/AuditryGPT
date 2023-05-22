# pip install streamlit streamlit-chat langchain python-dotenv
import streamlit as st
from type import Result
from dotenv import load_dotenv
import os
from typing import List
from audit import audit



def init():
    # Load the OpenAI API key from the environment variable
    load_dotenv()
    
    # test that the API key exists
    if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY") == "":
        print("OPENAI_API_KEY is not set")
        exit(1)
    else:
        print("OPENAI_API_KEY is set")

    # setup streamlit page
    st.set_page_config(
        page_title="Your own ChatGPT",
        page_icon="🤖"
    )

def main():
    init()
    # sidebar with user input
    results: list[Result] = []
    with st.sidebar:
        user_input = st.text_area("Contract: ", "// code here")
        # handle user input
        if user_input:
            with st.spinner("Thinking..."):
                results = audit(user_input)
    st.header("Audit AI for you 🤖")
    for result in results:
        st.code(result.function, language="sol", line_numbers=True)
        st.write(result.audit)
        st.divider()

if __name__ == '__main__':
    main()
