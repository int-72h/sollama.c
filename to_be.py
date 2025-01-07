import struct
from sys import argv
if len(argv) != 4:
	print("to_be: tokenizer_in vocab_size tokenizer_out")
tok_file = open(argv[1],'rb')
max_length = int.from_bytes(tok_file.read(4))
barr = struct.pack('>i',max_length)
for i in range(0,int(argv[2])):
	score,l = struct.unpack('fi',tok_file.read(8))
	tok = struct.unpack(f"{l}s",tok_file.read(l))[0]
	barr += struct.pack(f">fi{l}s",score,l,tok)
f = open(argv[3],'wb');
f.write(barr)
f.close()
