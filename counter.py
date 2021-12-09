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

# Markdown
st.markdown("### This is a markdown")

# success
st.success("Success")
 
# success
st.info("Information")
 
# success
st.warning("Warning")
 
# success
st.error("Error")

# Write text
st.write("Text with write")
 
# Writing python inbuilt function range()
st.write(range(10))

# Display Images
 
# import Image from pillow to open images
from PIL import Image
img = Image.open("streamlit.png")
 
# display image using streamlit
# width is used to set the width of an image
st.image(img, width=200)
