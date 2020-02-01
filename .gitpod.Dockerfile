FROM gitpod/workspace-full

USER root
RUN apt update
RUN apt install splint shellcheck dos2unix -y
RUN wget -c https://github.com/watchdog1023/bash-scripts/raw/master/Python%20interpreter%20add-on.sh
RUN dos2unix "Python interpreter add-on.sh"
#RUN sh "Python interpreter add-on.sh"
RUN pip3 install cpplint                    
USER gitpod

# Install custom tools, runtime, etc. using apt-get
# For example, the command below would install "bastet" - a command line tetris clone:
#
# RUN sudo apt-get -q update && #     sudo apt-get install -yq bastet && #     sudo rm -rf /var/lib/apt/lists/*
#
# More information: https://www.gitpod.io/docs/42_config_docker/
