# Upload shapefiles to postgis
Script to upload shapefiles to specific postgres database considering folders to be a schema

## Steps to execute:
1. Open terminal
2. Clone Repo
3. Go into /upload_shapes_postgis
4. Create a virtualenv (python 3.9.0) and activate   
5. Install the requirements packages (requirements.txt)
6. Create .env file on folder upload_shapes_postgis copying the env sample in contrib package and filling correctly


## Codes
```
git clone https://github.com/newmarwegner/upload_shapes_postgis.git
cd /upload_shapes_postgis
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
