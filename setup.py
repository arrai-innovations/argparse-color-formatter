from setuptools import setup, find_packages

setup(
    name='argparse_color_formatter',
    url='https://github.com/emergence/argparse-color-formatter/',
    version='1.0.0',
    description='a `formatter_class` for argparse that knows how to deal with color escapes.',
    author='Emergence by Design',
    author_email='support@emergence.com',
    packages=find_packages(),
    install_requires=[x for x in open('requirements.txt').read().split('\n') if x],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'License :: OSI Approved :: BSD-3-Clause',
        'Environment :: Console',
        'Environment :: Console',
    ]
)
