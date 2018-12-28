#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Rambo'

'''
handle web api
'''

import json, re, time, logging, hashlib, base64, asyncio

from coroweb import get, post

from models import User, Blog, Comment, next_id

@get('/index')
async def index(request):
    users = await User.findAll()
    return {
        '__template__': 'index.html',
        'users': users
    }
