"""Civit.AI Local Database

Usage:
  main.py creators [options]
  main.py models [options] (get|download)
  main.py version [options]
  main.py tags [options]
  main.py sync [options]
  main.py (-h | --help)
  main.py --version

Options:
    -i ID, --id ID              Model versions ID
    -l LIMIT, --limit LIMIT     Limit items returned
    --period PERIOD             Something???
    -q QUERY, --query QUERY     Text query
    -p PAGE, --page PAGE        Pagination offset
    -r RATING, --rating RATING  Search by model ratings
    -s SORT, --sort SORT        Sort results by
    --save                      Save results to database
    -t TAG, --tag TAG           Tag search
    -t TYPE, --type TYPE        Model type
    -u USER, --username USER    Model creator username

    -v --verbose    Increase verbosity
    -h --help       Show this screen.
    --version       Show version.
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import os
from docopt import docopt

from src.civit_api import get_creators, get_models, get_model_version,  get_tags

DATABASE_NAME = os.getenv("DATABASE_NAME","civitai_default_db")
Base = declarative_base()
engine = create_engine(f"sqlite:///{DATABASE_NAME}.db")
Base.metadata.create_all(engine)

VERBOSE = False

if __name__ == '__main__':
    arguments = docopt(
        __doc__,
        version=f'Civit.AI Local Database {os.getenv("PROGRAM_VERSION","0.0.1")}'
    )
    print(arguments)

    if arguments['--verbose']:
        VERBOSE = True

    if arguments["creators"]:
        passed_args = {}
        if arguments['--limit']:
            passed_args["limit"]=arguments['--limit']
        if arguments['--page']:
            passed_args["page"]=arguments['--page']
        if arguments['--query']:
            passed_args["query"]=arguments['--query']
        if arguments['--save']:
            passed_args["save"]=arguments['--save']
        get_creators(**passed_args)
    elif arguments["models"]:
        if arguments["get"]:
            passed_args = {}
            if arguments['--limit']:
                passed_args["limit"]=arguments['--limit']
            if arguments['--page']:
                passed_args["page"]=arguments['--page']
            if arguments['--query']:
                passed_args["query"]=arguments['--query']
            if arguments['--tag']:
                passed_args["tag"]=arguments['--tag']
            if arguments['--username']:
                passed_args["username"]=arguments['--username']
            if arguments['--type']:
                passed_args["type"]=arguments['--type']
            if arguments['--sort']:
                passed_args["sort"]=arguments['--sort']
            if arguments['--period']:
                passed_args["period"]=arguments['--period']
            if arguments['--rating']:
                passed_args["rating"]=arguments['--rating']
            if arguments['--save']:
                passed_args["save"]=arguments['--save']
            get_models(**passed_args)
        elif arguments["download"]:
            raise Exception('Not Implemented Yet!')
    elif arguments["version"]:
        passed_args = {}
        if arguments['--id']:
            passed_args["model_versions_id"]=arguments['--id']
        if arguments['--save']:
            passed_args["save"]=arguments['--save']
        get_model_version(**passed_args)
    elif arguments["tags"]:
        passed_args = {
            "limit":arguments['--limit'],
            "page":arguments['--page'],
            "query":arguments['--query'],
            "save":arguments['--save']
        }
        get_tags(**passed_args)
    elif arguments["sync"]:
        raise Exception('Not Implemented Yet!')
    else:
        raise Exception("Arguments parsing failed")
