import paramiko

servers = [("user", "ip1"), ("user", "ip2")]
for user, ip in servers:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, username=user)  # Add password/key as needed
    stdin, stdout, stderr = ssh.exec_command("df -h")
    print(f"{ip}:\n{stdout.read().decode()}")
    ssh.close()