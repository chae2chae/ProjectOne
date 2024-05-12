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
docker rm [container id] #docker remove
docker rmi [IMAGE ID] # docker images 삭제
docker ps -a  
docker commit [container id] [저장할 이름] # 저장 이름이 동일하면 동일한 이미지에 저장됨 ! 
```


# docker image 
```
- 외부에서 열어야 path 경로 설정이 제대로 되게 되어있음!
~/240421_Project1$ sh ./docker/ubuntu2204_cuda117_ros2humble/launch_container.sh cpu

```

# Trouble shootings
### docker 에서 GPU를 사용하고 싶어요 ! 
1. docker: Error response from daemon: could not select device driver "" with capabilities: [[gpu]].
- nvidia-container-toolkit 설치하기 
```
distribution=$(. /etc/os-release;echo $ID$VERSION_ID) \
   && curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add - \
   && curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list
sudo apt-get update && sudo apt-get install -y nvidia-container-toolkit
sudo systemctl restart docker
```
2. 위 과정중

```
E: Conflicting values set for option Signed-By regarding source https://nvidia.github.io/libnvidia-container/stable/ubuntu18.04/amd64/ /: /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg != 
```
- 기존의 nvidia-toolkit 과 겹치는 것임 
- /etc/apt/sources.list.d 폴더 내의 
- nvidia-contrianer-toolkit.list 삭제
- 그냥 nividia-container-toolkit 설치


3. docker , rviz 켜는 과정에서 libGL error: GLX drawable type is not supported
- │libGL error: failed to create drawable
- [해결 방법 1?](https://askubuntu.com/questions/1379973/opengl-libgl-error-glx-drawable-type-is-not-supported)
- failed to create drawable 다시 재 발생
- XDG_RUNTIME_DIR not set 문제 인것으로 보임
- [해결 1](https://dev.to/winebaths/getting-up-and-running-with-the-windows-subsystem-for-linux-8oc)
- [해결 2](https://askubuntu.com/questions/456689/error-xdg-runtime-dir-not-set-in-the-environment-when-attempting-to-run-naut)