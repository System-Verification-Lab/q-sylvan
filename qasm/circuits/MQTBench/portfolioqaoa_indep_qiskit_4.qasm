// Benchmark was created by MQT Bench on 2022-08-30
// For more information about MQT Bench, please visit https://www.cda.cit.tum.de/mqtbench/
// MQT Bench version: 0.1.0
// Qiskit version: {'qiskit-terra': '0.20.0', 'qiskit-aer': '0.10.4', 'qiskit-ignis': '0.7.0', 'qiskit-ibmq-provider': '0.19.0', 'qiskit-aqua': None, 'qiskit': '0.36.0', 'qiskit-nature': '0.3.1', 'qiskit-finance': '0.3.1', 'qiskit-optimization': '0.3.2', 'qiskit-machine-learning': '0.4.0'}

OPENQASM 2.0;
include "qelib1.inc";
qreg q[4];
creg meas[4];
u2(-0.013178571,-pi) q[0];
u2(-0.049254691,-pi) q[1];
rzz(3.05003266801766) q[0],q[1];
u2(0.0044679829,-pi) q[2];
rzz(3.0502404370983) q[0],q[2];
rzz(3.05018283489468) q[1],q[2];
u2(-0.008397409,-pi) q[3];
rzz(3.0503007813008) q[0],q[3];
u3(2.6814933,-1.5864501,pi/2) q[0];
rzz(3.04981754989869) q[1],q[3];
u3(2.6814933,-1.6293021,pi/2) q[1];
rzz(3.62289262015793) q[0],q[1];
rzz(3.05028221312826) q[2],q[3];
u3(2.6814933,-1.5654892,pi/2) q[2];
rzz(3.62313941261916) q[0],q[2];
rzz(3.62307099151646) q[1],q[2];
u3(2.6814933,-1.5807709,pi/2) q[3];
rzz(3.6232110907255) q[0],q[3];
u3(2.1987276,-1.5831652,pi/2) q[0];
rzz(3.62263709835521) q[1],q[3];
u3(2.1987276,-1.617025,pi/2) q[1];
rzz(2.86264806219089) q[0],q[1];
rzz(3.62318903506165) q[2],q[3];
u3(2.1987276,-1.5666028,pi/2) q[2];
rzz(2.86284306657964) q[0],q[2];
rzz(2.86278900327786) q[1],q[2];
u3(2.1987276,-1.5786778,pi/2) q[3];
rzz(2.86289970342034) q[0],q[3];
rx(9.03356371812423) q[0];
rzz(2.86244616026608) q[1],q[3];
rx(9.03356371812423) q[1];
rzz(2.86288227601909) q[2],q[3];
rx(9.03356371812423) q[2];
rx(9.03356371812423) q[3];
barrier q[0],q[1],q[2],q[3];
measure q[0] -> meas[0];
measure q[1] -> meas[1];
measure q[2] -> meas[2];
measure q[3] -> meas[3];
