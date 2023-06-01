import streamlit as st
import pandas as pd

from functions import dna_nucleotides_count, test_function

header = st.container()
body = st.container()

with header:
    st.title('Welcome to DNA Analyzator!')
    st.text('Hakuna Matata')

with body:
    st.header('Choose the Function')

    function_tuple = ("Nucleotides Count", "Test Function")

    user_input = st.text_input("Enter your DNA: ")
    selected_function = st.selectbox("Select a function:", function_tuple)

    st.text('You can try: AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC')

    if st.button("Apply"):
        if selected_function == "Nucleotides Count":
            result = dna_nucleotides_count(user_input)

            df = pd.DataFrame.from_dict(result, orient='index', columns=['Count'])

            st.bar_chart(df['Count'])

        elif selected_function == "Test Function":
            result = test_function(user_input)
        else:
            result = "No function selected."

        st.write("Result:", result)