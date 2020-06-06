from utilities.yaml_utils import YamlUtils
from core_framework_lib.project_paths import ProjectPath


class AppConfiguration:
	app_configuration = YamlUtils.load_yaml_file(ProjectPath.aut_configuration_file())

	@classmethod
	def selenium_easy_ui_url(cls):
		return AppConfiguration.app_configuration["aut"]["selenium_easy"]["ui"]["url"]


class FrameworkConfiguration:

	framework_configuration = YamlUtils.load_yaml_file(ProjectPath.framework_configuration_file())
	selenium_implicit_wait = framework_configuration["selenium"]["implicit_wait"]
	log_level = framework_configuration["logger"]["log_level"]


