import os
import geopandas as gpd
from sqlalchemy import create_engine
from sqlalchemy.schema import CreateSchema
from decouple import config

def folder_paths(folder):
    root_paths = []
    for root, directory, files in os.walk(folder):
        list_paths = [root, directory]
        if len(list_paths[1]) == 0:
            root_paths.append(list_paths[0])
        else:
            continue

    return root_paths


def paths(folder):
    full_paths = []
    for i in folder_paths(folder):
        for root, directory, files in os.walk(i):
            for file in files:
                if file.endswith('.shp'):
                    full_paths.append(os.path.join(i, file))
    return full_paths


def schemas_list(folder):
    schemas = []
    for i in folder_paths(folder):
        schema = i.split('/')[-1].lower()
        schemas.append(schema)

    return list(set(schemas))


def create_schemas(engine, folder):
    schemas = schemas_list(folder)
    for schema_name in schemas:
        if not engine.dialect.has_schema(engine, schema_name):
            engine.execute(CreateSchema(schema_name))


def upload_database(folder):
    file_paths = paths(folder)
    create_schemas(engine, folder)

    not_uploaded = []
    for i in file_paths:
        name = i.split('/')[-1][:-4].lower()
        schema = i.split('/')[-2].lower()
        print(f'Realizando upload da camada {name}')
        try:
            gdf = gpd.read_file(i)
            gdf.to_postgis(name, engine, schema=schema, index=True, index_label='id_pk')
        except:
            print(f'Impossível realizar upload da camada {name}')
            not_uploaded.append(i)

    return not_uploaded


if __name__ == "__main__":
    engine = create_engine(config('POSTGRES'))
    valores = upload_database('/home/newmar/Downloads/ibge')
    print(valores)
