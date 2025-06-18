import rsa

# gerando as chaves públicas e privadas
pubkey, privkey = rsa.newkeys(512)

def gerar_chaves():

    # Salvando a chave pública no arquivo.pem
    with open("/workspaces/Criptografia/1 - Descriptografar/chave_publica_a.pem", "wb") as arquivo:
        arquivo.write(pubkey.save_pkcs1("PEM"))

    # Salvando a chave privada no arquivo.pem
    with open("/workspaces/Criptografia/1 - Descriptografar/chave_privada_a.pem", "wb") as arquivo:
        arquivo.write(privkey.save_pkcs1("PEM"))


def ler_mensagem():
    # Lendo a mensagem do arquivo.txt
    with open("/workspaces/Criptografia/1 - Descriptografar/mensagem_criptografada.txt", "rb") as arquivo:
        mensagem = arquivo.read()
        return mensagem


def chave_privada():
    with open("/workspaces/Criptografia/1 - Descriptografar/chave_privada_a.pem", "rb") as arquivo:
        chave_privada = rsa.PrivateKey.load_pkcs1(arquivo.read())
        return chave_privada

def chave_publica():
    with open("/workspaces/Criptografia/1 - Descriptografar/chave_publica_b.pem", "rb") as file:
        chave_publica = rsa.PublicKey.load_pkcs1(file.read())
        return chave_publica

def descriptografar_mensagem():
    mensagem = rsa.decrypt(ler_mensagem(), chave_privada()).decode()
    return mensagem


def ler_assinatura():
    with open("/workspaces/Criptografia/1 - Descriptografar/assinatura.bin", "rb") as arquivo:
        assinatura = arquivo.read()
        return assinatura

def verificar_assinatura():
    try:
        rsa.verify(descriptografar_mensagem().encode(), ler_assinatura(), chave_publica())
        print("Assinatura válida")
    except rsa.VerificationError:
        print("Falha na assinatura!")

gerar_chaves()
# print(chave_publica())
# print(privkey.n == chave_privada().n)
# print()
# print(chave_privada())
# print(ler_mensagem())
# print(descriptografar_mensagem())
# print(ler_assinatura())
# verificar_assinatura()
# print()
# print(privkey)