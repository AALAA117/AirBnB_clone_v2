#!/usr/bin/python3
"""
Write a Fabric script
that creates and distributes an archive to your web servers
"""
from fabric.api import env
from fabric.operations import local, put
from os.path import exists
from datetime import datetime
from os import makedirs

env.hosts = ['34.204.82.115', '3.83.227.236']


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    """
    if not exists("versions"):
        makedirs("versions")

    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    archive_name = "web_static_{}.tgz".format(timestamp)
    result = local("tar -cvzf versions/{} web_static"
                   .format(archive_name), capture=True)
    if result.succeeded:
        archive_path = "versions/{}".format(archive_name)
        return archive_path
    else:
        return None


def do_deploy(archive_path):
    """
    Distributes an archive to the web servers and deploys it.
    """
    if not exists(archive_path):
        return False
    filename = archive_path.split('/')[-1]
    folder_name = filename.split('.')[0]
    put(archive_path, '/tmp/')
    run('mkdir -p /data/web_static/releases/{}/'.format(folder_name))
    run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'
        .format(filename, folder_name))
    run('rm /tmp/{}'.format(filename))
    run('rm -f /data/web_static/current')
    run('ln -s /data/web_static/releases/{}/ /data/web_static/current'
        .format(folder_name))
    return True


def deploy():
    """
    Creates and distributes an archive to the web servers.
    """
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
