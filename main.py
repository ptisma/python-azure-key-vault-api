#!/usr/bin/env python3
import os
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

def main():
    print("STARTED")
    keyVaultName = os.environ["KEY_VAULT_NAME"]
    KVUri = f"https://{keyVaultName}.vault.azure.net"

    credential = DefaultAzureCredential()
    client = SecretClient(vault_url=KVUri, credential=credential)

    secretName = os.environ["KEY_VAULT_SECRET_NAME"]

    retrieved_secret = client.get_secret(secretName)

    print(f"Your secret is '{retrieved_secret.value}'.")
    
    print("FINISHED")


if __name__ == '__main__':
    main()

