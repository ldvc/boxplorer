# boxplorer
webui for managing seedbox downloaded stuff

## installation
```bash
mkdir ~/.virtualenvs
virtualenv --no-site-packages -p /usr/bin/python2.7 venv_boxplorer
source ~/.virtualenvs/venv_boxplorer/bin/activate
pip install requests

mkdir ~/scripts
curl -O https://raw.githubusercontent.com/ldvc/boxplorer/master/client/downloader.py
curl -O https://raw.githubusercontent.com/ldvc/boxplorer/master/client/config.py
```

## usage
```bash
cd ~/scripts/
./downloader.py
```
