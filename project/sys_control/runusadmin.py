import ctypes, os, sys

def runadmin(path: str) -> None:
    if os.name == "nt":
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable,
                                        path, None, 1)
    else:
        print("Введите пароль рута!")
        os.system(f"sudo chmod +x {path}")
        os.system(f"sudo ./{path}")