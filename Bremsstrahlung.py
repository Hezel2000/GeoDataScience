#!/usr/bin/env python
# coding: utf-8
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from bokeh.plotting import figure, output_file, show
from bokeh.models import Panel, Tabs

st.header('Bremsstrahlung')

st.write('''
Kramers' Law describes on which parameters the Bremsstrahlung as a function of the photon energy 
of the Bremsstrahlung. The low-energy Bremsstrahlung photons are heavily absorbed, which is why 
there is a significant decrease towards lower energies – instead of the predicted increase –, and 
the resulting function is hill-shaped, and the function therefore also called 'Bremsberg'. \n
The maximums energy of the Bremsstrahlung photos equals the beam energy, and the total 
transformation of an electrons' kinetic energy to a photon, respectively. \n
''')

st.subheader("Kramer's Law:")

st.latex(r'''
$I_c$ = K $\frac{s}{d}$ \frac{I Z (E_0 - E)}{E} \n
with: \n
$I_c$ = intensity of the Bremsstrahlung (continuum radiation) \n
K = a constant \n
I = beam current (in nA) \n
Z = average atomic number of the sample \n
$E_0$ = beam energy in keV \n
$E$ = photon energy \n
''')

st.subheader('Plot')
 
 
fig1 = figure(plot_width=300, plot_height=300)

E0 = 15
Z = 27
I = 5

x = np.linspace(0,10,50)
y = I * Z * (E0 - x)/x
#interact(f, E0 = (5,30,5), Z = (1,92), I = 5)
 
fig1.line(x, y, line_color='green')
tab1 = Panel(child=fig1, title="Tab 1")
 
fig2 = figure(plot_width=400, plot_height=200)
 
fig2.line(y, x, line_color='red')
tab2 = Panel(child=fig2, title="Tab 2")
 
all_tabs = Tabs(tabs=[tab1, tab2])
 
st.bokeh_chart(all_tabs)




