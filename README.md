API for converting standard openapi.json to a vCard string targeting iOS Shortcuts.

## Getting Started

Install requirements, python, FastAPI and uvicorn.

## Running it as a service

```
nano /etc/systemd/system/openapi-to-vcard.service
```

```
[Unit]
Description=Converting openapi.json to vCard output targeting iOS
After=network.target
[Service]
User=root
Group=root
WorkingDirectory=/root/git/pi-remote
ExecStart=uvicorn main:app --reload --port 5010 --host 0.0.0.0
[Install]
WantedBy=multi-user.target
```

```
systemctl enable openapi-to-vcard
systemctl start openapi-to-vcard
systemctl restart openapi-to-vcard
systemctl status openapi-to-vcard
```
