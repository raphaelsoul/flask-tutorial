#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

__author__ = 'raphael'

from flask.ext.script import Manager
from apps import app

manager=Manager(app)
@manager.command
def hello():
    print "hello"

@manager.command
def initdb():
    from apps import db
    db.create_all()
    print "database initial complete"

@manager.command
def migrate():
    pass

#if __name__=="__main__":
#    manager.run()
if __name__=="__main__":
    if sys.argv.__len__() > 1:
        manager.run()
    else:
        app.run()
