from unittest.mock import patch

from core import utils


# specify what should be patched
patcher = patch('core.utils.list_files_only')
# attach the original function to the variable because it will be modified
# when the patcher will start
original = utils.list_files_only
# start the patcher and mock the function, this will produce a mock 
mock = patcher.start()

print(utils.list_files_only)
print(mock)
# the mock should be eaqul to the mocked function by a provided path
assert utils.list_files_only == mock

# stop the patcher and unmock the function
patcher.stop()
