from distutils.command.install import INSTALL_SCHEMES
from os.path import dirname, join, abspath
from setuptools import setup
from setuptools.command.install import install


for scheme in INSTALL_SCHEMES.values():
    scheme['data'] = scheme['purelib']

setup_args = {
    'cmdclass': {'install': install},
    'name': 'selenium',
    'version': "4.17.2",
    'license': 'Apache 2.0',
    'description': 'Python bindings for Selenium',
    'long_description': open(join(abspath(dirname(__file__)), "README.rst")).read(),
    'url': 'https://github.com/SeleniumHQ/selenium/',
    'project_urls': {
        'Bug Tracker': 'https://github.com/SeleniumHQ/selenium/issues',
        'Changes': 'https://github.com/SeleniumHQ/selenium/blob/trunk/py/CHANGES',
        'Documentation': 'https://www.selenium.dev/documentation/overview/',
        'Source Code': 'https://github.com/SeleniumHQ/selenium/tree/trunk/py',
    },
    'python_requires': '~=3.8',
    'classifiers': ['Development Status :: 5 - Production/Stable',
                    'Intended Audience :: Developers',
                    'License :: OSI Approved :: Apache Software License',
                    'Operating System :: POSIX',
                    'Operating System :: Microsoft :: Windows',
                    'Operating System :: MacOS :: MacOS X',
                    'Topic :: Software Development :: Testing',
                    'Topic :: Software Development :: Libraries',
                    'Programming Language :: Python',
                    'Programming Language :: Python :: 3.8',
                    'Programming Language :: Python :: 3.9',
                    'Programming Language :: Python :: 3.10',
                    'Programming Language :: Python :: 3.11',
                    'Programming Language :: Python :: 3.12'],
    'package_dir': {
        'selenium': 'selenium',
        'selenium.common': 'selenium/common',
        'selenium.webdriver': 'selenium/webdriver',
    },
    'packages': ['selenium',
                 'selenium.common',
                 'selenium.webdriver',
                 'selenium.webdriver.chromium',
                 'selenium.webdriver.chrome',
                 'selenium.webdriver.common',
                 'selenium.webdriver.support',
                 'selenium.webdriver.firefox',
                 'selenium.webdriver.ie',
                 'selenium.webdriver.edge',
                 'selenium.webdriver.remote',
                 'selenium.webdriver.support', ],
    'include_package_data': True,
    'install_requires': [
        "typing_extensions~= 4.9",
        "urllib3[socks]>=1.26,<3",
        "trio~=0.17",
        "trio-websocket~=0.9",
        "certifi>=2021.10.8",
    ],
    'zip_safe': False
}

setup(**setup_args)