
from src.os import platform
from setuptools import setup, find_packages

OS = platform()
print(OS)

requirements= [
	'beautifulsoup4==4.6.0',
	'colorama==0.3.9',
	'configparser==3.5.0',
	'mpmath==1.0.0',
	'numpy==1.13.3',
	'pathlib2==2.3.0',
	'ptyprocess==0.5.2',
	'PyAudio==0.2.11',
	'pylint==1.7.2',
	'python-dateutil==2.6.1',
	'pyttsx3==2.7',
	'regex==2017.12.12',
	'requests==2.18.4',
	'scandir==1.6',
	'six==1.11.0',
	'SpeechRecognition>=3.7.1',
	'style==1.1.0',
	'urllib3==1.22',
	'wikipedia==1.4.0',
	'youtube-dl==2017.12.14'
]


setup(

	name='Jarvis',
	version='0.1',
	description='Inspired by Iron Man',


	author='Rohan Kothapalli',
	author_git="https://github.com/rohanricky/",
	author_website="https://rohanricky.github.io/",
	author_email='rohanricky0609@gmail.com',
	project_url='https://github.com/rohanricky/Jarvis/',

	license='The MIT License 2017',


	classifiers=[

        'Development Status :: 1 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers and Users who want a digital Assistant',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
	packages=find_packages(exclude=('tests',)),
	install_requires=requirements,
	package_data={},
	data_file=[],
)
