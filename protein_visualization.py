import streamlit as st
from stmol import showmol
import py3Dmol
import requests
import biotite.structure.io as bsio

def molecule_render(pdb):
    """
    Function to visualize a 3D representation of a molecule based on its Protein Data Bank (PDB) string.

    Parameters
    ----------
    pdb : str
        A string representing the molecule in PDB format.

    Returns
    -------
    None
        The function does not return anything but visualizes the molecule using py3Dmol.
    """
    # Initialize a py3Dmol viewer instance
    pdbview = py3Dmol.view()

    # Add the molecule to the viewer using the pdb string, specifying the model type as 'pdb'
    pdbview.addModel(pdb, 'pdb')

    # Set the visual style for the molecule - 'cartoon' style and color is set to 'spectrum'
    pdbview.setStyle({'cartoon': {'color': 'spectrum'}})

    # Set the background color for the viewer as 'white' (here you could also use the hexadecimal color '0xeeeeee')
    pdbview.setBackgroundColor('white')

    # Adjust the viewer to center and zoom on the molecule
    pdbview.zoomTo()

    # Zoom out slightly to make sure the entire molecule is visible. Takes two arguments: the zoom factor and the duration of zoom in milliseconds
    pdbview.zoom(2, 800)

    # Stop the molecule from spinning (spin is usually set to True for interactive 3D rotations)
    pdbview.spin(False)

    # Display the molecule in the viewer with specific dimensions
    showmol(pdbview, height=500, width=800)

# ESMfold
def protein_fold(response):
    """
    Function to send a POST request with a Protein string/sequence to an external API (ESM Fold). The response is
    a PDB representation of the predicted protein structure, which is written into a file. The function then loads
    the structure from the file and calculates the mean B-factor. Finally, the protein structure is visualized.

    Parameters
    ----------
    result : str
        The DNA sequence to send in the POST request.

    Returns
    -------
    None
        The function does not return anything but writes the response to a file and visualizes the protein structure.
    """

    # Decode the content of the response and assign it to pdb_string
    pdb_string = response.content.decode('utf-8')

    # Write the pdb_string to a file named 'predicted.pdb'
    with open('predicted.pdb', 'w') as f:
        f.write(pdb_string)

    # Load the structure from the 'predicted.pdb' file. The extra_fields argument is used to specify additional fields to be parsed from the file.
    struct = bsio.load_structure('predicted.pdb', extra_fields=["b_factor"])

    # Calculate the mean B-factor - which tells us the quality of prediction
    b_value = round(struct.b_factor.mean(), 4)

    # plDDT value is stored in the B-factor field
    st.subheader('plDDT')
    st.write('plDDT is a per-residue estimate of the confidence in prediction on a scale from 0-100.')
    st.info(f'plDDT: {b_value}')

    # Display protein structure
    molecule_render(pdb_string)

    # Add a download button to the Streamlit app to download the predicted PDB file
    st.download_button(
        label="Download PDB",
        data=pdb_string,
        file_name='predicted.pdb',
        mime='text/plain',
    )


