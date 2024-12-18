from ecdsa import SigningKey, VerifyingKey, NIST256p
import binascii

def generate_keys():
    # Generate private key and public key using NIST256p curve
    private_key = SigningKey.generate(curve=NIST256p)
    public_key = private_key.verifying_key
    return private_key, public_key

def save_keys(private_key, public_key):
    # Save private key and public key to files
    with open("private_key.pem", "wb") as f:
        f.write(private_key.to_pem())
    
    with open("public_key.pem", "wb") as f:
        f.write(public_key.to_pem())

if __name__ == "__main__":
    private_key, public_key = generate_keys()
    save_keys(private_key, public_key)
    print("Keys generated and saved to 'private_key.pem' and 'public_key.pem'.")
