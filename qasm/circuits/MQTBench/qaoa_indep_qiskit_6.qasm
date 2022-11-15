// Benchmark was created by MQT Bench on 2022-08-30
// For more information about MQT Bench, please visit https://www.cda.cit.tum.de/mqtbench/
// MQT Bench version: 0.1.0
// Qiskit version: {'qiskit-terra': '0.20.0', 'qiskit-aer': '0.10.4', 'qiskit-ignis': '0.7.0', 'qiskit-ibmq-provider': '0.19.0', 'qiskit-aqua': None, 'qiskit': '0.36.0', 'qiskit-nature': '0.3.1', 'qiskit-finance': '0.3.1', 'qiskit-optimization': '0.3.2', 'qiskit-machine-learning': '0.4.0'}

OPENQASM 2.0;
include "qelib1.inc";
qreg q[6];
creg meas[6];
h q[0];
h q[1];
h q[2];
rzz(2.7527887923163) q[0],q[2];
h q[3];
rzz(2.7527887923163) q[0],q[3];
rx(-8.80156952470847) q[0];
h q[4];
rzz(2.7527887923163) q[1],q[4];
rzz(2.7527887923163) q[2],q[4];
rx(-8.80156952470847) q[2];
rzz(-6.09382676642028) q[0],q[2];
rx(-8.80156952470847) q[4];
h q[5];
rzz(2.7527887923163) q[1],q[5];
rx(-8.80156952470847) q[1];
rzz(-6.09382676642028) q[1],q[4];
rzz(-6.09382676642028) q[2],q[4];
rx(-0.863550172328646) q[2];
rzz(2.7527887923163) q[3],q[5];
rx(-8.80156952470847) q[3];
rzz(-6.09382676642028) q[0],q[3];
rx(-0.863550172328646) q[0];
rx(-0.863550172328646) q[4];
rx(-8.80156952470847) q[5];
rzz(-6.09382676642028) q[1],q[5];
rx(-0.863550172328646) q[1];
rzz(-6.09382676642028) q[3],q[5];
rx(-0.863550172328646) q[3];
rx(-0.863550172328646) q[5];
barrier q[0],q[1],q[2],q[3],q[4],q[5];
measure q[0] -> meas[0];
measure q[1] -> meas[1];
measure q[2] -> meas[2];
measure q[3] -> meas[3];
measure q[4] -> meas[4];
measure q[5] -> meas[5];
