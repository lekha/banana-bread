# banana-bread
A voting system for ranking banana breads in a bake-off competition

## Development

### Requirements

You should have the following installed and running:
* python 3
* vue-cli 3
* npm

### Setup

```bash
git clone git@github.com:lekha/banana-bread

virtualenv -p python3 server
source server/bin/activate

cd banana-bread/server
pip install -r requirements.txt
pip install -e .

FLASK_APP=server/app.py flask run
```

In another tab:

```bash
cd banana-bread/client
npm install
npm run serve
```
