from utilities.yaml_utils import YamlUtils
from core_framework_lib.project_paths import ProjectPath
import os


class Setup:
	configuration = YamlUtils.load_yaml_file(ProjectPath.configuration_file())




