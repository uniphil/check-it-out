import git
#from github3 import login
from . import app

repo = git.Repo(app.config.get('REPO_PATH'))
print "heads:\n", "\n".join("{}: {}".format(h.name, h.commit.hexsha) for h in repo.branches)


def get_app_from_ref(ref):
    pass


#gh = login('uniphil', password='zen of antigravity, import')

