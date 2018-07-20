# -*- coding: utf-8 -*-


#to initalize file, type git init in terminal within wd
#to add to it, type git add --all

__author__ = "colin mccormick"

import klibs
from klibs import P

class newcode(klibs.Experiment):

	def setup(self):
		pass #hi

	def block(self):
		pass

	def setup_response_collector(self):
		pass

	def trial_prep(self):
		pass

	def trial(self):

		return {
			"block_num": P.block_number,
			"trial_num": P.trial_number
		}

	def trial_clean_up(self):
		pass

	def clean_up(self):
		pass
