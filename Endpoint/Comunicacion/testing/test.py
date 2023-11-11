import base64
import zlib
#se abre el archivo en binario
with open("JS_2_3.json","rb") as fileBin:
    # se extraen los datos
    f=fileBin.read()
    print(len(f))
    print(f)
    #se pcodifica en base64 con caracteres seguros
    encoded_file = base64.urlsafe_b64encode(f)
    print(len(encoded_file))
    print(encoded_file,encoded_file[len(encoded_file)-1])
    #se comprime para compensar el aumento del buffer
    compres_file = zlib.compress(encoded_file)
    print(len(compres_file))
    print(compres_file,compres_file[len(compres_file)-1])
    fileBin.close()
#descomprimimos la informacion
decompres_file = zlib.decompress(compres_file)
#decodificamos con base 64 para caracteres seguros
decoded_file = base64.urlsafe_b64decode(decompres_file)
print(len(decoded_file))
print('\rpeer: {}\n> '.format(decoded_file), end='')