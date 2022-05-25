build_img:
	docker build -t ymcsabo/coingecko-api . --no-cache

push_img:
	docker push ymcsabo/coingecko-api:latest

run_api:
	docker run -d -p 5001:5001 --name coingecko-api coingecko-api

init_minikube:
	minikube start --driver=docker && \
	sudo minikube addons enable ingress && \
	sudo minikube tunnel

dashboard:
	minikube dashboard

load_img:
	minikube image load coingecko-api

k8s_api:
	kubectl apply -f k8s/coingecko_api.yaml && \
	kubectl apply -f k8s/coingecko_api_service.yaml && \
	kubectl apply -f k8s/coingecko_api_ingress.yaml \
	