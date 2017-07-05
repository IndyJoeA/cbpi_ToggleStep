# -*- coding: utf-8 -*-
import time


from modules.core.props import Property, StepProperty
from modules.core.step import StepBase
from modules import cbpi

@cbpi.step
class ToggleStep(StepBase):

	# Properties
	actor = StepProperty.Actor("Actor")
	power = Property.Number("Power", configurable=True)
	toggle_type = Property.Select("Toggle Type", options=["On", "Off", "Power Only"])

	def init(self):
		if self.toggle_type == "On":
			if self.power is not None and self.power:
				self.actor_on(int(self.actor), self.power)
			else:
				self.actor_on(int(self.actor))
		if self.toggle_type == "Off":
			self.actor_off(int(self.actor))
		if self.toggle_type == "Power Only" and self.power is not None and self.power:
			self.actor_power(int(self.actor), self.power)

	def finish(self):
		pass

	def execute(self):
		self.next()
