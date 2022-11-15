// Benchmark was created by MQT Bench on 2022-08-30
// For more information about MQT Bench, please visit https://www.cda.cit.tum.de/mqtbench/
// MQT Bench version: 0.1.0
// Qiskit version: {'qiskit-terra': '0.20.0', 'qiskit-aer': '0.10.4', 'qiskit-ignis': '0.7.0', 'qiskit-ibmq-provider': '0.19.0', 'qiskit-aqua': None, 'qiskit': '0.36.0', 'qiskit-nature': '0.3.1', 'qiskit-finance': '0.3.1', 'qiskit-optimization': '0.3.2', 'qiskit-machine-learning': '0.4.0'}

OPENQASM 2.0;
include "qelib1.inc";
qreg q[2];
qreg psi[1];
creg c[2];
h q[0];
h q[1];
x psi[0];
cp(pi) psi[0],q[0];
swap q[0],q[1];
h q[0];
cp(-pi/2) q[1],q[0];
h q[1];
barrier q[0],q[1],psi[0];
measure q[0] -> c[0];
measure q[1] -> c[1];
