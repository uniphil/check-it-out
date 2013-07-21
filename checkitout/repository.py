import git
from github3 import login
from . import app

repo = git.Repo(app.config.get('REPO_PATH'))
print "heads:\n", "\n".join("{}: {}".format(h.name, h.commit.hexsha) for h in repo.heads)

gh = login('uniphil', password='zen of antigravity, import')

print gh.user
