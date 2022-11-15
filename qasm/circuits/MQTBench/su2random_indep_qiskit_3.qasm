// Benchmark was created by MQT Bench on 2022-08-30
// For more information about MQT Bench, please visit https://www.cda.cit.tum.de/mqtbench/
// MQT Bench version: 0.1.0
// Qiskit version: {'qiskit-terra': '0.20.0', 'qiskit-aer': '0.10.4', 'qiskit-ignis': '0.7.0', 'qiskit-ibmq-provider': '0.19.0', 'qiskit-aqua': None, 'qiskit': '0.36.0', 'qiskit-nature': '0.3.1', 'qiskit-finance': '0.3.1', 'qiskit-optimization': '0.3.2', 'qiskit-machine-learning': '0.4.0'}

OPENQASM 2.0;
include "qelib1.inc";
qreg q[3];
creg meas[3];
u3(0.42647253,0.24615686,0) q[0];
u3(0.47739219,0.97622787,0) q[1];
cx q[0],q[1];
u3(0.0031334903,0.98231977,0) q[2];
cx q[0],q[2];
u3(0.01301705,0.91124164,0) q[0];
cx q[1],q[2];
u3(0.058779024,0.17055531,0) q[1];
cx q[0],q[1];
u3(0.7884484,0.13464204,0) q[2];
cx q[0],q[2];
u3(0.65491481,0.33118871,0) q[0];
cx q[1],q[2];
u3(0.27142846,0.075681174,0) q[1];
cx q[0],q[1];
u3(0.06587615,0.84497362,0) q[2];
cx q[0],q[2];
u3(0.058306557,0.097331708,0) q[0];
cx q[1],q[2];
u3(0.46212446,0.41691011,0) q[1];
u3(0.97552265,0.16311815,0) q[2];
barrier q[0],q[1],q[2];
measure q[0] -> meas[0];
measure q[1] -> meas[1];
measure q[2] -> meas[2];
