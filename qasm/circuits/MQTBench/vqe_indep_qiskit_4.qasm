// Benchmark was created by MQT Bench on 2022-08-31
// For more information about MQT Bench, please visit https://www.cda.cit.tum.de/mqtbench/
// MQT Bench version: 0.1.0
// Qiskit version: {'qiskit-terra': '0.20.0', 'qiskit-aer': '0.10.4', 'qiskit-ignis': '0.7.0', 'qiskit-ibmq-provider': '0.19.0', 'qiskit-aqua': None, 'qiskit': '0.36.0', 'qiskit-nature': '0.3.1', 'qiskit-finance': '0.3.1', 'qiskit-optimization': '0.3.2', 'qiskit-machine-learning': '0.4.0'}

OPENQASM 2.0;
include "qelib1.inc";
qreg q[4];
creg meas[4];
ry(1.68620448288078) q[0];
ry(3.13134072705113) q[1];
cx q[0],q[1];
ry(-3.01662504957312) q[2];
cx q[0],q[2];
cx q[1],q[2];
ry(-3.04690133272255) q[3];
cx q[0],q[3];
ry(0.472164489557088) q[0];
cx q[1],q[3];
ry(0.123381090387135) q[1];
cx q[0],q[1];
cx q[2],q[3];
ry(0.408322479273432) q[2];
cx q[0],q[2];
cx q[1],q[2];
ry(1.10405558553696) q[3];
cx q[0],q[3];
ry(-1.33070780803517) q[0];
cx q[1],q[3];
ry(-1.68609717840212) q[1];
cx q[2],q[3];
ry(1.20671926584002) q[2];
ry(2.10650083636768) q[3];
barrier q[0],q[1],q[2],q[3];
measure q[0] -> meas[0];
measure q[1] -> meas[1];
measure q[2] -> meas[2];
measure q[3] -> meas[3];
