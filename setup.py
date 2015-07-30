from setuptools import setup

version = '0.2.10'


def get_requirements(suffix=''):
    with open('requirements.txt') as f:
        rv = f.read().splitlines()
    return rv


def get_long_description():
    with open('Readme.md') as f:
        rv = f.read()
    return rv

setup(version=version,
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
    long_description=get_long_description(),
    classifiers=[],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    include_package_data=True,
    keywords='',
    author='Ian Dennis Miller',
    author_email='ian@iandennismiller.com',
    url='http://flask-diamond.readthedocs.org',
    install_requires=get_requirements(),
    license='MIT',
    zip_safe=False,
)
