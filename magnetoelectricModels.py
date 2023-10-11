from brian2 import *
from scipy import signal


def appl_menps_linearSq(num_menps, relative_epsilon, permitivity, scaled_me_coeff, h_amp, pulse_width, menp_diam, rx,
                        ry, duty_cy, time_step, sigma_ext):
    elect_mem_dist = sqrt((rx ** 2) + (ry ** 2))
    area = (pi / 4) * (menp_diam) ** 2
    appl_menps_lin_sq_values = {}
    polarization_curr_menps = (-1 * num_menps * permitivity * relative_epsilon * scaled_me_coeff * 2 * pi *
                               (duty_cy / pulse_width) * area * h_amp *
                               signal.square(2 * pi * ((duty_cy * time_step) / pulse_width), duty_cy))
    appl_mem_voltage = polarization_curr_menps / (4 * pi * elect_mem_dist * sigma_ext)
    appl_menps_lin_sq_values['MENPs Current'] = polarization_curr_menps
    appl_menps_lin_sq_values['MENPs Voltage at Neuron'] = appl_mem_voltage
    return appl_menps_lin_sq_values


def plot_linear_model(t, duty_cy, polarization_curr_menps, appl_mem_voltage):
    fig, axs = subplots(2, 1)

    axs[0].plot(t * 1e3, polarization_curr_menps * 1e15, color='red')
    axs[0].set_xlabel('Time (ms)')
    axs[0].set_ylabel('Current (fA)')
    axs[0].grid()

    axs[1].plot(t * 1e3, appl_mem_voltage * 1e9, color='blue')
    axs[1].set_xlabel('Time (ms)')
    axs[1].set_ylabel('Voltage (nV)')
    axs[1].grid()

    if duty_cy == 1:
        fig.suptitle('Single MENP, Monophasic ME Linear Model (20 Hz)')
        fig.tight_layout()
    else:
        fig.suptitle('Single MENP, Biphasic ME Linear Model (20 Hz)')
        fig.tight_layout()
    plt.show()
    return 0

def appl_menps_square(num_menps, relative_epsilon_shell, epsilon, coercivity, h_amp, pulse_width, menp_diam, core_diam,
                      rx, ry, remanence, saturation_m, ymod_shell, coupling1, coupling2, lambda111, piezod,
                      duty_cy, time_step, sigma_ext):

    appl_MENPs_square_values = {}

    n44 = (3*lambda111)/(saturation_m**2)
    alpha_consts = (0.67 * coupling1 * coupling2 * ymod_shell * piezod * n44)/(epsilon * (relative_epsilon_shell - 1))
    elect_mem_dist = sqrt((rx**2)+(ry**2))
    area = (pi/4) * ((menp_diam**2)-(core_diam**2))

    hmag = h_amp * signal.square(2 * pi * ((duty_cy * time_step) / pulse_width), duty_cy)

    delhmag_delt = hmag * 2 * pi * (duty_cy / pulse_width)

    magn = (2 / pi) * saturation_m * arctan((hmag / coercivity) * tan((pi / 2) * (remanence / saturation_m)))

    delmagn_delhmag = ((2 / pi) * saturation_m * tan((pi / 2) * (remanence / saturation_m)) * (1 / coercivity) *
                     1 / (1 + (((hmag * tan((pi / 2) * (remanence / saturation_m))) / coercivity) ** 2)))

    delmagn_delt = ((2 / pi) * saturation_m * tan((pi / 2) * (remanence / saturation_m)) * (1 / coercivity) *
                    delhmag_delt / (1 + (((hmag * tan((pi / 2) * (remanence / saturation_m))) / coercivity) ** 2)))

    magnetostriction = 0.33 * n44 * magn ** 2

    delmagnetostriction_delhmag = 0.67 * magn * delmagn_delhmag

    del2magn_deltdelhmag = (((-4 / pi) * saturation_m * ((tan((pi / 2) * (remanence / saturation_m))) ** 3) * (
                1 / (coercivity ** 3))
                          * hmag * delhmag_delt) / ((
                                     1 + (((hmag * tan((pi / 2) * (remanence / saturation_m))) / coercivity) ** 2))**2))

    delalpha_delt = alpha_consts * (delmagn_delt * delmagn_delhmag + magn * del2magn_deltdelhmag) * (1/delmagn_delhmag)

    alpha = absolute(alpha_consts * delmagnetostriction_delhmag)

    alpha_mixed = alpha * (10/(4*pi))

    polarizationI_MENPs = (area*num_menps*epsilon*relative_epsilon_shell*(delalpha_delt*hmag + alpha*delhmag_delt))

    applMembrane_voltage = polarizationI_MENPs / (4 * pi * elect_mem_dist * sigma_ext)

    appl_MENPs_square_values['MENPs Current'] = polarizationI_MENPs
    appl_MENPs_square_values['MENPs Voltage at Neuron'] = applMembrane_voltage
    appl_MENPs_square_values['MENPs Magnetization'] = magn
    appl_MENPs_square_values['MENPs Field'] = hmag
    appl_MENPs_square_values['MENPs Magnetostriction'] = magnetostriction
    appl_MENPs_square_values['MENPs Magnetostriction Change'] = delmagnetostriction_delhmag
    appl_MENPs_square_values['MENPs Alpha'] = alpha_mixed
    return appl_MENPs_square_values

