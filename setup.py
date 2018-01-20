from setuptools import setup

with open("README.rst", "rb") as f:
    long_descr = f.read().decode('utf-8')

setup(
    name = "castctrl",
    packages = ["castctrl"],
    install_requires = ['pychromecast==0.7.9'],
    dependency_links=["git+https://github.com/balloob/pychromecast@cda7a0c5ef804f5306be845f8ccbbc57f11e0421#egg=pychromecast-0.7.9"],
    entry_points = {
        "console_scripts": ['castctrl = castctrl.castctrl:main']
        },
    version = "1.1.1",
    description = "A Python program to simplify casting video to a Chromecast",
    long_description = long_descr,
    author = "Steven Smith",
    author_email = "stevensmith.ome@gmail.com",
    license = "MIT",
    url = "https://blha303.github.io/castctrl/",
    classifiers = [
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: System Administrators",
        "Topic :: Multimedia :: Sound/Audio"
        ]
    )
