from brian2 import *

import distanceNumparts
import menpLayers
import plotPickle
import singleCable
import initializeAx
import strengthDuration
import Fig1

# internode dimensions
internode_diam = 2 * um
internode_length = 199 * um

# node dimensions
node_diam = 1.4 * um
node_length = 1 * um

# potentials
leak_potential = -90 * mV
rest_potential = -90 * mV
na_potential = 50 * mV
k_potential = -90 * mV

# node electrical properties
g_na_f = 3 * siemens / cm ** 2
g_na_p = 0.01 * siemens / cm ** 2
g_k = 0.08 * siemens / cm ** 2
g_l_node = 0.007 * siemens / cm ** 2

# internode electrical properties
g_l_inter = 8e-5 * siemens / cm ** 2
inter_c = 1.6 * uF / cm ** 2

# membrane electrical properties
membrane_c = 2 * uF / cm ** 2
axial_rho = 70 * ohm * cm

# consts
epsilon0 = (8.85e-12) #* farad / meter
g_node = ((pi/4) * (node_diam**2))/(node_length * axial_rho)
sigma_ext = 0.2 * siemens/meter


eqs = '''
gNaf: siemens/meter**2
gNap: siemens/meter**2
gK : siemens/meter**2
gL : siemens/meter**2

Im = -1*(IK+INaf+INap+IL) : amp/meter**2
INaf = gNaf*(m**3)*h*(v-ENa) : amp/meter**2
INap = gNap*(mp**3)*(v-ENa) : amp/meter**2
IK = gK*s*(v-EK) : amp/meter**2
IL = gL*(v-EL) : amp/meter**2
i_appl : amp (point current)

dm/dt = (alpha_m * (1-m) - beta_m * m) : 1
dh/dt = (alpha_h * (1-h) - beta_h * h) : 1
dmp/dt = (alpha_mp * (1-mp) - beta_mp * mp) : 1
ds/dt = (alpha_s * (1-s) - beta_s * s) : 1

alpha_m = (1.85*(1/ms)*10.3*mV*3.82)/(mV*exprel(-1*(v+21.4*mV)/(10.3*mV))) : Hz
beta_m = (0.076*(1/ms)*9.16*mV*3.82)/(mV*exprel((v+25.7*mV)/(9.16*mV))) : Hz

alpha_h = (0.034*(1/ms)*11*mV*6.11)/(mV*exprel((v+112*mV)/(11*mV))) : Hz
beta_h = (2.3*6.11/ms)/(1+exp(-(v+28.8*mV)/(13.6*mV))) : Hz

alpha_mp = (0.03*(1/ms)*10.2*mV*3.82)/(mV*exprel(-1*(v+23*mV)/(10.2*mV))) : Hz
beta_mp = (0.00019*(1/ms)*10*mV*3.82)/(mV*exprel((v+38*mV)/(10*mV))) : Hz

alpha_s = (0.0138*(1/ms)*9.4*mV*1.12)/(mV*exprel(-1*(v+14*mV)/(9.4*mV))) : Hz
beta_s = (0.000138*(1/ms)*1*mV*1.12)/(mV*exprel((v+56*mV)/(1*mV))) : Hz

m_inf = alpha_m/(alpha_m + beta_m) : 1
h_inf = alpha_h/(alpha_h + beta_h) : 1
mp_inf = alpha_mp/(alpha_mp + beta_mp) : 1
s_inf = alpha_s/(alpha_s + beta_s) : 1

tau_m = 1/(alpha_m + beta_m) : second
tau_h = 1/(alpha_h + beta_h) : second
tau_mp = 1/(alpha_mp + beta_mp) : second
tau_s = 1/(alpha_s + beta_s) : second

'''

const_potentials = {'EL': leak_potential,
                    'ER': rest_potential,
                    'ENa': na_potential,
                    'EK': k_potential}

axon_morpho = singleCable.ax_morpho(node_diam, node_length, internode_diam, internode_length)

myelinated_axon = initializeAx.my_axon(axon_morpho, eqs, membrane_c, axial_rho, g_na_f, g_na_p, g_k, g_l_node,
                                       g_l_inter, inter_c, const_potentials)

# Fig1.figure_one(myelinated_axon, na_potential, k_potential, rest_potential)

# menpLayers.nonlinear_menp_layers(myelinated_axon, g_node, sigma_ext, epsilon0)

# strengthDuration.i_electrode(myelinated_axon, g_node, sigma_ext)

# distanceNumparts.nonlinear_menps(myelinated_axon, g_node, sigma_ext, epsilon0)

# plotPickle.graph_strength_duration('strength_duration.pkl')

# plotPickle.graph_distance_numparts('distance_numparts.pkl')

# plotPickle.graph_layers('menplayers_800_Oe.pkl')



