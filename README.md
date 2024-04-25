# DNA Analyzator

## Description
The DNA Analyzator is a Streamlit-based web application built with Python, designed to facilitate DNA sequence analysis and protein characterization. With this app, users can explore various functions for processing DNA data, including nucleotide counting, translation to protein sequences, visualization of protein structures, and classification of proteins based on its structure.


## Instalation and Running the app
1. Clone this repository to your local machine:

    ```
    git clone https://github.com/your-username/bio_data.git
    ```
    
2. Install the required dependencies:
   
    ```
    pip install -r requirements.txt
    ```

3.  Run the Streamlit app from command line:

    ```
    streamlit run main.py
    ```

## Usage
1. Enter a DNA sequence into the input field provided on the app's interface.
2. Choose from the available options to perform nucleotide counting, translation to protein sequences, etc.
3. Click on Data Visualization to see 3D structure of your created protein.
4. Click on Protein Classification, where you can see in which group your protein belongs.

## Example

## Description of Python files
### main.py 
The main.py script servers as the entry for the DNA Analyzator web application built with Streamlit. It contains the Streamlit app definition and itegrates various scripts or functions to manipulate with DNA sequence provided by user.

### functions.py
The functions.py script contains functions and class for manipulation with DNA sequence provided by user. Every function is described. It contains eve DNAProcessor class, which handles proteosynthesis. At the end of the script is a script for local use.

### model_classification_class.py
The model_classification_class.py script serves for classification of protein into protein classes using a trained model.

### protein_class_prep.ipynb
The protein_class_prep.ipynb is Jupyter notebook, which was used for training the model for protein classification.

### protein_visualization.py
The protein_visualization.py script, which is used to send a POST request with a Protein sequence to an external API (ESM Fold). The response is then visualize.

-------------------------------------------------------------------------------------------------------------------

##
#### Want explore more? Useful bioinformatics links:

https://rosalind.info/problems/locations/
