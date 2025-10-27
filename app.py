import streamlit as st
st.set_page_config(layout="wide")
st.markdown("""
<style>
.stApp {
    background-image: url('https://media.istockphoto.com/id/1162130673/photo/green-wheat-field.jpg?s=170667a&w=0&k=20&c=n1RnJfTLweksJlZX6l5CFavHzO6CSpLX2ECWrpa08uc=');  
    background-size: cover;
    background-attachment: fixed;
}
.block-container {
    padding-top: 2rem;
    padding-left: 6rem;
    padding-right: 6rem;
}
h2, h1 {
    text-align: center !important;
    color: #2c3e50;
}
.stColumns {
    gap: 40px !important;
}
.stButton>button {
    background-color:#f2e6ff;
    color:#2c3e50;
    font-size:20px;
    border-radius:10px;
    padding:10px 20px;
    border:none;
    transition: background-color 0.3s ease;
}
.stButton>button:hover {
    background-color:#b3ecff;
}
</style>
""", unsafe_allow_html=True)
# ----------------------------------------------------------- Page Control -------------------------------------------------------------

if "page" not in st.session_state:
    st.session_state.page = "home"

def go_to(page):
    st.session_state.page = page
    st.rerun()
# ------------------------------------------------------------ Home Page -----------------------------------------------------------------------
def home():
    st.markdown("<h2 style='text-align:center;'>GraintoGut</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center;'>Linking genomic potential of Millet derived Lactic Acid Bacteria to food and probiotic applications</h3>", unsafe_allow_html=True)
    st.write("") 
 # ----------------------------------- Sidebar with Project Description ------------------------------------------------------------------------
   # "Back to Home" button at the top of the sidebar
    
    with st.sidebar.expander("About This App", expanded=False):
        st.markdown("""
        1. This app is based on a research paper by our guide, where lactic acid bacteria (LAB) were isolated and characterized from millets([research paper link](https://github.com/Sandhyae2/grain2gut/blob/main/Isolation_%26_characterization_of_biological_traits_of_millet-derived_lactic_acid_bacteria.pdf)).
        2. Among the isolates, four LAB strains showed probiotic characteristics, and their 16S rRNA partial sequences were submitted to NCBI.
        3. These sequences have been used for functional prediction using PICRUSt (Phylogenetic Investigation of Communities by Reconstruction of Unobserved States).
        4. The raw PICRUSt outputs were processed to obtain KO (KEGG Orthology), EC (Enzyme Commission), and PWY (Pathway) dataframes.
        5. Each dataframe was independently linked to reference information from databases.
        6. These dataframes are present in the **Meta Data** section and are used for further analysis.
        """)
    left_col, middle_col, right_col = st.columns([1, 1, 1])  # left & middle for extra buttons/spaces, right for Detailed Analysis
    
# -------------------------------------------------Summarized Analysis-------------------------------------------------------------
    with left_col:
        if st.button("Summarized Analysis"):
            go_to("summarized_analysis")
 # --------------------------------------------------------------------- Navigation ---------------------------------------------------------------------
page = st.session_state.page
if page == "home":
    home()
elif page == "summarized_analysis":
    summary()

    

