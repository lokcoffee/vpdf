from cx_Freeze import setup, Executable


name = "lokcoffee"
version = "0.1"

# application entry
executables = [Executable("vpdf.py")]

# build config
build_options = {
    "packages": [],
    "excludes": [],
    # add data file if need
    "include_files": []
}

setup(
    name=name,
    version=version,
    options={"build_exe": build_options},
    executables=executables
)