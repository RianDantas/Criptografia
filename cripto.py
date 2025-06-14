import rsa

# gerando as chaves públicas e privadas
pubkey, privkey = rsa.newkeys(512)


#  escrevendo uma mensagem no arquivo.txt
with open("mensagem.txt", "w") as arquivo:
    arquivo.write("mensagem a ser criptografada")

# Lendo a mensagem do arquivo.txt
with open("mensagem.txt", "r") as arquivo:
    mensagem = arquivo.read()
    print("lendo o arquivo " + mensagem)


# Salvando a chave pública no arquivo.pem
with open("chave_publica.pem", "wb") as arquivo:
    arquivo.write(pubkey.save_pkcs1("PEM"))

# print("Chave publica" + pubkey)
# print(privkey)