# graintogut
## Millet-Derived Lactic Acid Bacteria – PICRUSt & Functional Analysis

- This project is based on a research paper by our guide, where lactic acid bacteria (LAB) were isolated and characterized from millets ([research paper link](https://github.com/Sandhyae2/grain2gut/blob/main/Isolation_%26_characterization_of_biological_traits_of_millet-derived_lactic_acid_bacteria.pdf)).
- Among the isolates, four LAB strains showed probiotic characteristics, and their 16S rRNA partial sequences were submitted to NCBI.
- These sequences have been used for functional prediction using PICRUSt (Phylogenetic Investigation of Communities by Reconstruction of Unobserved States).
- The raw PICRUSt outputs were processed to obtain KO (KEGG Orthology), EC (Enzyme Commission), and PWY (Pathway) dataframes.
- Each dataframe was independently linked to reference information from databases.
- These processed dataframes created from the raw files are used for further analysis.

## 📁 Repository Structure

### [📃 Research paper](https://github.com/Sandhyae2/grain2gut/blob/main/Isolation_%26_characterization_of_biological_traits_of_millet-derived_lactic_acid_bacteria.pdf)  
- Research paper used for this project

### [📁 Picrust Input Files](https://github.com/Sandhyae2/grain2gut/tree/main/picrust_input_files)  
-  Input data used for PICRUSt prediction.

### [📁 Picrust Raw Output Files](https://drive.google.com/drive/folders/1hWki1Y-hCqCOCOK4YIz8lqH8WLMMlRJk?usp=drive_link)  
- Unprocessed output from PICRUSt (KO/EC/pathway tables).

### [📁 Picrust Analysis Notebooks](https://github.com/Sandhyae2/grain2gut/tree/main/analysis_notebooks)  
- Colab notebooks used to process the raw EC,KO,PWY picrust output files.

### [📁 Picrust Processed Output Files](https://github.com/Sandhyae2/grain2gut/blob/main/analysis_notebooks/picrust_output.ipynb)  
- Cleaned & annotated analysis-ready csv files.
  
### [🦠 App](https://github.com/Sandhyae2/grain2gut/blob/main/app.py)  
- Streamlit Web app ([app link](https://graintogut.streamlit.app/)) containing results of the project.

### [📄 Requirements file](https://github.com/Sandhyae2/grain2gut/blob/main/requirements.txt)  
- Python dependencies for running the Streamlit application.
