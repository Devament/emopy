from setuptools import setup

setup(name='emopy',
      version='0.1',
      description='Emotion Recognition Package for Python',
      url='http://github.com/selameab/emopy',
      author='Selameab',
      author_email='email@selameab.com',
      license='',
      package_data={'emopy': ['models/*.h5', 'models/*.json']},
      include_package_data=True,
      packages=['emopy'],
      dependency_links=["https://github.com/tensorflow/tensorflow/tarball/master"],
      install_requires=[
          'dlib',
          'tensorflow',
          'keras>=2.0'
      ],
      zip_safe=False)
