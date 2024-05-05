# Test 
- ros2 run mf_tutorials ros2_node_tutorial.py 

## docker 
```bash
sh ./docker/ubuntu2204_cuda117_ros2humble/build_image.sh 
sh ./docker/ubuntu2204_cuda117_ros2humble/launch_contatiner.sh cpu # 안 쓰면 gpu

docker exec -it mfcontainer2204 bash # docker sub connect (이미 run되어있는 docker image 에 접속)
#===========docker file sh 설명
 -v /{local folder}:{docker folder mount}
--name => docker exec -it {name} bash : -it(terminal shell open) , (pre started)conntatiner connect! 
```

## docker 명령어
```bash
docker rm [contatiner id] #docker remove
docker rmi [IMAGE ID] # docker images 삭제 
docker commit [images 이름] [저장할 이름]
```
