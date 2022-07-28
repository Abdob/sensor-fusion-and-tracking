xhost +
nvidia-docker run -it --rm \
	--privileged=true \
	--ipc=host \
	--net=host \
	--volume=/tmp/.X11-unix:/tmp/.X11-unix \
	--volume=/home/${USER}/Videos:/Videos \
	--cap-add=SYS_ADMIN \
	-v $(pwd):/workspace \
	--volume=/home/${USER}/:/mnt/data \
	--volume=$XAUTHORITY:$XAUTHORITY \
	--volume=/tmp/nvidia-mps \
	--env=NVIDIA_DRIVER_CAPABILITIES=all \
	--env=DISPLAY=$DISPLAY \
	--security-opt "apparmor:unconfined" \
	sensor-fusion-tracking
