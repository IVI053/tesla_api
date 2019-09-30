# Tesla API
Version 1.1.1

This is a package for connecting to the Tesla API.
It's a fork of mlowijs work with refactored authentication and token handling.

## Usage

See `example.py` for more details.

On first use you will get asked to provide your credentials interactively. As you should never store credentials in code, only OAUTH-Tokens get saved in `token.json` and will be loaded from there for future requests.

## Roadmap

### 1.1
Refactoring authentication to facilitate tokens better

### 1.2
Add Powerwall API endpoints
