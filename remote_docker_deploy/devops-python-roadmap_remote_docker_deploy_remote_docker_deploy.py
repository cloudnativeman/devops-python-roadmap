import docker

client = docker.DockerClient(base_url='tcp://remotehost:2375')
container = client.containers.run("nginx:latest", detach=True, ports={'80/tcp': 8080})
print(f"Started container {container.id}")