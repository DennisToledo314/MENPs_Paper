import matplotlib.pyplot as plt
from brian2 import *
from scipy.optimize import curve_fit
import pickle

def graph_strength_duration (stren_dur_file):
    data_to_be_graphed = pickle.load(open(stren_dur_file, "rb"))
    data_list = sorted(data_to_be_graphed.items())
    pulse_width, i_elect = zip(*data_list)
    i_elect = -1 * np.asarray(i_elect)
    print(i_elect)
    plt.scatter(pulse_width, i_elect, color='black')
    i_elect_fitted = []
    rh = 7.56
    tm = 1.26
    for pw in pulse_width:
        i_elect_fitted_iter = rh/(1-exp(-tm*pw))
        i_elect_fitted.append(i_elect_fitted_iter)
    plt.plot(pulse_width, i_elect_fitted, color='black')
    plt.xlabel('PW (ms)')
    plt.ylabel(r'$I_{threshold} (mA)$')
    plt.title('Strength vs. Duration')
    plt.grid()
    plt.annotate(r'$I_{threshold}=\frac{7.56}{1-exp(\frac{-PW}{1.26})}$', xy=(1, 13.75), fontsize=13)
    plt.show()

def graph_distance_numparts (dist_numparts_file):
    data_to_be_graphed = pickle.load(open(dist_numparts_file, "rb"))
    data_list = sorted(data_to_be_graphed.items())
    m_dist, menps = zip(*data_list)
    menps = np.asarray(menps)
    print(menps)
    plt.scatter(m_dist, menps/1e5, color='black')
    p = np.polyfit(m_dist, menps/1e5, 2)
    print(p)
    menps_fitted = []
    for dist in m_dist:
        menps_iter = p[0] * (dist ** 2) + p[1] * dist + p[2]
        menps_fitted.append(menps_iter)
    plt.plot(m_dist, menps_fitted, color='black')
    plt.xlabel('$r_x (nm)$')
    plt.ylabel('MENPs (in hundreds of thousands)')
    plt.title('MENPs vs. Distance')
    plt.grid()
    plt.annotate(r'${MENPs}_{threshold}=0.0000308 r^{2}+0.00746r+0.033$', xy=(25, 2.55), fontsize=12)
    plt.show()

def graph_layers (layers_file):
    data_to_be_graphed = pickle.load(open(layers_file, "rb"))
    data_list = sorted(data_to_be_graphed.items())
    number_of_layers, delta_vm = zip(*data_list)
    plt.scatter(number_of_layers, delta_vm, color='black')
    deltaV_fitted = []
    for nlayer in number_of_layers:
        deltaV_fitted_iter = 19.5*np.log(nlayer)+45
        deltaV_fitted.append(deltaV_fitted_iter)
    plt.plot(number_of_layers, deltaV_fitted, color='black')
    plt.xlabel('Number of Layers (3500 MENPs per layer)')
    plt.ylabel(r'$\Delta V_{membrane} (mV)$')
    plt.title('Membrane Voltage Change')
    plt.grid()
    plt.annotate(r'$\Delta V_{membrane}=19.5 \ln(Layers) + 45$', xy=(0, 115), fontsize=12)
    plt.show()
