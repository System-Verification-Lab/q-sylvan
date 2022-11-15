// Benchmark was created by MQT Bench on 2022-08-30
// For more information about MQT Bench, please visit https://www.cda.cit.tum.de/mqtbench/
// MQT Bench version: 0.1.0
// Qiskit version: {'qiskit-terra': '0.20.0', 'qiskit-aer': '0.10.4', 'qiskit-ignis': '0.7.0', 'qiskit-ibmq-provider': '0.19.0', 'qiskit-aqua': None, 'qiskit': '0.36.0', 'qiskit-nature': '0.3.1', 'qiskit-finance': '0.3.1', 'qiskit-optimization': '0.3.2', 'qiskit-machine-learning': '0.4.0'}

OPENQASM 2.0;
include "qelib1.inc";
qreg q[2];
creg meas[2];
ry(0.748315801181478) q[0];
ry(0.877320552276841) q[1];
cx q[0],q[1];
ry(0.998581710489994) q[0];
ry(0.241679852272086) q[1];
cx q[0],q[1];
ry(0.661896985779086) q[0];
ry(0.0692035457515915) q[1];
cx q[0],q[1];
ry(0.166303880330811) q[0];
ry(0.374879319121241) q[1];
barrier q[0],q[1];
measure q[0] -> meas[0];
measure q[1] -> meas[1];
