import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from upsetplot import UpSet, from_memberships
from itertools import combinations

st.set_page_config(layout="wide",page_icon="🌾")

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
st.markdown("""
<style>
.stApp {
    background-image: url('data:image/jpeg;base64,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');
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
    background-color:#b3ecff;
    color:#2c3e50;
    font-size:20px;
    border-radius:10px;
    padding:10px 20px;
    border:none;
    transition: background-color 0.3s ease;
}
.stButton>button:hover {
    background-color:#f2e6ff;
}
</style>
""", unsafe_allow_html=True)

#---------------------------disclaimer-----------------------------
if "show_disclaimer" not in st.session_state:
    st.session_state.show_disclaimer = True
if st.session_state.show_disclaimer:
    st.markdown("""
    <div style="
        max-width: 400px;
        margin: 10px auto;
        padding: 14px 18px;
        border-radius: 10px;
        background-color:#b3ecff;
        font-size: 15px;
        line-height: 1.5;
    ">
        <div style="text-align:center;">
            <b>Welcome to GraintoGut 🌾</b><br>
            <b>⚠️ Disclaimer</b>
        </div>
        <div style="text-align:left; margin-top:8px;">
            <ul style="padding-left:16px; margin:0;">
                <li>Use the <b>Sidebar</b> to navigate the app sections.</li>
                <li><b>Do not</b> use the browser <b>Back</b> button as it will exit the app.</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([3,2,3])
    with col2:
        if st.button("Click here to reach the App 🦠"):
            st.session_state.show_disclaimer = False
            st.rerun()

    st.stop()

# ----------------------------------------------------------- Page Control -------------------------------------------------------------

if "page" not in st.session_state:
    st.session_state.page = "home"

def go_to(page):
    st.session_state.page = page
    st.rerun()
# ------------------------------------------------footer----------------------------------------------------------------------------------
def footer():
    st.markdown("""
    <style>
    .footer-container {
        position: fixed;
        left: 50%;
        bottom: 10px;  /* distance from bottom */
        transform: translateX(-50%);
        background-color: #b3ecff;  /* Yellow box */
        color: black;
        padding: 10px 20px;
        font-size: 14px;
        border-radius: 8px;  /* rounded corners */
        z-index: 100;
        text-align: center;
    }
    .footer-container a {
        color: 	 #004d66;  /* Dark blue links */
        text-decoration: none;
        font-weight: bold;
    }
    .footer-container a:hover {
        text-decoration: underline;
    }
    </style>
    
    <div class="footer-container">
        Jointly created by 
        <a href="https://github.com/Sandhyae2" target="_blank">Sandhya</a>&
        <a href="https://github.com/VarshaS-37" target="_blank">Varsha</a>|
        <a href="https://github.com/Sandhyae2/GraintoGut/tree/main" target="_blank">GitHub Repo</a>
    </div>
    """, unsafe_allow_html=True)
# ------------------------------------------------------------ Home Page -----------------------------------------------------------------------
def home():
    st.markdown("<h2 style='text-align:center;'>GraintoGut 🌾</h2>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align:center;  font-style:italic;'><i>Linking genomic potential of Millet derived Lactic Acid Bacteria to food and probiotic applications</i></h4>", unsafe_allow_html=True)
    st.write("") 
  

    
    # ====== PAGE LAYOUT ======
    left_col, middle_col, right_col = st.columns([1,2,3])
    
    # ================================
    # LEFT COLUMN
    # ================================
    with left_col:
        # ===== Expander: About this App ===== 
        with st.expander("About This App", expanded=False):
            st.markdown("""
            1. This app is based on a research paper on lactic acid bacteria (LAB) isolated from millets  
            (<a href="https://github.com/Sandhyae2/GraintoGut/blob/main/Isolation_%26_characterization_of_biological_traits_of_millet-derived_lactic_acid_bacteria.pdf" target="_blank">Research Paper</a>)  
            2. Four LAB strains showed probiotic potential, and their 16S rRNA sequences were submitted to NCBI.    
            2. Four LAB strains showed probiotic potential, and their 16S rRNA sequences were submitted to NCBI.  
            3. These sequences were analyzed using PICRUSt for functional prediction.  
            4. Outputs were processed into **KO**, **EC**, and **PWY** datasets linked to reference databases.
            """, unsafe_allow_html=True)
          # ===== Expander: Millet Data Overview =====
        with st.expander("Millet Data Overview", expanded=False):
            millet_data = {
                "Millet Source": ["Proso", "Foxtail", "Little", "Little"],
                "Strain": ['BM01', 'NM01', 'SM01', 'SM02'],
                "Organism": [
                    "Enterococcus casseliflavus",
                    "Weissella cibaria",
                    "Weissella cibaria",
                    "Lactococcus lactis"
                ],
                "NCBI ID": ['PP355677', 'PP355678', 'PP355679', 'PP355680'],
                "NCBI Link": [
                    "https://www.ncbi.nlm.nih.gov/nuccore/PP355677.1/",
                    "https://www.ncbi.nlm.nih.gov/nuccore/pp355678",
                    "https://www.ncbi.nlm.nih.gov/nuccore/pp355679",
                    "https://www.ncbi.nlm.nih.gov/nuccore/pp355680"
                ]
            }
            millet_df = pd.DataFrame(millet_data) 
        
            st.data_editor(
                millet_df,
                column_config={
                    "NCBI Link": st.column_config.LinkColumn("NCBI Link", display_text="NCBI Link"),
                },
                hide_index=True,
                use_container_width=True
            )
     # ================================
    # RIGHT COLUMN
    # ================================
    with middle_col:
        # ===== Row 1: Analysis Section =====
        with st.container(border=True):
            st.markdown("<h4 style='text-align:center;'>Analysis</h4>", unsafe_allow_html=True)
            col1, col2 = st.columns(2)
    
            with col1:
                with st.container(border=True):
                    if st.button("Millet-wise Analysis", use_container_width=True):
                        go_to("milletwise_analysis")
                    st.write("Detailed comparison of functions across millet strains.")
    
            with col2:
                with st.container(border=True):
                    if st.button("Inference", use_container_width=True):
                        go_to("summarized_analysis")
                    st.write("Summarized overall interpretation of results.")
    
        st.markdown(" ")
    with right_col:
        # ===== Row 2: Functional Prediction Section =====
        with st.container(border=True):
            st.markdown("<h4 style='text-align:center;'>Functional Prediction</h4>", unsafe_allow_html=True)
            ec_col, ko_col, pwy_col = st.columns(3)
    
            with ec_col:
                with st.container(border=True):
                    if st.button("Predicted ECs", use_container_width=True):
                        go_to("ec_analysis")
                    st.write("Explore enzyme-level functions based on EC numbers.")
    
            with ko_col:
                with st.container(border=True):
                    if st.button("Predicted KOs", use_container_width=True):
                        go_to("ko_analysis")
                    st.write("Explore gene functions using KEGG Orthology mappings.")
    
            with pwy_col:
                with st.container(border=True):
                    if st.button("Predicted Pathways", use_container_width=True):
                        go_to("pwy_analysis")
                    st.write("Explore metabolic and biologically associated pathways.")

    # ===== FOOTER =====
    footer()     
# -------------------------------------------------- Millet Data Mapping -------------------------------------------------------------------
millet_map = {
    "Enterococcus casseliflavus (Proso Millet)": "77",
    "Weisella cibaria NM01 (Foxtail Millet)": "78",
    "Weisella cibaria SM01 (Little Millet)": "79",
    "Lactococcus lactis (Little Millet)": "80"
 }
    
 # ---------------------------------------------------- EC Analysis ------------------------------------------------------------------------------
def ec_page():
    st.markdown("<h3 style='text-align:center;'>EC Analysis</h3>", unsafe_allow_html=True)
     # ------------------------------------------ Sidebar with instructions -----------------------------------------------------
    with st.sidebar:
        if st.button("Back to Homepage 🏠"):
            go_to("home")  # Your navigation function
        with st.sidebar.expander("How to Use this Page", expanded=False):
            st.markdown("""
            **Instructions:**
            1. Select the millet LAB from the dropdown at the top.
            2. On the left, the entire EC dataframe for the selected LAB is displayed.
            3. Use the **EC number dropdown** above the dataframe to select an EC number.
            4. The right column will show the textual interpretation for the selected EC number.
            5. Use the **"Back to Home"** button at the bottom to return to the home page.
            """)
        with st.sidebar.expander("What is an EC Number?", expanded=False):
            st.markdown("""
            **EC (Enzyme Commission) numbers** are a numerical classification scheme for enzymes, 
            based on the chemical reactions they catalyze.  
            - Each EC number consists of four numbers separated by periods (e.g., `2.7.1.1`).  
            - The first number represents the main enzyme class (6 major classes: Oxidoreductases, Transferases, Hydrolases, Lyases, Isomerases, Ligases).  
            - The subsequent numbers give more specific subclass, sub-subclass, and the serial number of the enzyme.  
            """)
        with st.sidebar.expander("Why is it relevant?", expanded=False):
            st.markdown("""
            EC numbers tell us **what each enzyme in a LAB can do**. 
            
            For example:   
            - Which sugars or fibers the bacteria can break down  
            - Which beneficial compounds (like vitamins or organic acids) they might produce  
            - How they might interact in food or the gut  
            
            So EC numbers help in **connecting the functional predictions from PICRUSt to real biological activities**.
            """)
        with st.sidebar.expander("What is in the EC Dataframe?", expanded=False):
            st.markdown("""
            1. Only EC numbers with abundance greater than 1 are considered.
            2. Here's what each column means:
            - **ec_number**: The Enzyme Commission (EC) number classifying the enzyme's activity.
            - **ec_abundance**: How many times this enzyme is predicted to be present in the strain.
            - **ec_function**: Description of the enzyme's function.
            - **ec_class**: The main EC class (number 1–6) the enzyme belongs to.
            - **ec_class_name**: The name of the EC class (e.g., Transferases, Hydrolases).
            - **ko_ids**: KEGG Orthology IDs linked to this enzyme.
            - **ko_functions**: Descriptions of the KO functions linked to this enzyme.
            - **pathway_ids**: KEGG pathway IDs associated with this enzyme.
            - **pathway_names**: Names of the KEGG pathways this enzyme participates in.
            - **brite_subclass**: KEGG BRITE hierarchy subclass for this enzyme.
            - **brite_class**: KEGG BRITE hierarchy main class for this enzyme.
        """)
    #--------------------------------------------------------Select LAB----------------------------------------------------------------------
    col1, col2, col3 = st.columns([3, 3, 3])
    with col2:
        st.markdown("<h4 style='text-align:center;'>Select the Millet LAB</h4>", unsafe_allow_html=True)
        selected_strain = st.selectbox(
            "",
            list(millet_map.keys()),
            label_visibility="collapsed",
            key=f"strain_select_{st.session_state.page}",
        )
    suffix = millet_map[selected_strain]
    
    # Load EC dataframe
    try:
        df = pd.read_csv(f"picrust_output_files/ec{suffix}.csv")
    except FileNotFoundError:
        st.error(f"File ec{suffix}.csv not found.")
        return

    # Load textual interpretation CSV
    try:
        text_df = pd.read_csv(f"picrust_output_files/ec{suffix}_text.csv", encoding='ISO-8859-1')  # columns: ec_number, description
    except FileNotFoundError:
        st.error(f"Text file ec{suffix}_text.csv not found.")
        return
    st.write("")  # spacing

    # ----------------------------------------------- Side-by-Side Columns ---------------------------------------------------------------------------
    left_col, right_col = st.columns([1, 2])  # left smaller, right bigger

    # ----------------------------------- Left Column: EC number dropdown + Full EC DataFrame ----------------------------------------------------
    with left_col:
        st.markdown("<h4 style='text-align:center;'>Select a EC Number</h4>", unsafe_allow_html=True)
        if 'ec_number' in df.columns:
            selected_ec = st.selectbox("",df['ec_number'].unique(), label_visibility="collapsed",key="ec_select")
        else:
            st.warning("Column 'ec_number' not found in dataframe.")
            selected_ec = None
        st.markdown("<h4 style='text-align:center;'>EC DataFrame</h4>", unsafe_allow_html=True)
        st.dataframe(df, use_container_width=True)

    # -------------------------------------------- Right Column: Textual Interpretation -------------------------------------------------------
    with right_col:
        st.markdown("<h4 style='text-align:center;'>Interpretation</h4>", unsafe_allow_html=True)
        if selected_ec:
            ec_text = text_df[text_df['ec_number'] == selected_ec]
            if not ec_text.empty:
                # Display EC number in larger bold font
                st.markdown(f"<h3 style='text-align:center;'>{selected_ec}</h3>", unsafe_allow_html=True)
                # Split the description by semicolon
                description = ec_text.iloc[0]['description']
                parts = [part.strip() for part in description.split(';')]
                for part in parts:
                    # Split at the first colon to bold the section title
                    if ':' in part:
                        title, text = part.split(':', 1)
                        st.markdown(f"<p style='font-size:16px;'><strong>{title}:</strong> {text.strip()}</p>", unsafe_allow_html=True)
                    else:
                        st.markdown(f"<p style='font-size:16px;'>{part}</p>", unsafe_allow_html=True)
            else:
                st.warning("No textual description found for this EC number.")
# --------------------------------------------------- KO Page: Side-by-Side + Sidebar -------------------------------------------------------------
def ko_page():
    st.markdown("<h3 style='text-align:center;'>KO Analysis</h3>", unsafe_allow_html=True)
    # ------------------------------------- Sidebar with instructions ----------------------------------------------------------------------
    with st.sidebar:
        if st.button("Back to Homepage 🏠"):
            go_to("home")  # Your navigation function
        with st.sidebar.expander("How to Use this Page", expanded=False):
            st.markdown("""
            **Instructions:**
            1. Select the millet LAB from the dropdown at the top.
            2. On the left, the entire KO dataframe for the selected LAB is displayed.
            3. Use the **KO ID dropdown** above the dataframe to select a KO ID.
            4. The right column will show the textual interpretation for the selected KO number.
            5. Use the **"Back to Home"** button at the bottom to return to the home page.
            """)
        with st.sidebar.expander("What is a KO ID?", expanded=False):
            st.markdown("""
            
            **KO (KEGG Orthology) IDs** represent groups of genes/proteins that have the **same functional role** in different organisms.  
            - Each KO ID corresponds to a specific **orthologous gene** in the KEGG database.  
            - KOs help in linking **genes to metabolic pathways** and **enzyme functions**.  
            """)
        with st.sidebar.expander("Why is it relevant?", expanded=False):
            st.markdown("""
            KO IDs are important because they tell us **what functions a LAB strain may carry out at the gene level**.
            
            For example:  
            - Which transporters, enzymes, or proteins are present  
            - Which metabolic or signaling pathways the strain may be capable of  
            - How the predicted functions relate to **probiotic and food applications** 
            
            In this app, KO IDs help connect **genomic predictions to real biological activities** and link them to EC numbers and pathways.
            """)
        with st.sidebar.expander("What is in the KO Dataframe?", expanded=False):
            st.markdown("""
            1. Only KO ids with abundance greater than 2 are considered.
            2. Here's what each column in the KO dataframe means:
            - **ko_id**: KEGG Orthology ID for a gene/protein with a specific function.
            - **ko_abundance**: Number of times this KO is predicted in the strain.
            - **ko_function**: Description of the KO’s functional role.
            - **ec_id**: Associated EC number(s) for this KO (if available).
            - **ec_class**: The EC class of the linked enzyme.
            - **ec_function**: Function of the linked enzyme.
            - **map_ids**: KEGG pathway map IDs associated with this KO.
            - **pathway_names**: Names of KEGG pathways this KO participates in.
            - **brite_subclass**: KEGG BRITE hierarchy subclass for this KO.
            - **brite_class**: KEGG BRITE hierarchy main class for this KO.
            - **ec_abundance**: Abundance of the linked EC(s).
            """)
    # ------------------------------------------ Millet LAB Selection --------------------------------------------------------------------------
    col1, col2, col3 = st.columns([3, 3, 3])
    with col2:
        st.markdown("<h4 style='text-align:center;'>Select the Millet LAB</h4>", unsafe_allow_html=True)
        selected_strain = st.selectbox(
            "",
            list(millet_map.keys()),
            label_visibility="collapsed",
            key=f"ko_strain_select_{st.session_state.page}",
        )
    suffix = millet_map[selected_strain]
    # Load KO DataFrame
    try:
        df = pd.read_csv(f"picrust_output_files/ko{suffix}.csv")
    except FileNotFoundError:
        st.error(f"File ko{suffix}.csv not found.")
        return
    # Load textual interpretation CSV
    try:
        text_df = pd.read_csv(f"picrust_output_files/ko{suffix}_text.csv", encoding='ISO-8859-1')  # columns: ko_number, description
    except FileNotFoundError:
        st.error(f"Text file ko{suffix}_text.csv not found.")
        return
    st.write("")  # spacing
    # ------------------------------------------------- Side-by-Side Columns ---------------------------------------------------------------------------
    left_col, right_col = st.columns([1, 2])  # left smaller, right bigger
    # ---------------------------------------- Left Column: KO number dropdown + Full KO DataFrame ----------------------------------------------
    with left_col:
        st.markdown("<h4 style='text-align:center;'>Select a KO ID</h4>", unsafe_allow_html=True)
        if 'ko_id' in df.columns:
            selected_ko = st.selectbox("", df['ko_id'].unique(), label_visibility="collapsed",key="ko_select")
        else:
            st.warning("Column 'ko_number' not found in dataframe.")
            selected_ko = None
        st.markdown("<h4 style='text-align:center;'>KO DataFrame</h4>", unsafe_allow_html=True)
        st.dataframe(df, use_container_width=True)
    # ---------------------------------------- Right Column: Textual Interpretation -------------------------------------------------------------
    with right_col:
        st.markdown("<h4 style='text-align:center;'>Interpretation</h4>", unsafe_allow_html=True)
        if selected_ko:
            ko_text = text_df[text_df['ko_id'] == selected_ko]
            if not ko_text.empty:
                # Display KO ID in larger bold font
                st.markdown(f"<h3 style='text-align:center;'>{selected_ko}</h3>", unsafe_allow_html=True)
                # Split the description by semicolon
                description = ko_text.iloc[0]['description']
                parts = [part.strip() for part in description.split(';')]
                for part in parts:
                    # Split at the first colon to bold the section title
                    if ':' in part:
                        title, text = part.split(':', 1)
                        st.markdown(f"<p style='font-size:16px;'><strong>{title}:</strong> {text.strip()}</p>", unsafe_allow_html=True)
                    else:
                        st.markdown(f"<p style='font-size:16px;'>{part}</p>", unsafe_allow_html=True)
            else:
                st.warning("No textual description found for this KO ID.")
   
# --------------------------------------------------- Pathway Page: Side-by-Side + Sidebar ----------------------------------------------------------
def pwy_page():
    st.markdown("<h3 style='text-align:center;'>Pathway Analysis</h3>", unsafe_allow_html=True)
    # ---------------------------------------------------- Sidebar with instructions ------------------------------------------------------------------
    with st.sidebar:
        if st.button("Back to Homepage 🏠"):
            go_to("home")  # Your navigation function
        with st.sidebar.expander("How to Use this Page", expanded=False):
            st.markdown("""
            **Instructions:**
            1. Select the millet LAB from the dropdown at the top.
            2. On the left, the entire pathway dataframe for the selected LAB is displayed.
            3. Use the **Pathway ID dropdown** above the dataframe to select a pathway.
            4. The right column will show the textual interpretation for the selected pathway.
            5. Use the **"Back to Home"** button at the bottom to return to the home page.
            """)
        with st.sidebar.expander("What is a Pathway?", expanded=False):
            st.markdown("""
            **Pathways** represent a series of biochemical reactions or processes that occur in the cell, often involving multiple enzymes and genes.  
            """)
        with st.sidebar.expander("Why is it relevant?", expanded=False):
            st.markdown("""
            Pathway analysis shows **how the predicted enzymes and genes work together** in biological processes.  
            This helps us understand:  
            - Which **metabolic or biosynthetic pathways** are present in the LAB strain  
            - How complete these pathways are  
            - The potential **functional and probiotic properties** of the strain
            """)
        with st.sidebar.expander("What is in the Pathway Dataframe?", expanded=False):
            st.markdown("""
            1. Only pathways with completeness greater than 0.79 are considered.
            2. Here's what each column in the dataframe means:
            - **Pathway**: Unique pathway ID in the database (e.g., `ANAGLYCOLYSIS-PWY`).  
            - **fam_total**: Total number of gene families expected in this pathway.  
            - **fam_found**: Number of gene families found in the LAB strain for this pathway.  
            - **completeness**: Fraction of the pathway that is present (0–1), calculated as `fam_found / fam_total`.  
            - **pathway_name**: Descriptive name of the pathway (e.g., `glycolysis III (from glucose)`).  
            """)
    # ---------------------------------------------- Millet LAB Selection -------------------------------------------------------------------
    col1, col2, col3 = st.columns([3, 3, 3])
    with col2:
        st.markdown("<h4 style='text-align:center;'>Select the Millet LAB</h4>", unsafe_allow_html=True)
        selected_strain = st.selectbox(
            "",
            list(millet_map.keys()),
            label_visibility="collapsed",
            key=f"pwy_strain_select_{st.session_state.page}",
        )
    suffix = millet_map[selected_strain]
    # Load Pathway DataFrame
    try:
        df = pd.read_csv(f"picrust_output_files/pwy_{suffix}.csv")
    except FileNotFoundError:
        st.error(f"File pwy_{suffix}.csv not found.")
        return
    # Load textual interpretation CSV
    try:
        text_df = pd.read_csv(f"picrust_output_files/pwy{suffix}_text.csv")  # columns: pathway_id, description
    except FileNotFoundError:
        st.error(f"Text file pwy{suffix}_text.csv not found.")
        return
    st.write("")  # spacing
    # ---------------------------------------------------- Side-by-Side Columns -----------------------------------------------------------------
    left_col, right_col = st.columns([1, 2])  # left smaller, right bigger
    # ------------------------------------- Left Column: Pathway ID dropdown + Full Pathway DataFrame -------------------------------------------------
    with left_col:
        st.markdown("<h4 style='text-align:center;'>Select a Pathway</h4>", unsafe_allow_html=True)
        if 'Pathway' in df.columns:
            selected_pwy = st.selectbox("", df['Pathway'].unique(), label_visibility="collapsed",key="pwy_select")
        else:
            st.warning("Column 'pathway_id' not found in dataframe.")
            selected_pwy = None
        st.markdown("<h4 style='text-align:center;'>Pathway DataFrame</h4>", unsafe_allow_html=True)
        st.dataframe(df, use_container_width=True)
    # -------------------------------------------- Right Column: Textual Interpretation -------------------------------------------------------
    with right_col:
        st.markdown("<h4 style='text-align:center;'>Interpretation</h4>", unsafe_allow_html=True)
        if selected_pwy:
            pwy_text = text_df[text_df['Pathway'] == selected_pwy]
            if not pwy_text.empty:
                # Display Pathway ID in larger bold font
                st.markdown(f"<h3 style='text-align:center;'>{selected_pwy}</h3>", unsafe_allow_html=True)
                # Split the description/interpretation by semicolon (if available)
                description = pwy_text.iloc[0]['description']  # make sure your dataframe has a 'description' column
                parts = [part.strip() for part in description.split(';')]
                for part in parts:
                    # Split at first colon to bold section titles
                    if ':' in part:
                        title, text = part.split(':', 1)
                        st.markdown(f"<p style='font-size:16px;'><strong>{title}:</strong> {text.strip()}</p>", unsafe_allow_html=True)
                    else:
                        st.markdown(f"<p style='font-size:16px;'>{part}</p>", unsafe_allow_html=True)
            else:
                st.warning("No textual description found for this pathway.")
    
#---------------------------------------------------millet analysis --------------------------------------------------------------------------
def millet():
    st.markdown("<h4 style='text-align:center;'>Millet-wise Analysis</h4>", unsafe_allow_html=True)
    if st.button("Back to Homepage 🏠"):
        go_to("home") 
    col1, col2,col3 = st.columns(3)
    with col1:
        with st.container(border=True):
            cola,colb,colc=st.columns([0.5,2,0.5])
            with colb:
                if st.button("EC class Distribution"):
                    go_to("ec_class")
            st.write("""Shows the distribution of EC numbers across the six major EC classes for each millet.""")
    with col2:
        with st.container(border=True):
            cola,colb,colc=st.columns([0.5,2,0.5])
            with colb:
                if st.button("Trait Distribution"):
                    go_to("trait")
            st.markdown("""
            - Based on our understanding of all the data, we have assigned biological traits to each EC, KO, PWY.
            - Their distribution is plotted for each millet.
            """)
    with col3:
        with st.container(border=True):
            cola,colb,colc=st.columns([0.5,2,0.5])
            with colb:
                if st.button("Common & Unique Traits"):
                    go_to("couq")
            st.markdown("""
            - The assigned biological traits are compared across millets.
            - The common and unique traits across millets are plotted here.
            """)
#--------------------------------------ec class------------------------------------------------------------------------------------------------
def ec_class():
    with st.sidebar:
        if st.button("Back to Homepage  🏠"):
            go_to("home")
        if st.button("Back to Analysis Menu"):
            go_to("milletwise_analysis")    
    with st.sidebar.expander("What are the major EC classes?", expanded=False):
            st.markdown("""
            1. **Oxidoreductases (EC 1):** Catalyzes redox reactions, moves electrons between molecules.  
            2. **Transferases (EC 2):** Moves functional groups from one molecule to another.  
            3. **Hydrolases (EC 3):** Breaks molecules using water.  
            4. **Lyases (EC 4):** Breaks bonds in molecules without water or oxidation.  
            5. **Isomerases (EC 5):** Rearranges molecules into different forms.  
            6. **Ligases (EC 6):** Joins two molecules together using energy.
            7. **Translocase (EC 7) : ** Moves ions or molecules acorss membrane or within cells.
            """)
    with st.sidebar.expander("How are they relevant?", expanded=False):
            st.markdown("""
            The presence of these enzymes implies their diverse functional capabilities related to food fermentation and probiotic activity:
        
            1. **Oxidoreductases (EC 1):** Helps in fermentation, making acids, and giving antioxidant benefits.  
            2. **Transferases (EC 2):** Helps in making vitamins and amino acids that improve nutrition.  
            3. **Hydrolases (EC 3):** Helps in breaking food molecules, improving digestibility, and releasing helpful compounds.  
            4. **Lyases (EC 4):** Helps in forming flavor compounds and allowing flexible use of nutrients.  
            5. **Isomerases (EC 5):** Helps in changing sugars and amino acids into useful forms and making prebiotics.  
            6. **Ligases (EC 6):** Helps in bacterial growth and stability in foods.
            7. ** Translocase (EC 7) :** Helps in transporting proteins and molecules across membranes.
            """)
    col1, col2, col3 = st.columns([3, 3, 3])
    with col2:
        st.markdown("<h4 style='text-align:center;'>EC class distribution</h4>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align:center;'>Select the Millet LAB</h4>", unsafe_allow_html=True)
        selected_strain = st.selectbox(
            "",
            list(millet_map.keys()),
            label_visibility="collapsed",
            key=f"ec_class_select_{st.session_state.page}",
        )
    suffix = millet_map[selected_strain]
    # ---- EC DISTRIBUTION ----
    try:
        # Load EC CSV from local folder
        df = pd.read_csv(f"picrust_output_files/ec{suffix}.csv")
    except FileNotFoundError:
        st.error(f"File ec{suffix}.csv not found in 'picrust_output_files/' folder.")
        return
    # Validate presence of required column
    if "ec_class_name" not in df.columns:
        st.warning(f"'ec_class_name' column not found in ec{suffix}.csv.")
        return
    # Count enzymes by EC class
    class_counts = df["ec_class_name"].value_counts().reset_index()
    class_counts.columns = ["EC Class", "Count"]
# --- Layout: Left (figure) + Right (interpretation) ---
    left_col, right_col = st.columns([2, 2])

    with left_col:
        # Plot EC class distribution
        fig, ax = plt.subplots(figsize=(6, 4))
        bars=ax.bar(class_counts["EC Class"], class_counts["Count"], color="#4C72B0")
        ax.set_xlabel("EC Class", fontsize=10)
        ax.set_ylabel("Number of Enzymes", fontsize=10)
        ax.set_title(f"EC Class Distribution - {selected_strain}", fontsize=12)
        plt.xticks(rotation=45, ha="right")
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, height, str(int(height)),ha='center', va='bottom', fontsize=9)
        plt.tight_layout()
        st.pyplot(fig)

    with right_col:
        st.markdown("### Interpretation")
        st.write(f"""
        - **Dominant EC classes:** {', '.join(class_counts['EC Class'].head(3).tolist())}
        """)
    #-----------------------------------------------------------brite class-------------------------------------------------------------------
import glob
import os

def brite():
    result = {"EC": {}, "KO": {}}

    for strain_name, suffix in millet_map.items():

        # -------- EC --------
        ec_file = f"picrust_output_files/ec{suffix}.csv"
        try:
            ec_df = pd.read_csv(ec_file, encoding="latin1")
        except:
            continue
        ec_df["brite_class"] = ec_df["brite_class"].astype(str).str.split(";")
        ec_df["brite_subclass"] = ec_df["brite_subclass"].astype(str).str.split(";")
        
        ec_df = ec_df.explode("brite_class").explode("brite_subclass")
        ec_df["brite_class"] = ec_df["brite_class"].str.strip()
        ec_df["brite_subclass"] = ec_df["brite_subclass"].str.strip()

        ec_df["brite_class"] = ec_df["brite_class"].replace(["", " ", "nan", None], pd.NA)
        ec_df["brite_subclass"] = ec_df["brite_subclass"].replace(["", " ", "nan", None], pd.NA)

        irrelevant_keywords = [
            "Cancer",
            "disease",
            "viral",
            "bacterial",
            "parasitic",
            "Endocrine",
            "Cardiovascular",
            "Neurodegenerative",
            "Immune system",
            "Substance dependence",
            "Aging"
        ]
        def is_relevant(name):
            if pd.isna(name): 
                return False
            return not any(kw.lower() in name.lower() for kw in irrelevant_keywords)
  
        filtered_class = ec_df["brite_class"].dropna().apply(lambda x: x if is_relevant(x) else None).dropna()
        filtered_subclass = ec_df["brite_subclass"].dropna().apply(lambda x: x if is_relevant(x) else None).dropna()
      
        ec_top_class = filtered_class.value_counts().head(5).to_dict()
        ec_top_subclass = filtered_subclass.value_counts().head(5).to_dict()
        
        result["EC"][strain_name] = {
            "top_5_brite_class": ec_top_class,
            "top_5_brite_subclass": ec_top_subclass
        }
        # -------- KO --------
        ko_file = f"picrust_output_files/ko{suffix}.csv"
        try:
            ko_df = pd.read_csv(ko_file, encoding="latin1")
        except:
            continue
        ko_df["brite_class"] = ko_df["brite_class"].astype(str).str.split(";")
        ko_df["brite_subclass"] = ko_df["brite_subclass"].astype(str).str.split(";")
        
        ko_df = ko_df.explode("brite_class").explode("brite_subclass")
        ko_df["brite_class"] = ko_df["brite_class"].str.strip()
        ko_df["brite_subclass"] = ko_df["brite_subclass"].str.strip()
        
        ko_df["brite_class"] = ko_df["brite_class"].replace(["", " ", "nan", None], pd.NA)
        ko_df["brite_subclass"] = ko_df["brite_subclass"].replace(["", " ", "nan", None], pd.NA)
  
        filtered_class = ko_df["brite_class"].dropna().apply(lambda x: x if is_relevant(x) else None).dropna()
        filtered_subclass = ko_df["brite_subclass"].dropna().apply(lambda x: x if is_relevant(x) else None).dropna()
      
        ko_top_class = filtered_class.value_counts().head(5).to_dict()
        ko_top_subclass = filtered_subclass.value_counts().head(5).to_dict()

        result["KO"][strain_name] = {
            "top_5_brite_class": ko_top_class,
            "top_5_brite_subclass": ko_top_subclass
        }
    return result 

#----------------------------------------------------trait distribution--------------------------------------------------------------------------------            
def trait():
    st.markdown("<h4 style='text-align:center;'>Biological Trait Distribution</h4>", unsafe_allow_html=True)
    with st.sidebar:
        if st.button("Back to Homepage 🏠"): 
            go_to("home") 
        if st.button("Back to Analysis Menu"):
            go_to("milletwise_analysis") 
    with st.sidebar.expander("Why are they relevant?", expanded=False): 
        st.markdown("""
        By assigning biological traits, we can predict how a LAB may behave in food or in the gut,  
        which helps identify **better LAB strains** for use in food applications.
        """, unsafe_allow_html=True)
 
    col1, col2, col3 = st.columns([3, 3, 3]) 
    with col2:
        st.write("")
        st.markdown("<h5 style='text-align:center;'>Select distribution category</h5>", unsafe_allow_html=True)
        selected_dist = st.selectbox(
            "",
            ['EC Traits','KO Traits','PWY Traits'],
            label_visibility="collapsed",
            key=f"brite_class_select_{st.session_state.page}",
        )
        st.markdown("<h5 style='text-align:center;'>Select the Millet LAB</h5>", unsafe_allow_html=True)
        selected_strain = st.selectbox(
            "",
            list(millet_map.keys()),
            label_visibility="collapsed",
            key=f"pwy_strain_select_{st.session_state.page}",
        )
    suffix = millet_map[selected_strain]
    try:
        df = pd.read_csv(f"picrust_output_files/{selected_dist.split(' ')[0].lower()}{suffix}_word.csv")
    except FileNotFoundError:
        st.error(f"File {selected_dist.strip(' ')[0].lower()}{suffix}.csv not found.")
        return
    
    # Validate columns
    if 'trait' not in df.columns:
        st.warning("trait column not found in the CSV.")
        return
    trait_counts = (
        df["trait"].dropna().value_counts()
    )
    trait_counts = trait_counts[trait_counts >= 2]  # Keep only counts >= 3
    trait_counts = trait_counts.reset_index()
    trait_counts.columns = ["Trait", "Count"]
    
    fig, ax = plt.subplots(figsize=(6, 4))
    bars=ax.bar(trait_counts["Trait"], trait_counts["Count"], color="#4C72B0")
    ax.set_xlabel("Trait")
    ax.set_ylabel("Count")
    ax.set_title(f"Trait Distribution - {selected_strain}")
    plt.xticks(rotation=45, ha="right")
    # Add value labels on top of bars
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, height, str(int(height)), ha='center', va='bottom', fontsize=9)
    plt.tight_layout()
    st.pyplot(fig)
    #-------------------------------------------------common & unique-----------------------------------------------------------------------------
def couq():
    with st.sidebar:
        if st.button("Back to Homepage 🏠"): 
            go_to("home") 
        if st.button("Back to Analysis Menu"):
            go_to("milletwise_analysis") 

    with st.sidebar.expander("Why is this relevant?", expanded=False): 
        st.markdown("""
        - Common traits indicates shared core metabolic functions and probiotic capabilities.
        - Unique traits indicates special metabolic or adaptive features linked to each millet.""")
    with st.sidebar.expander("What is an Upset plot?", expanded=False): 
        st.markdown("""     
        - An **UpSet Plot** is a visualization used to compare **overlaps between multiple groups**.  
        - Here, it is used to compare **functional traits** (EC, KO, Pathway features) across the **four millet-derived LAB strains**.
        - It serves a similar purpose as a **Venn diagram**, but works much better when comparing **more than 3 groups**.
        """)
    with st.sidebar.expander("How to Read the UpSet Plot?", expanded=False): 
        st.markdown("""    
        The plot has two main parts:
        ### 1) Dot Matrix (Bottom Panel)
        This shows **which strain combinations are being compared**.
        
        | Pattern | Meaning |
        |--------|---------|
        | ● A single dot under one strain | Trait is **unique** to that strain |
        | ● ● Two dots connected by a line | Trait is **shared** between those two strains |
        | ● ● ● Three connected dots | Trait is **shared by three strains** |
        | ● ● ● ● All four connected dots | Trait is **common to all four LAB strains** |
        
        So, **the dots tell *who shares the trait*.**
        
        ---
        
        ### 2) Vertical Bars (Top Panel)
        The **bar height** tells **how many traits** fall into that particular combination.
        
        | Bar Height | Interpretation |
        |------------|----------------|
        | Tall Bar | Many traits in that group/overlap |
        | Short Bar | Fewer traits in that group/overlap |
        
        So:
        - A **tall bar with all dots connected** = Many **core shared traits**
        - A **tall bar with only one dot** = Many **unique traits for that strain**
        
        """)

    st.write('')
    st.markdown(f"<h5 style='text-align:center;'>Common & Unique traits</h5>", unsafe_allow_html=True) 
    from itertools import combinations
    millet_sets={}
    # Combine EC, KO, PWY for each millet LAB
    for strain_name, suffix in millet_map.items():
        combined_traits = set()
        files = [f"ec{suffix}_word.csv", f"ko{suffix}_word.csv", f"pwy{suffix}_word.csv"]
        for f in files:
            try:
                df = pd.read_csv(f"picrust_output_files/{f}")
                if "trait" in df.columns:
                    combined_traits.update(df["trait"].dropna().unique())
            except FileNotFoundError:
                st.warning(f"File {f} not found, skipping.")
        millet_sets[strain_name] = combined_traits

    from upsetplot import UpSet, from_memberships
   

    # millet_sets: dict of millet_name -> set of traits
    memberships = []
    for millet, traits in millet_sets.items():
        for trait in traits:
            memberships.append((trait, millet))
    
    # Create the UpSet data
    data = from_memberships(
        [[millet for millet in millet_sets if trait in millet_sets[millet]] for trait in set.union(*millet_sets.values())]
    )
    
    fig = plt.figure(figsize=(8,6))
    upset = UpSet(data, subset_size='count', show_counts=True)
    upset.plot(fig=fig)  # pass the figure explicitly
    st.pyplot(fig)


    # --- Common to all 4 LABs ---
    common_4 = set.intersection(*millet_sets.values())
    st.markdown(f"<h5 style='text-align:center;'>Traits Common to All 4 Millets</h5>", unsafe_allow_html=True)
    st.dataframe(pd.DataFrame({"Trait": sorted(common_4)}))

    # --- Unique to each LAB ---
    unique_rows = []
    for millet, traits in millet_sets.items():
        # union of all traits in *other* millets
        other_traits = set.union(*(t for m, t in millet_sets.items() if m != millet))
        unique_traits = traits - other_traits  # traits found only in this millet
        for trait in sorted(unique_traits):
            unique_rows.append({"Millet": millet, "Trait": trait})
    
    st.markdown(f"<h5 style='text-align:center;'>Unique Traits</h5>", unsafe_allow_html=True)
    st.dataframe(pd.DataFrame(unique_rows))
    
    # --- Common to exactly 3 LABs ---
    common_3_rows = []
    for combo in combinations(millet_sets.keys(), 3):
        s1, s2, s3 = millet_sets[combo[0]], millet_sets[combo[1]], millet_sets[combo[2]]
        common_3 = (s1 & s2 & s3) - common_4  # remove traits in all 4
        for trait in sorted(common_3):
            common_3_rows.append({"Millets": " & ".join(combo), "Trait": trait})
    st.markdown(f"<h5 style='text-align:center;'> Traits Common to Exactly 3 Millets</h5>", unsafe_allow_html=True)
    st.dataframe(pd.DataFrame(common_3_rows))
    
    # --- Common to exactly 2 LABs ---
    common_2_rows = []
    for combo in combinations(millet_sets.keys(), 2):
        s1, s2 = millet_sets[combo[0]], millet_sets[combo[1]]
        common_2 = (s1 & s2) - common_4
        # remove traits in any common_3 combination
        for combo3 in combinations(millet_sets.keys(), 3):
            common_3 = set.intersection(*(millet_sets[c] for c in combo3)) - common_4
            common_2 -= common_3
        for trait in sorted(common_2):
            common_2_rows.append({"Millets": " & ".join(combo), "Trait": trait})
    st.markdown(f"<h5 style='text-align:center;'>Traits Common to Exactly 2 Millets</h5>", unsafe_allow_html=True)
    st.dataframe(pd.DataFrame(common_2_rows))

    #--------------------------------------------------------------Summary--------------------------------------------------------------------------
def summary():
    with st.sidebar:
        if st.button("Back to Homepage 🏠"):
            go_to("home") 
    st.markdown("<h3 style='text-align:center;'>Summary</h4>", unsafe_allow_html=True)


  #---------------------------------ec analysis-------------------------------------------------------
    st.markdown("<h4 style='text-align:center;'>EC Analysis Summary</h4>", unsafe_allow_html=True) 
    with st.expander("Which are the top abundant EC numbers and what do they imply? "):
        with st.expander("Enterococcus casseliflavus (Proso Millet)"):
            st.markdown("""
            1. **EC:2.7.7.7 – DNA-directed RNA Polymerase**  
           - This enzyme drives RNA synthesis for essential gene expression and cellular function.  
           - Stable gene expression ensures reliable probiotic activity and long-term viability in the gut environment.
            
            2. **EC:2.7.1.69 – Phosphotransferase / Kinase Activity**  
           - Regulates energy metabolism by transferring phosphate groups to key substrates.  
           - Efficient energy utilization enhances probiotic growth, persistence, and interaction with host cells.
            
            3. **EC:3.6.4.12 – DNA Helicase**  
           - Unwinds DNA for accurate replication and repair, maintaining genomic integrity.  
           - Supports probiotic stability under gut stresses such as bile salts, low pH, and oxidative conditions.
            
            4. **EC:3.6.3.14 – Proton-Transporting ATPase**  
           - Maintains intracellular pH balance by actively pumping protons across membranes.  
           - Enhances acid and bile tolerance, improving probiotic survival through gastrointestinal transit.
            
            5. **EC:3.6.3.21 – Amino Acid ABC Transporter**  
           - Facilitates uptake of amino acids for protein synthesis and metabolic processes.  
           - Supports nutrient assimilation, growth, and production of beneficial metabolites like short-chain fatty acids.
            
            ⭐ **Key Takeaway**  
            This enzyme set enables **stable gene expression, energy efficiency, stress resistance, and nutrient utilization**, making *Enterococcus casseliflavus* a robust **probiotic candidate with strong gut survival, metabolic adaptability, and health-promoting potential**.
            """)
        with st.expander("Weisella cibaria NM01 (Foxtail Millet)"):
            st.markdown("""
            1. **EC:3.6.4.12 – DNA Helicase**  
           - Unwinds DNA strands for accurate replication and repair.  
           - By maintaining genomic integrity under gut stresses such as acid and bile exposure, it supports long-term probiotic stability and viability.
            
            2. **EC:2.7.7.7 – DNA Polymerase**  
           - Synthesizes new DNA during cell division, ensuring faithful genetic replication.  
           - Promotes consistent growth and persistence of the probiotic population within the gastrointestinal tract.
            
            3. **EC:2.7.1.69 – Phosphotransferase / Kinase Activity**  
           - Regulates energy metabolism through phosphate transfer to key intermediates.  
           - Enhances carbohydrate utilization and energy efficiency, supporting active colonization and metabolic performance in the gut.
            
            4. **EC:1.1.1.1 – Alcohol Dehydrogenase**  
           - Balances cellular redox reactions during carbohydrate metabolism.  
           - Contributes to stress adaptation and the production of beneficial metabolites that can influence gut microecology and flavor in fermented foods.
            
            5. **EC:6.3.5.5 – Carbamoyl-Phosphate Synthase**  
           - Catalyzes the synthesis of precursors for amino acids and nucleotides.  
           - Supports cell growth, repair, and protein biosynthesis even in nutrient-limited gastrointestinal or plant-based environments.
            
            6. **EC:6.4.1.2 – Acetyl-CoA Carboxylase**  
           - Initiates fatty acid biosynthesis required for cell membrane formation.  
           - Strengthens membrane integrity, enhancing acid and bile resistance and improving probiotic survival through the digestive tract.
        
            ⭐ **Key Takeaway**  
            This enzyme profile demonstrates strong **genetic stability, metabolic efficiency, stress resilience, and membrane integrity**, making the strain a powerful **probiotic candidate capable of surviving gut conditions and promoting host health**.
            """)

            
        with st.expander("Weissella cibaria SM01 (Foxtail Millet)"):
            st.markdown("""
            Same as Weisella cibaria NM01 (Foxtail Millet)
            """)

        with st.expander("Lactococcus lactis (Little Millet)"):
            st.markdown("""
            1. **EC:2.7.7.7 – DNA Polymerase**  
           - Synthesizes new DNA strands during replication and repair to ensure accurate cell division.  
           - By preserving genome stability under gut and environmental stresses, it supports consistent growth and reliable probiotic performance.
            
            2. **EC:3.6.4.12 – DNA Helicase**  
           - Unwinds DNA strands to enable proper replication and repair.  
           - Maintains genetic integrity under acidic and oxidative stress, enhancing the strain’s survival during gastrointestinal transit and product storage.
            
            3. **EC:2.7.1.69 – Phosphotransferase / Kinase Activity**  
           - Transfers phosphate groups to regulate carbohydrate metabolism and energy generation.  
           - Enables efficient utilization of dietary sugars, supporting probiotic energy balance, colonization potential, and cross-feeding within the gut microbiota.
            
            4. **EC:2.7.7.6 – RNA Polymerase**  
           - Synthesizes RNA from a DNA template to drive gene expression and protein synthesis.  
           - Active transcription ensures metabolic adaptability, allowing the strain to respond effectively to gut environmental changes and maintain probiotic functionality.
        
            5. **EC:2.3.1.128 – Ribosomal Protein Acetyltransferase**  
           - Modifies ribosomal proteins for proper ribosome assembly and efficient protein synthesis.  
           - Enhances cellular growth, enzyme production, and stress resilience, promoting effective colonization and metabolic activity in the host gut.
            
            ⭐ **Key Takeaway**  
            These enzymes collectively support **genomic stability, efficient energy metabolism, adaptive gene expression, and strong protein synthesis**, equipping the strain for **robust probiotic survival, gut colonization, and health-promoting activity**.
            """)

        with st.expander("Overall Summary"):
            st.markdown("""
            | **Functional Feature** | **Key Enzymes** | **Relevance to Probiotic Function & Gut Adaptation** |
            |---|---|---|
            | **Genome Stability & Controlled Growth** | DNA Polymerase, DNA Helicase, RNA Polymerase | Maintains accurate replication and gene expression, ensuring stable growth, stress resilience, and long-term probiotic viability in the gut. |
            | **Efficient Carbohydrate & Energy Metabolism** | Phosphotransferase / Kinase Enzymes | Enables effective utilization of dietary and plant-derived sugars, supporting energy production, colonization efficiency, and cross-feeding within the gut microbiota. |
            | **Acid Tolerance & Stress Resistance** | Proton-Transporting ATPase, Alcohol Dehydrogenase | Enhances survival under acidic and bile conditions, promoting persistence through gastrointestinal transit and stability during storage. |
            | **Nutrient Uptake & Biosynthesis** | Amino Acid ABC Transporters, Carbamoyl-Phosphate Synthase, Acetyl-CoA Carboxylase, Ribosomal Protein Acetyltransferase | Improves amino acid and lipid metabolism, membrane integrity, and protein synthesis—supporting growth, resilience, and beneficial metabolite production. |
            
            ⭐ **Key Takeaway**  
            These *millet-adapted lactic acid bacteria (LAB)* strains demonstrate:  
            - **Stable genetic and metabolic regulation**  
            - **High tolerance to acid and bile stress**  
            - **Efficient nutrient and energy utilization**  
            - **Strong survival and functional activity in the gut**, highlighting their potential as **robust and health-promoting probiotic candidates**.
            """)


    with st.expander("Which are the dominant EC classes and what do they mean?"):
        with st.expander("Enterococcus casseliflavus (Proso Millet)"):
           st.markdown("""
            1. **Hydrolases**  
           - Break down complex carbohydrates, proteins, and other macromolecules into simpler, bioavailable nutrients.  
           - Enhance nutrient release, digestibility, and prebiotic substrate availability, supporting both fermentation efficiency and gut health benefits.
            
            2. **Transferases**  
           - Catalyze the transfer of functional groups between molecules, driving essential metabolic and biosynthetic pathways.  
           - Improve energy balance, metabolic adaptability, and cellular maintenance, enabling probiotics to thrive under variable gut and fermentation conditions.
            
            3. **Lyases**  
           - Catalyze bond cleavage without water, producing key intermediates and volatile compounds.  
           - Contribute to flavor and aroma formation in fermented foods while supporting stress response and redox balance in probiotic cells.
            
            ⭐ **Key Takeaway**  
            Hydrolases, Transferases, and Lyases collectively enhance **nutrient bioavailability, metabolic adaptability, and sensory quality**, reinforcing the **probiotic efficacy and functional performance** of *Lactic Acid Bacteria* in millet-based fermented foods and within the gut environment.
            """)

        with st.expander("Weisella cibaria NM01 (Foxtail Millet)"):
           st.markdown("""
            1. **Transferases**  
           - Catalyze the transfer of functional groups between molecules, driving key metabolic and biosynthetic pathways.  
           - Support energy balance, biosynthesis of essential biomolecules, and metabolic flexibility, enabling LAB to adapt and remain active in both fermentation and gut environments.
            
            2. **Hydrolases**  
           - Break down complex carbohydrates, proteins, and other macromolecules into simpler, bioavailable units.  
           - Enhance nutrient availability, digestibility, and flavor development, while supporting probiotic functionality through improved substrate utilization.
            
            3. **Ligases**  
           - Join molecules together, facilitating DNA repair, amino acid synthesis, and cellular maintenance.  
           - Strengthen genomic stability and metabolic resilience, promoting consistent growth and survival during fermentation and gastrointestinal transit.
            
            ⭐ **Key Takeaway**  
            Transferases, Hydrolases, and Ligases collectively enhance **metabolic efficiency, nutrient assimilation, and cellular integrity**, contributing to **robust fermentation performance, gut adaptability, and sustained probiotic functionality** in millet-derived *Lactic Acid Bacteria*.
            """)

        with st.expander("Weisella cibaria SM01 (Little Millet)"):
            st.write("Same as Weisella cibaria NM01 (Foxtail Millet)")
        with st.expander("Lactococcus lactis (Little Millet)"):
            st.markdown("""
            1. **Hydrolases**  
           - Break down complex carbohydrates, proteins, and other biopolymers into smaller, bioavailable molecules.  
           - Enhance nutrient accessibility, improve fermentation efficiency, and contribute to better digestibility, flavor, and texture in millet-based probiotic foods.
            
            2. **Oxidoreductases**  
           - Catalyze redox reactions that maintain cellular energy balance and redox homeostasis.  
           - Support oxidative stress resistance, enhance antioxidant potential, and improve LAB survival during fermentation, storage, and gastrointestinal passage.
        
            3. **Transferases**  
           - Transfer functional groups between molecules, driving key biosynthetic and metabolic processes.  
           - Facilitate the formation of essential biomolecules, promoting metabolic flexibility, efficient growth, and adaptation in both food matrices and gut environments.
            
            ⭐ **Key Takeaway**  
            Hydrolases, Oxidoreductases, and Transferases synergistically enhance **nutrient utilization, redox balance, and metabolic adaptability**, leading to **robust fermentation, improved probiotic survival, and functional health benefits** in millet-derived *Lactic Acid Bacteria*.
            """)

        with st.expander("Overall Summary"):
            st.markdown("""
            | **Dominant EC Class** | **Role in Probiotic Function & Fermentation** | **Overall Benefit in Millet-Based Functional Foods** |
            |---|---|---|
            | **Hydrolases** | Degrade complex carbohydrates, proteins, and other biomolecules into simpler, absorbable units. | Enhance nutrient bioavailability, digestibility, and sensory quality while supporting probiotic metabolism. |
            | **Transferases** | Transfer functional groups to drive metabolic and biosynthetic pathways essential for growth. | Improve energy utilization, metabolic adaptability, and consistent LAB performance during fermentation and in the gut. |
            | **Oxidoreductases** *(notable in* *Lactococcus lactis*) | Regulate redox balance and maintain cellular homeostasis under stress. | Boost oxidative stress tolerance, antioxidant activity, and probiotic survival in acidic or oxygen-variable environments. |
            | **Lyases** *(distinct in* *Enterococcus casseliflavus*) | Catalyze bond cleavage or formation without water, producing key flavor intermediates. | Contribute to desirable aroma and flavor compounds in fermented millet foods while aiding adaptive metabolism. |
            | **Ligases** *(distinct in* *Weissella cibaria*) | Join molecules to support DNA repair and biosynthetic processes. | Strengthen genomic integrity, membrane stability, and long-term fermentation resilience. |
            
            ⭐ **Key Takeaway**  
            Across millet-derived *Lactic Acid Bacteria* (LAB), **Hydrolases and Transferases** emerge as the dominant enzyme classes, reflecting:  
            - **Efficient nutrient breakdown and energy metabolism**  
            - **Enhanced stress tolerance and growth stability**  
            - **Strong adaptability and probiotic potential**  
            """)
       
        with st.expander("Which are the dominant BRITE classes and subclasses of the pathways associated with each EC number and what do they mean?"):
           dict=brite()
           for isolate, values in dict["EC"].items():
               with st.expander(isolate):
                    st.markdown("**Top 5 BRITE Classes:**")
                    st.write(values["top_5_brite_class"])
                    st.markdown("**Top 5 BRITE Sub-classes:**")
                    st.write(values["top_5_brite_subclass"])
        with st.expander("Overall Summary"):
            st.markdown("""
            **Overall Probiotic Functional Pattern**  
            
            Across all isolates, **Metabolism** dominates, reflecting their ability to survive, adapt, and function in the gut by:  
            - Enhancing nutrient breakdown and bioavailability  
            - Producing metabolites that support gut health  
            - Maintaining cellular stability under stress  
            
            **Isolate-wise Probiotic Summary**  
            
            1. **Enterococcus casseliflavus (Proso Millet)**  
            
            **Probiotic Strengths:**  
            - Amino acid metabolism: supports gut nutrient availability and bioactive metabolite production  
            - Signal and transport systems: promote survival under gastrointestinal conditions  
            - Stable cellular function: ensures resilience during gut transit  
            
            **Interpretation:** Highly adaptable probiotic with strong survival and functional potential in the gastrointestinal tract.
            
            2. **Weissella cibaria NM01 (Foxtail Millet)**  
            3. **Weissella cibaria SM01 (Little Millet)**  
            
            **Probiotic Strengths:**  
            - Carbohydrate metabolism: allows utilization of dietary fibers and prebiotic substrates  
            - DNA repair and cell maintenance: supports survival and steady activity in the gut  
            - Moderate amino acid metabolism: contributes to mild production of beneficial metabolites  
            
            **Interpretation:** Mild probiotics, effective for gentle modulation of gut environment and nutrient support.
            
            4. **Lactococcus lactis (Little Millet)**  
            
            **Probiotic Strengths:**  
            - Carbohydrate and amino acid metabolism: produces metabolites that can benefit gut health  
            - Stable genome: ensures consistent survival and functionality  
            - Lipid metabolism: may contribute to bioactive compound synthesis in the gut  
            
            **Interpretation:** Strong probiotic starter strain with reliable survival, metabolic activity, and potential gut health benefits.
            
            **Key Comparative Insight**  
            
            | Strain | Probiotic Strength | Functional Behavior in Gut |
            |-------|-----------------|---------------------------|
            | **E. casseliflavus** | Highly adaptable | Broad metabolic flexibility; strong survival in gastrointestinal conditions |
            | **W. cibaria NM01 & SM01** | Mild, balanced | Focused on carbohydrate utilization; moderate production of beneficial metabolites |
            | **L. lactis** | Strong starter probiotic | High metabolic activity; consistent survival and bioactive metabolite potential |
            """)


                  
    with st.expander("Overall, are the predicted ECs supporting the use of these LAB in probiotic/food applications?"):
        st.markdown("""
        **Overall Probiotic Functional Pattern**  
        - All strains are active in nutrient metabolism, indicating potential to support digestion, nutrient absorption, and a balanced gut environment.
        
        **Enterococcus casseliflavus (Proso Millet)**  
        - Exhibits broad metabolic functions, suggesting it may aid in breaking down diverse food components and support gut adaptation and microbial balance.
        
        **Weissella cibaria NM01 (Foxtail Millet) & Weissella cibaria SM01 (Little Millet)**  
        - Both strains efficiently utilize plant-based sugars and maintain stable growth, indicating gentle support for digestion and maintenance of a healthy gut environment.
        
        **Lactococcus lactis (Little Millet)**  
        - Strong carbohydrate and amino acid metabolism suggests potential to enhance nutrient breakdown, support digestive comfort, and contribute to overall gut health.
        """)



    st.markdown("<h4 style='text-align:center;'>KO Analysis Summary</h4>", unsafe_allow_html=True)
    with st.expander("Which are the top abundant KO ids and what do they imply?"):
        with st.expander("Enterococcus casseliflavus (Proso Millet)"):
            st.markdown("""
            1. **K02003 – ABC Transporter ATP-Binding Protein**  
            - Uses ATP to transport nutrients and other molecules across the cell membrane.  
            - Supports LAB survival and stress tolerance in the gut by enabling efficient nutrient uptake and toxin removal.
            
            2. **K01223 – 6-Phospho-β-D-Glucosidase**  
            - Breaks down phosphorylated glucosides into fermentable sugars.  
            - Enhances LAB growth and activity in the digestive tract by improving carbohydrate metabolism.
            
            3. **K01990 – ABC-2 Type ATP-Binding Transport Protein**  
            - Hydrolyzes ATP to power transport of nutrients and metabolites.  
            - Strengthens LAB adaptability and stable metabolic function during gut transit.
            
            4. **K01992 – ABC-2 Type Transport System Permease**  
            - Forms a selective membrane channel for transported substrates.  
            - Helps LAB maintain nutrient balance and metabolic flexibility under varying gut conditions.
            
            5. **K02004 – ABC Transport System Membrane Component**  
            - Creates the membrane-spanning portion of ABC transporters for substrate movement.  
            - Promotes LAB nutrient acquisition and stress response, supporting probiotic viability.
            
            6. **K02757 – PTS Beta-Glucoside Transport Protein**  
            - Transports and phosphorylates beta-glucosides for energy use.  
            - Enhances LAB carbohydrate metabolism, contributing to energy availability and activity in the gut.
            
            7. **K06147 – ABC Transporter (Subfamily B) ATP-Binding Protein**  
            - Drives substrate import and export using ATP.  
            - Maintains cellular homeostasis, supporting LAB survival and functionality during digestion.
            
            8. **K07024 – Sucrose-6-Phosphate Hydrolase**  
            - Breaks down sucrose-6-phosphate for energy.  
            - Facilitates efficient carbohydrate utilization, helping LAB stay metabolically active in the gut.
            
            9. **K02761 – PTS Cellobiose Transport Protein**  
            - Transports and phosphorylates cellobiose for energy.  
            - Supports LAB energy metabolism, aiding survival and functional activity in the gastrointestinal tract.
            
            ⭐ **Key Takeaway**  
            These carbohydrate metabolism and ABC transport proteins collectively enhance nutrient uptake, energy utilization, stress resilience, and gut survival, ensuring that LAB remain active and viable as probiotics during digestion.
            """)

        with st.expander("Weisella cibaria NM01 (Foxtail Millet)"):
            st.markdown("""
            1. **K01223 – 6-Phospho-β-Glucosidase**  
            - Breaks down phosphorylated β-glucosides into glucose-6-phosphate for energy.  
            - Helps LAB stay active when simple sugars are scarce, supporting gut survival, stable growth, and metabolic function.
            
            2. **K07024 – Sucrose-6-Phosphate Hydrolase**  
            - Converts sucrose-6-phosphate into usable sucrose.  
            - Enhances carbohydrate utilization in the gut, supporting LAB activity and contributing to overall digestive comfort.
            
            3. **K02073 – D-Methionine ABC Transporter (Binding Protein)**  
            - Binds and imports D-methionine to support protein synthesis.  
            - Helps LAB thrive under nutrient-limited conditions, improving adaptation and functionality during gut transit.
            
            4. **K07335 – ABC Transporter Membrane Component**  
            - Forms part of the membrane channel for nutrient and metabolite transport.  
            - Supports nutrient uptake and resilience, enabling LAB to maintain activity in varying gut environments.
            
            5. **K03294 – Basic Amino Acid / Polyamine Transporter**  
            - Exchanges amino acids and polyamines to maintain cellular balance.  
            - Enhances LAB survival under acidic or stressful conditions in the digestive tract by supporting pH homeostasis and stable growth.
            
            ⭐ **Key Takeaway**  
            These genes collectively support carbohydrate and amino acid utilization, stress tolerance, and metabolic stability, helping LAB remain active, resilient, and functional as probiotics during digestion.
            """)

        with st.expander("Weisella cibaria SM01 (Little Millet)"):
            st.write("Same as Weisella cibaria NM01 (Foxtail Millet)")
        with st.expander("Lactococcus lactis (Little Millet)"):
            st.markdown("""
            1. **K01990 – ABC Transport System ATP-Binding Protein**
            - Uses ATP to import and export nutrients and metabolites across the cell membrane.  
            - Supports LAB survival, activity, and metabolic function in the gut, helping maintain a healthy microbial balance.
            
            2. **K07024 – Sucrose-6-Phosphate Hydrolase**
            - Breaks down sucrose-6-phosphate into usable sugars for energy.  
            - Enhances carbohydrate utilization, supporting LAB growth and digestive function during gut transit.
            
            3. **K01992 – ABC-2 Type Transport System Permease**
            - Forms the membrane channel for selective nutrient and metabolite transport.  
            - Maintains internal balance and improves LAB resilience under gut stress conditions.
            
            4. **K02003 – ABC Transport System ATP-Binding Component**
            - Provides energy for nutrient transport by hydrolyzing ATP.  
            - Strengthens nutrient acquisition and stress tolerance, supporting LAB activity and persistence in the digestive tract.
            
            5. **K01223 – 6-Phospho-β-Glucosidase**
            - Converts phosphorylated sugars into glucose-6-phosphate for energy.  
            - Promotes efficient carbohydrate metabolism, aiding LAB growth, metabolic activity, and digestive support.
            
            ⭐ **Key Takeaway**  
            These genes collectively enhance **nutrient uptake, energy metabolism, and stress resilience**, enabling LAB to remain active, stable, and functional as probiotics while contributing to gut health and food flavor.
            """)

        with st.expander("Overall Summary"):
            st.markdown("""
            | **Functional Feature** | **Key Genes / Proteins** | **Probiotic & Food Relevance** |
            |---|---|---|
            | **Carbohydrate Breakdown & Energy Use** | 6-Phospho-β-Glucosidase (K01223), Sucrose-6-Phosphate Hydrolase (K07024), PTS Transport Proteins (K02757 / K02761) | Enables LAB to efficiently utilize millet sugars, supporting steady growth, consistent fermentation, and mild flavor formation in foods. |
            | **Nutrient Transport & Cell Support** | ABC Transport System Proteins (K01990, K01992, K02003, K02004, K07335) | Facilitates uptake of nutrients and removal of metabolic waste, enhancing LAB survival and activity in foods and during gut transit. |
            | **Amino Acid Balance & Growth Maintenance** | D-Methionine Transporter (K02073), Polyamine/Amino Acid Transporter (K03294) | Supports protein synthesis, cell stability, and resilience, helping strains remain active in the digestive tract and during storage. |
            | **Stress Protection & Environmental Adaptation** | Signal Transduction & Membrane Transport Systems | Helps LAB adapt to acidic and changing conditions in fermented foods and the gut, promoting probiotic survival and functional stability. |
            
            ⭐ **Key Takeaway**  
            Millet-derived LAB strains demonstrate strong probiotic potential by:
            - Efficiently utilizing plant-based sugars  
            - Maintaining stable growth and cellular health  
            - Surviving acidic and digestive stress  
            - Supporting gentle gut balance and overall digestive wellness
            """)

      
    with st.expander("Which are the dominant BRITE classes and subclasses of the pathways associated with each KO id and what do they mean?"):
        dict=brite()
        for isolate, values in dict["KO"].items():
            with st.expander(isolate):
                st.markdown("**Top 5 BRITE Classes:**")
                st.write(values["top_5_brite_class"])
                st.markdown("**Top 5 BRITE Sub-classes:**")
                st.write(values["top_5_brite_subclass"])
        with st.expander("Overall Summary"):
                st.markdown("""
                **Overall Functional Pattern**
                - Across all isolates, **Metabolism** is the most dominant BRITE class.  
                - This indicates that these LAB strains actively contribute to **nutrient breakdown, energy generation, and gut biochemical balance**, supporting:
                    - Enhanced nutrient absorption  
                    - Smoother digestion  
                    - Maintenance of healthy gut microbiota  
                
                **Isolate-wise Functional Summary**
                
                1. **Enterococcus casseliflavus (Proso Millet)**
                
                **Key Functional Strengths:**
                - **Membrane transport:** efficient nutrient uptake, resilience in gut/stress conditions  
                - **Carbohydrate metabolism:** effective breakdown of dietary sugars  
                - **Glycan biosynthesis & microbial interactions:** supports cell wall stability and beneficial gut interactions  
                - **Energy metabolism:** maintains activity under stress  
                
                **Interpretation:** A **resilient and adaptable probiotic**, ideal for **gut stability, nutrient utilization, and digestive balance**.
                
                2. **Weisella cibaria NM01 (Foxtail Millet)**  
                3. **Weisella cibaria SM01 (Little Millet)**
                
                **Key Functional Strengths (both strains):**
                - **Carbohydrate metabolism:** aids smooth digestion of plant-derived sugars  
                - **Amino acid metabolism:** provides gentle gut nourishment  
                - **Membrane transport:** maintains cellular balance in the gut  
                - **Signal transduction:** enables response to gut environmental changes  
                
                **Interpretation:** **Mild and gut-friendly probiotics**, supporting **routine digestive comfort and microbiome balance**.
                
                4. **Lactococcus lactis (Little Millet)**
                
                **Key Functional Strengths:**
                - **Strong carbohydrate metabolism:** ensures reliable energy and activity  
                - **Amino acid metabolism:** supports beneficial gut metabolites and digestive comfort  
                - **Signal transduction & membrane transport:** enhances adaptability  
                - **Energy metabolism:** promotes sustained probiotic function  
                
                **Interpretation:** A **highly reliable probiotic**, suitable for **digestive wellness and balanced gut flora**.
                
                **Key Comparative Insight**
                
                | Strain | Best Role | Functional Behavior |
                |-------|-----------|-------------------|
                | **E. casseliflavus** | Gut-adaptive and stable performer | Broad metabolic flexibility and survival strength |
                | **W. cibaria NM01 & SM01** | Gentle digestion support | Smooth carbohydrate breakdown and balanced growth |
                | **L. lactis** | Reliable routine probiotic | High and steady nutrient metabolism with stable activity |
                """)

                
    with st.expander("Overall, are the predicted KOs supporting the use of these LAB in probiotic/food applications?"):
        st.markdown("""
        **Overall Probiotic Functional Pattern**  
        - All strains actively contribute to nutrient metabolism, supporting digestion, nutrient absorption, and a balanced gut environment.
        
        **Enterococcus casseliflavus (Proso Millet)**  
        - A resilient probiotic that efficiently utilizes nutrients and helps maintain gut stability under stress.
        
        **Weissella cibaria NM01 (Foxtail Millet) & Weissella cibaria SM01 (Little Millet)**  
        - Gentle, gut-friendly probiotics that support smooth carbohydrate digestion and maintain microbiome balance.
        
        **Lactococcus lactis (Little Millet)**  
        - A reliable probiotic with sustained energy and nutrient metabolism, promoting digestive wellness and balanced gut flora.
        """)

    st.markdown("<h4 style='text-align:center;'>PWY Analysis Summary</h4>", unsafe_allow_html=True) 
    with st.expander("Which are the pathways which have completeness as 1 and what do they imply?"):
        with st.expander("Enterococcus casseliflavus (Proso Millet)"):
            st.markdown("""
            
            1. **ANAGLYCOLYSIS-PWY – Glycolysis III (from glucose)**  
           - Provides energy for LAB growth and survival by converting glucose to pyruvate.  
           - Supports acid production that helps probiotics thrive and contributes to gut health.  
            
            2. **ARGSYNBSUB-PWY – L-Arginine Biosynthesis II (Acetyl Cycle)**  
           - Produces arginine to support protein synthesis and bacterial metabolism.  
           - Enhances probiotic metabolic versatility and resilience in the gut.  
            
            3. **PEPTIDOGLYCANSYN-PWY – Peptidoglycan Biosynthesis I**  
           - Builds strong bacterial cell walls, maintaining structural integrity.  
           - Ensures probiotic survival under gut stress and during food fermentation.  
            
            4. **PWY-6386 – UDP-N-Acetylmuramoyl-Pentapeptide Biosynthesis II**  
               - Generates lysine-containing peptidoglycan precursors for robust cell walls.  
               - Supports probiotic persistence and stability in the gastrointestinal tract.  
            
            5. **PWY-6387 – UDP-N-Acetylmuramoyl-Pentapeptide Biosynthesis I**  
           - Forms meso-diaminopimelate-containing peptidoglycan precursors.  
           - Maintains probiotic viability and resilience under stress conditions.  
            
            6. **PWY-5100 – Pyruvate Fermentation to Acetate and Lactate II**  
           - Produces lactate and acetate to generate energy anaerobically.  
           - Helps probiotics survive in the gut and supports a healthy microbial balance.  
            
            7. **UDPNAGSYN-PWY – UDP-N-Acetyl-D-Glucosamine Biosynthesis I**  
           - Supplies building blocks for cell wall and peptidoglycan biosynthesis.  
           - Maintains probiotic integrity and functionality in food and gut environments.  
            
            8. **GALACTUROCAT-PWY – D-Galacturonate Degradation I**  
           - Enables utilization of plant-derived sugars as energy sources.  
           - Supports probiotic growth in plant-based foods and contributes to gut fiber metabolism.  
            
            ⭐ **Key Takeaway**  
            These pathways collectively enhance **energy metabolism, cell wall integrity, amino acid utilization, and fiber breakdown**, ensuring probiotics remain active, resilient, and beneficial for gut health.
            """)

        with st.expander("Weisella cibaria NM01 (Foxtail Millet)"):
            st.markdown("""
            **1. ANAGLYCOLYSIS-PWY (Glycolysis III)**  
            - Provides a primary energy source by metabolizing glucose anaerobically, supporting LAB growth and survival.  
            - Drives fermentation, producing acids that influence flavor, texture, and preservation of fermented foods.  
            
            **2. ARGSYNBSUB-PWY (L-arginine biosynthesis II)**  
            - Supports bacterial growth and stress response by supplying L-arginine for cellular functions.  
            - Enhances fermentation performance, potentially improving flavor and nutritional value of products.  
            
            **3. PEPTIDOGLYCANSYN-PWY (Peptidoglycan biosynthesis I)**  
            - Maintains cell wall integrity and shape, essential for bacterial viability and resistance to stress.  
            - Supports robustness during fermentation, contributing to product consistency, safety, and texture.  
            
            **4. PWY-6386 (UDP-N-acetylmuramoyl-pentapeptide biosynthesis II, lysine-containing)**  
            - Ensures strong cell wall assembly, supporting bacterial survival in challenging fermentation conditions.  
            - Contributes to texture and stability of fermented products by maintaining cell viability.  
            
            **5. PWY-6387 (UDP-N-acetylmuramoyl-pentapeptide biosynthesis I, meso-diaminopimelate-containing)**  
            - Strengthens peptidoglycan biosynthesis, promoting bacterial resistance to environmental stress.  
            - Enhances probiotic stability and consistency in fermented foods.  
            
            **6. PWY-5100 (Pyruvate fermentation to acetate and lactate II)**  
            - Enables energy production under anaerobic conditions, supporting LAB growth.  
            - Produces acids that improve flavor, preservation, and sensory qualities of fermented foods.  
            
            **7. UDPNAGSYN-PWY (UDP-N-acetyl-D-glucosamine biosynthesis I)**  
            - Supports cell wall formation and structural integrity, crucial for bacterial viability.  
            - Enhances probiotic durability and texture-modifying properties during fermentation.  
            
            **8. GALACTUROCAT-PWY (D-galacturonate degradation I)**  
            - Allows utilization of plant-derived pectin components, supporting growth in fiber-rich environments.  
            - Improves breakdown of dietary fibers during fermentation, enhancing texture and nutritional value.

            ⭐ **Key Takeaway** 
            These pathways collectively enhance LAB growth, stress resistance, and energy metabolism, while supporting fermentation-driven acid production, cell wall integrity, and breakdown of dietary fibers, ultimately improving probiotic viability, stability, and the sensory and nutritional quality of fermented foods.
            """)
        with st.expander("Weisella cibaria SM01 (Little Millet)"):
            st.write("Same as Weisella cibaria NM01 (Foxtail Millet)")
        with st.expander("Lactococcus lactis (Little Millet)"):
            st.markdown("""
            **1. ANAGLYCOLYSIS-PWY**  
            - Catalyzes glycolysis, converting glucose to pyruvate and generating ATP and NADH, providing primary energy for LAB growth.  
            - Drives fermentation processes, producing acids that improve flavor, texture, and preservation of fermented foods.  
            
            **2. ARGSYNBSUB-PWY**  
            - Catalyzes L-arginine biosynthesis, supporting protein synthesis and nitrogen metabolism in LAB.  
            - Enhances bacterial vitality and fermentation performance, potentially improving flavor and nutritional value of fermented products.  
            
            **3. PEPTIDOGLYCANSYN-PWY**  
            - Synthesizes peptidoglycan precursors essential for cell wall formation and structural integrity.  
            - Supports bacterial robustness and survival during fermentation, contributing to product consistency and safety.  
            
            **4. PWY-6386**  
            - Produces UDP-N-acetylmuramoyl-pentapeptide (lysine-containing) for peptidoglycan biosynthesis.  
            - Maintains bacterial cell wall strength, improving survival and stability during fermentation.  
            
            **5. PWY-6387**  
            - Produces UDP-N-acetylmuramoyl-pentapeptide (meso-diaminopimelate-containing), crucial for robust cell wall formation.  
            - Enhances stress tolerance and viability of LAB in food fermentation.  
            
            **6. PWY-5100**  
            - Converts pyruvate to acetate and lactate, generating ATP anaerobically.  
            - Contributes to acidification, flavor, and preservation in fermented foods.  
            
            **7. UDPNAGSYN-PWY**  
            - Synthesizes UDP-N-acetyl-D-glucosamine, a key precursor for peptidoglycan and exopolysaccharide formation.  
            - Supports cell wall integrity and probiotic survival, enhancing texture and stability in fermented products.  
            
            **8. GALACTUROCAT-PWY**  
            - Metabolizes D-galacturonate into central metabolites for energy production.  
            - Improves breakdown of dietary fibers, supporting fermentation performance and nutritional properties.  
            
            ⭐ **Key Takeaway**  
            - These eight pathways are central to probiotic function, ensuring LAB energy generation, robust cell wall formation, amino acid and nucleotide metabolism, and effective fermentation, collectively enhancing probiotic viability, food quality, and health benefits.
            """)

        with st.expander("Overall Summary"):
            st.markdown("""
            | **Functional Feature** | **Key Enzymes / Pathways** | **Relevance to Probiotic Function & Gut Adaptation** |
            |---|---|---|
            | **Energy Production & Glycolysis** | ANAGLYCOLYSIS-PWY | Converts glucose to pyruvate, generating ATP and NADH to support LAB growth, survival, and fermentation-driven acid production in the gut. |
            | **Amino Acid Biosynthesis** | ARGSYNBSUB-PWY | Produces L-arginine for protein synthesis and nitrogen metabolism, enhancing bacterial growth, stress resilience, and metabolic versatility. |
            | **Cell Wall Integrity & Peptidoglycan Formation** | PEPTIDOGLYCANSYN-PWY, PWY-6386, PWY-6387, UDPNAGSYN-PWY | Synthesizes peptidoglycan precursors and UDP-N-acetylglucosamine, maintaining robust cell walls that ensure survival under gut stress and during fermentation. |
            | **Fermentation & Acid Production** | PWY-5100 | Converts pyruvate to lactate and acetate, supporting anaerobic energy generation, acidification of foods, and healthy microbial balance in the gut. |
            | **Plant Sugar Utilization & Fiber Metabolism** | GALACTUROCAT-PWY | Metabolizes D-galacturonate from plant sources, enabling energy extraction from dietary fibers and promoting colonization in fiber-rich gut environments. |
            
            ⭐ **Key Takeaway**  
            These eight pathways collectively ensure:  
            - **Efficient energy metabolism and fermentation capacity**  
            - **Strong cell wall formation and structural stability**  
            - **Amino acid biosynthesis supporting growth and stress tolerance**  
            - **Utilization of dietary fibers for enhanced gut adaptation**  
            """)

   
    with st.expander("Overall, how relevant are the predicted pathways in terms of probiotic/food appplications?"):
         
            st.markdown("""
              **Overall Probiotic Functional Pattern**  
              - All millet-derived LAB strains exhibit complete and enriched pathways for energy metabolism, amino acid biosynthesis, and cell wall formation, reflecting strong probiotic potential.  
              - These pathways collectively indicate efficient fermentation ability, gut adaptability, and metabolic resilience** suitable for probiotic and food applications.  
    
              **Enterococcus casseliflavus (Proso Millet)**  
              - Shows enhanced glycolysis and amino acid biosynthesis, promoting robust growth and fermentation-driven acid production.  
              - Strengthened cell wall synthesis and coenzyme pathways ensure resilience under gut and fermentation stress.  
    
              **Weissella cibaria NM01 (Foxtail Millet) & Weissella cibaria SM01 (Little Millet)**  
              - Exhibit **efficient utilization of plant sugars and fibers**, supporting growth in plant-based environments and improved prebiotic interactions.  
              - Maintain **balanced energy metabolism and acid production**, promoting gut colonization and microbiome stability.  
    
               **Lactococcus lactis (Little Millet)**  
               - Demonstrates strong amino acid and nucleotide biosynthesis, enhancing protein metabolism and growth stability.  
               - Possesses cell wall and fermentation pathways, ensuring survival, acidification ability, and probiotic persistence.  
    
              ⭐ **Key Takeaway**  
              - Collectively, these LAB strains display **robust metabolic versatility, structural integrity, and fermentation efficiency**
              """)
      
    
    st.markdown("<h4 style='text-align:center;'>Biological Traits Analysis Summary</h4>", unsafe_allow_html=True)
    with st.expander("Which are the common and unique biological traits?"):
            df = create_trait_table(millet_map, path="picrust_output_files/")
            df = style_trait_table(df)
            st.dataframe(df, use_container_width=True)
    with st.expander("Overall, what are the biological traits supporting the use of these LABs in probiotic/food applications?"):
            st.markdown("""
            **Enterococcus casseliflavus (Proso Millet)** 
            
            **Traits:** Acid tolerance, adhesion to intestinal cells, amino acid & carbohydrate metabolism, cell wall integrity, DNA repair, enzyme regulation, fermentation efficiency, flavor enhancement, genomic stability, lactic acid production, membrane integrity, oxidative stress resistance, protein synthesis, salt tolerance, signal transduction, stress response, temperature resistance.  
            
            **Probiotic Relevance:**  
            1. Strong acid tolerance, adhesion, and oxidative stress resistance → high potential to survive gut conditions and interact with intestinal cells.  
            2. Lactic acid production, fermentation efficiency, and flavor enhancement → useful for gut health and food fermentation applications.  
            
            **Weissella cibaria NM01 (Foxtail Millet)**
            
            **Traits:** Amino acid & carbohydrate metabolism, cell wall integrity, DNA replication, enzyme regulation, fermentation efficiency, lactic acid production, membrane integrity, oxidative stress resistance, stress response.  
            
            **Probiotic Relevance:**  
            1. Limited acid tolerance and adhesion → moderate gut survival, but stress response and oxidative stress resistance support resilience.  
            2. Maintains metabolic and fermentation functions → suitable for food applications rather than strong gut colonization.  
            
            **Weissella cibaria SM01 (Little Millet)** 
            
            **Traits:** Amino acid & carbohydrate metabolism, cell wall integrity, DNA replication, energy metabolism, fermentation efficiency, flavor enhancement, genomic stability, lactic acid production, membrane integrity, oxidative stress resistance, nutrient uptake, stress resistance, transport.  
            
            **Probiotic Relevance:**  
            1. Limited acid tolerance and adhesion → weaker gut colonization potential.  
            2. Strong metabolic versatility, energy metabolism, and stress resistance → useful for food fermentation and nutrient processing.  
            
            **Lactococcus lactis (Little Millet)**  
            
            **Traits:** Acid tolerance, adhesion, amino acid & carbohydrate metabolism, antioxidant activity, cell wall integrity, DNA repair & replication, energy metabolism, environmental adaptation, enzyme regulation, fermentation, fermentation efficiency, flavor enhancement, genomic stability, lactic acid production, membrane integrity, metabolic regulation, nutrient uptake, oxidative stress resistance, protein processing & synthesis, redox balance, salt tolerance, stress response & tolerance, substrate utilization.  
            
            **Probiotic Relevance:**  
            1. Exhibits nearly all probiotic-relevant traits → high potential for gut survival, functionality, and colonization.  
            2. Antioxidant activity, protein synthesis, and substrate utilization → additional health-promoting effects and fermentation versatility.  
            
            **Overall Summary**
            1. **Gut survival & health impact:** Millet 1 and Millet 4 LAB are most promising due to acid tolerance, adhesion, and stress resistance. Millet 2 and 3 are less robust but metabolically capable.  
            2. **Fermentation & functional foods:** All strains contribute to fermentation, lactic acid production, and flavor enhancement, with Millet 4 being the most versatile, followed by Millet 1.  
            """)

def create_trait_table(millet_map, path=""):
    
    prefixes = ["ec", "ko", "pwy"]
    millet_traits = {}
   
    for millet, number in millet_map.items():
        traits_set = set()
        for prefix in prefixes:
            file_path = f"{path}{prefix}{number}_word.csv"
            try:
                df = pd.read_csv(file_path)
                if "trait" in df.columns:
                    traits_set.update(df["trait"].dropna().astype(str).tolist())
                else:
                    print(f"Warning: 'trait' column not found in {file_path}")
            except FileNotFoundError:
                print(f"Warning: {file_path} not found!")
        millet_traits[millet] = traits_set
   
    all_traits = sorted(set().union(*millet_traits.values()))

    data = {}
    for millet, traits in millet_traits.items():
        data[millet] = ["Yes" if trait in traits else "No" for trait in all_traits]
    
    trait_df = pd.DataFrame(data, index=all_traits)
    trait_df.index.name = "Trait"
    
    return trait_df
def style_trait_table(df):
    return df.style.applymap(lambda x: 'background-color: #DFFBB9' if x == "Yes" else '')
    
# --------------------------------------------------------------------- Navigation ---------------------------------------------------------------------
page = st.session_state.page
if page == "home":
    home()
elif page == "summarized_analysis":
    summary()
elif page == "ec_analysis":
    ec_page()
elif page == "ko_analysis":
    ko_page()
elif page == "pwy_analysis":
    pwy_page()  
elif page == "milletwise_analysis":
    millet()
elif page == "ec_class":
    ec_class()
elif page=="trait":
    trait()
elif page=="couq":
    couq()

