// Benchmark was created by MQT Bench on 2022-08-30
// For more information about MQT Bench, please visit https://www.cda.cit.tum.de/mqtbench/
// MQT Bench version: 0.1.0
// Qiskit version: {'qiskit-terra': '0.20.0', 'qiskit-aer': '0.10.4', 'qiskit-ignis': '0.7.0', 'qiskit-ibmq-provider': '0.19.0', 'qiskit-aqua': None, 'qiskit': '0.36.0', 'qiskit-nature': '0.3.1', 'qiskit-finance': '0.3.1', 'qiskit-optimization': '0.3.2', 'qiskit-machine-learning': '0.4.0'}

OPENQASM 2.0;
include "qelib1.inc";
qreg q[3];
creg meas[3];
u2(-0.095429703,-pi) q[0];
u2(-0.21037461,-pi) q[1];
rzz(-6.08769576082301) q[0],q[1];
u2(-0.076651209,-pi) q[2];
rzz(-6.08313074322751) q[0],q[2];
u3(2.7928811,2.2497743,pi/2) q[0];
rzz(-6.0866354775839) q[1],q[2];
u3(2.7928811,2.1788027,pi/2) q[1];
rzz(-3.75878967113842) q[0],q[1];
u3(2.7928811,2.2613689,pi/2) q[2];
rzz(-3.75597104457417) q[0],q[2];
u3(2.6054696,0.37040105,pi/2) q[0];
rzz(-3.75813500936749) q[1],q[2];
u3(2.6054696,0.334341,pi/2) q[1];
rzz(-1.909807009069) q[0],q[1];
u3(2.6054696,0.37629216,pi/2) q[2];
rzz(-1.90837489042461) q[0],q[2];
rx(-8.94915432898866) q[0];
rzz(-1.90947438134889) q[1],q[2];
rx(-8.94915432898866) q[1];
rx(-8.94915432898866) q[2];
barrier q[0],q[1],q[2];
measure q[0] -> meas[0];
measure q[1] -> meas[1];
measure q[2] -> meas[2];
