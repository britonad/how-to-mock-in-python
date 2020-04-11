from unittest.mock import patch

from core import utils

patcher = patch('core.utils.PythonFilesLookUp')
original = utils.PythonFilesLookUp
mock = patcher.start()
mock.return_value.list_python_files.return_value = ['python.py']

print(utils.PythonFilesLookUp)
print(mock)
assert utils.PythonFilesLookUp == mock

# check if PythonFilesLookUp was mocked properly
pfl = utils.PythonFilesLookUp('.')
assert pfl.list_python_files() == ['python.py']

patcher.stop()