def plot_nonlinear_model(t, h_menps, m_menps, magnetostrict_menps, alpha_menps, duty_cy_freq):
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2)

    ax1.set_title('Magnetic Field')
    ax1.plot(t*1e3, h_menps, color='red')
    ax1.set_xlabel('Time (ms)')
    ax1.set_ylabel('H Field (A/m)')
    ax1.grid()

    ax2.set_title('Magnetization (M)')
    ax2.plot(t*1e3, m_menps, color='blue')
    ax2.set_xlabel('Time (ms)')
    ax2.set_ylabel('Magnetization (A/m)')
    ax2.grid()

    ax3.set_title('Magnetostriction')
    ax3.plot(t*1e3, magnetostrict_menps, color='green')
    ax3.set_xlabel('Time (ms)')
    ax3.set_ylabel('Magnetostriction (unitless)')
    ax3.grid()

    ax4.set_title('Magnetoelectric Coefficient')
    ax4.plot(t*1e3, alpha_menps, color='green')
    ax4.set_xlabel('Time (ms)')
    ax4.set_ylabel('ME Coeff (V/cm*Oe)')
    ax4.grid()

    if duty_cy_freq == 1:
        fig.suptitle('Single MENP, Monophasic ME Nonlinear Model (20 Hz)')
        fig.tight_layout()
    elif duty_cy_freq > 1:
        fig.suptitle('Single MENP, Sine ME Nonlinear Model (100 Hz)')
        fig.tight_layout()
    else:
        fig.suptitle('Single MENP, Biphasic ME Nonlinear Model (20 Hz)')
        fig.tight_layout()

    plt.show()
    return 0

def plot_nonlinear_model_waveforms(t, duty_cy, polarization_curr_menps, appl_mem_voltage):
    fig, axs = subplots(2, 1)

    axs[0].plot(t * 1e3, polarization_curr_menps * 1e15, color='red')
    axs[0].set_xlabel('Time (ms)')
    axs[0].set_ylabel('Current (fA)')
    axs[0].grid()

    axs[1].plot(t * 1e3, appl_mem_voltage * 1e9, color='blue')
    axs[1].set_xlabel('Time (ms)')
    axs[1].set_ylabel('Voltage (nV)')
    axs[1].grid()

    if duty_cy == 1:
        fig.suptitle('Single MENP, Monophasic ME Nonlinear Model (20 Hz)')
        fig.tight_layout()
    else:
        fig.suptitle('Single MENP, Biphasic ME Nonlinear Model (20 Hz)')
        fig.tight_layout()
    plt.show()
    return 0

