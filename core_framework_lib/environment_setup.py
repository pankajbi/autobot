from utilities.yaml_utils import YamlUtils
from core_framework_lib.project_paths import ProjectPath


class Env:
	configuration = YamlUtils.load_yaml_file(ProjectPath.configuration_file())

	@classmethod
	def selenium_easy_ui_url(cls):
		return Env.configuration["aut"]["selenium_easy"]["ui"]["url"]




