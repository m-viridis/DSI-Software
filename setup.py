from setuptools import setup

setup(
  name='GitAPI',
  version='0.1.0',
  author='M. viridis',
  packages=['DSI_software'],
  data_files=[('configs', ['configs/user_config.yml', 'configs/system_config.yml'])]
)
