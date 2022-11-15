// Benchmark was created by MQT Bench on 2022-08-30
// For more information about MQT Bench, please visit https://www.cda.cit.tum.de/mqtbench/
// MQT Bench version: 0.1.0
// Qiskit version: {'qiskit-terra': '0.20.0', 'qiskit-aer': '0.10.4', 'qiskit-ignis': '0.7.0', 'qiskit-ibmq-provider': '0.19.0', 'qiskit-aqua': None, 'qiskit': '0.36.0', 'qiskit-nature': '0.3.1', 'qiskit-finance': '0.3.1', 'qiskit-optimization': '0.3.2', 'qiskit-machine-learning': '0.4.0'}

OPENQASM 2.0;
include "qelib1.inc";
qreg q[3];
creg meas[3];
h q[0];
h q[1];
rzz(5.35941511230875) q[0],q[1];
h q[2];
rzz(5.35941511230875) q[0],q[2];
rx(-2.84939310851987) q[0];
rzz(5.35941511230875) q[1],q[2];
rx(-2.84939310851987) q[1];
rzz(-1.31030717334637) q[0],q[1];
rx(-2.84939310851987) q[2];
rzz(-1.31030717334637) q[0],q[2];
rx(1.66744920351056) q[0];
rzz(-1.31030717334637) q[1],q[2];
rx(1.66744920351056) q[1];
rx(1.66744920351056) q[2];
barrier q[0],q[1],q[2];
measure q[0] -> meas[0];
measure q[1] -> meas[1];
measure q[2] -> meas[2];
