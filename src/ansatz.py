from qiskit.circuit.library import TwoLocal

def build_ansatz(num_qubits):
    ansatz = TwoLocal(num_qubits, "ry", "cx", reps=2, entanglement="full")
    params = ansatz.parameters
    return ansatz, params