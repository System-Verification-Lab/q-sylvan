// Benchmark was created by MQT Bench on 2022-08-30
// For more information about MQT Bench, please visit https://www.cda.cit.tum.de/mqtbench/
// MQT Bench version: 0.1.0
// Qiskit version: {'qiskit-terra': '0.20.0', 'qiskit-aer': '0.10.4', 'qiskit-ignis': '0.7.0', 'qiskit-ibmq-provider': '0.19.0', 'qiskit-aqua': None, 'qiskit': '0.36.0', 'qiskit-nature': '0.3.1', 'qiskit-finance': '0.3.1', 'qiskit-optimization': '0.3.2', 'qiskit-machine-learning': '0.4.0'}

OPENQASM 2.0;
include "qelib1.inc";
qreg q[3];
creg meas[3];
ry(0.372862770152996) q[0];
ry(0.170119091954265) q[1];
cx q[0],q[1];
ry(0.190643438476326) q[2];
cx q[0],q[2];
ry(0.603037591426033) q[0];
cx q[1],q[2];
ry(0.720343495768409) q[1];
cx q[0],q[1];
ry(0.720245964866493) q[2];
cx q[0],q[2];
ry(0.389811466397823) q[0];
cx q[1],q[2];
ry(0.431011743736745) q[1];
cx q[0],q[1];
ry(0.383487906747056) q[2];
cx q[0],q[2];
ry(0.33643657878745) q[0];
cx q[1],q[2];
ry(0.295714031886189) q[1];
ry(0.2190618163231) q[2];
barrier q[0],q[1],q[2];
measure q[0] -> meas[0];
measure q[1] -> meas[1];
measure q[2] -> meas[2];
