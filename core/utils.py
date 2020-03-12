import pathlib


def list_files_only() -> list:
    """Lists files in the current path."""

    return [p for p in pathlib.Path('.').iterdir() if p.is_file()]


def list_dirs_only() -> list:
    """Lists directories in the current path."""

    return [p for p in pathlib.Path('.').iterdir() if p.is_dir()]
