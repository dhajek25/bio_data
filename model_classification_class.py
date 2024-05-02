import pandas as pd

from keras.models import load_model
from keras.preprocessing.text import tokenizer_from_json
from keras.preprocessing import sequence

model_path = 'trained_model/Protein_Classification_LSTM.keras'
tokenizer_path = 'trained_model/tokenizer_LSTM.json'

def classify_protein(protein_seq):

    """
    Classifies a protein sequence into one or more protein classes using a trained model.

    Parameters:
    - protein_seq (str): The protein sequence to be classified.

    Returns:
    - pandas.DataFrame: A DataFrame containing the top predicted protein classes along with their probabilities.
      The DataFrame has two columns: 'protein_class' and 'class_probability'. The top 3 predicted protein classes
      are returned, sorted by probability in descending order.
    """

    # Rename the columns (just 10 is used)
    col_names = [
        'HYDROLASE',
        'HYDROLASE/HYDROLASE INHIBITOR',
        'IMMUNE SYSTEM',
        'ISOMERASE',
        'LYASE',
        'OXIDOREDUCTASE',
        'SIGNALING PROTEIN',
        'TRANSCRIPTION',
        'TRANSFERASE',
        'TRANSPORT PROTEIN'
    ]

    # maximum length of sequence, everything afterwards is discarded
    max_length = 350

    # Load the trained model
    model_loaded = load_model(model_path)

    # Load the trained tokenizer
    with open(tokenizer_path, 'r', encoding='utf-8') as f:
        loaded_tokenizer_json = f.read()
        loaded_tokenizer = tokenizer_from_json(loaded_tokenizer_json)

    # # Load the tokenizer
    # loaded_tokenizer = Tokenizer()
    # loaded_tokenizer = loaded_tokenizer.from_json(open(tokenizer_path).read())

    # Tokenize the protein sequence
    test_protein = loaded_tokenizer.texts_to_sequences([protein_seq])
    test_protein = sequence.pad_sequences(test_protein, maxlen=max_length)

    # Predict the protein class
    predicted_protein = model_loaded.predict(test_protein)

    # Convert the predicted protein class to a dataframe
    predicted_protein = pd.DataFrame(predicted_protein)

    predicted_protein.columns = col_names

    # Find the highest number in the dataframe
    max_probability = predicted_protein.values.max()

    # Find the row with the highest number
    row_with_max_prob = predicted_protein[predicted_protein.isin([max_probability]).any(axis=1)]

    # Sort this row from the highest number to lowest while preserving column names
    sorted_indices = row_with_max_prob.iloc[0].sort_values(ascending=False).index
    sorted_row = row_with_max_prob[sorted_indices]

    # Transpose the sorted row to a column
    transposed = sorted_row.T

    # Rename the column to "class_probability"
    transposed.columns = ['class_probability']

    return round(transposed, 3).head(3) * 100

# FOR LOCAL TESTING

# # Usage:
# model_path = 'trained_model/protein_classification.keras'
# tokenizer_path = 'trained_model/tokenizer.json'
# protein_sequence = 'MVLSEGEWQLVLHVWAKVEADVAGHGQDILIRLFKSHPETLEKFDRVKHLKTEAEMKASEDLKKHGVTVLTALGAILKKKGHHEAELKPLAQSHATKHKIPIKYLEFISEAIIHVLHSRHPGNFGADAQGAMNKALELFRKDIAAKYKELGYQG'
# result = classify_protein(model_path)
# print(result)