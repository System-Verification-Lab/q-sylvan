// Benchmark was created by MQT Bench on 2022-08-30
// For more information about MQT Bench, please visit https://www.cda.cit.tum.de/mqtbench/
// MQT Bench version: 0.1.0
// Qiskit version: {'qiskit-terra': '0.20.0', 'qiskit-aer': '0.10.4', 'qiskit-ignis': '0.7.0', 'qiskit-ibmq-provider': '0.19.0', 'qiskit-aqua': None, 'qiskit': '0.36.0', 'qiskit-nature': '0.3.1', 'qiskit-finance': '0.3.1', 'qiskit-optimization': '0.3.2', 'qiskit-machine-learning': '0.4.0'}

OPENQASM 2.0;
include "qelib1.inc";
qreg q[2];
creg meas[2];
u3(0.48241442,0.67726296,0) q[0];
u3(0.29192203,0.048063985,0) q[1];
cx q[0],q[1];
u3(0.96839793,0.18834625,0) q[0];
u3(0.13130518,0.79238971,0) q[1];
cx q[0],q[1];
u3(0.28799068,0.38225793,0) q[0];
u3(0.32167831,0.51105321,0) q[1];
cx q[0],q[1];
u3(0.92553811,0.2917477,0) q[0];
u3(0.91605419,0.49264292,0) q[1];
barrier q[0],q[1];
measure q[0] -> meas[0];
measure q[1] -> meas[1];
