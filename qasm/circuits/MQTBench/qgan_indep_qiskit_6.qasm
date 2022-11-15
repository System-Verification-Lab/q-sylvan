// Benchmark was created by MQT Bench on 2022-08-30
// For more information about MQT Bench, please visit https://www.cda.cit.tum.de/mqtbench/
// MQT Bench version: 0.1.0
// Qiskit version: {'qiskit-terra': '0.20.0', 'qiskit-aer': '0.10.4', 'qiskit-ignis': '0.7.0', 'qiskit-ibmq-provider': '0.19.0', 'qiskit-aqua': None, 'qiskit': '0.36.0', 'qiskit-nature': '0.3.1', 'qiskit-finance': '0.3.1', 'qiskit-optimization': '0.3.2', 'qiskit-machine-learning': '0.4.0'}

OPENQASM 2.0;
include "qelib1.inc";
qreg q[6];
creg meas[6];
u3(0.031395055,-pi,0) q[0];
u3(0.72298592,0,-pi) q[1];
cz q[0],q[1];
u3(2.8896418,0,-pi) q[2];
cz q[0],q[2];
cz q[1],q[2];
u3(1.1927648,0,-pi) q[3];
cz q[0],q[3];
cz q[1],q[3];
cz q[2],q[3];
u3(1.3884811,0,-pi) q[4];
cz q[0],q[4];
cz q[1],q[4];
cz q[2],q[4];
cz q[3],q[4];
u3(2.1365496,-pi,0) q[5];
cz q[0],q[5];
ry(2.93003534504862) q[0];
cz q[1],q[5];
ry(1.37847223922684) q[1];
cz q[2],q[5];
ry(3.60970363434768) q[2];
cz q[3],q[5];
ry(4.43182617931675) q[3];
cz q[4],q[5];
ry(3.94025927769102) q[4];
ry(5.97417001924248) q[5];
barrier q[0],q[1],q[2],q[3],q[4],q[5];
measure q[0] -> meas[0];
measure q[1] -> meas[1];
measure q[2] -> meas[2];
measure q[3] -> meas[3];
measure q[4] -> meas[4];
measure q[5] -> meas[5];
