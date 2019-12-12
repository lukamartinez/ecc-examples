import secrets


def generate_key_pair(curve):
    private_key = secrets.randbelow(curve.field.n)
    public_key_test = private_key * curve.g
    return private_key, public_key_test


def generate_shared_secret(curve):
    ana_priv_key = secrets.randbelow(curve.field.n)
    ana_pub_key = ana_priv_key * curve.g

    karlo_priv_key = secrets.randbelow(curve.field.n)
    karlo_pub_key = karlo_priv_key * curve.g

    ana_shared_key = ana_priv_key * karlo_pub_key
    karlo_shared_key = karlo_priv_key * ana_pub_key

    print("Equal shared keys:", ana_shared_key == karlo_shared_key)
    return ana_shared_key


def ecc_calc_encryption_keys(curve, public_key):
    ciphertext_private_key = secrets.randbelow(curve.field.n)
    ciphertext_public_key = ciphertext_private_key * curve.g
    shared_ecc_key = public_key * ciphertext_private_key
    return shared_ecc_key, ciphertext_public_key


def ecc_calc_decryption_key(private_key, ciphertext_public_key):
    shared_ecc_key = ciphertext_public_key * private_key
    return shared_ecc_key
