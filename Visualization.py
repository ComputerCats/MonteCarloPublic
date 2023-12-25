import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def plot_x_distr(name_pict, electron_gas):

    N_electrons = electron_gas.shape[0]

    for i in range(N_electrons):
        plt.scatter(electron_gas[i, 0], electron_gas[i, 2], color = 'blue')

    plt.grid()
    plt.xlabel('X')
    plt.ylabel('Y')

    plt.savefig(f'slide={name_pict}.png')

def plot_E_distr(name_pict, electron_gas):

    fig, ax = plt.subplots()

    ax.scatter(electron_gas[:, 2], electron_gas[:, -1], color = 'blue')

    ax.grid()
    ax.set_ylabel('E')
    ax.set_xlabel('Z')

    plt.savefig(f'E_slide={name_pict}.png')

def plot_coor_distr(name_pict, electron_gas):

    dz = 0.003

    min_z = np.min(electron_gas[:, 2])
    max_z = np.max(electron_gas[:, 2])

    N_iter = int((max_z - min_z)/dz) - 1

    fig, ax = plt.subplots()

    for i in range(N_iter):

        prev_down = min_z + i*dz
        curr_up = min_z + (i+1)*dz

        prev_mask = electron_gas[:, 2] > prev_down
        curr_mask = electron_gas[:, 2] < curr_up

        all_mask = np.logical_and(prev_mask, curr_mask)

        curr_value_plot = electron_gas[all_mask, 2].shape[0]

        ax.scatter(prev_down, curr_value_plot, color = 'blue')

    ax.grid()
    ax.set_ylabel('N electrons')
    ax.set_xlabel('Z')

    plt.savefig(f'{name_pict}.png')

def plot_initial_energy_distr(name_pict, electron_gas, all_energies):

    dE = 0.05

    fig, ax = plt.subplots()

    N_electrons = all_energies.shape[0]

    result = np.zeros((N_electrons, 2))
    
    for i in range(N_electrons):

        energy = all_energies[i]

        N_electron_energy = electron_gas[electron_gas[:, -1] == energy, -1].shape[0]

        result[i, 0] = energy
        result[i, 1] = N_electron_energy

    ax.plot(result[:, 0], result[:, 1], color = 'blue')
    ax.grid()
    ax.set_ylabel('N electrons')
    ax.set_xlabel('E, ev')

    plt.savefig(f'{name_pict}.png')

def compare_with_exp(QE):

    exp_data = pd.read_csv(r'experiment\K2CsSb\ExpK2CsSb.csv', header = None, sep = '; ').to_numpy()

    fig, ax = plt.subplots()

    ax.plot(QE[:, 0], 100*QE[:, 1], label = 'Monte Carlo', color = 'red')
    ax.plot(exp_data[:, 0], exp_data[:, 1], label = 'Experiment', color = 'blue')

    ax.grid()
    ax.set_xlabel('$\hbar\omega$')
    ax.set_ylabel('QE')
    ax.legend()

    fig.savefig('Comparing.png')