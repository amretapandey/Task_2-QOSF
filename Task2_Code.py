from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit.visualization import plot_histogram
from qiskit.tools.monitor import job_monitor
from qiskit import QuantumCircuit, execute, Aer, IBMQ
from qiskit_textbook.tools import array_to_latex
import numpy


def CNOT_ancillary(q,x,y): # CNOT Gate to ancillary qubits x, y; with q as control qubit
    circuit.cx(q, x)
    circuit.cx(q, y)

def H_all(q,x,y): # Hadamard Gate to qubits q, x, y
    circuit.h(q)
    circuit.h(x)
    circuit.h(y)



def encode(): # Encoding for possible errors
    
    # Encoding Q0 for Phase Flip Error #
    circuit.barrier()
    CNOT_ancillary(0,4,5) # Apply CNOT Gate to ancillary qubits Q4, Q5 with Q0 as control qubit
    H_all(0,4,5) # Apply Hadamard Gate to Q0 and ancillary qubits Q4, Q5
    
    # Encoding Q1 for Bit Flip Error #
    circuit.barrier()
    CNOT_ancillary(1,2,3) # Apply CNOT Gate to ancillary qubits Q2, Q3 with Q1 as control qubit


def decode(): # Decoding the encoded qubits
    
    # Decoding Q0 for Phase Flip Error #
    circuit.barrier()
    H_all(0,4,5) # Apply Hadamard Gate to Q0 and ancillary qubits Q4, Q5
    CNOT_ancillary(0,4,5) # Apply CNOT Gate to ancillary qubits Q4, Q5 with Q0 as control qubit
    circuit.ccx(4,5,0) # Toffoli Gate for decoding Q0
    
    # Decoding Q1 for Bit Flip Error #
    circuit.barrier()
    CNOT_ancillary(1,2,3) # Apply CNOT Gate to ancillary qubits Q2, Q3 with Q1 as control qubit
    circuit.ccx(2,3,1) # Toffoli Gate for decoding Q1



##### The Circuit #####

qreg_q = QuantumRegister(6, 'q')
creg_c = ClassicalRegister(2, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)

#### Bell State is formed by Q0 and Q1 ####
circuit.h(0) # Hadamard Gate at Q0
             # No Gate to Q1
             # CNOT Gate to Q0 & Q1 after encoding & decoding them for phase and bit flip errors respectively

encode()

##### Adding Errors Probabilistically #####
circuit.barrier()

error_prob=(0.3,0.35,0.35) # error_prob: tuple giving probability of (I, X, Z) error gates
                           #            (the 3 elements of the tuple must be non_zero & sum to 1)

i_error = i.to_instruction()
x_error = x.to_instruction()
z_error = z.to_instruction()

unitary_error = numpy.random.choice([i_error, x_error, z_error], 2, p=error_prob)
circuit.append(error_gates[0],[0])
circuit.append(error_gates[1],[1])
###########################################

decode()

circuit.barrier()
circuit.cx(0,1) # CNOT Gate at Q0 and Q1 for Bell State

circuit.draw() # Draw the circuit



# Create a Quantum Circuit
meas = QuantumCircuit(6, 2)
meas.measure(range(2), range(2))
qc = circuit + meas
backend_sim = Aer.get_backend('qasm_simulator') # Use Aer's qasm_simulator

# Execute the circuit on the qasm simulator.
job_sim = execute(qc, backend_sim, shots=1000) # The number of repeats of the circuit is 1000
result_sim = job_sim.result() # Grab the results from the job.

counts = result_sim.get_counts(qc)
print("Simulation with combination of unitary errors at Q0 & Q1 with different probabilities:", counts)

plot_histogram(counts) #Plot Histogram for final Bell State
