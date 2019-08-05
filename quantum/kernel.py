from pyquil import Program, get_qc
from pyquil gates import
from foresttools import init_qvm_and_quilc

"""
Kernel method for spatial mapping.
"""

qvm_server, quilc_server, fc = init_qvm_and_quilc("")
qc == get_qc("4q-qvm", connection=fc)

# Data
training_set = [[0, 1], [0.78861006, 0.61489363]]
labels = [0, 1]
test_set = [[-0.549, 0.836], [0.053 , 0.999]]
