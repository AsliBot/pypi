from setuptools import setup

setup(
    name='aslibot',
    version='0.0.1',
    description='Virtual Assistants & Chat Bot',
    long_description=open('README.md').read(),
    author='Udit Vasu',
    author_email='admin@codenirvana.in',
    license='MIT',
    url='https://github.com/aslibot/pypi',
    packages=['aslibot'],
    install_requires=[],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
    keywords="AsliBot Virtual Assistants Chat Bot",
    entry_points={
        'console_scripts': [
            'aslibot = aslibot.aslibot:main'
        ],
    }
)
