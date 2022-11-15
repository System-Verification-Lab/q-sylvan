// Benchmark was created by MQT Bench on 2022-08-30
// For more information about MQT Bench, please visit https://www.cda.cit.tum.de/mqtbench/
// MQT Bench version: 0.1.0
// Qiskit version: {'qiskit-terra': '0.20.0', 'qiskit-aer': '0.10.4', 'qiskit-ignis': '0.7.0', 'qiskit-ibmq-provider': '0.19.0', 'qiskit-aqua': None, 'qiskit': '0.36.0', 'qiskit-nature': '0.3.1', 'qiskit-finance': '0.3.1', 'qiskit-optimization': '0.3.2', 'qiskit-machine-learning': '0.4.0'}

OPENQASM 2.0;
include "qelib1.inc";
qreg q[7];
creg meas[7];
u3(0.7579785,-pi,0) q[0];
u3(1.6591397,-pi,0) q[1];
cz q[0],q[1];
u3(0.91819049,0,-pi) q[2];
cz q[0],q[2];
cz q[1],q[2];
u3(0.77679766,0,-pi) q[3];
cz q[0],q[3];
cz q[1],q[3];
cz q[2],q[3];
u3(2.0147976,0,-pi) q[4];
cz q[0],q[4];
cz q[1],q[4];
cz q[2],q[4];
cz q[3],q[4];
u3(0.8291491,-pi,0) q[5];
cz q[0],q[5];
cz q[1],q[5];
cz q[2],q[5];
cz q[3],q[5];
cz q[4],q[5];
u3(1.7463892,-pi,0) q[6];
cz q[0],q[6];
ry(4.87243394737454) q[0];
cz q[1],q[6];
ry(1.78666271360766) q[1];
cz q[2],q[6];
ry(2.2371797989476) q[2];
cz q[3],q[6];
ry(3.24827971852798) q[3];
cz q[4],q[6];
ry(1.14982069566644) q[4];
cz q[5],q[6];
ry(3.98275426804554) q[5];
ry(4.43144763019138) q[6];
barrier q[0],q[1],q[2],q[3],q[4],q[5],q[6];
measure q[0] -> meas[0];
measure q[1] -> meas[1];
measure q[2] -> meas[2];
measure q[3] -> meas[3];
measure q[4] -> meas[4];
measure q[5] -> meas[5];
measure q[6] -> meas[6];
