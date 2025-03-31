#!/usr/bin/python3

import pymongo
from pymongo import MongoClient, errors
from bson.json_util import dumps
import os
from db import *


print("connecting to Mongo")

MONGOUSER = os.getenv('MONGOUSER')
MONGOPASS = os.getenv('MONGOPASS')
MONGOHOST = os.getenv('MONGOHOST')
client = MongoClient(MONGOHOST, username=MONGOUSER, password=MONGOPASS, connectTimeoutMS=200, retryWrites=True)

print("listing dbs")
dbs = client.list_database_names()
print(dbs)

print("switching into gbv6nj database")

gbv6nj = client.gbv6nj

print("creating a new collections named - courses")

courses = gbv6nj.courses

print("adding five records")

course_records = [
    {
        "course_number": "ENWR1001",
        "course_name": "Introduction to Essay Writing",
        "professor": {
            "name": "Dr. Jane Smith",
            "department": "English",
            "email": "lru7pq@virginia.edu"
        },
        "average_gpa": 3.5
    },
    {
        "course_number": "PLAN5022",
        "course_name": "Financial Real Estate",
        "professor": {
            "name": "Fred Rowe",
            "department": "Urban Planning",
            "email": "pwg9qr@virginia.edu"
        },
        "average_gpa": 3.8
    },
    {
        "course_number": "ENWR1020",
        "course_name": "Language in the 1800s",
        "professor": {
            "name": "Peter Stew",
            "department": "English",
            "email": "bhj3ui@virginia.edu"
        },
        "average_gpa": 3.3
    }
    {
        "course_number": "ENWR3070",
        "course_name": "Poetry Writing Basics",
        "professor": {
            "name": "Emily Johnson",
            "department": "English",
            "email": "pwd4hx@virginia.edu"
        },
        "average_gpa": 3.9
    }
    {
        "course_number": "DS2002",
        "course_name": "Data Science Systems",
        "professor": {
            "name": "Neal Magee",
            "department": "Data Science",
            "email": "asg6@virginia.edu"
        },
        "average_gpa": 3.7
    }
]


result = courses.insert_many(course_records)

print("Inserted IDs:", result.inserted_ids)


print("displaying results where the course department is English")

english_classes = courses.find({"department": "English"})

print(dumps(english_classes, indent=2))
