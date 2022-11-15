// Benchmark was created by MQT Bench on 2022-08-30
// For more information about MQT Bench, please visit https://www.cda.cit.tum.de/mqtbench/
// MQT Bench version: 0.1.0
// Qiskit version: {'qiskit-terra': '0.20.0', 'qiskit-aer': '0.10.4', 'qiskit-ignis': '0.7.0', 'qiskit-ibmq-provider': '0.19.0', 'qiskit-aqua': None, 'qiskit': '0.36.0', 'qiskit-nature': '0.3.1', 'qiskit-finance': '0.3.1', 'qiskit-optimization': '0.3.2', 'qiskit-machine-learning': '0.4.0'}

OPENQASM 2.0;
include "qelib1.inc";
qreg q[5];
creg meas[5];
u3(1.3578739,-pi,0) q[0];
u3(2.7170458,-pi,0) q[1];
cz q[0],q[1];
u3(0.45783122,0,-pi) q[2];
cz q[0],q[2];
cz q[1],q[2];
u3(2.5108704,-pi,0) q[3];
cz q[0],q[3];
cz q[1],q[3];
cz q[2],q[3];
u3(0.12984839,0,-pi) q[4];
cz q[0],q[4];
ry(3.38638036888638) q[0];
cz q[1],q[4];
ry(4.01171612676398) q[1];
cz q[2],q[4];
ry(3.61727471637309) q[2];
cz q[3],q[4];
ry(0.258481555117673) q[3];
ry(2.63692565313805) q[4];
barrier q[0],q[1],q[2],q[3],q[4];
measure q[0] -> meas[0];
measure q[1] -> meas[1];
measure q[2] -> meas[2];
measure q[3] -> meas[3];
measure q[4] -> meas[4];
