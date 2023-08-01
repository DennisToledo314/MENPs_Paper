from brian2 import *
from scipy import signal
import pickle
import pprint


def v_appl_square(current_amplitude, pulse_width, rx, ry, sigma_ext):
    elect_memb_dist = sqrt((rx**2)+(ry**2))
    appl_memb_voltage = (current_amplitude * signal.square(2 * pi * ((0.5 * defaultclock.dt) / pulse_width), 0.5)
                            ) / (4 * pi * elect_memb_dist * sigma_ext)
    return appl_memb_voltage


def i_electrode (myelinated_axon, g_node, sigma_ext):
    defaultclock.dt = 0.001 * ms

    strength_vs_duration_values = {}
    pulse_widths = np.linspace(5, 0.25, 20)
    # pulse_widths = [5 * ms, 4 * ms, 3 * ms, 2 * ms, 1 * ms, 0.515 * ms, 0.1 * ms, 0.01 * ms]
    m_dist = 100 * umeter
    voltage_monitor = StateMonitor(myelinated_axon, 'v', record=True)
    net = Network(myelinated_axon, voltage_monitor)
    net.store()
    i_elect = -7.56 * mA
    for pulse_width in pulse_widths:
        pw = pulse_width * ms
        delta_vm = 0
        n = 0
        while delta_vm <= 119.99:
            net.restore()
            net.run(2 * pw)
            vm_initial = -90
            i_elect = i_elect + n * -0.001 * mA

            v_jminus1 = v_appl_square(current_amplitude=i_elect, pulse_width=pw, rx=m_dist, ry=500 * nmeter,
                                      sigma_ext=sigma_ext)
            v_j = v_appl_square(current_amplitude=i_elect, pulse_width=pw, rx=m_dist, ry=0, sigma_ext=sigma_ext)
            v_jplus1 = v_appl_square(current_amplitude=i_elect, pulse_width=pw, rx=m_dist, ry=500 * nmeter,
                                     sigma_ext=sigma_ext)

            myelinated_axon[2].i_appl = g_node * (v_jminus1 - 2 * v_j + v_jplus1)

            net.run(2 * pw, report='text')
            myelinated_axon[2].i_appl = 0
            net.run(2 * pw)
            n += 1
            v_mont = voltage_monitor.v[2] / mV
            vm_peak = max(v_mont)
            delta_vm = vm_peak - vm_initial
            print(vm_peak)
            print(delta_vm)
            print(i_elect)
        pw_save = pulse_width
        strength_vs_duration_values[pw_save] = i_elect/mA

        pprint.pprint(strength_vs_duration_values, width=1)
    with open('strength_duration.pkl', 'wb') as fp:
        pickle.dump(strength_vs_duration_values, fp)
        print('data saved to file')

