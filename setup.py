from setuptools import setup

setup(name='pyclone',
      version='0.1.0',
      description='A small script to download all of the public repos of a user.',
      py_modules=["pyclone"],
      package_dir={'': 'src'},
      author='Onur Ravli',
      author_email='onurravli@hotmail.com',
      long_description=open('readme.md').read() + '\n\n' +
      open('CHANGELOG.md').read(),
      long_description_content_type="text/markdown",
      url='https://github.com/onurravli/pyclone',
      include_package_data=True,
      classifiers=[
          'Development Status :: Beta',
          'Programming Language :: Python :: 3.10',
          'Intended Audience :: Developers',
          'Intended Audience :: Other Audience',
          'Intended Audience :: Science/Research',
          'Intended Audience :: Education',
          'Topic :: GitHub',
          'Operating System :: OS Independent',
      ],
      install_requires=['bs4', 'requests'],
      keywords=['pyclone', 'git clone', 'clone all repos'])
