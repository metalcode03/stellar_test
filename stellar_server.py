from stellar_sdk import Server

first_account = "GCYY2S223RCBAXJHFQL72AU6AC6B2JOA7VEBKFRIK2Z4W42QPOST4YFF"
second_account = "GB6MQYFGYIX6UWE3VRNBOIZORBQRVBVHQZTIZD4PDGCSCNDYIBAYPXIY"

server = Server("https://horizon-testnet.stellar.org")
public_key = second_account
account = server.accounts().account_id(public_key).call()
for balance in account['balances']:
    print(f"Type: {balance['asset_type']}, Balance: {balance['balance']}")