#!/usr/bin/python3
"""
Fabric script that generates a
.tgz archive from the contents of the web_static
"""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """All files in the folder web_static must be added to the final archive"""
    if not os.path.exists("versions"):
        local("mkdir -p versions")
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    archive_name = "web_static_{}.tgz".format(timestamp)
    result = local("tar -cvzf versions/{} web_static".format(archive_name))
    if result.succeeded:
        path = "versions/{}".format(archive_name)
        return (path)
    else:
        return (None)
