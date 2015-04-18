#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

__author__ = 'raphael'
__version_info__ = ('0', '0', '2')
__version__ = '.'.join(__version_info__)

from apps import manager
#from apps import app




@manager.command
def initdb():
    from apps import db
    db.create_all()
    print "database initial complete"

'''
@manager.command
def migrate():
    pass
'''

if __name__=="__main__":
    manager.run()
