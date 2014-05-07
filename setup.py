from distutils.core import setup

setup(
    name='decc-form',
    version='0.1',
    packages=['decc_form',],
    license='copyright NOI',
    long_description='DECC Form Submission Website',
    install_requires = [
        'Django>=1.6.1',
        'django-braces>=1.4.0',
        'django-localflavor>=1.0',
        'psycopg2>=2.5.2',
        'South>=0.8.4'
    ],
)
