# Kubernetes Tutorial

Kubernetes configuration files for a MongoDB + webapp deployment.

| File | Description |
|------|-------------|
| [mongo.yaml](mongo.yaml) | MongoDB Deployment and Service |
| [mongo-config.yml](mongo-config.yml) | ConfigMap for MongoDB URL |
| [mongo-secret.yml](mongo-secret.yml) | Secret for MongoDB credentials |
| [webapp.yml](webapp.yml) | Web application Deployment and Service |

## Apply all configs
```bash
kubectl apply -f mongo-secret.yml
kubectl apply -f mongo-config.yml
kubectl apply -f mongo.yaml
kubectl apply -f webapp.yml
kubectl get pods
kubectl get services
```
