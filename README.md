# python-azure-key-vault-api
Need an API and or script in python that can access and pull a secret from the Azure key vault.

## How to run
### Using venv locally:
1. az login
2. set env vars in env_vars.txt file (key vault name and secret)
2. ensure the az ad account has needed access for key vault
3. activate venv
3. python 3 main.py

### Using docker:
1. build docker image:
docker buildx build . --platform linux/arm64 -t python-azure-key-vault-api:latest or 
docker buildx build . --platform linux/amd64 -t python-azure-key-vault-api:latest
2. set env vars in env_vars.txt file
4. Run docker container:
docker run it --env-file env_vars.txt python-azure-key-vault-api:latest

Once the container is up, login through browser on your host machine using the device code from the terminal shell.



