#!/usr/bin/python3
import socket, urllib.request
from os import environ


def get_home_address():
    return socket.gethostbyname(environ["HOME_DOMAIN_NAME"])


def get_current_ip():
    return urllib.request.urlopen("https://ipinfo.io/ip").read().decode()


def get_pid(proc):
    from subprocess import check_output, CalledProcessError
    try:
        return int(check_output(["pidof", proc]))
    except CalledProcessError:
        return None


def kill_process(pid):
    from os import kill
    from signal import SIGKILL
    kill(pid, SIGKILL)
    print("killed the offender")


def is_safe():
    home_address = get_home_address()
    current_ip = get_current_ip()
    return home_address != current_ip


def main():
    pid = get_pid("qbittorrent-nox")
    if pid:
        if not is_safe():
            kill_process(pid)


if __name__ == "__main__":
    main()