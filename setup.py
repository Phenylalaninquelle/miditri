from setuptools import setup


setup(name='Miditri',
      version='0.1',
      py_modules=['miditri'],
      install_requires=[
          'Click',
      ],
      entry_points='''
        [console_scripts]
        miditri=miditri:cli
      '''
)
