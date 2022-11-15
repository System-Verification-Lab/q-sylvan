// Benchmark was created by MQT Bench on 2022-08-31
// For more information about MQT Bench, please visit https://www.cda.cit.tum.de/mqtbench/
// MQT Bench version: 0.1.0
// Qiskit version: {'qiskit-terra': '0.20.0', 'qiskit-aer': '0.10.4', 'qiskit-ignis': '0.7.0', 'qiskit-ibmq-provider': '0.19.0', 'qiskit-aqua': None, 'qiskit': '0.36.0', 'qiskit-nature': '0.3.1', 'qiskit-finance': '0.3.1', 'qiskit-optimization': '0.3.2', 'qiskit-machine-learning': '0.4.0'}

OPENQASM 2.0;
include "qelib1.inc";
qreg q[3];
creg meas[3];
ry(-2.03615710094374) q[0];
ry(-0.907854792287582) q[1];
cx q[0],q[1];
ry(-0.81681446843974) q[2];
cx q[0],q[2];
ry(-0.190312603369693) q[0];
cx q[1],q[2];
ry(-1.74486082640676) q[1];
cx q[0],q[1];
ry(2.81029745817081) q[2];
cx q[0],q[2];
ry(2.32669315533907) q[0];
cx q[1],q[2];
ry(1.98527134182859) q[1];
ry(-2.31123179472155) q[2];
barrier q[0],q[1],q[2];
measure q[0] -> meas[0];
measure q[1] -> meas[1];
measure q[2] -> meas[2];
