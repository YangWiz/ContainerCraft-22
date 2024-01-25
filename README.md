# ContainerCraft-22
Hands-on practices for containerizing software systems

# Setup
1. Deploy postgresql
2. Backend api
```
microk8s kubectl apply -f ./k8s-services/backend/todolist-api-deployment.yaml
```

# Update docker registry
sudo docker push yanghoo/todolist-backend:<tag>

## TODO(modify container versions in the deployment)

# Helm Charts

## Create


## Install
```

```

## Uninstall

## Upgrade

# Deploy applications on GKE at the first time.
### Connect to the GKE via Google cloud console
```
gcloud container clusters get-credentials todolist-cluster-yanghoo --region europe-central2 --project dev-trees-407820
```

### Install coredns on GKE.
```
helm repo add coredns https://coredns.github.io/helm
helm --namespace=kube-system install coredns coredns/coredns
```

### Install cert-manager
```
helm repo add jetstack https://charts.jetstack.io

helm repo update

kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.13.3/cert-manager.crds.yaml

helm install \
  cert-manager jetstack/cert-manager \
  --namespace cert-manager \
  --create-namespace \
  --version v1.13.3
```

### Pull the Git repository
```
git clone https://github.com/PolymagicYang/ContainerCraft-22.git
```

### Install applications by applying helm charts.
```
```
