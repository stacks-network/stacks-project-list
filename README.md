# stacks-community-projects
 A list of community projects in the Stacks ecosystem

## Install

```shell
pip install requirements.txt
```

## Set token
Before running the script, in the `enrich.py` file, you will need to set your own [GitHub personal access token](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token).

## Generate enriched list
The Python script is used to run through a CSV file of relevant Stacks repos and enrich them using the GitHub API.

```shell
python enrich.py
```

## Contributions
If you would like your repo to be part of the list, please submit a PR with a new line in the `github-repos.csv` file. The format is `<user>/<repo>`. For instance:

```csv
agraebe/stacks-community-projects
```
