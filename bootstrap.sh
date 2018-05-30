#!/bin/bash

# Get super user privileges
if [[ $EUID != 0 ]]; then
	sudo -E "$0" "$@"
  exit $?
fi

set -e

apt update
apt install --no-install-recommends -y \
    libsm6 libxext6 libxrender-dev     \
    swig