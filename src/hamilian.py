from qiskit_nature.second_q.hamiltonians import ElectronicStructureHamiltonian
from qiskit_nature.second_q.drivers import PySCFDriver

def build_h2_hamiltonian():
    driver = PySCFDriver(atom="H 0 0 0; H 0 0 0.735")
    molecule = driver.run()

    hamiltonian = molecule.hamiltonian.second_q_op()
    num_qubits = hamiltonian.num_spin_orbitals

    return hamiltonian, num_qubits