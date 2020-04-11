from unittest.mock import patch

from core.utils import list_dirs_only


patcher = patch('__main__.list_dirs_only')
original = list_dirs_only
mock = patcher.start()

print(list_dirs_only)
print(mock)
assert list_dirs_only == mock

patcher.stop()
