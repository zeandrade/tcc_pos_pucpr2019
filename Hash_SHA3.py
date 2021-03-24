
import hashlib




str = "String_senha" #Senha em texto aberto

hash_sha3_512 = hashlib.new("sha3_512", str.encode()) #Algoritimo de Hash selecionado e executado

print(hash_sha3_512)
print(hash_sha3_512.hexdigest())#Hash gerada