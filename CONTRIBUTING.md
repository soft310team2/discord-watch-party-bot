# Contributing to Popcorn

:tada: Thanks for contributing! :tada:

When contributing to this repository, please first discuss the change you wish to make via issue,
email, or any other method with the owners of this repository before making a change.

## Contributing code and documentation:

### Issues

- All code or documentation contributions should be associated
  with an open issue. If an issue does not exist, you should create one first (see guidance
  below).
- All additions or modifications to code should include associated tests.

### Required packages
- Python 3.7+
- pip package manager
After `git clone` ing this repository, you will need to:
`pip install python-dotenv`
`pip install nextcord`

We also require that SonarLint is used during development. 

### Working with branches

Make a branch:

1. If you are making a new feature branch, run `git checkout main` to switch to the main branch. Otherwise, switch onto the feature branch your are working off
2. Run `git pull upstream main` to make sure your branch is up to date
3. Run `git branch [branch-name]` to create the branch
4. Run `git checkout [branch-name]` to switch to the branch

Committing: Always commit to origin, not to upstream!

1. Run `git add .` to add all your modified files
2. Run `git commit -m "Type your commit message"` to make the commit
3. Run `git push origin` to push your changes onto your forked repository

### Merging Your Changes

Everytime you want to update the shared repository with your changes, you need to make a Pull Request (PR). All code contributions must be peer reviewed by at least one other member.

Make sure your code is up-to-date with the shared repository before you make a pull request.

1. Run `git pull upstream main` to sync your branch with the master branch
2. Run `git pull upstream [your-branch]` to sync your local branch with the shared feature branch. This makes sure that any other work on the feature is included with your work.

Groupwork Features: If you are working in a group on a feature, and need to give the group access to your work, without pushing it to main

1. First, make sure you have a feature branch on the shared repository. Go into the repository, select on the branches dropdown, and type the name of the feature branch you have been working from.
2. If no branches show up, click 'Create branch: [branch-name]'
3. Go to your forked repository, and onto the branch that you want push
4. Click on 'Pull Request' to open the PR
5. Make sure that 'base Repository' is set to 'softeng310team2/discord_watch_party_bot', 'base' is set to your feature branch name, 'head repository' is set to your forked repo, and 'head' is set to your feature branch that you're pushing
6. Write a short descriptive title for the PR to summarise your changes. Use the comment box to describe what you have changed, and any decisions you had to make
7. On the right-hand side, select a 'Reviewer' to review your PR, and give it a label
8. Click 'Create pull request'

Independent Features & Bugfixes: Can go straight onto upstream/main

- If you have a piece of finished work that you need to give the rest of the team access to, you can set the base branch to 'main'
- The rest of the PR process should be kept the same

With your PR open, you should wait for at least 1 approval on your pull request. Your reviewers may ask you to change some of the code. If you need to make changes, you can make them and and push them to your origin branch. They will then appear in the pull request.

Most PRs should be associated with an issue. To link an issue and a PR, go to the 'issues' tab, select the relevant issue, click on 'Linked pull requests' in the lower-right of the page, and select the PR you just created. When your PR is merged, the issue will be automatically closed.

- All pull requests must be reviewed by at least one other team member.
  To prevent breaking builds, the code review should include running the test suite, running the code, and ensuring the code works as expected.
- If bugs or other issues are found during the code review, these should be fixed before the pull request is accepted (a new issue does not need to be created).
- After review and any required changes are incorporated (and approved by the reviewer), someone on the team can merge the pull request.

- Do not merge pull requests until appropriate approval has been obteained.
- Prior to merging, all commits should be squashed and merge conflicts should be fixed.

Please note we have a code of conduct, please follow it in all your interactions with the project.

### Reporting Bugs

Bugs are tracked through GitHub issues, to report a bug, create an issue and provide the following information:

- A Description of the Bug.
- Steps to reproduce the bug.
- Any necessary additional information.

Bugs should be appropriately labelled as such.

### Suggesting Enhancements

Enhancements are tracked through GitHub issues, to suggest an enhancement, create an issue and provide the following information:

- Provide a clear and informative title to identify the suggestion.
- Provide a detailed description of the suggested enhancement.
- Explain why this enhancment would be useful to most Mello users.

Enhancements should be appropriately labelled as such.

## Acknowledgements

- This CONTRIBUTING.md was based on [SoftEng701-Group5 Assignment1 CONTRIBUTING.md](https://github.com/SoftEng701-Group5/assignment1/blob/main/CONTRIBUTING.md) which was based on [The Atom CONTRIBUTING.md](https://github.com/atom/atom/blob/master/CONTRIBUTING.md)
