import json
import requests
from pathlib import Path

import typer
from pymongo import MongoClient

from app.models import RequestPayload

HEADERS = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
}

URL = 'https://api.reporter.nih.gov/v2/projects/search'


def get_mongo_client():
    return MongoClient(
        host='mongo-docker-example-mongo-1',
        port=27017,
        # Authentication should be set up in a more secure way,
        # but this is just an example.
        # TODO: make auth more secure.
        username='root',
        password='example',
    )


def get_data(payload: RequestPayload):
    res = requests.post(url=URL, headers=HEADERS, json=payload.model_dump())
    return res.json()


def load_data(client: MongoClient, data: list[dict]):
    db = client['testdb']
    collection = db['testdata']
    # clear out the collection for testing
    collection.drop()
    collection.insert_many(data)


def main(payload: Path):
    data = RequestPayload.model_validate_json(payload.read_text())
    res = get_data(data)
    client = get_mongo_client()
    load_data(client, res['results'])

    # display the inserted data
    cursor = client['testdb']['testdata'].find({})
    for item in cursor:
        print(item)


if __name__ == '__main__':
    typer.run(main)

