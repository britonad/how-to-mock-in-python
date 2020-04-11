import pathlib


def list_files_only() -> list:
    """Lists files in the current path."""

    return [p for p in pathlib.Path('.').iterdir() if p.is_file()]


def list_dirs_only() -> list:
    """Lists directories in the current path."""

    return [p for p in pathlib.Path('.').iterdir() if p.is_dir()]


class PythonFilesLookUp:
    def __init__(self, path):
        self.path = path

    def list_python_files(self) -> list:
        """Lists python files by a provided path."""

        return [p for p in pathlib.Path(self.path).glob('*.py')]
