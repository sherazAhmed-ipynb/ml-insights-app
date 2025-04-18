import streamlit as st

# adding title to the app
st.title("My first app for my model testing")

# adding simple text
st.write("this the simple app testing")

# user input
num = st.slider('Pick a number', 0, 100,30)

# print the text of number
st.write(f"you selected: {num}")

# adding a button to the app
if st.button("Click me"):
    st.write("Button clicked")
else:
    st.write("Button not clicked")

# adding radio button to the app
st.write("Select your favorite moive genre")
options = ["Action", "Comedy", "Drama"]
selected_option = st.radio("Pick one", options)
st.write(f"You selected: {selected_option}")

# adding a drop down list to the app
# option = st.selectbox(
#     "How would you like to be contacted?",
#     ("Email", "Phone", "SMS"))
# st.write(f"You selected: {option}")

# adding a drop down list on the left sidebar to the app
option = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Phone", "SMS"))
st.sidebar.write(f"You selected: {option}")

# adding a text input from the user to the app
# st.sidebar.write("Enter your name below")
name = st.sidebar.text_input("Enter your name")
st.sidebar.write(f"Hello {name}")

# adding a file uploader to the app
upload_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

# adding a drop down list to the app
# option = st.selectbox(

