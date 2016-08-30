

with open("01 - Crystal Ann.mp3", "rb") as f:
	byte = f.read(3)
	print(byte.decode('ISO-8859-1'))
	byte = f.read(2)
	print(byte)
	byte = f.read(3)
	print(byte)
	byte = f.read(2)
	byte = f.read(4)
	print(byte)
	byte = f.read(50)
	print(byte)