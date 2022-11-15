// Benchmark was created by MQT Bench on 2022-08-30
// For more information about MQT Bench, please visit https://www.cda.cit.tum.de/mqtbench/
// MQT Bench version: 0.1.0
// Qiskit version: {'qiskit-terra': '0.20.0', 'qiskit-aer': '0.10.4', 'qiskit-ignis': '0.7.0', 'qiskit-ibmq-provider': '0.19.0', 'qiskit-aqua': None, 'qiskit': '0.36.0', 'qiskit-nature': '0.3.1', 'qiskit-finance': '0.3.1', 'qiskit-optimization': '0.3.2', 'qiskit-machine-learning': '0.4.0'}

OPENQASM 2.0;
include "qelib1.inc";
qreg q[3];
creg meas[3];
ry(0.369231982147473) q[0];
ry(0.731896986257005) q[1];
cx q[0],q[1];
ry(0.163707268901186) q[2];
cx q[0],q[2];
ry(0.371074539178286) q[0];
cx q[1],q[2];
ry(0.209100120653304) q[1];
cx q[0],q[1];
ry(0.0591767232881104) q[2];
cx q[0],q[2];
ry(0.971425758981784) q[0];
cx q[1],q[2];
ry(0.933349847655293) q[1];
cx q[0],q[1];
ry(0.807286067675768) q[2];
cx q[0],q[2];
ry(0.901957134475734) q[0];
cx q[1],q[2];
ry(0.565996273007498) q[1];
ry(0.690502684256472) q[2];
barrier q[0],q[1],q[2];
measure q[0] -> meas[0];
measure q[1] -> meas[1];
measure q[2] -> meas[2];
