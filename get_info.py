import requests

def get_github_user_location_n_followers_count(username, token):
    url = f"https://api.github.com/users/{username}"
    headers = {
        "Accept": "application/vnd.github+json",
        # "Authorization": f"Bearer {token}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        user_data = response.json()
        return user_data.get('location'), user_data.get('followers')
    else:
        return None
    

def get_repo_languages(owner, repo, token):
    url = f"https://api.github.com/repos/{owner}/{repo}/languages"
    headers = {
        "Accept": "application/vnd.github+json",
        # "Authorization": f"Bearer {token}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Example usage
owner = "jeffrey82221"  # Replace with the repository owner's username
repo = "JSkiner"  # Replace with the repository name

languages = get_repo_languages(owner, repo, token='')
print(languages)


# Example usage
username = "jeffrey82221"  # Replace with the GitHub username
token = "YOUR_GITHUB_TOKEN"  # Replace with your GitHub token
result = get_github_user_location_n_followers_count(username, token='')
print(result)
