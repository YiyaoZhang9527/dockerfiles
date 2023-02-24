from mmap import PROT_READ
import os

def set_ssh_prot(prot_id):
    cmd = f"docker run -it -p {prot_id}:22 --name Ubuntu_rtsp_server -h MANMAN-PC opencv-rtsp-server:test"
    os.system(cmd)

if __name__ == "__main__":
    set_ssh_prot(7777)