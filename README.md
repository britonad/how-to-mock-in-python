# mocks
An aim of the repository is to show how to effortlessly use `mock.patch` and its main 3 strategies to mock things
during the writing of tests.

To see how it works just do one of the following commands:
```sh
mocks on master via 🐍 system
➜ python3 make_mock_by_function_import.py
<MagicMock name='list_dirs_only' id='140457111239256'>
<MagicMock name='list_dirs_only' id='140457111239256'>

mocks on master via 🐍 system
➜ python3 make_mock_by_module_import.py
<MagicMock name='list_files_only' id='140112833133536'>
<MagicMock name='list_files_only' id='140112833133536'>

mocks on master via 🐍 system
➜ python3 make_mock_instance_method.py   
<MagicMock name='PythonFilesLookUp' id='140463660157976'>
<MagicMock name='PythonFilesLookUp' id='140463660157976'>
```
You may put `import pdb; pdb.set_trace()` in any of the files above to debug their behaviour.
