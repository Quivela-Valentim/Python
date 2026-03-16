import platform
import getpass
from datetime import datetime
print(f"nome do dispositivo: {platform.node()}" )
print(f"Arquitectura: {platform.architecture()}")
print(f"sistema operacional{platform.system()}")
print(f"versão de SO: {platform.release()}")
print(f"processador: {platform.processor()}")
print(f"Versão do python: {platform.python_version()}")

print(datetime.now().year)

print(getpass.getuser())