import csv
from github import Github

token = "<GITHUB_ACCESS_TOKEN>"
g = Github(token)
repos = []

with open("github-repos.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row["Repository"])
        try:
            repo = g.get_repo(row["Repository"])
            repos.append(repo)
        except:
            print("Could not find GitHub repository")

with open("github-repos-enriched.csv", mode="w") as csv_file:
    fieldnames = [
        "url",
        "name",
        "description",
        "homepage",
        "forks",
        "stars",
        "subscribers_count",
        "watchers_count",
        "created_at",
    ]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=",")

    writer.writeheader()
    for repo in repos:

        writer.writerow(
            {
                "url": repo.url,
                "name": repo.name,
                "description": repo.description,
                "homepage": repo.homepage,
                "forks": repo.forks_count,
                "stars": repo.stargazers_count,
                "subscribers_count": repo.subscribers_count,
                "watchers_count": repo.watchers_count,
                "created_at": repo.created_at,
            }
        )

