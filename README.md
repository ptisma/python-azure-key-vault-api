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
1. Set env vars in env_vars_docker.txt file
2. ensure the service principal has needed access for key vault
3. Build docker image:
docker buildx build . --platform linux/arm64 -t python-azure-key-vault-api:latest or 
docker buildx build . --platform linux/amd64 -t python-azure-key-vault-api:latest
4. Run docker container:
docker run --env-file env_vars_docker.txt python-azure-key-vault-api:latest






