#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Configuration.
Local config override default config.
'''

__author__ = 'Tan Chao'


import json


class Config(dict):
	def __init__(self, config={}):
		super(Config, self).__init__()
		for key, value in config.iteritems():
			if isinstance(value, dict):
				self[key] = Config(value)
			else:
				self[key] = value

	def __getattr__(self, key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError("Config object has no config item '%s'" % key)

	def __setattr__(self, key, value):
		self[key] = value

	def update(self, config):
		if not config:
			return
		for key, value in config.iteritems():
			if isinstance(value, dict):
				if key in self:
					self[key].update(value)
				else:
					self[key] = Config(value) # new config item
			else:
				self[key] = value

	def __str__(self):
		return json.dumps(self)

	def __repr__(self):
		return str(self)


import config_default

try:
	import config_local
except ImportError:
	config_local = None


configs = Config(config_default.configs)
if config_local:
	configs.update(config_local.configs)


if __name__ == '__main__':
	print('config items json:')
	print(configs)