import docker

client = docker.from_env()

print("Building Docker image: flask-apparmor...")
client.images.build(path=".", tag="flask-apparmor")

print("Running container with AppArmor profile: my-apparmor-profile...")
container = client.containers.run(
    "flask-apparmor",
    ports={'5000/tcp': 5000},
    security_opt=["apparmor=my-apparmor-profile"],
    detach=True
)

print(f"Container started: {container.short_id}")

container_info = client.api.inspect_container(container.id)
apparmor_profile = container_info['HostConfig']['SecurityOpt']
print(f"AppArmor profile applied: {apparmor_profile}")

container.stop()
container.remove()
print("Container stopped and removed.")
