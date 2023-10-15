from Connections import packing
from hashlib import sha512
print(packing.header(4,99,sha512(b'esto es').digest(),sha512(b'esto es una prueva').digest()))