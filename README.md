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

### Santa App Deployment
1. **Deploy the Santa app, which represents a demon in the game, where each instance is a pod**
    ```bash
    kubectl apply -f ./deployments/demo/namespace.yaml 
    kubectl apply -f ./deployments/demo/deployment.yaml 
    kubectl apply -f ./deployments/demo/service.yaml
    ```
2. **Set the DOMAIN environment variable**
    ```sh
    # export DOMAIN=yourdomain.com
    ```
3. **Deploy Santa app ingress**
```sh
cat ./deployments/demo/ingress.yaml | envsubst | kubectl apply -f -
```

## Running Kube DOOM Locally

### Prerequisites

- Docker or Podman installed
- VNC viewer installed
- Kubernetes configuration file (`~/.kube/config`)

### Running with Docker

```sh
docker run -p 5901:5900 \
  --net=host \
  -v ~/.kube:/root/.kube \
  --rm -it --name kubedoom \
  ghcr.io/storax/kubedoom:latest
```

### Optional: Limit to a Namespace

```sh
docker run -p 5901:5900 \
  --net=host \
  -v ~/.kube:/root/.kube \
  -e NAMESPACE={your namespace} \
  --rm -it --name kubedoom \
  ghcr.io/storax/kubedoom:latest
```

### Connecting via VNC

1. Start a VNC viewer.
2. Connect to `localhost:5901`.
3. The password is `idbehold`.

```sh
vncviewer viewer localhost:5901
```

### Playing DOOM

- Enter the cheat `idspispopd` to walk through walls.
- Your pods will appear as little pink monsters.
- Press `CTRL` to fire.
- Use `idkfa` for all weapons and press `5` for a surprise.
- Pause the game with `ESC`.


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
