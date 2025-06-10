import requests

owner = "owner"
repo = "repo"
token = "YOUR_GITHUB_TOKEN"
headers = {"Authorization": f"token {token}"}
url = f"https://api.github.com/repos/{owner}/{repo}/actions/runs"
r = requests.get(url, headers=headers)
data = r.json()
latest = data["workflow_runs"][0]
print(f"Status: {latest['status']}, Conclusion: {latest['conclusion']}")