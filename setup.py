""" Project package description
"""

from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='stay-awake',
    version='1.0.0',
    description='A sample Python project to keep your computer awake',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/HansDaigle/stay-awake',
    author='Hans Daigle',
    author_email='me@hansdaigle.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    packages=find_packages(where='stay_awake'),
    python_requires='>=3.6, <4',
    install_requires=['pynput'],
    entry_points={  # Optional
        'console_scripts': [
            'stay-awake=stay_awake.__main__:main',
        ],
    },
    project_urls={
        'Key pressing guide': 'https://nitratine.net/blog/post/simulate-keypresses-in-python/',
    },
)
