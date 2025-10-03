# openconnect-sso

> This is a fork of [vlaci/openconnect-sso](https://github.com/vlaci/openconnect-sso) maintained by [kowyo](https://github.com/kowyo).

Wrapper script for OpenConnect supporting Azure AD (SAMLv2) authentication
to Cisco SSL-VPNs

## Installation

### Install OpenConnect

```shell
sudo apt install openconnect # Debian
brew install openconnect # macOS
```
### Install OpenConnect-SSO

We use [uv](https://docs.astral.sh/uv/) to install the project:

```shell
# Install uv first (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone the latest version of this fork
git clone https://github.com/kowyo/openconnect-sso
uv run openconnect-sso --help # test the installation
```

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
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone and set up the project
git clone https://github.com/kowyo/openconnect-sso
cd openconnect-sso

# Create the virtual environment and install all dependency groups
make dev

# Run development commands without activating the venv manually
uv run openconnect-sso --help
```

