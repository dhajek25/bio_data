import pandas as pd
import datetime
import os

from streamlit_option_menu import option_menu

import dtb_connection as dtb

# Importing the required functions and classes from external modules
from functions import dna_nucleotides_count, transcription, complement, reverse_complement, DNAProcessor
from helper_functions import is_dna_valid, upper_letters

from protein_visualization import *
from model_classification_class import classify_protein

st.set_page_config(page_title="Analyse yourself!", layout="centered")
st.title("DNA Analyzator")


selected_menu = option_menu(menu_title=None,
            options=["Data Entry", "Data Visualization", "Protein Classification"],
            icons=["pencil_fill", "bar-chart-fill"],
            orientation="horizontal")

# Populating the main body content

if selected_menu == "Data Entry":

    st.header('Choose the Function')

    # List of functions available for users to choose from
    function_tuple = ("Nucleotides Count", "Transcription", "Complement", "Reverse Complement", 'Protein Creation')

    # Taking DNA input from user and converting it to uppercase
    user_input = upper_letters(st.text_input("Enter your DNA: "))

    # Dropdown menu for users to select the function they want to apply on their DNA input
    selected_function = st.selectbox("Select a function:", function_tuple)

    # Suggesting a sample DNA sequence for the users to try out
    st.text('You can try: AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC')

    # Check if user's DNA input is valid
    # If users input contains invalid symbols, the function returns a list of invalid symbols
    # If users input is valid, the function returns an empty list
    is_dna_valid = is_dna_valid(user_input)

    # If the DNA is valid, execute the following
    if len(is_dna_valid) <= 0:

        # Creating an instance of DNAProcessor with user_input
        processor = DNAProcessor(user_input)

        # When the user clicks on the "Apply" button, execute the following
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

            elif selected_function == "Protein Creation":

                proteins = processor.process('aminoacids_combination.json')
                result = "".join(proteins)

                # protein_fold(result)

            # Displaying the result to the user
            else:
                result = "No function selected."

            # Define string str_date, where you will write the actual date and time
            str_date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

            dtb.insert_result(str_date, result)

            st.write("Result:", result)

    # If the DNA is not valid, display a warning message
    else:
        st.warning(f"The entered DNA contains invalid symbols: {is_dna_valid}! Valid symbols/nucleotides are 'A', 'T', 'C', 'G'!")

if selected_menu == "Data Visualization":

    data_list = dtb.fetch_result()

    options = [item['result'] for item in data_list]

    selected_option = st.selectbox("Choose a result:", options)

    if st.button("Select Result"):

        st.write("You selected:", selected_option.split(" (")[0])

    #choosen_result = data_list[0]['result']

    #protein_fold(choosen_result)
    #st.write(choosen_result)

if selected_menu == "Protein Classification":

    data_list = dtb.fetch_result()

    options = [item['result'] for item in data_list]

    selected_option = st.selectbox("Choose a result:", options)

    if st.button("Select Result"):

        protein_class = classify_protein(selected_option)

        st.write("Your protein belongs to:", protein_class)