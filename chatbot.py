import openai
import streamlit as st
from streamlit_chat import message


openai.api_key = st.secrets["api_secret"]

def generate_response(prompt):
    completions = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        prompt = prompt,
        messages = [{'role':'user','content' : 'Hello!'}],
        max_tokens = 1024,
        n = 1,
        stop = None,
        temperature=0,
    )
    message = completions.choices[0].message.content
    return message 

# Fake ChatAI Interface
st.title("Fake ChatAI")


# Storing the chat 
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

# Get the user Input
def get_text():
    input_text = st.text_input("You: ","Hello, how are you?", key="input")
    return input_text

# Return the user input
user_input = get_text()

if user_input:
    output = generate_response(user_input)
    # store the output 
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)


# Generating chat history
if st.session_state['generated']:
    
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')