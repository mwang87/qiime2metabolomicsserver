build:
	docker build -t qiime2metabolomicsserver .

bash:
	docker run -it -p 5024:5000 --rm --name qiime2metabolomicsserver qiime2metabolomicsserver bash

interactive:
	docker run -it -p 5024:5000 --rm --name qiime2metabolomicsserver qiime2metabolomicsserver /app/run_server.sh

server:
	docker run -d -p 5024:5000 --rm --name qiime2metabolomicsserver qiime2metabolomicsserver /app/run_server.sh
