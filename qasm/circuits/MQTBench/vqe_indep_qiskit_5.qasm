// Benchmark was created by MQT Bench on 2022-08-31
// For more information about MQT Bench, please visit https://www.cda.cit.tum.de/mqtbench/
// MQT Bench version: 0.1.0
// Qiskit version: {'qiskit-terra': '0.20.0', 'qiskit-aer': '0.10.4', 'qiskit-ignis': '0.7.0', 'qiskit-ibmq-provider': '0.19.0', 'qiskit-aqua': None, 'qiskit': '0.36.0', 'qiskit-nature': '0.3.1', 'qiskit-finance': '0.3.1', 'qiskit-optimization': '0.3.2', 'qiskit-machine-learning': '0.4.0'}

OPENQASM 2.0;
include "qelib1.inc";
qreg q[5];
creg meas[5];
ry(0.902794663849798) q[0];
ry(0.391786752287573) q[1];
cx q[0],q[1];
ry(-1.5507815084192) q[2];
cx q[0],q[2];
cx q[1],q[2];
ry(2.97496735026474) q[3];
cx q[0],q[3];
cx q[1],q[3];
cx q[2],q[3];
ry(2.33320359440915) q[4];
cx q[0],q[4];
ry(-1.66458323626722) q[0];
cx q[1],q[4];
ry(1.61203413952141) q[1];
cx q[0],q[1];
cx q[2],q[4];
ry(-2.65685638327112) q[2];
cx q[0],q[2];
cx q[1],q[2];
cx q[3],q[4];
ry(0.129345579045278) q[3];
cx q[0],q[3];
cx q[1],q[3];
cx q[2],q[3];
ry(1.08916794595567) q[4];
cx q[0],q[4];
ry(-0.920283236920413) q[0];
cx q[1],q[4];
ry(-0.865270424121802) q[1];
cx q[2],q[4];
ry(0.585840032287207) q[2];
cx q[3],q[4];
ry(2.92109211446205) q[3];
ry(0.605195694550211) q[4];
barrier q[0],q[1],q[2],q[3],q[4];
measure q[0] -> meas[0];
measure q[1] -> meas[1];
measure q[2] -> meas[2];
measure q[3] -> meas[3];
measure q[4] -> meas[4];
