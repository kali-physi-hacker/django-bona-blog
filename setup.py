import pathlib
from setuptools import find_packages, setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name='django-bona-blog',
    version='v1.0.0',
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    author='William Kpabitey Kwabla (fork author)',
    author_email='paawilly17@gmail.com',
    description='A Django blog app with features of a standard blogging platform.',
    long_description=README,
    long_description_content_type="text/markdown",
    license='MIT License',
    keywords='django-blogging django django-app django-blog-app django-blog ',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Framework :: Django',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    platforms=['any'],
    url='https://github.com/Williano/django-bona-blog',
    install_requires=[
        'Django>=2.2',
        'Pillow',
        'django-tinymce4-lite',
        'django-filter',
        'django-taggit',
        'djangorestframework',
    ],
    python_requires='>=3.5',
    zip_safe=False,
)
