#!/usr/bin/env python3
"""
insert new document
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection
    """
    new = mongo_collection.insert_one(kwargs)
    return new.inserted_id
