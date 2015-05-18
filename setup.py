import setuptools

from icekit import __version__

setuptools.setup(
    name='icekit',
    version=__version__,
    packages=setuptools.find_packages(),
    install_requires=[
        'coverage',
        'django-bootstrap3',
        'django-brightcove',
        'django-dynamic-fixture',
        'django-fluent-pages[flatpage,fluentpage,redirectnode]',
        'django-fluent-contents',
        'django-nose',
        'django-webtest',
        'mkdocs',
        'nose-progressive',
        'Pillow',
        'tox',
        'WebTest',
    ],
    extras_require={
        'search': ['django-haystack', ]
    }
)
