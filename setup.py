#! /usr/bin/env python
import os
from setuptools import setup

import django_admin_sso
setup(
    name='django-admin-sso',
    version=django_admin_sso.__version__,
    description='django sso solution',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    author='Marc Egli',
    author_email='egli@allink.ch',
    url='http://github.com/frog32/django-admin-sso/',
    license='BSD License',
    platforms=['OS Independent'],
    packages=[
        'django_admin_sso',
    ],
    # package_data={'django_admin_sso':'templates/*.html'},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    requires=[
        'Django(>=1.3)',
    ],
    include_package_data=True,
)
