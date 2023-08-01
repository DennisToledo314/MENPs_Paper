from brian2 import *

def figure_one (myelinated_axon, na_potential, k_potential, rest_potential):
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, figsize=(16, 8))

    myelinated_axon.v = np.linspace(-100, 100, len(myelinated_axon)) * mV

    ax2.plot(myelinated_axon.v / mV, myelinated_axon.tau_s[:] / ms, label=r'$\tau_s$', color='red')
    ax2.plot(myelinated_axon.v / mV, myelinated_axon.tau_mp[:] / ms, label=r'$\tau_{Nap,m}$', color='green')
    ax2.set_title('Channel Time Constants')
    ax2.set_xlabel('V (mV)')
    ax2.set_ylabel(r'$\tau_x$ (ms)')
    ax2.legend()
    ax2.grid()

    ax4.plot(myelinated_axon.v / mV, myelinated_axon.tau_m[:] / ms, label=r'$\tau_{Naf,m}$')
    ax4.plot(myelinated_axon.v / mV, myelinated_axon.tau_h[:] / ms, label=r'$\tau_h$')
    ax4.set_title('Channel Time Constants')
    ax4.set_xlabel('V (mV)')
    ax4.set_ylabel(r'$\tau_x$ (ms)')
    ax4.legend()
    ax4.grid()

    defaultclock.dt = 0.01 * ms

    myelinated_axon.v = rest_potential
    voltM = StateMonitor(myelinated_axon, 'v', record=True)

    M = StateMonitor(myelinated_axon, 'm', record=True)
    N = StateMonitor(myelinated_axon, 'mp', record=True)
    S = StateMonitor(myelinated_axon, 's', record=True)
    H = StateMonitor(myelinated_axon, 'h', record=True)

    myelinated_axon.i_appl[2] = 2 * nA
    run(5 * ms)

    myelinated_axon.i_appl[2] = 0 * amp
    run(195 * ms, report='text')

    myelinated_axon.i_appl[2] = 2 * nA
    run(5 * ms)

    myelinated_axon.i_appl[2] = 0 * amp
    run(195 * ms, report='text')

    myelinated_axon.i_appl[2] = 2 * nA
    run(5 * ms)

    myelinated_axon.i_appl[2] = 0 * amp
    run(195 * ms, report='text')

    ax1.plot(M.t / ms, voltM.v[2] / mV, label='Node 2', color='blue')
    ax1.hlines(na_potential / mV, voltM.t[0] / ms, voltM.t[-1] / ms, label='Sodium Reversal Potential', color='green')
    ax1.hlines(k_potential / mV, voltM.t[0] / ms, voltM.t[-1] / ms, label='Potassium/Leak Reversal Potential', color='red')
    ax1.grid()
    ax1.legend(loc='center right')

    ax1.set_title('Action Potential')
    ax1.set_xlabel('t (ms)')
    ax1.set_ylabel('V (mV)')

    ax3.plot(M.t/ms, M.m[2], label=r'$m_{Naf}$')
    ax3.plot(M.t/ms, N.mp[2], label=r'$m_{Nap}$')
    ax3.plot(M.t/ms, S.s[2], label='s')
    ax3.plot(M.t/ms, H.h[2], label='h')

    ax3.set_title('Activation/Inactivation')
    ax3.set_xlabel('t (ms)')
    ax3.set_ylabel('x (unitless)')
    ax3.legend(loc='center right')
    ax3.grid()

    fig.tight_layout()
    plt.show()
    return 0
