// Benchmark was created by MQT Bench on 2022-08-30
// For more information about MQT Bench, please visit https://www.cda.cit.tum.de/mqtbench/
// MQT Bench version: 0.1.0
// Qiskit version: {'qiskit-terra': '0.20.0', 'qiskit-aer': '0.10.4', 'qiskit-ignis': '0.7.0', 'qiskit-ibmq-provider': '0.19.0', 'qiskit-aqua': None, 'qiskit': '0.36.0', 'qiskit-nature': '0.3.1', 'qiskit-finance': '0.3.1', 'qiskit-optimization': '0.3.2', 'qiskit-machine-learning': '0.4.0'}

OPENQASM 2.0;
include "qelib1.inc";
qreg q[3];
creg meas[3];
ry(-4.92957188724183) q[0];
ry(3.9526234378606) q[1];
cz q[0],q[1];
ry(-2.75734090644635) q[2];
cz q[0],q[2];
ry(-4.28058161075665) q[0];
cz q[1],q[2];
ry(-2.35089760285961) q[1];
cz q[0],q[1];
ry(0.923643007666373) q[2];
cz q[0],q[2];
ry(4.61650672823475) q[0];
cz q[1],q[2];
ry(-4.46833140394506) q[1];
cz q[0],q[1];
ry(-5.57751663611277) q[2];
cz q[0],q[2];
ry(4.2115290636763) q[0];
cz q[1],q[2];
ry(-6.21548059907051) q[1];
ry(-3.26573506002874) q[2];
barrier q[0],q[1],q[2];
measure q[0] -> meas[0];
measure q[1] -> meas[1];
measure q[2] -> meas[2];
