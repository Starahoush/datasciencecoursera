# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 10:13:46 2022

This application will read roster data in JSON format, parse the file, and then produce an SQLite database that contains a User, Course, and Member table and populate the tables from the data file.

@author: Igor
"""

import sqlite3
import json

conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Member;

CREATE TABLE User (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Course (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title   TEXT UNIQUE
);

CREATE TABLE Member (
    user_id  INTEGER,
    course_id  INTEGER,
    role INTEGER,
    PRIMARY KEY (user_id,course_id)
)
''')

file = open("roster_data.json").read()
data = json.loads(file)

for relation in data:
    user = relation[0]
    course = relation[1]
    role = relation[2]
    cur.execute('INSERT OR IGNORE INTO User (name) VALUES (?)',(user,))
    cur.execute('SELECT id FROM User WHERE name = ?', (user,))
    user_id = cur.fetchone()[0]
    cur.execute('INSERT OR IGNORE INTO Course (title) VALUES (?)',(course,))
    cur.execute('SELECT id FROM Course WHERE title = ?', (course,))
    course_id = cur.fetchone()[0]
    cur.execute('INSERT OR IGNORE INTO Member (user_id, course_id, role) VALUES (?,?,?)',(user_id, course_id, role))

conn.commit()