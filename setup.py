from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    readme = fh.read()

setup(name='bsdotpy',
      version='0.1.1',
      description='BSDotPy, A module to get a bombsquad player\'s account data.',
      long_description=readme,
      long_description_content_type="text/markdown",
      url='https://github.com/FireHead90544/bsdotpy',
      project_urls={
        "Issue tracker": "https://github.com/FireHead90544/bsdotpy/issues",
      },
      author='Rudransh Joshi',
      author_email='rudranshjoshi1806@gmail.com',
      platforms='any',
      license='Apache License 2.0',
      packages=['bsdotpy'],
      zip_safe=False,
      install_requires=["requests", "bs4"])