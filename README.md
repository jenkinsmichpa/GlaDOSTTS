# Home Assistant Component for GLaDOS Text to Speech Engine

✨ This is a component for Home Assistant which integrates the [glados-tts](https://github.com/R2D2FISH/glados-tts) engine by [R2D2FISH](https://github.com/R2D2FISH). It is built on the [Remote-PicoTTS](https://github.com/Poeschl/Remote-PicoTTS) component by [Poeschl](https://github.com/Poeschl). ✨

# Installation

## HACS Installation
1. Using the sidebar, navigate to the "Integrations" page of HACS on Home Assistant.
    * For help installing HACS, read their documentation [here](https://hacs.xyz/docs/setup/download/). 
3. Click the triple dots and select "Custom repositories".
4. Paste in the GlaDOSTTS repository URL and select the "Integration" category before clicking "ADD". 
5. Click the newly shown GLaDOSTTS repository and then "Download". 
6. Restart the Home Assistant instance.

## Manual Installation
Copy the `gladostts/` directory located under `GlaDOSTTS/custom_components/` to the `/config/custom_components/` directory of your home assistant installation.

This can be performed using Home Assistant addons such as [Samba](https://github.com/home-assistant/addons/blob/master/samba/DOCS.md) or [SSH](https://github.com/home-assistant/addons/blob/master/ssh/DOCS.md).

# Configuration

## Same Host
Add following lines of configuration to  `/config/configuration.yaml` if you are running the GLaDOSTTS engine on the same machine

```yaml
tts:
  - platform: gladostts

```
The integration will connect to GlaDOSTTS after a Home Assistant restart or configuration reload.

## Remote Host
Instructions for running the engine within a remote LXC container on Proxmox or other virtualization platform are available [here](https://github.com/jenkinsmichpa/GlaDOSTTS/blob/master/ExampleLXCContainerSetup.md).

Add following lines of configuration to `/config/configuration.yaml` if you are running the GLaDOSTTS engine on a different machine than the Home Assistant instance.
```yaml
tts:
  - platform: gladostts
    host: <engine_host>
    port: <engine_port>

```
The integration will connect to GlaDOSTTS after a Home Assistant restart or configuration reload.

# Security Disclaimer
Please note the risk of running the engine as a permanent service. As the engine's HTTP traffic is unencrypted, it should only be made accessible over a secure, private network when running on a remote host. If running on the same host, host-based firewall rules should configured to block external access.

