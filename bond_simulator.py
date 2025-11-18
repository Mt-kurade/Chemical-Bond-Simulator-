import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

st.set_page_config(page_title="Chemical Bonding Simulator", layout="wide")

#
st.markdown("""
<style>
/* Define the increased grid color here: (White with 8% opacity) */
:root {
    --grid-color: rgba(255, 255, 255, 0.08); 
}

/* Root app container: Holds the actual grid background */
.stApp {
    background-color: #000000;
    /* This creates the repeating grid pattern */
    background-image: 
        linear-gradient(var(--grid-color) 1px, transparent 1px),
        linear-gradient(90deg, var(--grid-color) 1px, transparent 1px);
    background-size: 40px 40px; 
}

/* IMPORTANT: Ensure ALL internal Streamlit containers are TRANSPARENT */
[data-testid="stAppViewContainer"], 
[data-testid="stAppViewContainer"] > .main,
[data-testid="stSidebar"],
section.main { 
    background-color: transparent !important;
}

/* --- FONT COLOR FIXES --- */

/* 1. KEY CHANGE: General body text (st.write() and core text content) is set to a slightly dimmer light gray */
html, body, [class*="css"], p, div[data-testid="stMarkdownContainer"] {
    color: #EEEEEE !important; /* Slightly dimmer white */
    font-family: 'Times New Roman', serif !important;
}

h1, h2, h3, h4, h5, h6 {
    color: #FFFFFF !important;
    font-family: 'Times New Roman', serif !important;
}

div[data-testid="stSlider"] label {
    color: #FFFFFF !important;
    font-family: 'Times New Roman', serif !important;
}

div[data-testid="stThumbValue"] {
    color: #FFFFFF !important; 
    background-color: #111111 !important; 
    border: 1px solid #FFFFFF50;
}

/* 4. Caption Text is set to the slightly dimmer light gray */
footer [data-testid="stCaptionContainer"] {
    color: #EEEEEE !important;
}

/* --- Other Styling (Unchanged) --- */

/* Slider thumb and track */
[data-baseweb="slider"] > div {
    background: #222222 !important;
}

/* Horizontal dividers */
hr {
    border: 1px solid #333333 !important;
}
</style>
""", unsafe_allow_html=True)

plt.style.use("dark_background")
matplotlib.rcParams["font.family"] = "Times New Roman"
matplotlib.rcParams["axes.edgecolor"] = "white"
matplotlib.rcParams["axes.labelcolor"] = "white"
matplotlib.rcParams["xtick.color"] = "white"
matplotlib.rcParams["ytick.color"] = "white"


st.title("Chemical Bonding Simulator")
st.write("""
Explore how **bond energy** changes with **bond length** using the Morse Potential, 
and how **lattice energy** depends on **ion distance** using the Born–Lande model.
""")

DEFAULT_DE = 400
DEFAULT_A = 1.2
DEFAULT_RE = 1.0

D_e = DEFAULT_DE
a = DEFAULT_A
r_e = DEFAULT_RE
atom_distance = DEFAULT_RE

tab1, tab2 = st.tabs(["Bond Energy vs. Bond Length (Morse)", " Lattice Energy vs. Ionic Distance (Born–Lande)"])

