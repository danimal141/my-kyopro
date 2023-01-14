# my-kyopro-tessoku

## Dependencies
- [atcoder-cli](https://github.com/Tatamo/atcoder-clihttps://github.com/Tatamo/atcoder-cli)
- [online-judge-tools](https://github.com/online-judge-tools/oj)

## Get started
### Poetry
```shell
$ poetry install

$ poetry run python -m flake8 **/*.py # lint
$ poetry run python -m black **/*.py # format
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
```

## Memo
### How to use PyPy as the default language
- Reference: https://github.com/Tatamo/atcoder-cli/issues/29
