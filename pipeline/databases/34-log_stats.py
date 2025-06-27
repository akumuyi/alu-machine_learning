#!/usr/bin/env python3
"""
Nginx logs stored in MongoDB:
"""

from pymongo import MongoClient

if __name__ == '__main__':
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    # Get the total number of documents
    total_logs = collection.count_documents({})

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {}
    for method in methods:
        method_counts[method] = collection.count_documents({"method": method})

    # Get the count of status check
    status_check_count = collection.count_documents(
        {"method": "GET", "path": "/status"}
    )

    # Print the stats in Python 3.5 compatible format
    print("{} logs".format(total_logs))
    print("Methods:")
    for method in methods:
        print("\tmethod {}: {}".format(method, method_counts[method]))
    print("{} status check".format(status_check_count))
