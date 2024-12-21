# Dockerの設定
IMAGE_NAME = myflaskapp
CONTAINER_NAME = myflaskcontainer
DOCKERFILE = Dockerfile

#dockerをデタッチモードでポート8000番で立ち上げ
dockers:
	docker build -t ${IMAGE_NAME} .
	docker container run --name ${CONTAINER_NAME} -d -p 8000:80 ${IMAGE_NAME}

#dockerをもう一度同じ名前で再起動(実際には強制削除込みっていう結構な荒技)
dockers re:
	docker build -t ${IMAGE_NAME} .
	docker container rm -f ${CONTAINER_NAME} 2>/dev/null || true
	docker container run --name ${CONTAINER_NAME} -d -p 8000:8100 ${IMAGE_NAME}