# 1. Bond Energy vs. Bond Length 
with tab1:
    st.markdown("### Morse Potential Parameters and Visualization")
    
    col1, col2, col3, col4 = st.columns(4) 
    
    with col1:
        D_e = st.slider("Bond Dissociation Energy, $D_e$ (kJ/mol)", 100, 1000, DEFAULT_DE)
    with col2:
        a = st.slider("Steepness Constant, $a$", 0.5, 3.0, DEFAULT_A, 0.1)
    with col3:
        r_e = st.slider("Equilibrium Bond Length, $r_e$ (Å)", 0.5, 2.5, DEFAULT_RE, 0.05)
    with col4:
        atom_distance = st.slider("Current Bond Length (Å)", 0.3, 3.0, r_e, 0.01) 
    
    st.latex(r"E(r) = D_e (1 - e^{-a(r - r_e)})^2") 
    
    # Range of bond lengths
    r = np.linspace(0.3, 3.0, 400)
    E = D_e * (1 - np.exp(-a * (r - r_e)))**2
    E_current = D_e * (1 - np.exp(-a * (atom_distance - r_e)))**2

    viz_col, plot_col = st.columns(2)

    with viz_col:
        st.markdown("#### Atom Distance Visualization")
        fig_atom, ax_atom = plt.subplots(figsize=(4.5, 1.2), facecolor='none') 
        ax_atom.set_facecolor('none')
        ax_atom.set_xlim(0, 4)
        ax_atom.set_ylim(-1, 1)
        ax_atom.axis("off")

        # positions
        atom1_x = 2 - atom_distance / 2
        atom2_x = 2 + atom_distance / 2

        # draw atoms
        color1 = "#00BFFF"
        color2 = "#FF6347"
        alpha_val = 0.9 - (abs(atom_distance - r_e) / (3.0 - 0.3)) * 0.5 
        circle1 = plt.Circle((atom1_x, 0), 0.35, color=color1, alpha=alpha_val)
        circle2 = plt.Circle((atom2_x, 0), 0.35, color=color2, alpha=alpha_val)
        ax_atom.add_artist(circle1)
        ax_atom.add_artist(circle2)
        ax_atom.plot([atom1_x, atom2_x], [0, 0], 'w--', linewidth=0.5) 
        ax_atom.text(0.5, 0.6, f"Bond Length = **{atom_distance:.2f} Å**",
                     fontsize=12, color="white", fontfamily="Times New Roman",
                     horizontalalignment='left')

        st.pyplot(fig_atom)
    
    # 1B. MORSE POTENTIAL PLOT 
    with plot_col:
        fig, ax = plt.subplots(figsize=(5, 3.5), facecolor='none') 
        ax.set_facecolor('none') 
        ax.plot(r, E, label='Bond Energy Curve', linewidth=3, color='#00BFFF')
        ax.axvline(r_e, color='r', linestyle='--', label=f'Equilibrium $r_e$ = {r_e} Å')
        
        ax.plot(atom_distance, E_current, 'o', color='yellow', markersize=8, 
                label=f'Current ($E$ = {E_current:.0f} kJ/mol)')
                
        ax.set_xlabel("Bond Length (Å)")
        ax.set_ylabel("Energy (kJ/mol)")
        ax.set_title("Bond Energy vs Bond Length (Morse Potential)")
        
        ax.legend()
        st.pyplot(fig)

    st.markdown("---")
    st.write(f"""
    **Current Energy:** **{E_current:.2f} kJ/mol** at **{atom_distance:.2f} Å**. 
    The bond is most stable (lowest energy) at the equilibrium length $r_e$ = {r_e} Å. 
    As bond length increases, energy rises towards $D_e$, indicating **bond dissociation**.
    """)


# 2. Lattice Energy 
with tab2:
    st.markdown("### Born–Lande Model for Lattice Energy")
    st.latex(r"U = -\frac{N_A M |z^+ z^-| e^2}{4 \pi \varepsilon_0 r_0}\left(1 - \frac{1}{n}\right)") 
    
    st.markdown("#### Ionic Crystal Parameters")
    colA, colB, colC, colD = st.columns(4)
    with colA:
        z_plus = st.slider("Cation Charge ($|z⁺|$)", 1, 3, 1)
    with colB:
        z_minus = st.slider("Anion Charge ($|z⁻|$)", 1, 3, 1)
    with colC:
        n = st.slider("Born Exponent ($n$)", 5, 15, 9)
    with colD:
        M = st.slider("Madelung Constant ($M$)", 1.5, 2.5, 1.75, 0.01)

    r0_nm = np.linspace(0.1, 1.0, 300)

    e = 1.602176634e-19
    NA = 6.02214076e23
    eps0 = 8.8541878128e-12

    # Lattice energy calculation
    C = (NA * e**2) / (4 * np.pi * eps0)
    r_meters = r0_nm * 1e-9
    U_Jmol = -(C * M * z_plus * z_minus) / r_meters * (1 - 1/n)
    U_kJmol = U_Jmol / 1000

    # Plot
    fig2, ax2 = plt.subplots(figsize=(6, 4), facecolor='none')
    ax2.set_facecolor('none')
    ax2.plot(r0_nm, U_kJmol, color='#FF6347', linewidth=3)
    ax2.set_xlabel("Interionic Distance $r_0$ (nm)")
    ax2.set_ylabel("Lattice Energy $U$ (kJ/mol)")
    ax2.set_title("Lattice Energy vs Ionic Distance (Born–Lande)")
    
    st.pyplot(fig2)

    st.write("""
    **Observation:** Lattice energy ($U$) is **negative**, indicating an **exothermic** process. 
    It becomes **more negative** (stronger attraction) as ionic distance $r_0$ **decreases** or as ionic charges **increase**.
    """)

st.markdown("---")

st.caption("Made with ❤️ for STEAM-H :3 Integrating Chem + Maths through Modeling and Visualization.")
