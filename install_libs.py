import subprocess, sys, shutil, os

def check_pip_available():
    if shutil.which("pip") is None:
        print(f"""
            O pip não está instalado no sistema.
            Por favor, instale o pip antes de continuar.
              
                Exemplo para instalar:
                    - Ubuntu/debian:
                        >>> sudo apt install python3-pip
                    - Windows:
                        >>> python -m ensurepip
                    - MacOS (Homebrew):
                        >>> brew install python3 

            Depois de instalar o pip, execute novamente:
                >>> python install_libs.py
                ou
                >>> python3 install_libs.py
        """)
        sys.exit(1)

def install_libs():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt", "--target=libs"])
    print("==> Bibliotecas instaladas com sucesso em ./libs ")

if __name__ == "__main__":
    check_pip_available()
    install_libs()