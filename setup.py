from setuptools import setup, find_namespace_packages


setup(
    name="seppl-example",
    description="Example code demonstrating the use of the seppl library.",
    url="https://github.com/waikato-datamining/seppl-example",
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Topic :: Utilities',
        'Programming Language :: Python :: 3',
    ],
    license='MIT License',
    package_dir={
        '': 'src'
    },
    packages=find_namespace_packages(where='src'),
    install_requires=[
        "seppl",
    ],
    version="0.0.1",
    author='Peter Reutemann',
    author_email='fracpete@waikato.ac.nz',
    entry_points={
        "myplugins": [
            "some-plugin=my.plugins:SomePlugin",
            "other=my.plugins:OtherPlugin",
            "dud=my.plugins:Dud",
        ],
    }
)

