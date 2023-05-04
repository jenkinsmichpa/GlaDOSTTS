# Example Ubuntu 22.04 LXC Container Setup
## Update OS 
```
apt update
apt upgrade -y
apt autoremove -y
```

## Install required apt packages
```
apt install git pip espeak-ng ufw -y
```

## Install required pip packages
```
pip install -U Flask
```

## Download and set up glados-tts
```
cd /root
git clone https://github.com/R2D2FISH/glados-tts.git
cd glados-tts
pip install -r requirements.txt
mkdir audio
```

## Verify engine  functionality
```
python3 engine.py
```

## Create systemctl service
```
nano /etc/systemd/system/gladostts.service
```

Enter the following content:
```
[Unit]
Description=GlaDOS TTS Engine
After=multi-user.target
[Service]
Type=simple
Restart=always
WorkingDirectory=/root/glados-tts
ExecStart=/usr/bin/python3 /root/glados-tts/engine.py
[Install]
WantedBy=multi-user.target
```

## Load and start systemctl service 
```
systemctl daemon-reload
systemctl enable gladostts.service
systemctl start gladostts.service
```

## Set up firewall rules
```
ufw allow 8124/tcp
ufw enable
```