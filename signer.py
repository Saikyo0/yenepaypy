import OpenSSL
import base64


def sign(pem_file, data_text):
    key_file = open(pem_file, 'rb')
    keyfile = key_file.read()
    key_file.close()
    private_key = OpenSSL.crypto.load_privatekey(OpenSSL.crypto.FILETYPE_PEM, keyfile)
    data = data_text.encode('utf-8')
    sign = OpenSSL.crypto.sign(private_key, data, "sha256")
    signature = base64.b64encode(sign)
    return signature.decode('utf-8')
