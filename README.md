# Kubernetes DOOM Demo

## Install
Instructions for installing the necessary components in the existing Kubernetes clusters

### Cert Manager
[cert-manager][url-certmanager] is used for issuing an SSL certificate from Let's Encrypt (ACME) in this project

```bash
    kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.13.3/cert-manager.yaml
```

## Deployment
This deployment assumes you already have a Kubernetes cluster. Works with K3s

### LetsEncrypt
Ensure application is running securely using SSL

```bash
# EMAIL environment variable required
# export EMAIL=your@email.com
cat ./deployments/letsencrypt/letsencrypt-prod.yaml | envsubst | kubectl apply -f -

cat ./deployments/letsencrypt/traefik-https-redirect-middleware.yaml | envsubst | kubectl apply -f -
```

### Traefik whoami
[Traefik whoami][url-whoami] is a tiny Go webserver that prints OS information and HTTP request to output.

```bash
kubectl apply -f ./deployments/whoami/namespace.yaml 
kubectl apply -f ./deployments/whoami/deployment.yaml 
kubectl apply -f ./deployments/whoami/service.yaml

# DOMAIN environment variable required
# export DOMAIN=yourdomain.com
cat ./deployments/whoami/ingress.yaml | envsubst | kubectl apply -f -

```

## Convenience

```bash
source <(kubectl completion bash) # set up autocomplete in bash into the current shell, bash-completion package should be installed first.
echo "source <(kubectl completion bash)" >> ~/.bashrc # add autocomplete permanently to your bash shell.

# shorthand for kubectl
alias k=kubectl
complete -o default -F __start_kubectl k
```


[url-certmanager]: https://github.com/cert-manager/cert-manager
[url-whoami]: https://github.com/traefik/whoami