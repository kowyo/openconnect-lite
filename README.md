# openconnect-sso

> This is a fork of [vlaci/openconnect-sso](https://github.com/vlaci/openconnect-sso) maintained by [kowyo](https://github.com/kowyo).

Wrapper script for OpenConnect supporting Azure AD (SAMLv2) authentication
to Cisco SSL-VPNs

[![Tests Status
](https://github.com/vlaci/openconnect-sso/workflows/Tests/badge.svg?branch=master&event=push)](https://github.com/vlaci/openconnect-sso/actions?query=workflow%3ATests+branch%3Amaster+event%3Apush)

## Installation

### Using uv

The fastest way to install `openconnect-sso` is using [uv](https://docs.astral.sh/uv/), an extremely fast Python package installer written in Rust:

```shell
# Install uv first (if not already installed)
$ curl -LsSf https://astral.sh/uv/install.sh | sh

# Install openconnect-sso globally
$ uv tool install openconnect-sso

# Or install from the repository directly
$ uv tool install git+https://github.com/vlaci/openconnect-sso
```

You can also use uv to create a virtual environment and install locally:

```shell
# Create a virtual environment and activate it
$ uv venv
$ source .venv/bin/activate  # On Linux/macOS
# or .venv\Scripts\activate  # On Windows

# Install openconnect-sso
$ uv add openconnect-sso
```

### On Arch Linux

There is an unofficial package available for Arch Linux on
[AUR](https://aur.archlinux.org/packages/openconnect-sso/). You can use your
favorite AUR helper to install it:

``` shell
yay -S openconnect-sso
```

### Windows *(EXPERIMENTAL)*

Install with [uv](#using-uv) and be sure that you have `sudo` and `openconnect`
executable commands in your PATH.

## Usage

If you want to save credentials and get them automatically
injected in the web browser:

```shell
$ openconnect-sso --server vpn.server.com/group --user user@domain.com
Password (user@domain.com):
[info     ] Authenticating to VPN endpoint ...
```

User credentials are automatically saved to the users login keyring (if
available).

If you already have Cisco AnyConnect set-up, then `--server` argument is
optional. Also, the last used `--server` address is saved between sessions so
there is no need to always type in the same arguments:

```shell
$ openconnect-sso
[info     ] Authenticating to VPN endpoint ...
```

Configuration is saved in `$XDG_CONFIG_HOME/openconnect-sso/config.toml`. On
typical Linux installations it is located under
`$HOME/.config/openconnect-sso/config.toml`

For CISCO-VPN and TOTP the following seems to work by tuning the config.toml
and removing the default "submit"-action to the following:

```
[[auto_fill_rules."https://*"]]
selector = "input[data-report-event=Signin_Submit]"
action = "click"

[[auto_fill_rules."https://*"]]
selector = "input[type=tel]"
fill = "totp"
```

### Adding custom `openconnect` arguments

Sometimes you need to add custom `openconnect` arguments. One situation can be if you get similar error messages:

```shell
Failed to read from SSL socket: The transmitted packet is too large (EMSGSIZE).
Failed to recv DPD request (-5)
```

or:

```shell
Detected MTU of 1370 bytes (was 1406)
```

Generally, you can add `openconnect` arguments after the `--` separator. This is called _"positional arguments"_. The
solution of the previous errors is setting `--base-mtu` e.g.:

```shell
openconnect-sso --server vpn.server.com/group --user user@domain.com -- --base-mtu=1370
#                                                          separator ^^|^^^^^^^^^^^^^^^ openconnect args
```

## Development

This project uses [uv](https://docs.astral.sh/uv/) for dependency management. To set up the development environment:

```shell
# Install uv first (if not already installed)
$ curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone and set up the project
$ git clone https://github.com/vlaci/openconnect-sso
$ cd openconnect-sso
$ uv sync --extra dev

# Activate the virtual environment
$ source .venv/bin/activate  # On Linux/macOS
# or .venv\Scripts\activate  # On Windows

# Install pre-commit hooks
$ pre-commit install

# Run development commands
$ make help  # See available commands
```

Alternatively, you can use the included `Makefile` which will use uv automatically.
