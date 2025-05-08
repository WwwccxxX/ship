from cx_Freeze import setup, Executable

build_options = {
    "packages": ["os", "tkinter"],  # 根据你的依赖修改
    "excludes": [],
}

setup(
    name="Ship",
    version="1.0",
    description="A GUI Application",
    options={"build_exe": build_options},
    executables=[Executable("ship.py", base="Win32GUI")]
)
