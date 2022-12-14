import hashlib, getopt, requests, sys

from Crypto.Cipher import ARC4

# URL del proxy
server = "http://127.0.0.1:8003/service"

# Guardar salida
def save_output(text: str):
    with open('out.txt', 'w') as f:
        f.write(text)
        f.write("0")
    f.close

# Procesar peticion
def process(file: str):
    if file == "":
        print("ERROR: No se introdujo un archivo de entrada.\n\tPara informacion de uso: python main.py -h")
        exit(0)
    with open(file) as f:
        operation = f.readline().strip()
        if operation == "INTEGRIDAD":
            # Comparar hash descifrado con el hash calculado del mensaje
            key = f.readline().strip()
            message = f.readline().strip()
            hash = f.readline().strip()
            hash = decipher(hash, key)
            if hashlib.md5(message.encode()).hexdigest() == hash:
                save_output("INTEGRO\n")
            else:
                save_output("NO INTEGRO\n")
        elif operation == "AUTENTICAR":
            key = f.readline().strip()
            name = f.readline().strip()
            # Enviado al proxy
            r = requests.post(f"{server}/?type={operation}&key={key}&name={name}")
            save_output(f"{r.json().get('response')}\n")
        elif operation == "FIRMAR":
            name = f.readline().strip()
            message = f.readline().strip()
            # Enviado al proxy
            r = requests.post(f"{server}/?type={operation}&name={name}")
            key = r.json().get('key')
            # Uso de MD5 para hashing
            hash = hashlib.md5(message.encode())
            save_output(f"{key}\n{cipher(hash, key)}\n")

    f.close

# Cifrar hash
def cipher(hash: str, key: str) -> str:
    cipherSuite = ARC4.new(key.encode())
    return cipherSuite.encrypt(hash.digest()).hex()

# Descifrar hash
def decipher(hash: str, key: str) -> str:
    cipherSuite = ARC4.new(key.encode())
    return cipherSuite.decrypt(bytes.fromhex(hash)).hex()

# Funcion principal
def main(argv):
    inputFile = ''
    opts, args = getopt.getopt(argv,"hi:",["ifile="])
    for opt, arg in opts:
        # Actuar segun las opciones
        if opt == '-h':
            print ('Uso: main.py -i <ARCHIVO DE ENTRADA>')
            sys.exit()
        elif opt in ("-i", "--input"):
            inputFile = arg
    process(inputFile)

if __name__ == "__main__":
    main(sys.argv[1:])