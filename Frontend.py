from lxml.etree import Error

import cherrypy
import os
import Question
import sys
import Answer
from spacy.en import English
from jinja2 import Environment, FileSystemLoader

class Frontend:
	@cherrypy.expose
	def index(self, question=None):
		"""

			My project specific stuff not related (not super secret either)
			
		"""

	def __init__(self, nlp):
		self.nlp = nlp
		self.env = Environment(loader=FileSystemLoader('Templates'))
		try:
			self.kb =KnowledgeBase.get_FAQ_Only()
			print("loaded KB")
		except Error as e:
			pass


def setup(nlp)
	conf = {
		'/': {
			'tools.sessions.on': True,
			'tools.staticdir.root': os.path.abspath(os.getcwd())
		},
		'/CSS': {
			'tools.staticdir.on': True,
			'tools.staticdir.dir': './Templates/CSS'
		}
	}
	cherrypy.quickstart(Frontend(nlp), '/', conf)

if __name__=='__main__':
	print("(Frontend)Loading Spacy: waiting",end="",flush=True)
	nlp = English()
	print("\r(Frontend)Loading Spacy: done")
	setup(nlp)