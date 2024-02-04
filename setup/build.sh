USER=toy64bit
VERSION=$(date "+%Y%m%d")
CONTEXT=$(dirname $0)

docker build $CONTEXT -f comfyui.docker -t "${USER}/comfyui:${VERSION}"
