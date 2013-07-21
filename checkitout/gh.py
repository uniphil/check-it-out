from . import app
from github3 import login

gh = login('uniphil', password='zen of antigravity, import')

print gh.user
