from setuptools import setup

setup(name='emopy',
      version='0.1',
      description='Emotion Recognition Package for Python',
      url='http://github.com/selameab/emopy',
      author='Selameab',
      author_email='email@selameab.com',
      license='',
      packages=['emopy'],
      install_requires=[
          'keras>=2.0'
      ],
      zip_safe=False)
