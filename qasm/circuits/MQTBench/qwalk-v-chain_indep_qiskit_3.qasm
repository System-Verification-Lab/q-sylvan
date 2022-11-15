// Benchmark was created by MQT Bench on 2022-09-01
// For more information about MQT Bench, please visit https://www.cda.cit.tum.de/mqtbench/
// MQT Bench version: 0.1.0
// Qiskit version: {'qiskit-terra': '0.20.0', 'qiskit-aer': '0.10.4', 'qiskit-ignis': '0.7.0', 'qiskit-ibmq-provider': '0.19.0', 'qiskit-aqua': None, 'qiskit': '0.36.0', 'qiskit-nature': '0.3.1', 'qiskit-finance': '0.3.1', 'qiskit-optimization': '0.3.2', 'qiskit-machine-learning': '0.4.0'}

OPENQASM 2.0;
include "qelib1.inc";
qreg node[2];
qreg coin[1];
creg meas[3];
h coin[0];
ccx coin[0],node[1],node[0];
cx coin[0],node[1];
x coin[0];
x node[1];
ccx coin[0],node[1],node[0];
cx coin[0],node[1];
u2(-pi,-pi) coin[0];
x node[1];
ccx coin[0],node[1],node[0];
cx coin[0],node[1];
x coin[0];
x node[1];
ccx coin[0],node[1],node[0];
cx coin[0],node[1];
u2(-pi,-pi) coin[0];
x node[1];
ccx coin[0],node[1],node[0];
cx coin[0],node[1];
x coin[0];
x node[1];
ccx coin[0],node[1],node[0];
cx coin[0],node[1];
x coin[0];
x node[1];
barrier node[0],node[1],coin[0];
measure node[0] -> meas[0];
measure node[1] -> meas[1];
measure coin[0] -> meas[2];
