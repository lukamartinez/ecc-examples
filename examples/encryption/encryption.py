from Crypto.Cipher import AES
import hashlib
import secrets


def encrypt_aes_gcm(msg, secret_key):
    aes_cipher = AES.new(secret_key, AES.MODE_GCM)
    ciphertext, auth_tag = aes_cipher.encrypt_and_digest(msg)
    return ciphertext, aes_cipher.nonce, auth_tag


def decrypt_aes_gcm(ciphertext, nonce, auth_tag, secret_key):
    aes_cipher = AES.new(secret_key, AES.MODE_GCM, nonce)
    plaintext = aes_cipher.decrypt_and_verify(ciphertext, auth_tag)
    return plaintext


def ecc_point_to_256_bit_key(point):
    sha = hashlib.sha256(int.to_bytes(point.x, 32, 'big'))
    sha.update(int.to_bytes(point.y, 32, 'big'))
    return sha.digest()


def encrypt_ecc(curve, msg, public_key):
    ciphertext_priv_key = secrets.randbelow(curve.field.n)
    shared_ecc_key = ciphertext_priv_key * public_key
    secret_key = ecc_point_to_256_bit_key(shared_ecc_key)
    ciphertext, nonce, auth_tag = encrypt_aes_gcm(msg, secret_key)
    ciphertext_pub_key = ciphertext_priv_key * curve.g
    return ciphertext, nonce, auth_tag, ciphertext_pub_key


def decrypt_ecc(encrypted_msg, priv_key):
    (ciphertext, nonce, authTag, ciphertextPubKey) = encrypted_msg
    shared_ecc_key = priv_key * ciphertextPubKey
    secret_key = ecc_point_to_256_bit_key(shared_ecc_key)
    plaintext = decrypt_aes_gcm(ciphertext, nonce, authTag, secret_key)
    return plaintext
