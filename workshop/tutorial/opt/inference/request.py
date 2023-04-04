import requests
import subprocess

def main():

  body = {
    "max_tokens": 64,
    "prompt": "I want to buy a new phone today.",
    "top_k": 50,
    "top_p": 0.5,
    "temperature": 0.7
  }

  # Obtaining the IP address of the inference containe is necessary only because
  # of the containerized environment we are running in.
  container_name = "opt-inference"
  ip_address = get_container_ip(container_name)

  url = f'http://{ip_address}:7070/generation'
  response = requests.post(url=url, json=body)

  print(response.json()['text'])

# This function is used to obtain the IP address of the inference container. We only need it here
# because of the containerized structure of this lab environment.
def get_container_ip(container_name):
    cmd = 'docker inspect -f "' + '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' + f'" {container_name}'
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
    
    if result.returncode == 0:
        return result.stdout.strip()
    else:
        print(f"Error: {result.stderr}")
        return None

if __name__ == '__main__':
  main()
