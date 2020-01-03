from setuptools import setup


with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='argparse-color-formatter',
    url='https://github.com/arrai-innovations/argparse-color-formatter/',
    version='1.2.2.post2',
    description='a `formatter_class` for `argparse` that deals with ANSI colour escapes.'
                ' Specifically, this formatter does not count escape characters as displayed'
                ' characters when wrapping `argparse`\'s help text into the terminal.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Arrai Innovations',
    author_email='support@arrai.com',
    py_modules=['argparse_color_formatter'],
    install_requires=[x for x in open('requirements.txt').read().split('\n') if x],
    license='LICENSE',
    test_suite='tests',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: BSD License',
        'Environment :: Console',
        'Intended Audience :: Developers',
    ]
)
