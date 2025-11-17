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
        background-color: #ffff66;  /* Yellow box */
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
    st.markdown("<h2 style='text-align:center;'>GraintoGut</h2>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align:center;  font-style:italic;'><i>Linking genomic potential of Millet derived Lactic Acid Bacteria to food and probiotic applications</i></h4>", unsafe_allow_html=True)
    st.write("") 
  
 # ----------------------------------- Sidebar with Project Description ------------------------------------------------------------------------
   # "Back to Home" button at the top of the sidebar
    
    # ====== PAGE LAYOUT ======
    left_col, middle_col, right_col = st.columns([1,2,3])
    
    # ================================
    # LEFT COLUMN
    # ================================
    with left_col:
        # ===== Expander: About this App ===== 
        with st.sidebar.expander("About This App", expanded=False):
            st.markdown("""
            1. This app is based on a research paper on lactic acid bacteria (LAB) isolated from millets  
            (<a href="https://github.com/VarshaS-37/Grain2Gut/blob/main/Isolation_%26_characterization_of_biological_traits_of_millet-derived_lactic_acid_bacteria.pdf" target="_blank">Research Paper</a>)  
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

