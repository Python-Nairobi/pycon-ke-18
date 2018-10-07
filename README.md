PyConKE 2018 Website Repo
==========

## INTRO
This repository contains the sources used to build the PyConKE 2018 Website.
We use [pelican](http://docs.getpelican.com) to build the contents of this repository
into the site you see at http://pycon.or.ke

## PREREQUIESITES
To contribute, we recommend you install:-

- [Python >= 3.6](https://www.python.org/downloads/release/python-366/)
- [PIP]("http://www.pip-installer.org/en/latest/installing.html)

## CLONING
1. <a href="https://github.com/Python-Nairobi/pyconke/fork" target="_blank">Click here to fork this Repo</a>.
1. Clone your fork and cd into it.
1. Create a virtualenv for your repo:- `python3 -m venv ~/.virtualenvs/pyconke18`.
1. Activate your virtualenv:- `source ~/.virtualenvs/pyconke18/bin/activate`
1. Install the remaining dependencies:- `pip install -r requirements.txt`.
1. Initialize & update submodule dependencies (plugins, theme ..etc): `git submodule update --init --recursive`.
1. Then create a branch, naming it along the lines as your topic of contribution.

## TIPS
1. Alternative lazy way to update submodule(s): `git submodule foreach --recursive git pull origin master` or `git submodule update --remote --merge`
1. Clean and reset submodule(s): `git submodule foreach --recursive git reset --hard`

## EDITING
Start the development server:- `./develop_server.sh start`. Open http://127.0.0.1:8000 to view.
Any changes you make will automatically be reflected there.

1. Add, commit and push your changes.
1. Send us a pull request against [master](https://github.com/Python-Nairobi/pyconke/tree/master).

We'll review your contribution and maybe ask you to make further changes before we merge.
