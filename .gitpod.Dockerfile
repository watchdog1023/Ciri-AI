FROM gitpod/workspace-full

USER root
RUN source <(curl -s https://github.com/watchdog1023/bash-scripts/raw/master/Python%20interpreter%20add-on.sh)
RUN pip3 install cpplint                    
USER gitpod

# Install custom tools, runtime, etc. using apt-get
# For example, the command below would install "bastet" - a command line tetris clone:
#
# RUN sudo apt-get -q update && #     sudo apt-get install -yq bastet && #     sudo rm -rf /var/lib/apt/lists/*
#
# More information: https://www.gitpod.io/docs/42_config_docker/
