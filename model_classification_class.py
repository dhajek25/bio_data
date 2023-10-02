import pandas as pd

from keras.models import load_model
from keras.preprocessing.text import tokenizer_from_json
from keras.preprocessing import sequence

model_path = 'trained_model/protein_classification.keras'
tokenizer_path = 'trained_model/tokenizer.json'

def classify_protein(protein_seq):

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
    model = load_model(model_path)

    # Load the trained tokenizer
    with open(tokenizer_path, 'r', encoding='utf-8') as f:
        loaded_tokenizer_json = f.read()
        loaded_tokenizer = tokenizer_from_json(loaded_tokenizer_json)

    # Tokenize the protein sequence
    token_protein = loaded_tokenizer.texts_to_sequences(protein_seq)
    token_protein = sequence.pad_sequences(token_protein, maxlen=max_length)

    # Predict the protein class
    predicted_protein = model.predict(token_protein)

    # Convert the predicted protein class to a dataframe
    predicted_protein = pd.DataFrame(predicted_protein)


    predicted_protein.columns = col_names

    # Get the predicted class with the highest probability
    # predicted_class = predicted_protein.max().idxmax()

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

# Usage:
#model_path = 'trained_model/protein_classification.keras'
#tokenizer_path = 'trained_model/tokenizer.json'
#protein_sequence = 'MVLSEGEWQLVLHVWAKVEADVAGHGQDILIRLFKSHPETLEKFDRVKHLKTEAEMKASEDLKKHGVTVLTALGAILKKKGHHEAELKPLAQSHATKHKIPIKYLEFISEAIIHVLHSRHPGNFGADAQGAMNKALELFRKDIAAKYKELGYQG'
#result = classify_protein(model_path)
#print(result)