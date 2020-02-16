from utilities.yaml_utils import YamlUtils


class Setup():

	@classmethod
	def setup(cls):

		configuration_file = 'C:\\Code\\pythonautomationframework\\config\\configuration.yaml'
		return YamlUtils.load_yaml_file(configuration_file)


