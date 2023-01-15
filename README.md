# my-kyopro-tessoku

## Dependencies
- pyenv
- poetry
- [atcoder-cli](https://github.com/Tatamo/atcoder-clihttps://github.com/Tatamo/atcoder-cli)
- [online-judge-tools](https://github.com/online-judge-tools/oj)

## Get started
### Poetry
```shell
$ poetry install

# using poetry
$ poetry shell or poetry run xx

$ poetry run python -m flake8 **/*.py # lint
$ poetry run python -m black **/*.py # format

# pre-commit
$ poetry run pre-commit install
```

### Sign in to Atcoder
```shell
$ acc login # login your atcoder account
$ acc session # check login status
```

### Start programming
```shell
$ acc new tessoku-bookh # create

$ cd path/to/task
$ acc s main.py # using Python3.8
$ acc s main.py -- --guess-python-interpreter pypy # using PyPy

# Try the exam before submitting
$ oj test -c "python3 main.py" -d tests
```

## Memo
### How to use PyPy as the default language
- Reference: https://github.com/Tatamo/atcoder-cli/issues/29
