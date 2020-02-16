from core_framework_lib.utils.yaml_utils import YamlUtils
import logging

class Setup():

	@classmethod
	def setup(cls):

		configuration_file = 'C:\\Code\\pythonautomationframework\\config\\configuration.yaml'
		return YamlUtils.load_yaml_file(configuration_file)


