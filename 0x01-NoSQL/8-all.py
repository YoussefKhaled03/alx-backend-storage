#!/usr/bin/env python3
"""
list all documents
"""


def list_all(mongo_collection):
    """
    List all documents in a collection
    """
    return mongo_collection.find()
