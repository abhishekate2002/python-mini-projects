alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',

'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt():

print('Welcome to cesar cipher encryption.')
print("What operation would you like to do?")
print("1. Encrypt")
print("2. Decrypt")
print("3. Exit")

operation = input('Enter a operation: ')
message = input('Enter a message: ').lower()
shift = int(input('Enter a shift: '))
exit = False
output = []

def cesar(cipher_text):

	for char in message:
		shifted_position = alphabets.index(char) + shift
		cipher_text += alphabets[shifted_position]
		print(cipher_text)

def de_ceaser(cipher_text,shift):
	for char in message:
		shifted_position = alphabets.index(char) - shift
		cipher_text += alphabets[shifted_position]
	print(cipher_text)

	
	exit=False
	cipher_text = ""
	while(exit== False):
		if operation == '1':
			cesar(cipher_text=cipher_text)
			exit = True
		elif operation == '2':
			de_ceaser(cipher_text,shift)
			exit = True
		elif operation == '3':
			exit = True
		else:
			print("Please enter a valid operation")

  

encrypt()
