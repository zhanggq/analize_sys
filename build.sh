#!/bin/bash

name="analize-sys"
tag="latest"
dockerfile="Dockerfile"

build_img(){
    echo -e "[Start to build image]\nname:$name\ntag:$tag"
    rm -rf analize.sys.tar.gz
    tar -zcf analize.sys.tar.gz analize_sys
    docker build -t "$name:$tag" . < $dockerfile
}
build_img
