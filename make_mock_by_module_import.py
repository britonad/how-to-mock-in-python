from unittest.mock import patch

from core import utils


patcher = patch('core.utils.list_files_only')
original = utils.list_files_only
mock = patcher.start()

print(utils.list_files_only)
print(mock)
assert utils.list_files_only == mock

patcher.stop()
