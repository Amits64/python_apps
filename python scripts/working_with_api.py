import requests

response = requests.get('https://api.github.com/repos/Amits64/Terraform_repo')
repo_info = response.json()

print("Repository Name: ", repo_info['name'])
print("Description: ", repo_info['description'])
print("Stars: ", repo_info['stargazers_count'])
print("Language: ", repo_info['language'])
print(repo_info)
