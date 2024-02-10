from stellar_sdk import Keypair

pair = Keypair.random()

print(f"Secret: {pair.secret}")

print(f"Public key: {pair.public_key}")