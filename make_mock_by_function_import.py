from unittest.mock import patch

from core.utils import list_dirs_only

# specify what should be patched
# i.e. if one wants to mock datetime.datetime but it used by your module x.py
# then it required to mock x.datetime but not datetime.datetime
patcher = patch('__main__.list_dirs_only')
# attach the original function to the variable because it will be modified
# when the patcher will start
original = list_dirs_only
# start the patcher and mock the function, this will produce a mock 
mock = patcher.start()

print(list_dirs_only)
print(mock)
# the mock should be eaqul to the mocked function by a provided path
assert list_dirs_only == mock

# stop the patcher and unmock the function
patcher.stop()
