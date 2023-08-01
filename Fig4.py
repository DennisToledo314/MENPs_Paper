import numpy as np
import magnetoelectricModels


epsilon0 = (8.85e-12)  # * farad / meter
t = np.arange(0, 50.1e-3, 1e-4)

menps_nonlinear_sq = magnetoelectricModels.appl_menps_square(num_menps=1, relative_epsilon_shell=200, epsilon=epsilon0,
                                                             coercivity=25464, h_amp=63662, pulse_width=50e-3,
                                                             menp_diam=20e-9, core_diam=15e-9, rx=2e-8, ry=0,
                                                             remanence=520, saturation_m=1587, ymod_shell=67e9,
                                                             coupling1=1, coupling2=1, lambda111=120e-6, piezod=191e-12,
                                                             duty_cy=1, time_step=t, sigma_ext=0.2)

menps_nonlinear_sq_bi = magnetoelectricModels.appl_menps_square(num_menps=1, relative_epsilon_shell=200, epsilon=epsilon0,
                                                                coercivity=25464, h_amp=63662, pulse_width=25e-3,
                                                                menp_diam=20e-9, core_diam=15e-9, rx=2e-8, ry=0,
                                                                remanence=520, saturation_m=1587, ymod_shell=67e9,
                                                                coupling1=1, coupling2=1, lambda111=120e-6, piezod=191e-12,
                                                                duty_cy=0.5, time_step=t, sigma_ext=0.2)


magnetoelectricModels.plot_figtwo_waveforms(t, polarization_curr_menps=menps_nonlinear_sq['MENPs Current'],
                                            appl_mem_voltage=menps_nonlinear_sq['MENPs Voltage at Neuron'],
                                            polarization_curr_menps_bi = menps_nonlinear_sq_bi['MENPs Current'],
                                            appl_mem_voltage_bi = menps_nonlinear_sq_bi['MENPs Voltage at Neuron'])
