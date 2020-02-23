from qiskit import *
from qiskit.visualization import plot_histogram
import random
import matplotlib.pyplot as plt
import json


with open("data.json") as f:
    info = json.load(f)

info = info["action"]
del info["value"]

flips = list(info.values()).count(1)
no_flips = list(info.values()).count(0)
backend_sim = Aer.get_backend('qasm_simulator')

def get_classical(data):
    classical = {"0":0,"1":0}
    for i in data:
        circ_classical = QuantumCircuit(1)

        choice = random.randint(0,1)
        if(choice==0):
            circ_classical.iden(0)
        else:
            circ_classical.x(0)
        if(i==0):
            circ_classical.iden(0)
        if(i==1):
            circ_classical.x(0)

        choice = random.randint(0,1)
        if(choice==0):
            circ_classical.iden(0)
        else:
            circ_classical.x(0)

        meas = QuantumCircuit(1, 1)
        meas.measure(0, 0)

        qc_classical = circ_classical + meas



        job_sim = execute(qc_classical, backend_sim, shots=1024)

        result_sim = job_sim.result().get_counts(qc_classical)

        if("0" in result_sim):
            classical["0"] += result_sim["0"]
        if("1" in result_sim):
            classical["1"] += result_sim["1"]

    total = classical["0"] + classical["1"]
    classical["0"] = classical["0"]/total
    classical["1"] = classical["1"]/total

    return classical

def get_quantum(data):
    quantum = {"0":0,"1":0}
    for i in data:
        circ_quantum = QuantumCircuit(1)

        circ_quantum.h(0)
        
        if(i==0):
            circ_quantum.iden(0)
        if(i==1):
            circ_quantum.x(0)

        circ_quantum.h(0)

        meas = QuantumCircuit(1, 1)
        meas.measure(0, 0)

        qc_quantum = circ_quantum + meas



        job_sim = execute(qc_quantum, backend_sim, shots=1024)

        result_sim = job_sim.result().get_counts(qc_quantum)
        if("0" in result_sim):
            quantum["0"] += result_sim["0"]
        if("1" in result_sim):
            quantum["1"] += result_sim["1"]
    total = quantum["0"] + quantum["1"]
    quantum["0"] = quantum["0"]/total
    quantum["1"] = quantum["1"]/total

    return quantum

classical_counts = get_classical(list(info.values()))
plot_histogram(classical_counts)
plt.show()

quantum_counts = get_quantum(list(info.values()))
plot_histogram(quantum_counts)
plt.show()
