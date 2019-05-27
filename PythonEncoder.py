choice = input('1 encoding or 2 for decoding: ')
message = input('input your message: ')
shift = int(input('input how many letters you want to shift: '))

new = list(message)

if choice == "1":
	#encode
	translated = ''

	for symbol in message:
		if symbol.isalpha():
			num = ord(symbol)
			num += shift

			if symbol.isupper():
				if num > ord('Z'):
					num -= 26
				elif num < ord('A'):
					num += 26
			elif symbol.islower():
				if num > ord('z'):
					num -= 26
				elif num < ord('a'):
					num += 26

			translated += chr(num)
		else:
			translated += symbol
			
	print(translated)

	
	
	
	