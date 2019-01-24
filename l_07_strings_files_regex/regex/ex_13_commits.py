import re

GITHUB = "https://github.com/"

PATTERN = r"^https://github\.com/(?P<user>[A-Za-z0-9-]+)/(?P<repo>[A-Za-z_-]+)/commit/(?P<hash>[0-9A-Fa-f]{40}),(?P<message>[^\n]+),(?P<additions>[0-9]+),(?P<deletions>[0-9]+)$"

users = {}

while True:
    input_line = input()
    if input_line == "git push":
        break

    match = re.fullmatch(PATTERN, input_line)

    if not match:
        continue

    username = match.group("user")
    repo = match.group("repo")
    commit_hash = match.group("hash")
    message = match.group("message")
    additions = match.group("additions")
    deletions = match.group("deletions")

    if username not in users:
        users[username] = {}

    if repo not in users[username]:
        users[username][repo] = []

    commit = {
        'hash': commit_hash,
        'message': message,
        'additions': int(additions),
        'deletions': int(deletions)
    }

    users[username][repo].append(commit)


def get_total_count(repo_commits, type):
    return sum(list(map(lambda a: a[type], repo_commits)))


for user, repos in sorted(users.items()):
    print(F"{user}:")
    for repo, commits in sorted(repos.items()):
        print(f"  {repo}:")
        for commit in commits:
            print(
                f"    commit {commit['hash']}: {commit['message']} ({commit['additions']}"
                f" additions, {commit['deletions']} deletions)")
        print(
            f"    Total: {get_total_count(commits, 'additions')}"
            f" additions, {get_total_count(commits, 'deletions')} deletions")
