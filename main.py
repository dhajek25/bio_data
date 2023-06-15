import streamlit as st
import pandas as pd

from functions import dna_nucleotides_count, transcription, complement, reverse_complement
from helper_functions import is_dna_valid, upper_letters

header = st.container()
body = st.container()

with header:
    st.title('Welcome to DNA Analyzator!')
    st.text('Hakuna Matata')

with body:
    st.header('Choose the Function')

    function_tuple = ("Nucleotides Count", "Transcription", "Complement", "Reverse Complement")

    user_input = upper_letters(st.text_input("Enter your DNA: "))
    selected_function = st.selectbox("Select a function:", function_tuple)

    st.text('You can try: AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC')

    is_dna_valid = is_dna_valid(user_input)

    if len(is_dna_valid) <= 0:

        if st.button("Apply"):
            if selected_function == "Nucleotides Count":
                result = dna_nucleotides_count(user_input)

                df = pd.DataFrame.from_dict(result, orient='index', columns=['Count'])

                st.bar_chart(df['Count'])

            elif selected_function == "Transcription":
                result = transcription(user_input)

            elif selected_function == "Complement":
                result = complement(user_input)

            elif selected_function == "Complement":
                result = complement(user_input)

            elif selected_function == "Reverse Complement":
                result = reverse_complement(user_input)

            else:
                result = "No function selected."

            st.write("Result:", result)

    else:
        st.warning(f"The entered DNA contains invalid symbols: {is_dna_valid}! Valid symbols/nucleotides are 'A', 'T', 'C', 'G'!")