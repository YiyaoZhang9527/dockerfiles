docker build -f Dockerfile_base . -t ubuntu-cpp-env:base
docker build -f Dockerfile_build_opencv_core_modules . -t ubuntu-cpp-opencv:core
docker build -f Dockerfile_build_opencv_contrib . -t ubuntu-cpp-opencv:contrib