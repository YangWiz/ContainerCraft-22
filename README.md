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
