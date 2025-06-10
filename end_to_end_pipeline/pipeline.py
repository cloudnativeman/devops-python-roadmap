# Pseudocode: Fill in details as needed
import boto3, paramiko, time

# 1. Launch VM
ec2 = boto3.resource('ec2')
instance = ec2.create_instances(...)[0]
instance.wait_until_running()
instance.reload()
ip = instance.public_ip_address

# 2. SSH deploy app, run test
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ip, username="ec2-user", key_filename="path.pem")
ssh.exec_command("sudo yum install -y nginx")
ssh.exec_command("systemctl start nginx")
# 3. Run test
stdin, stdout, stderr = ssh.exec_command("curl -I localhost")
print(stdout.read().decode())
# 4. Teardown
instance.terminate()