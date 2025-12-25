# Port Checker for NVDA Remote

A simple Flask web application that checks if a specified port is open on the client's IP address. This is useful for verifying that NVDA Remote port forwarding is configured correctly.

## Usage

The web interface is available at the root URL. To check a specific port programmatically:

```
GET /port/<port_number>
```

Returns JSON:
```json
{
  "host": "client_ip_address",
  "port": 6837,
  "open": true
}
```

## Running Locally

```bash
pip install -r requirements.txt
python portcheck.py
```

## Production Deployment

Use gunicorn with the run_gunicorn.py module:

```bash
gunicorn run_gunicorn:app
```
