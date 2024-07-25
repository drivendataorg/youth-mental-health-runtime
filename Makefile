## Generate .env file to put on LastPass
.env:

## Push .env file secrets to GitHub
gh-secrets:

## Copy appropriate files into public repo
public-repo: 

## Log in to Azure
login:
	az login

## Create the cluster
cluster: login

## Admin commands
admin: cluster 