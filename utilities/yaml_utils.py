import yaml


class YamlUtils():

	@classmethod
	def load_yaml_file(cls, file_path):
		"""
		:param file_path:
		:return:
		"""

		with open(file_path) as f:
			content = yaml.load(f)

		return content
