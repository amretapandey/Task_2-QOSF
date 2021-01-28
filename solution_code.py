get_ipython().run_line_magic('matplotlib', 'inline')
# Importing standard Qiskit libraries
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from numpy import pi
from qiskit.visualization import plot_histogram
from qiskit.tools.monitor import job_monitor
from qiskit import QuantumCircuit, execute, Aer, IBMQ

provider = IBMQ.load_account() # Loading your IBM Q account(s)


qreg_q = QuantumRegister(6, 'q')
creg_c = ClassicalRegister(2, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)


def CNOT_ancillary(q, x, y): # CNOT Gate to ancillary qubits x, y; with q as control qubit
    circuit.cx(q, x)
    circuit.cx(q, y)

def H_all(q, x, y): # Hadamard Gate to qubits q, x, y
    circuit.h(q)
    circuit.h(x)
    circuit.h(y)


qreg_q = QuantumRegister(6, 'q')
creg_c = ClassicalRegister(2, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)


def CNOT_ancillary(q,x,y): # CNOT Gate to ancillary qubits x, y; with q as control qubit
    circuit.cx(q,x)
    circuit.cx(q,y)

def H_all(q,x,y): # Hadamard Gate to qubits q, x, y
    circuit.h(q)
    circuit.h(x)
    circuit.h(y)
    

#### Bell State is formed by Q0 and Q1 ####
circuit.h(0) # Hadamard Gate at Q0
             # No Gate to Q1
             # CNOT Gate to Q0 & Q1 after encoding & decoding them for phase and bit flip errors respectively'''
###########################################   


#### Encoding ####
# Encoding Q0 for Sign-Flip Error #
circuit.barrier()
CNOT_ancillary(0,4,5) # Apply CNOT Gate to ancillary qubits Q4, Q5 with Q0 as control qubit
H_all(0,4,5) # Apply Hadamard Gate to Q0 and ancillary qubits Q4, Q5

# Encoding Q1 for Bit-Flip Error #
circuit.barrier()
CNOT_ancillary(1,2,3) # Apply CNOT Gate to ancillary qubits Q2, Q3 with Q1 as control qubit
#################


##### Simulating Errors #####
circuit.barrier()
circuit.z(0) # Simulating Q0 for Phase Flip Error 
circuit.x(1) # Simulating Q1 for Bit Flip Error
#############################


#### Decoding ####
# Decoding Q0 for Sign-Flip Error #
circuit.barrier()
H_all(0, 4, 5) # Apply Hadamard Gate to Q0 and ancillary qubits Q4, Q5
CNOT_ancillary(0, 4, 5) # Apply CNOT Gate to ancillary qubits Q4, Q5 with Q0 as control qubit
circuit.ccx(0, 4, 5) # Toffoli Gate for decoding Q0

# Decoding Q1 for Bit-Flip Error #
circuit.barrier()
CNOT_ancillary(1, 2, 3) # Apply CNOT Gate to ancillary qubits Q2, Q3 with Q1 as control qubit
circuit.ccx(1, 2, 3) # Toffoli Gate for decoding Q1
#################


circuit.barrier()
circuit.cx(0, 1) # CNOT Gate at Q0 & Q1 for Bell State


circuit.draw() # Draw circuit



# Create a Quantum Circuit
meas = QuantumCircuit(6, 2)
meas.measure(range(2), range(2))

qc = circuit + meas

backend_sim = Aer.get_backend('qasm_simulator') # Use Aer's qasm_simulator

# Execute the circuit on the qasm simulator.
job_sim = execute(qc, backend_sim, shots=1024) # The number of repeats of the circuit is 1024

result_sim = job_sim.result() # Grab the results from the job.


counts = result_sim.get_counts(qc)
print(counts)

plot_histogram(counts) # Plot Histogram for Bell State
