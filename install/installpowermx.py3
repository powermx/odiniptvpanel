#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Editador por PowerMX

import os
import subprocess
import sys
import base64
import socket
import random
import string
import json
from urllib.request import Request, urlopen
from itertools import cycle, zip_longest
from datetime import datetime

rDownloadURL = {
    "main": "https://github.com/amidevous/odiniptvpanelfreesourcecode/raw/master/install/install-bin-main.sh",
    "sub": "https://github.com/amidevous/odiniptvpanelfreesourcecode/raw/master/install/install-bin-sub.sh"
}
rInstall = {"MAIN": "main", "LB": "sub"}

eMySQLenc = """IyBYdHJlYW0gQ29kZXMKCltjbGllbnRdCnBvcnQgICAgICAgICAgICA9IDMzMDYKCltteXNxbGRfc2FmZV0KbmljZSAgICAgICAgICAgID0gMAoKW215c3FsZF0KdXNlciAgICAgICAgICAgID0gbXlzcWwKcG9ydCAgICAgICAgICAgID0gNzk5OQpiYXNlZGlyICAgICAgICAgPSAvdXNyCmRhdGFkaXIgICAgICAgICA9IC92YXIvbGliL215c3FsCnRtcGRpciAgICAgICAgICA9IC90bXAKbGMtbWVzc2FnZXMtZGlyID0gL3Vzci9zaGFyZS9teXNxbApza2lwLWV4dGVybmFsLWxvY2tpbmcKc2tpcC1uYW1lLXJlc29sdmU9MQoKYmluZC1hZGRyZXNzICAgICAgICAgICAgPSAqCmtleV9idWZmZXJfc2l6ZSA9IDEyOE0K"""
rMySQLCnf = base64.b64decode(eMySQLenc).decode("utf-8")


def install_package(pkg):
    """Instalacion de paquetes"""
    try:
        subprocess.run(["dpkg", "-s", pkg], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    except subprocess.CalledProcessError:
        print(f"📦 Instalando {pkg} ...")
        subprocess.run(["sudo", "apt", "update", "-y"], check=True)
        subprocess.run(["sudo", "apt", "install", "-y", pkg], check=True)


def download_and_run(script_url, script_name="installer.sh"):
    """Descarga y ejecucion"""
    print(f"⬇️ Descargando {script_url}")
    subprocess.run(["wget", "-q", "-O", script_name, script_url], check=True)
    subprocess.run(["chmod", "+x", script_name], check=True)
    subprocess.run(["bash", script_name], check=True)


def configure_mysql():
    """Guarda configuración MySQL en Ubuntu 22.04"""
    conf_path = "/etc/mysql/mysql.conf.d/xtream.cnf"
    print(f"⚙️ Escribiendo configuración MySQL en {conf_path}")
    with open(conf_path, "w") as f:
        f.write(rMySQLCnf)
    print("✅ Configuración MySQL guardada.")


def main():
    print("🚀 Iniciando instalador Odin IPTV Panel")

    # Verificar dependencias mínimas
    install_package("wget")
    install_package("mysql-server")

    # Configurar MySQL
    configure_mysql()

    # Instalar binario principal
    download_and_run(rDownloadURL["main"], "install-bin-main.sh")

    print("✅ Instalación finalizada correctamente.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)
