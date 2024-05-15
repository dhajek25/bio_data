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

## Data Entry
We can enter DNA sequence as you can see below into user field and select "Protein Synthesis" function. <br>
App will accept the DNA sequence, which user provided and returned protein structure for provided DNA sequence. <br>

![image](https://github.com/dhajek25/bio_data/assets/79058813/af9a448a-fd99-483a-9d80-bf3f13aadde1)

## Protein Visiualization
We can select protein from database. The result is predicted protein structure for protein, which we selected. <br>
Every aminoacid would have different color. You can see plDDT, which tells us how confident the prediction was. Scale is from 0-100 (100 highest). <br>

![image](https://github.com/dhajek25/bio_data/assets/79058813/be699b30-05fe-4359-9d7a-b35393f2d24a)


## Protein Classification
Another step could be to click on "Protein Classification" bar. Here under "Choose classification method" you can choose "Database" and from the filter you can choose your protein. <br>
The result will be table, in which we can see TOP3 results for your protein with the name of the protein class and probability, which says how likely your protein belongs under certain class.

![image](https://github.com/dhajek25/bio_data/assets/79058813/64bb1521-e437-464f-9420-f1f5479f0c40)


## Description of Python files under main folder bio_data
### main.py 
The main.py script servers as the entry for the DNA Analyzator web application built with Streamlit. It contains the Streamlit app definition and itegrates various scripts or functions to manipulate with DNA sequence provided by user.

### functions.py
The functions.py script contains functions and class for manipulation with DNA sequence provided by user. Every function is described. It contains eve DNAProcessor class, which handles proteosynthesis. At the end of the script is a script for local use.

### model_classification_class.py
The model_classification_class.py script serves for classification of protein into protein classes using a trained model.

### protein_visualization.py
The protein_visualization.py script, which is used to send a POST request with a Protein sequence to an external API (ESM Fold). The response is then visualize.

### dtb_connection.py
Enables connection and writing/retrieving data to/from database.

NOTE: inside folder **protein_class_model** you can find README about model, which is used for protein classification

-------------------------------------------------------------------------------------------------------------------


#### Want explore more? Useful bioinformatics links:

https://rosalind.info/problems/locations/
