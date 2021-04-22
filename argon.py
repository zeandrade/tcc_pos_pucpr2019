from argon2 import PasswordHasher
import argon2

ph = PasswordHasher()
hash = ph.hash("String_senha")

try :
	ph.verify(hash, "String_senh@")
	print("Senha correta")
except argon2.exceptions.VerifyMismatchError:
	print("Senha incorreta")