def plot_figtwo_waveforms(t, polarization_curr_menps, appl_mem_voltage, polarization_curr_menps_bi, appl_mem_voltage_bi):
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2)

    ax1.plot(t * 1e3, polarization_curr_menps * 1e15, color='red')
    ax1.set_xlabel('t (ms)')
    ax1.set_ylabel(r'$I_{MENP}$ (fA)')
    ax1.set_title('MENP Current, Monophasic (20 Hz)')
    ax1.grid()

    ax3.plot(t * 1e3, appl_mem_voltage * 1e9, color='blue')
    ax3.set_xlabel('t (ms)')
    ax3.set_ylabel(r'$V_{MENP}$ (nV)')
    ax3.set_title('MENP Voltage, Monophasic (20 Hz)')
    ax3.grid()

    ax2.plot(t * 1e3, polarization_curr_menps_bi * 1e15, color='red')
    ax2.set_xlabel('t (ms)')
    ax2.set_ylabel(r'$I_{MENP}$ (fA)')
    ax2.set_title('MENP Current, Biphasic (20 Hz)')
    ax2.grid()

    ax4.plot(t * 1e3, appl_mem_voltage_bi * 1e9, color='blue')
    ax4.set_xlabel('t (ms)')
    ax4.set_ylabel(r'$V_{MENP}$ (nV)')
    ax4.set_title('MENP Voltage, Biphasic (20 Hz)')
    ax4.grid()

    fig.tight_layout()
    plt.show()
    return 0


def appl_menps_sine(num_menps, relative_epsilon_shell, epsilon, coercivity, h_amp, hdc, menp_diam, core_diam,
                    rx, ry, remanence, saturation_m, ymod_shell, coupling1, coupling2, lambda111, piezod,
                    frequency, time_step, sigma_ext):

    appl_MENPs_square_values = {}

    n44 = (3*lambda111)/(saturation_m**2)
    alpha_consts = (0.67 * coupling1 * coupling2 * ymod_shell * piezod * n44)/(epsilon * (relative_epsilon_shell - 1))
    elect_mem_dist = sqrt((rx**2)+(ry**2))
    area = (pi/4) * ((menp_diam**2)-(core_diam**2))

    hmag = h_amp * sin(2 * pi * frequency * time_step) + hdc

    delhmag_delt = h_amp * cos(2 * pi * frequency * time_step) * 2 * pi * frequency

    magn = (2 / pi) * saturation_m * arctan((hmag / coercivity) * tan((pi / 2) * (remanence / saturation_m)))

    delmagn_delhmag = ((2 / pi) * saturation_m * tan((pi / 2) * (remanence / saturation_m)) * (1 / coercivity) *
                       1 / (1 + (((hmag * tan((pi / 2) * (remanence / saturation_m))) / coercivity) ** 2)))

    delmagn_delt = ((2 / pi) * saturation_m * tan((pi / 2) * (remanence / saturation_m)) * (1 / coercivity) *
                    delhmag_delt / (1 + (((hmag * tan((pi / 2) * (remanence / saturation_m))) / coercivity) ** 2)))

    magnetostriction = 0.33 * n44 * magn ** 2

    delmagnetostriction_delhmag = 0.67 * magn * delmagn_delhmag

    del2magn_deltdelhmag = (((-4 / pi) * saturation_m * ((tan((pi / 2) * (remanence / saturation_m))) ** 3) * (
                1 / (coercivity ** 3))
                          * hmag * delhmag_delt) / ((
                                     1 + (((hmag * tan((pi / 2) * (remanence / saturation_m))) / coercivity) ** 2))**2))

    delalpha_delt = alpha_consts * (delmagn_delt * delmagn_delhmag + magn * del2magn_deltdelhmag*(1/delmagn_delhmag))

    alpha = absolute(alpha_consts * delmagnetostriction_delhmag)

    alpha_mixed = alpha * (10/(4*pi))

    polarizationI_MENPs = (area*num_menps*epsilon*relative_epsilon_shell*(delalpha_delt*hmag + alpha*delhmag_delt))

    applMembrane_voltage = polarizationI_MENPs / (4 * pi * elect_mem_dist * sigma_ext)

    appl_MENPs_square_values['MENPs Current'] = polarizationI_MENPs
    appl_MENPs_square_values['MENPs Voltage at Neuron'] = applMembrane_voltage
    appl_MENPs_square_values['MENPs Magnetization'] = magn
    appl_MENPs_square_values['MENPs Field'] = hmag
    appl_MENPs_square_values['MENPs Magnetostriction'] = magnetostriction
    appl_MENPs_square_values['MENPs Magnetostriction Change'] = delmagnetostriction_delhmag
    appl_MENPs_square_values['MENPs Alpha'] = alpha_mixed
    return appl_MENPs_square_values
