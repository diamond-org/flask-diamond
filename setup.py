import re
import os
from setuptools import setup


# mimicking flask-admin setup.py
# https://github.com/flask-admin/flask-admin/blob/master/setup.py
def fpath(name):
    return os.path.join(os.path.dirname(__file__), name)


def read(fname):
    return open(fpath(fname)).read()


file_text = read(fpath('flask_diamond/__init__.py'))


def grep(attrname):
    pattern = r"{0}\W*=\W*'([^']+)'".format(attrname)
    strval, = re.findall(pattern, file_text)
    return strval


setup(
    version=grep('__version__'),
    name='Flask-Diamond',
    description="""\
        Flask-Diamond provides a path that can guide your thought and development.
        Flask-Diamond is the road that leads to other ideas.
        """,
    packages=[
        "flask_diamond",
        "flask_diamond.models",
        "flask_diamond.views",
        "flask_diamond.views.diamond",
        "flask_diamond.utils",
    ],
    scripts=[
        "bin/diamond-scaffold.sh",
    ],
    long_description=read('Readme.rst'),
    classifiers=[],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    include_package_data=True,
    keywords='',
    author=grep('__author__'),
    author_email=grep('__email__'),
    url='http://flask-diamond.readthedocs.org',
    install_requires=read('requirements.txt'),
    license='MIT',
    zip_safe=False,
)
