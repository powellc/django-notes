from setuptools import setup, find_packages

setup(
    name='django-notes',
    version=__import__('notes').__version__,
    license="BSD",

    install_requires = [],

    description='A reusable applicaton to add arbitrary notes to a model.',
    long_description=open('README.md').read(),

    author='Colin Powell',
    author_email='colin@onecardinal.com',

    url='http://github.com/powellc/django-notes',
    download_url='http://github.com/powellc/django-notes/downloads',

    include_package_data=True,

    packages=['notes'],

    zip_safe=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)
