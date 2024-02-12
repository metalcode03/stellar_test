import requests

first_account = "GCA6XXWLDPBRYYBDXEEGBIBD2DAGRRVQQDMADACL2YDUXUUQENJJILEQ"
second_account = "GCZQSQ2OWK3UTC73X4HC55ELK4RH2WKCOFM5KJ27BFJ3UEKPYGBIQNOU"

public_key = first_account


response = requests.get(f"https://friendbot.stellar.org?addr={public_key}")

if response.status_code == 200:
    print(f"SUCCESS! You have a new account :) \n{response.text}")
else:
    print(f"ERROR! Response: \n{ response.text}")



# secret_key = ["SD7G5LSOFSY5RUZ7SLBKL4OGPK5GAZQWVVCZX7EC26QIRHQNWPBQS4YR", "SALBJUKRDCHXM47MKJAFS52BDPE5UFCKRNS4GCC35ECG3EQJVHQ6VPO2"]
