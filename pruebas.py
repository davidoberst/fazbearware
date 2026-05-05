import platform
import socket
import psutil

system_info = (
    f"PC Name: {socket.gethostname()}\n"
    f"CPU: {platform.processor()}\n"
    f"RAM: {round(psutil.virtual_memory().total / (1024**3), 2)} GB\n"
    f"System: {platform.system()}\n"
    f"Version: {platform.version()}\n"
    f"Release: {platform.release()}\n"
    f"Architecture: {platform.machine()}\n"
    f"Full name: {platform.platform()}"
)
print(system_info)