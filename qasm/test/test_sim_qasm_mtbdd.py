"""
Testing running sim_qasm for MTBDD from command line.
"""
import os
import subprocess
import json
import numpy as np
import pytest


TOLERANCE = 1e-6
SIM_QASM = './build/qasm/run_qasm_on_mtbdd'
QASM_DIR = 'qasm/circuits/'


def fidelity(a, b):
    """
    Compute the fidelity of two vectors.
    """
    in_prod = np.dot(a.conj().T, b)
    return (abs(in_prod))**2


def get_vector(qasm_file : str, args : list):
    """
    Simulate given quantum circuit and return state vector.
    """
    filepath = os.path.join(QASM_DIR, qasm_file)
    output = subprocess.run([SIM_QASM, filepath, '--state-vector', *args],
                            stdout=subprocess.PIPE, check=False)
    data = json.loads(output.stdout)
    vector = np.apply_along_axis(lambda args: [complex(*args)], 1,
                                 data['state_vector']).flatten()
    return vector


@pytest.mark.parametrize("cl_args",
                         [['-p', '256']])

class TestCircuits:
    """
    Test sim_qasm on all given circuits, with CL arguments given above.
    """

    def test_adder_n4(self, cl_args : str):
        """
        Test adder_n4.qasm
        """
        vector = get_vector('adder_n4.qasm', cl_args)
        ref = np.array([0.00000000e+00+0.j, 2.36158002e-17+0.j, 0.00000000e+00+0.j,
                        0.00000000e+00+0.j, 0.00000000e+00+0.j, 0.00000000e+00+0.j,
                        0.00000000e+00+0.j, 0.00000000e+00+0.j, 0.00000000e+00+0.j,
                        1.00000000e+00+0.j, 0.00000000e+00+0.j, 0.00000000e+00+0.j,
                        0.00000000e+00+0.j, 0.00000000e+00+0.j, 0.00000000e+00+0.j,
                        0.00000000e+00+0.j])
        assert abs(fidelity(vector, ref) - 1) < TOLERANCE


    def test_basis_change_n3(self, cl_args : str):
        """
        Test basis_change_n3.qasm
        """
        vector = get_vector('basis_change_n3.qasm', cl_args)
        ref = np.array([ 9.06686370e-01-4.21805437e-01j,  3.21841592e-16+3.59799267e-16j,
                         1.96261557e-16+3.14018492e-16j, -3.50542195e-18-1.10979812e-17j,
                         3.32473560e-16-1.96808529e-16j, -1.82945633e-17-1.03747177e-17j,
                        -3.85650646e-17-1.11262893e-16j,  1.17333381e-17+7.41092244e-18j])
        assert abs(fidelity(vector, ref) - 1) < TOLERANCE


    def test_bell_state(self, cl_args : str):
        """
        Test bell_state.qasm
        """
        vector = get_vector('bell_state.qasm', cl_args)
        ref = np.array([0+0j, 0.70710678+0j, 0.70710678+0j, 0+0j])
        assert abs(fidelity(vector, ref) - 1) < TOLERANCE


    def test_dnn_n8(self, cl_args : str):
        """
        Test dnn_n8.qasm
        """
        vector = get_vector('dnn_n8.qasm', cl_args)
        ref = np.array([ 0.12641004+5.31293856e-01j, -0.07648447-3.72236104e-02j,
                        -0.06822525-1.20937515e-01j,  0.10077743-4.19485017e-02j,
                        -0.07648447-3.72236104e-02j,  0.09757202-1.17331258e-02j,
                         0.0109432 +1.40583012e-01j,  0.05292486-1.58594015e-01j,
                        -0.06822525-1.20937515e-01j,  0.03204555-1.57138851e-02j,
                         0.02604237+2.40148329e-02j, -0.02380459-1.51537614e-02j,
                         0.10077743-4.19485017e-02j, -0.04134054+4.07984689e-02j,
                        -0.04044471-1.72663937e-02j,  0.00892337+4.71213470e-02j,
                        -0.07648447-3.72236104e-02j,  0.01673732+3.79095110e-03j,
                         0.01324859-2.51813525e-02j,  0.00453264+1.70332048e-02j,
                         0.09757202-1.17331258e-02j, -0.00615046+2.18937245e-02j,
                        -0.03070889+2.04780306e-02j,  0.01096824-5.04777498e-03j,
                         0.0109432 +1.40583012e-01j,  0.01168173+2.52999889e-03j,
                        -0.10126317-2.63587809e-02j,  0.0941019 -3.23422643e-02j,
                         0.05292486-1.58594015e-01j,  0.03495767+5.65770822e-03j,
                         0.01226119+8.62905034e-02j, -0.00964648-3.73388811e-02j,
                        -0.06822525-1.20937515e-01j,  0.01324859-2.51813525e-02j,
                         0.01275733+2.44040989e-02j, -0.00768092+2.29361852e-02j,
                         0.03204555-1.57138851e-02j, -0.02168349+1.31762102e-02j,
                        -0.01002828-3.81971492e-02j, -0.01674623+4.01859119e-02j,
                         0.02604237+2.40148329e-02j,  0.00253765+8.10026137e-03j,
                        -0.02555926+2.29115023e-03j,  0.01116755-8.58145935e-03j,
                        -0.02380459-1.51537614e-02j,  0.00641802-7.67101659e-03j,
                         0.02244218+7.38399759e-03j, -0.01469433-1.53390778e-02j,
                         0.10077743-4.19485017e-02j,  0.00453264+1.70332048e-02j,
                        -0.00768092+2.29361852e-02j, -0.02740137-1.47984868e-02j,
                        -0.04134054+4.07984689e-02j, -0.0094759 -2.14561876e-02j,
                         0.03597617-1.85729877e-02j, -0.01754544-5.31071685e-03j,
                        -0.04044471-1.72663937e-02j, -0.01380899-5.76202290e-03j,
                         0.03408207-2.45710819e-02j, -0.01090296+3.25737193e-02j,
                         0.00892337+4.71213470e-02j, -0.00632533+1.53474785e-02j,
                        -0.02059268-1.43735313e-02j,  0.00926439+1.15263465e-03j,
                        -0.07648447-3.72236104e-02j,  0.09757202-1.17331258e-02j,
                         0.03204555-1.57138851e-02j, -0.04134054+4.07984689e-02j,
                         0.01673732+3.79095110e-03j, -0.00615046+2.18937245e-02j,
                         0.01168173+2.52999889e-03j,  0.03495767+5.65770822e-03j,
                         0.01324859-2.51813525e-02j, -0.02168349+1.31762102e-02j,
                         0.00253765+8.10026137e-03j,  0.00641802-7.67101659e-03j,
                         0.00453264+1.70332048e-02j, -0.0094759 -2.14561876e-02j,
                        -0.01380899-5.76202290e-03j, -0.00632533+1.53474785e-02j,
                         0.09757202-1.17331258e-02j, -0.00615046+2.18937245e-02j,
                        -0.02168349+1.31762102e-02j, -0.0094759 -2.14561876e-02j,
                        -0.00615046+2.18937245e-02j, -0.00212947-3.34982299e-02j,
                         0.01866758-3.88288993e-04j, -0.01526814-7.21120895e-03j,
                        -0.03070889+2.04780306e-02j,  0.01866758-3.88288993e-04j,
                         0.01283417-1.13119330e-02j, -0.00700464+3.03791437e-02j,
                         0.01096824-5.04777498e-03j, -0.01526814-7.21120895e-03j,
                        -0.00364199+2.12691508e-02j,  0.03092621-1.59134136e-02j,
                         0.0109432 +1.40583012e-01j, -0.03070889+2.04780306e-02j,
                        -0.01002828-3.81971492e-02j,  0.03597617-1.85729877e-02j,
                         0.01168173+2.52999889e-03j,  0.01866758-3.88288993e-04j,
                        -0.0201309 +4.63262054e-02j,  0.01879401-3.68975748e-02j,
                        -0.10126317-2.63587809e-02j,  0.01283417-1.13119330e-02j,
                         0.00624573-2.12638164e-02j,  0.02296651+2.58150474e-02j,
                         0.0941019 -3.23422643e-02j, -0.00700464+3.03791437e-02j,
                        -0.04300331+4.56514012e-03j,  0.01192333+1.44386801e-02j,
                         0.05292486-1.58594015e-01j,  0.01096824-5.04777498e-03j,
                        -0.01674623+4.01859119e-02j, -0.01754544-5.31071685e-03j,
                         0.03495767+5.65770822e-03j, -0.01526814-7.21120895e-03j,
                         0.01879401-3.68975748e-02j, -0.0493597 +2.30043110e-02j,
                         0.01226119+8.62905034e-02j, -0.00364199+2.12691508e-02j,
                        -0.04210754-2.03056271e-02j,  0.0272914 -5.21209112e-03j,
                        -0.00964648-3.73388811e-02j,  0.03092621-1.59134136e-02j,
                         0.01221778+3.55257330e-02j, -0.00041774-1.76806932e-02j,
                        -0.06822525-1.20937515e-01j,  0.0109432 +1.40583012e-01j,
                         0.02604237+2.40148329e-02j, -0.04044471-1.72663937e-02j,
                         0.01324859-2.51813525e-02j, -0.03070889+2.04780306e-02j,
                        -0.10126317-2.63587809e-02j,  0.01226119+8.62905034e-02j,
                         0.01275733+2.44040989e-02j, -0.01002828-3.81971492e-02j,
                        -0.02555926+2.29115023e-03j,  0.02244218+7.38399759e-03j,
                        -0.00768092+2.29361852e-02j,  0.03597617-1.85729877e-02j,
                         0.03408207-2.45710819e-02j, -0.02059268-1.43735313e-02j,
                         0.03204555-1.57138851e-02j,  0.01168173+2.52999889e-03j,
                         0.00253765+8.10026137e-03j, -0.01380899-5.76202290e-03j,
                        -0.02168349+1.31762102e-02j,  0.01866758-3.88288993e-04j,
                         0.01283417-1.13119330e-02j, -0.00364199+2.12691508e-02j,
                        -0.01002828-3.81971492e-02j, -0.0201309 +4.63262054e-02j,
                         0.00624573-2.12638164e-02j, -0.04300331+4.56514012e-03j,
                        -0.01674623+4.01859119e-02j,  0.01879401-3.68975748e-02j,
                        -0.04210754-2.03056271e-02j,  0.01221778+3.55257330e-02j,
                         0.02604237+2.40148329e-02j, -0.10126317-2.63587809e-02j,
                        -0.02555926+2.29115023e-03j,  0.03408207-2.45710819e-02j,
                         0.00253765+8.10026137e-03j,  0.01283417-1.13119330e-02j,
                         0.00624573-2.12638164e-02j, -0.04210754-2.03056271e-02j,
                        -0.02555926+2.29115023e-03j,  0.00624573-2.12638164e-02j,
                        -0.00998988-2.55123201e-02j,  0.00172567+1.71363053e-03j,
                         0.01116755-8.58145935e-03j,  0.02296651+2.58150474e-02j,
                         0.00172567+1.71363053e-03j,  0.00568722-8.97120460e-03j,
                        -0.02380459-1.51537614e-02j,  0.0941019 -3.23422643e-02j,
                         0.01116755-8.58145935e-03j, -0.01090296+3.25737193e-02j,
                         0.00641802-7.67101659e-03j, -0.00700464+3.03791437e-02j,
                         0.02296651+2.58150474e-02j,  0.0272914 -5.21209112e-03j,
                         0.02244218+7.38399759e-03j, -0.04300331+4.56514012e-03j,
                         0.00172567+1.71363053e-03j,  0.01428279-4.83854290e-02j,
                        -0.01469433-1.53390778e-02j,  0.01192333+1.44386801e-02j,
                         0.00568722-8.97120460e-03j, -0.03004111+8.61599384e-03j,
                         0.10077743-4.19485017e-02j,  0.05292486-1.58594015e-01j,
                        -0.02380459-1.51537614e-02j,  0.00892337+4.71213470e-02j,
                         0.00453264+1.70332048e-02j,  0.01096824-5.04777498e-03j,
                         0.0941019 -3.23422643e-02j, -0.00964648-3.73388811e-02j,
                        -0.00768092+2.29361852e-02j, -0.01674623+4.01859119e-02j,
                         0.01116755-8.58145935e-03j, -0.01469433-1.53390778e-02j,
                        -0.02740137-1.47984868e-02j, -0.01754544-5.31071685e-03j,
                        -0.01090296+3.25737193e-02j,  0.00926439+1.15263465e-03j,
                        -0.04134054+4.07984689e-02j,  0.03495767+5.65770822e-03j,
                         0.00641802-7.67101659e-03j, -0.00632533+1.53474785e-02j,
                        -0.0094759 -2.14561876e-02j, -0.01526814-7.21120895e-03j,
                        -0.00700464+3.03791437e-02j,  0.03092621-1.59134136e-02j,
                         0.03597617-1.85729877e-02j,  0.01879401-3.68975748e-02j,
                         0.02296651+2.58150474e-02j,  0.01192333+1.44386801e-02j,
                        -0.01754544-5.31071685e-03j, -0.0493597 +2.30043110e-02j,
                         0.0272914 -5.21209112e-03j, -0.00041774-1.76806932e-02j,
                        -0.04044471-1.72663937e-02j,  0.01226119+8.62905034e-02j,
                         0.02244218+7.38399759e-03j, -0.02059268-1.43735313e-02j,
                        -0.01380899-5.76202290e-03j, -0.00364199+2.12691508e-02j,
                        -0.04300331+4.56514012e-03j,  0.01221778+3.55257330e-02j,
                         0.03408207-2.45710819e-02j, -0.04210754-2.03056271e-02j,
                         0.00172567+1.71363053e-03j,  0.00568722-8.97120460e-03j,
                        -0.01090296+3.25737193e-02j,  0.0272914 -5.21209112e-03j,
                         0.01428279-4.83854290e-02j, -0.03004111+8.61599384e-03j,
                         0.00892337+4.71213470e-02j, -0.00964648-3.73388811e-02j,
                        -0.01469433-1.53390778e-02j,  0.00926439+1.15263465e-03j,
                        -0.00632533+1.53474785e-02j,  0.03092621-1.59134136e-02j,
                         0.01192333+1.44386801e-02j, -0.00041774-1.76806932e-02j,
                        -0.02059268-1.43735313e-02j,  0.01221778+3.55257330e-02j,
                         0.00568722-8.97120460e-03j, -0.03004111+8.61599384e-03j,
                         0.00926439+1.15263465e-03j, -0.00041774-1.76806932e-02j,
                        -0.03004111+8.61599384e-03j,  0.02427846+1.56785055e-02j])
        assert abs(fidelity(vector, ref) - 1) < TOLERANCE


    def test_ghz_n4(self, cl_args : str):
        """
        Test ghz_n4.qasm
        """
        vector = get_vector('ghz_n4.qasm', cl_args)
        ref = np.array([0.70710678+0.j, 0.        +0.j, 0.        +0.j, 0.        +0.j,
                        0.        +0.j, 0.        +0.j, 0.        +0.j, 0.        +0.j,
                        0.        +0.j, 0.        +0.j, 0.        +0.j, 0.        +0.j,
                        0.        +0.j, 0.        +0.j, 0.        +0.j, 0.70710678+0.j])
        assert abs(fidelity(vector, ref) - 1) < TOLERANCE


    def test_ghz_n8(self, cl_args : str):
        """
        Test ghz_n8.qasm
        """
        vector = get_vector('ghz_n8.qasm', cl_args)
        ref = np.array([0.70710678+0.j, 0.        +0.j, 0.        +0.j, 0.        +0.j,
                        0.        +0.j, 0.        +0.j, 0.        +0.j, 0.        +0.j,
                        0.        +0.j, 0.        +0.j, 0.        +0.j, 0.        +0.j,
                        0.        +0.j, 0.        +0.j, 0.        +0.j, 0.        +0.j,
                        0.        +0.j, 0.        +0.j, 0.        +0.j, 0.        +0.j,
                        0.        +0.j, 0.        +0.j, 0.        +0.j, 0.        +0.j,
                        0.        +0.j, 0.        +0.j, 0.        +0.j, 0.        +0.j,
                        0.        +0.j, 0.        +0.j, 0.        +0.j, 0.        +0.j,
                        0.        +0.j, 0.        +0.j, 0.        +0.j, 0.        +0.j,
                        0.        +0.j, 0.        +0.j, 0.        +0.j, 0.        +0.j,
                        0.        +0.j, 0.        +0.j, 0.        +0.j, 0.        +0.j,
                        0.        +0.j, 0.        +0.j, 0.        +0.j, 0.        +0.j,
                        0.        +0.j, 0.        +0.j, 0.        +0.j, 0.        +0.j,
                        0.        +0.j, 0.        +0.j, 0.        +0.j, 0.        +0.j,
                        0.        +0.j, 0.        +0.j, 0.        +0.j, 0.        +0.j,
                        0.        +0.j, 0.        +0.j, 0.        +0.j, 0.        +0.j,
                        0.        +0.j, 0.        +0.j, 0.        +0.j, 0.        +0.j,
                        0.        +0.j, 0.        +0.j, 0.        +0.j, 0.        +0.j,
                        0.        +0.j, 0.        +0.j, 0.        +0.j, 0.        +0.j,
                        0.        +0.j, 0.        +0.j, 0.        +0.j, 0.        +0.j,
                        0.        +0.j, 0.        +0.j, 0.        +0.j, 0.        +0.j,
                        0.        +0.j, 0.        +0.j, 0.        +0.j, 0.        +0.j,
                        0.        +0.j, 0.        +0.j, 0.        +0.j, 0.        +0.j,
                        0.        +0.j, 0.        +0.j, 0.        +0.j, 0.        +0.j,
                        0.        +0.j, 0.        +0.j, 0.        +0.j, 0.        +0.j,
                        0.        +0.j, 0.        +0.j, 0.        +0.j, 0.        +0.j,
                        0.        +0.j, 0.        +0.j, 0.        +0.j, 0.        +0.j,
                        0.        +0.j, 0.        +0.j, 0.        +0.j, 0.        +0.j,
                        0.        +0.j, 0.        +0.j, 0.        +0.j, 0.        +0.j,
                        0.        +0.j, 0.        +0.j, 0.        +0.j, 0.        +0.j,
                        0.        +0.j, 0.        +0.j, 0.        +0.j, 0.        +0.j,
                        0.        +0.j, 0.        +0.j, 0.        +0.j, 0.        +0.j,
                        0.        +0.j, 0.        +0.j, 0.        +0.j, 0.        +0.j,
                        0.        +0.j, 0.        +0.j, 0.        +0.j, 0.        +0.j,
                        0.        +0.j, 0.        +0.j, 0.        +0.j, 0.        +0.j,
                        0.        +0.j, 0.        +0.j, 0.        +0.j, 0.        +0.j,
                        0.        +0.j, 0.        +0.j, 0.        +0.j, 0.        +0.j,
                        0.        +0.j, 0.        +0.j, 0.        +0.j, 0.        +0.j,
                        0.        +0.j, 0.        +0.j, 0.        +0.j, 0.        +0.j,
                        0.        +0.j, 0.        +0.j, 0.        +0.j, 0.        +0.j,
                        0.        +0.j, 0.        +0.j, 0.        +0.j, 0.        +0.j,
                        0.        +0.j, 0.        +0.j, 0.        +0.j, 0.        +0.j,
                        0.        +0.j, 0.        +0.j, 0.        +0.j, 0.        +0.j,
                        0.        +0.j, 0.        +0.j, 0.        +0.j, 0.        +0.j,
                        0.        +0.j, 0.        +0.j, 0.        +0.j, 0.        +0.j,
                        0.        +0.j, 0.        +0.j, 0.        +0.j, 0.        +0.j,
                        0.        +0.j, 0.        +0.j, 0.        +0.j, 0.        +0.j,
                        0.        +0.j, 0.        +0.j, 0.        +0.j, 0.        +0.j,
                        0.        +0.j, 0.        +0.j, 0.        +0.j, 0.        +0.j,
                        0.        +0.j, 0.        +0.j, 0.        +0.j, 0.        +0.j,
                        0.        +0.j, 0.        +0.j, 0.        +0.j, 0.        +0.j,
                        0.        +0.j, 0.        +0.j, 0.        +0.j, 0.        +0.j,
                        0.        +0.j, 0.        +0.j, 0.        +0.j, 0.        +0.j,
                        0.        +0.j, 0.        +0.j, 0.        +0.j, 0.        +0.j,
                        0.        +0.j, 0.        +0.j, 0.        +0.j, 0.        +0.j,
                        0.        +0.j, 0.        +0.j, 0.        +0.j, 0.        +0.j,
                        0.        +0.j, 0.        +0.j, 0.        +0.j, 0.        +0.j,
                        0.        +0.j, 0.        +0.j, 0.        +0.j, 0.        +0.j,
                        0.        +0.j, 0.        +0.j, 0.        +0.j, 0.        +0.j,
                        0.        +0.j, 0.        +0.j, 0.        +0.j, 0.        +0.j,
                        0.        +0.j, 0.        +0.j, 0.        +0.j, 0.        +0.j,
                        0.        +0.j, 0.        +0.j, 0.        +0.j, 0.        +0.j,
                        0.        +0.j, 0.        +0.j, 0.        +0.j, 0.        +0.j,
                        0.        +0.j, 0.        +0.j, 0.        +0.j, 0.70710678+0.j])
        assert abs(fidelity(vector, ref) - 1) < TOLERANCE



    def test_fredkin_n3(self, cl_args : str):
        """
        Test fredkin_n3.qasm
        """
        vector = get_vector('fredkin_n3.qasm', cl_args)
        ref = np.array([0.00000000e+00+0.j, 0.00000000e+00+0.j, 0.00000000e+00+0.j,
                        2.36158002e-17+0.j, 0.00000000e+00+0.j, 1.00000000e+00+0.j,
                        0.00000000e+00+0.j, 0.00000000e+00+0.j])
        assert abs(fidelity(vector, ref) - 1) < TOLERANCE


    def test_qaoa_n3(self, cl_args : str):
        """
        Test qaoa_n3.qasm
        """
        vector = get_vector('qaoa_n3.qasm', cl_args)
        ref = np.array([-0.44546064-0.1658815j , -0.16261527-0.26478867j,
                        -0.16759538-0.09325885j,  0.12584213+0.35336909j,
                        -0.16261527-0.26478867j, -0.44546064-0.1658815j ,
                         0.12584213+0.35336909j, -0.16759538-0.09325885j])
        assert abs(fidelity(vector, ref) - 1) < TOLERANCE


    def test_qft_n4(self, cl_args : str):
        """
        Test qft_n4.qasm
        """
        vector = get_vector('qft_n4.qasm', cl_args)
        ref = np.array([ 2.50000000e-01+0.j       , -1.76776695e-01-0.1767767j,
                         1.53080850e-17+0.25j     ,  1.76776695e-01-0.1767767j,
                        -2.50000000e-01+0.j       ,  1.76776695e-01+0.1767767j,
                        -1.53080850e-17-0.25j     , -1.76776695e-01+0.1767767j,
                         2.50000000e-01+0.j       , -1.76776695e-01-0.1767767j,
                         1.53080850e-17+0.25j     ,  1.76776695e-01-0.1767767j,
                        -2.50000000e-01+0.j       ,  1.76776695e-01+0.1767767j,
                        -1.53080850e-17-0.25j     , -1.76776695e-01+0.1767767j])
        assert abs(fidelity(vector, ref) - 1) < TOLERANCE


    def test_simon_n6(self, cl_args : str):
        """
        Test simon_n6.qasm
        """
        vector = get_vector('simon_n6.qasm', cl_args)
        ref = np.array([ 2.50000000e-01+0.j, -2.38105196e-18+0.j,  2.38105196e-18+0.j,
                        -2.50000000e-01+0.j,  2.50000000e-01+0.j, -2.38105196e-18+0.j,
                         2.38105196e-18+0.j, -2.50000000e-01+0.j,  2.50000000e-01+0.j,
                         2.38105196e-18+0.j,  2.38105196e-18+0.j,  2.50000000e-01+0.j,
                         2.50000000e-01+0.j,  2.38105196e-18+0.j,  2.38105196e-18+0.j,
                         2.50000000e-01+0.j,  2.50000000e-01+0.j,  2.38105196e-18+0.j,
                         2.38105196e-18+0.j,  2.50000000e-01+0.j, -2.50000000e-01+0.j,
                        -2.38105196e-18+0.j, -2.38105196e-18+0.j, -2.50000000e-01+0.j,
                         2.50000000e-01+0.j, -2.38105196e-18+0.j,  2.38105196e-18+0.j,
                        -2.50000000e-01+0.j, -2.50000000e-01+0.j,  2.38105196e-18+0.j,
                        -2.38105196e-18+0.j,  2.50000000e-01+0.j,  0.00000000e+00+0.j,
                         0.00000000e+00+0.j,  0.00000000e+00+0.j,  0.00000000e+00+0.j,
                         0.00000000e+00+0.j,  0.00000000e+00+0.j,  0.00000000e+00+0.j,
                         0.00000000e+00+0.j,  0.00000000e+00+0.j,  0.00000000e+00+0.j,
                         0.00000000e+00+0.j,  0.00000000e+00+0.j,  0.00000000e+00+0.j,
                         0.00000000e+00+0.j,  0.00000000e+00+0.j,  0.00000000e+00+0.j,
                         0.00000000e+00+0.j,  0.00000000e+00+0.j,  0.00000000e+00+0.j,
                         0.00000000e+00+0.j,  0.00000000e+00+0.j,  0.00000000e+00+0.j,
                         0.00000000e+00+0.j,  0.00000000e+00+0.j,  0.00000000e+00+0.j,
                         0.00000000e+00+0.j,  0.00000000e+00+0.j,  0.00000000e+00+0.j,
                         0.00000000e+00+0.j,  0.00000000e+00+0.j,  0.00000000e+00+0.j,
                         0.00000000e+00+0.j])
        assert abs(fidelity(vector, ref) - 1) < TOLERANCE


    def test_vqe_n4(self, cl_args : str):
        """
        Test vqe_n4.qasm
        """
        vector = get_vector('vqe_n4.qasm', cl_args)
        ref = np.array([ 0.22310975+0.03591277j,  0.07716044+0.06874446j,
                        -0.02409975-0.23946403j, -0.1988335 -0.33044344j,
                         0.22921453+0.01693273j,  0.03096892-0.16783964j,
                        -0.17358726-0.19121655j, -0.17475247+0.51206682j,
                         0.01452133-0.01450461j, -0.08246217+0.2670658j ,
                        -0.04425131-0.16862705j, -0.11001101+0.04121341j,
                        -0.01348307+0.03699337j,  0.26031501-0.00411195j,
                        -0.04888739-0.16588764j, -0.12254994+0.23065344j])
        assert abs(fidelity(vector, ref) - 1) < TOLERANCE


    def test_wstate_n3(self, cl_args : str):
        """
        Test wstate_n3.qasm
        """
        vector = get_vector('wstate_n3.qasm', cl_args)
        ref = np.array([0.00000000e+00+0.00000000e+00j, 4.08249225e-01+4.08249225e-01j,
                        4.08247823e-01+4.08247823e-01j, 4.23739404e-17-4.23739404e-17j,
                        4.08247823e-01+4.08247823e-01j, 0.00000000e+00+0.00000000e+00j,
                        0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j])
        assert abs(fidelity(vector, ref) - 1) < TOLERANCE
