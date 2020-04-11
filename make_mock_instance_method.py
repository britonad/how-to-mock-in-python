from unittest.mock import patch

from core import utils

# specify what should be patched
patcher = patch('core.utils.PythonFilesLookUp')
# attach the original class to the variable because it will be modified
# when the patcher will start
original = utils.PythonFilesLookUp
# start the patcher and mock the class, this will produce a mock 
mock = patcher.start()
# mocks instance.list_python_files() and on invokation returns ['python.py']
mock.return_value.list_python_files.return_value = ['python.py']

print(utils.PythonFilesLookUp)
print(mock)
# the mock should be eaqul to the mocked class by a provided path
assert utils.PythonFilesLookUp == mock

# check if PythonFilesLookUp was mocked properly
pfl = utils.PythonFilesLookUp('.')
assert pfl.list_python_files() == ['python.py']

# stop the patcher and unmock the function
patcher.stop()
