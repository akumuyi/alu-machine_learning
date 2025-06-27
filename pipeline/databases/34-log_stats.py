#!/usr/bin/env python3
"""
Nginx logs stored in MongoDB statistics
"""

from pymongo import MongoClient
import sys

def main():
    """Main function to retrieve and display log statistics"""
    try:
        # Connect to MongoDB
        client = MongoClient('mongodb://127.0.0.1:27017', serverSelectionTimeoutMS=2000)
        db = client.logs
        collection = db.nginx
        
        # Get total logs
        total_logs = collection.count_documents({})
        
        # Get method counts
        methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
        method_counts = {method: collection.count_documents({"method": method}) for method in methods}
        
        # Get status check count
        status_check_count = collection.count_documents(
            {"method": "GET", "path": "/status"}
        )
        
        # Print results
        print("{} logs".format(total_logs))
        print("Methods:")
        for method in methods:
            print("\tmethod {}: {}".format(method, method_counts[method]))
        print("{} status check".format(status_check_count))
        
    except Exception as e:
        print("Error: {}".format(e), file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
