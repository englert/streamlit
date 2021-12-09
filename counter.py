import streamlit as st

st.title('Counter')

if 'count' not in st.session_state:
	st.session_state.count = 0

increment = st.button('Increment')
if increment:
    st.session_state.count += 1

decrement = st.button('Decrement')
if decrement:
    st.session_state.count -= 1

st.write('Count = ', st.session_state.count)

 
# Title
st.title("Hello GeeksForGeeks !!!")

# Header
st.header("This is a header")
 
# Subheader
st.subheader("This is a subheader")
