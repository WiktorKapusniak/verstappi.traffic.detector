## Pushing to dev

Before running those commands make sure that you change used image to dev from prod in `(backend/frontend)/deployments/deployment.yml`

```
./run-makefile.sh (frontend/backend)

# if change in k8s deployment file:
kubectl apply -f deployment

# if not:
kubectl rollout restart deployment (backend/frontend)-deployment
```
