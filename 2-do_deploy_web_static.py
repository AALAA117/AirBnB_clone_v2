#!/usr/bin/python3
"""Compress web static package
"""
from fabric.api import *
from datetime import datetime
from os import path


env.hosts = ['34.204.82.115', '3.83.227.236']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


def do_deploy(archive_path):
    """
    Deploy web files to server
    """
    try:
        if not (path.exists(archive_path)):
            return False
        put(archive_path, '/tmp/')

        # Uncompress the archive to the folder
        filename = path.basename(archive_path)
        name, ext = os.path.splitext(filename)
        if ext != '.tgz':
            return (False)
        release_path = "/data/web_static/releases/{}".format(name)
        run("sudo mkdir -p {}".format(release_path))
        run("sudo tar -xzf /tmp/{} -C {}".format(filename, release_path))

        # Delete the archive from the web server
        run("sudo rm /tmp/{}".format(filename))
        # Move the contents of the web_static directory
        # one level up to get desired structure
        run("sudo mv {}/web_static/* {}".format(release_path, release_path))

        # Delete the symbolic link /data/web_static/current
        run("sudo rm -rf /data/web_static/current")

        # Create a new the symbolic link /data/web_static/current
        run("sudo ln -sf {} /data/web_static/current".format(release_path))
        return (True)
    except Exception:
        return(False)
