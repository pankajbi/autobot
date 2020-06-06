import os

class ProjectPath:

    root = os.getcwd().split('test_cases')[0]

    @classmethod
    def get_root_path(cls):
        return ProjectPath.root

    @classmethod
    def tmp(cls):
        return os.path.join(ProjectPath.root, 'tmp')

    @classmethod
    def reports(cls):
        return os.path.join(ProjectPath.root, 'reports')

    @classmethod
    def scripts(cls):
        return os.path.join(ProjectPath.root, 'scripts')

    @classmethod
    def config(cls):
        return os.path.join(ProjectPath.root, 'config')

    @classmethod
    def logfile_name(cls):
        return os.path.join(ProjectPath.reports(), os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0])

    @classmethod
    def aut_configuration_file(cls):
        return os.path.join(ProjectPath.config(), 'application_configuration.yaml')

    @classmethod
    def framework_configuration_file(cls):
        return os.path.join(ProjectPath.config(), 'framework_configuration.yaml')