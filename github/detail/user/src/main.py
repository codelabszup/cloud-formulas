#!/usr/bin/python3
import os

from formula import formula

user = os.environ.get("RIT_GIT_USER")
key = os.environ.get("RIT_GIT_TOKEN")
username = os.environ.get("RIT_GITHUB_USERNAME")
repo_details = os.environ.get("RIT_REPO_DETAILS")

formula.run(username, repo_details, user, key)
