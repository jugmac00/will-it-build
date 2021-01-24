# will-it-build

a GitHub action to [build](https://pypi.org/project/build/) and verify a Python package

## using this action

```
name: Will it build?

on:
  pull_request:
  push:
    branches: [main]

jobs:
  will-it-build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - uses: actions/setup-python@v2
    - uses: jugmac00/will-it-build@main
```

This does a couple of things:
- clones the code
- installs Python
- builds your Python package via [build](https://pypi.org/project/build/)
- verifies the build via `python -m twine check dist/*`

## contributing

You are very welcome to contribute!

## credits

This GitHub Action was inspired when reading 
[Python in GitHub Actions](https://hynek.me/articles/python-github-actions/)
by Hynek.

Thanks a lot for your awesome blog posts!

Also, I'd like to thank the developers of
[build](https://github.com/pypa/build)
and [twine](https://github.com/pypa/twine/).

Thanks for spending your free time!
