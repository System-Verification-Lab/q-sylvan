// Benchmark was created by MQT Bench on 2022-08-30
// For more information about MQT Bench, please visit https://www.cda.cit.tum.de/mqtbench/
// MQT Bench version: 0.1.0
// Qiskit version: {'qiskit-terra': '0.20.0', 'qiskit-aer': '0.10.4', 'qiskit-ignis': '0.7.0', 'qiskit-ibmq-provider': '0.19.0', 'qiskit-aqua': None, 'qiskit': '0.36.0', 'qiskit-nature': '0.3.1', 'qiskit-finance': '0.3.1', 'qiskit-optimization': '0.3.2', 'qiskit-machine-learning': '0.4.0'}

OPENQASM 2.0;
include "qelib1.inc";
qreg q[4];
creg meas[4];
ry(-1.23537581683996) q[0];
ry(-4.03743672172939) q[1];
cz q[0],q[1];
ry(4.13660532443072) q[2];
cz q[0],q[2];
cz q[1],q[2];
ry(-3.93700847700788) q[3];
cz q[0],q[3];
ry(3.72452459324249) q[0];
cz q[1],q[3];
ry(-0.826083752599149) q[1];
cz q[0],q[1];
cz q[2],q[3];
ry(-3.08457461956496) q[2];
cz q[0],q[2];
cz q[1],q[2];
ry(5.4147475311289) q[3];
cz q[0],q[3];
ry(1.11436368164155) q[0];
cz q[1],q[3];
ry(-3.59770543349693) q[1];
cz q[0],q[1];
cz q[2],q[3];
ry(1.41754557518564) q[2];
cz q[0],q[2];
cz q[1],q[2];
ry(1.00055362222087) q[3];
cz q[0],q[3];
ry(3.29957405629309) q[0];
cz q[1],q[3];
ry(-5.92072353929213) q[1];
cz q[2],q[3];
ry(4.83795432269906) q[2];
ry(-2.4739555888174) q[3];
barrier q[0],q[1],q[2],q[3];
measure q[0] -> meas[0];
measure q[1] -> meas[1];
measure q[2] -> meas[2];
measure q[3] -> meas[3];
