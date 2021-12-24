:: docker run --name minio_container -p 9000:9000 -p 9001:9001 minio/minio server /data --console-address ":9001"
docker start minio_container