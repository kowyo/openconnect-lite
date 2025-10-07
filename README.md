# openconnect-sso

> [!NOTE]
> This project is a fork of [vlaci/openconnect-sso](https://github.com/vlaci/openconnect-sso) and is still under development. Please open issues or discussions in [kowyo/openconnect-sso](https://github.com/kowyo/openconnect-sso) if you find any issues. Questions and contribution is cordially welcome.

Wrapper script for OpenConnect supporting Azure AD (SAMLv2) authentication
to Cisco SSL-VPNs

## Installation

### Install OpenConnect

```shell
sudo apt install openconnect # Debian
brew install openconnect # macOS
# other systems should be supported, but haven't been tested by me
```

### Install uv

We use [uv](https://docs.astral.sh/uv/) to install this project. If you don't have `uv` installed, you can install it by running:

```shell
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Option 1: Install from source

```shell
# Clone the latest version of this fork
git clone https://github.com/kowyo/openconnect-sso
uv run openconnect-sso --help # test the installation
uv run openconnect-sso --server  --user 
```

### Option 2: Install as a global tool

Alternatively, you can use `uv tool install` or `uvx` to install `openconnect-sso` as a global tool.

```shell
# install the latest version
uv tool install git+https://github.com/kowyo/openconnect-sso

# install the latest version and execute `openconnect-sso` directly
uvx git+https://github.com/kowyo/openconnect-sso
```

## Usage

```shell
openconnect-sso --server <vpn_server_addr> --user <your_username>
```

## Configuration

You can customize the behavior of `openconnect-sso` by creating a configuration file at
`$XDG_CACHE_HOME/.config/openconnect-sso/config.toml` or `$HOME/.config/openconnect-sso/config.toml` on Unix and `%LOCALAPPDATA%\.config\openconnect-sso\config.toml` on Windows

```yaml
on_disconnect = ""

[default_profile]
server = "<VPN_SERVER_ADDRESS>"
user_group = ""
name = ""

[credentials]
username = "<YOUR_USERNAME>"

[auto_fill_rules]
[[auto_fill_rules."https://*"]]
selector = "div[id=passwordError]"
action = "stop"

[[auto_fill_rules."https://*"]]
selector = "input[type=email]"
fill = "username"

[[auto_fill_rules."https://*"]]
selector = "input[name=Password]"
fill = "password"

[[auto_fill_rules."https://*"]]
selector = "input[data-report-event=Signin_Submit]"
action = "click"

[[auto_fill_rules."https://*"]]
selector = "#submitButton"
action = "click"

[[auto_fill_rules."https://*"]]
selector = "div[data-value=PhoneAppOTP]"
action = "click"

[[auto_fill_rules."https://*"]]
selector = "a[id=signInAnotherWay]"
action = "click"

[[auto_fill_rules."https://*"]]
selector = "input[name=otc]"
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
