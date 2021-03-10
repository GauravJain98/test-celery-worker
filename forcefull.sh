sudo docker kill -s SIGKILL celery_worker 
until [ "`/usr/bin/docker inspect -f {{.State.Running}} celery_worker`"=="false" ]; do
    sleep 0.1;
done;
sudo docker-compose up -d --build celery_worker 
