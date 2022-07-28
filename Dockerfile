FROM nvcr.io/nvidia/cudagl:11.1.1-devel-ubuntu18.04
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys A4B469963BF863CC
RUN apt update -y
RUN apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget -y
RUN apt install tk8.6 tk8.6-dev -y
RUN apt install libsqlite3-dev -y
RUN apt install libbz2-dev -y
RUN apt-get install -y build-essential dpkg-dev
RUN apt-get install -y libgtk2.0-dev libgtk-3-dev
RUN apt install -y make gcc libgtk-3-dev libwebkitgtk-dev libwebkitgtk-3.0-dev \
    libgstreamer-gl1.0-0 freeglut3 freeglut3-dev python-gst-1.0 python3-gst-1.0 \
    libglib2.0-dev ubuntu-restricted-extras libgstreamer-plugins-base1.0-dev
RUN apt-get install -y python-wxtools libwxgtk3.0-dev
ENV PYTHON_VERSION=3.7.6
RUN wget https://www.python.org/ftp/python/$PYTHON_VERSION/Python-$PYTHON_VERSION.tgz
RUN tar xzf Python-$PYTHON_VERSION.tgz
WORKDIR /Python-$PYTHON_VERSION
RUN ./configure 
RUN make && make install
RUN ln -s /usr/local/bin/python3.7 /usr/local/bin/python
RUN python -m pip install numpy==1.20.2
RUN python -m pip install Pillow==8.2.0
RUN python -m pip install matplotlib==3.4.1
RUN python -m pip install protobuf==3.15.6
RUN python -m pip install easydict==1.9
RUN python -m pip install open3d==0.9.0.0
RUN python -m pip install pip==21.0.1
RUN pip install opencv-python==4.5.1.48
RUN pip install shapely==1.7.1
RUN apt-get install software-properties-common -y
#RUN add-apt-repository ppa:ubuntu-toolchain-r/test
#RUN apt update && apt install gcc-4.9 -y
#RUN apt-get upgrade libstdc++6 -y
#RUN apt-get dist-upgrade -y
RUN pip install sklearn
RUN apt install -y mesa-utils
RUN apt install -y libgl1-mesa-glx
RUN pip install torch==1.8.1
RUN pip install tqdm==4.59.0
WORKDIR /workspace/
