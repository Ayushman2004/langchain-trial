import lc_helper as lch
import streamlit as st

st.title("Pets name generator")

animal_type = st.sidebar.selectbox("Whats your pet?", ("Cat", "Dog", "Cow", "Rabbit", "Dino"))
pet_color = st.sidebar.text_area("And the color?", max_chars = 15)

if pet_color:
    res = lch.gen_pet_name(animal_type, pet_color)
    st.write(res["pet_names"])