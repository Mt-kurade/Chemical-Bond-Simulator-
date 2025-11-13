# Visualizing the Maths of Chemical bonding [The Morse Potential & Born-Landé Equation]
https://chemical-bond-simulator.streamlit.app/

An interactive simulator that models and visualizes **bonding relationships** in chemistry through **mathematical equations**.  
Built using **Python + Streamlit**, this project graphs the mathematical formula for The Morse Potential and Born-Landé Equation. 

## Overview

1. **Morse Potential** — models the relationship between **bond energy** and **bond length** for covalent bonds.
The Morse Potential parameters are:
2. **Born–Lande Equation** — models **lattice energy** and **ionic distance** for ionic compounds.

## Background

### 1. Bond Energy vs Bond Length — *Morse Potential*

<img width="656" height="197" alt="Screenshot 2025-11-13 141753" src="https://github.com/user-attachments/assets/d34127aa-fe72-40ba-8aec-7fbf1be00ced" />
<img width="888" height="652" alt="Screenshot 2025-11-13 141635" src="https://github.com/user-attachments/assets/2380abf3-99ad-4cce-a744-3170a3b0eaa0" />

- **\(Er))** – potential energy of the bond  
- **\(De)** – bond dissociation energy  
- **\(re\)** – equilibrium bond length  
- **\(a)** – steepness constant

Demonstrates how atoms achieve **stability at minimum energy** when attractive and repulsive forces balance.


###  2. Lattice Energy — *Born–Lande Equation*
<img width="674" height="236" alt="Screenshot 2025-11-13 142019" src="https://github.com/user-attachments/assets/0d3bc4c5-b6a3-48d4-828d-fb35822bec98" />
<img width="884" height="775" alt="Screenshot 2025-11-13 141415" src="https://github.com/user-attachments/assets/cd5e563c-966e-4976-b228-776b1bdce730" />

- **\(|Z+|, |Z-|)** – ionic charges (Cation, Anion) 
- **\(r0)** – inter-ionic distance  
- **\(M)** – Madelung constant  
- **\(n)** – Born exponent  
- **\(U)** – lattice energy  

How ionic attraction and repulsion determine crystal stability.


## Running the Simulator

###  Requirements
- Python 3.10+
- [Streamlit](https://streamlit.io)
- Matplotlib
- NumPy

Install libs in venv:
```bash
pip install streamlit matplotlib numpy
