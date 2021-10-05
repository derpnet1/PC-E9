from cryptography.fernet import Fernet
clave = Fernet.generate_key()
f = Fernet(clave)
archivo_key = open ('clave.key', 'wb')
archivo_key.write(clave)
archivo_key.close()
