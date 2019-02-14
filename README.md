# dell-omreport-parser

## How To

- Clone repo in `/opt/`

- Move `omsa-scripts/config.example.py` to `omsa-scripts/config.py`

- Edit `omsa-scripts/config.py`
    - `host` is the name of the server
    - `api_server` is the OMSA-Web server. See the API section for more info.
    - `verify_ssl` determines whether or not `requests` will verify the TLS certificate when posting metrics

- Run `install.sh` as root

If you want to clone the repo elsewhere, you'll need to modify `/etc/cron.d/omsa-metrics`.

## API

Metrics are sent to an API server that you define. 

The API server can be found in [this repo](https://github.com/mitchya1/dell-omreport-web)
