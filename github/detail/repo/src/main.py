#!/usr/bin/python3
import os

from formula import formula

user = os.environ.get("RIT_GITHUB_USER")
key = os.environ.get("RIT_GITHUB_TOKEN")
repository = os.environ.get("RIT_GITHUB_REPO")
contribution = os.environ.get("RIT_CONTRIBUTION")

formula.run(user, key, repository, contribution)
