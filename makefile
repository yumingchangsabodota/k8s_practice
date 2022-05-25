build_img:
	docker build -t coingecko-api . --no-cache

run_api:
	docker run -d -p 5001:5001 --name coingecko-api coingecko-api