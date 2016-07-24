#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Default configurations.
'''

__author__ = 'Tan Chao'

configs = {
	'debug': True,
	'server': {
		'host': '0.0.0.0',
		'port': 9000,
	},
	'db': {
		'host': '127.0.0.1',
		'port': 3306,
		'user': 'www',
		'password': 'www',
		'db': 'awesome'
	},
	'session': {
		'secret': 'Awesome'
	}
}
