### build image 
docker build -t coingecko-api . --no-cache

### run image
docker run -d -p 5001:5001 --name coingecko-api coingecko-api

### start minikube
minikube start --force
or
minikube start --driver=docker

### enalbe ingress
minikube addons enable ingress

## run ingress tunnel 
minikube tunnel

### get ingress nginx
kubectl get pods -n ingress-nginx

### minikub dashboard
minikube dashboard

### import image
minikube image load coingecko-api

### deployment
kubectl create -f k8s/coingecko_api.yaml

### expose node port
kubectl expose deployment coingecko-api --type=ClusterIP --port=5001

### delete deployment
kubectl delete deployment coingecko-api

### service
kubectl create -f k8s/coingecko_api_service.yaml

### ingress
kubectl create -f k8s/coingecko_api_ingress.yaml

### apply change
kubectl apply -f k8s/coingecko_api_ingress.yaml


### Cluster steps
Componets: Deployment -> Service -> Ingress
start minikube -> load image -> deploy
corresponding make commands: init_minikube -> load_img -> k8s_api