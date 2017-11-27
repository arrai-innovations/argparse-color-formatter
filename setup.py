from setuptools import setup

setup(
    name='argparse-color-formatter',
    url='https://github.com/emergence/argparse-color-formatter/',
    version='1.0.0',
    description='a `formatter_class` for `argparse` that deals with ANSI colour escapes.'
                ' Specifically, this formatter does not count escape characters as displayed'
                ' characters when wrapping `argparse`\'s help text into the terminal.',
    author='Emergence by Design',
    author_email='support@emergence.com',
    py_modules=['argparse_color_formatter'],
    install_requires=[x for x in open('requirements.txt').read().split('\n') if x],
    license='LICENSE',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'License :: OSI Approved :: BSD-3-Clause',
        'Environment :: Console',
        'Intended Audience :: Developers',
    ]
)
