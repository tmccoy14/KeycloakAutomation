# Keycloak Automation

Keycloak Automation CLI is a tool to automate the creation of realms and clients to easily integrate authentication with applications.

## Development & Setup

Create some sort of virtual environment before install `keycli` the CLI tool.

#### Install Keycloak Automation CLI Tool

```sh
# Activate your virtual enviroment!
#
# In the root of the project / repository
$ pip install --editable .
```

The `--editable` flag will allow for you to make edits to code without having to
re-run `pip install ...` locally.

#### Validate the Install

```sh
$ keycli --version
API version: v0.1.0
```
