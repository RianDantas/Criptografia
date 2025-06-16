import rsa
import base64

# def gerar_chaves():
#     # gerando as chaves públicas e privadas
#     pubkey, privkey = rsa.newkeys(512)

#     # Salvando a chave pública no arquivo.pem
#     with open("/workspaces/Criptografia/2 - Criptografar/chave_publica_a.pem", "wb") as arquivo:
#         arquivo.write(pubkey.save_pkcs1("PEM"))

#     # Salvando a chave privada no arquivo.pem
#     with open("/workspaces/Criptografia/2 - Criptografar/chave_privada_a.pem", "wb") as arquivo:
#         arquivo.write(privkey.save_pkcs1("PEM"))


def escrever_mensagem():
    #  escrevendo uma mensagem no arquivo.txt
    with open("/workspaces/Criptografia/2 - Criptografar/mensagem.txt", "w") as arquivo:
        arquivo.write("mensagem para Jefferson")


def ler_mensagem():
    # Lendo a mensagem do arquivo.txt
    with open("/workspaces/Criptografia/2 - Criptografar/mensagem.txt", "r") as arquivo:
        mensagem = arquivo.read()
        return mensagem


def chave_privada():
    with open("/workspaces/Criptografia/1 - Descriptografar/chave_privada_b.pem", "rb") as arquivo:
        chave_privada = rsa.PrivateKey.load_pkcs1(arquivo.read())
        return chave_privada
    

def chave_publica():
    with open("/workspaces/Criptografia/2 - Criptografar/minha_chave_publica.pem", "rb") as arquivo:
        chave_publica = rsa.PublicKey.load_pkcs1(arquivo.read())
        return chave_publica


def criptografar_mensagem():
    mensagem_criptografada = rsa.encrypt(ler_mensagem().encode(), chave_publica())
    mensagem_criptografada_base64 = base64.b64encode(mensagem_criptografada)
    with open("/workspaces/Criptografia/2 - Criptografar/mensagem_criptografada.txt", "wb") as arquivo:
        arquivo.write(mensagem_criptografada_base64)
    print("Mensagem criptografa com suscesso!")


def assinatura():
    assinatura = rsa.sign(ler_mensagem().encode(), chave_privada(), "SHA-256")
    assinatura_base64 = base64.b64encode(assinatura)
    with open("/workspaces/Criptografia/1 - Descriptografar/assinatura.bin", "wb") as arquivo:
        arquivo.write(assinatura_base64)


# escrever_mensagem()
# print(ler_mensagem())
# criptografar_mensagem()
# print(chave_privada())
assinatura()
