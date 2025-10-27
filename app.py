import streamlit as st
st.set_page_config(layout="wide")
st.markdown("""
<style>
.stApp {
    background-image: url('https://thumbs.dreamstime.com/b/vibrant-green-wheat-field-isolated-white-background-nature-farm-food-crop-plant-grass-rural-grain-fresh-beautiful-green-wheat-355319893.jpg');  
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
    background-color:#FEF7A2;
    color:#2c3e50;
    font-size:20px;
    border-radius:10px;
    padding:10px 20px;
    border:none;
    transition: background-color 0.3s ease;
}
.stButton>button:hover {
    background-color:#DFFBB9;
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
 # --------------------------------------------------------------------- Navigation ---------------------------------------------------------------------
page = st.session_state.page
if page == "home":
    home()
    

