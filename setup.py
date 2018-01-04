from setuptools import setup

setup(
    name='argparse-color-formatter',
    url='https://github.com/emergence/argparse-color-formatter/',
    version='1.1.1',
    description='a ``formatter_class`` for ``argparse`` that deals with ANSI colour escapes.'
                ' Specifically, this formatter does not count escape characters as displayed'
                ' characters when wrapping ``argparse``\'s help text into the terminal.',
    long_description='''
.. list-table::
   :header-rows: 1

   * - Branch
     - Build Status
     - Coverage Status
   * - master
     - .. image:: https://semaphoreci.com/api/v1/emergence/argparse-color-formatter/branches/master/shields_badge.svg
          :target: https://semaphoreci.com/emergence/argparse-color-formatter
          :alt: Build Status

     -  .. image:: https://docs.emergence.com/argparse-color-formatter/htmlcov_master/coverage.svg
           :target: https://docs.emergence.com/argparse-color-formatter/htmlcov_master/
           :alt: Coverage Status

   * - develop
     -  .. image:: https://semaphoreci.com/api/v1/emergence/argparse-color-formatter/branches/develop/shields_badge.svg
           :target: https://semaphoreci.com/emergence/argparse-color-formatter
           :alt: Build Status

     -  .. image:: https://docs.emergence.com/argparse-color-formatter/htmlcov_develop/coverage.svg
           :target: https://docs.emergence.com/argparse-color-formatter/htmlcov_develop/
           :alt: Coverage Status

Install
-------

.. code-block:: shell

   $ pip install argparse-color-formatter

Usage
-----

Pass in ``argparse_color_formatter.ColorHelpFormatter`` to a new argument parser as ``formatter_class``

.. code-block:: python

   import argparse
   from argparse_color_formatter import ColorHelpFormatter

   parser = argparse.ArgumentParser(
       formatter_class=ColorHelpFormatter
   )
    ''',
    author='Emergence by Design',
    author_email='support@emergence.com',
    py_modules=['argparse_color_formatter'],
    install_requires=[x for x in open('requirements.txt').read().split('\n') if x],
    license='LICENSE',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'License :: OSI Approved :: BSD License',
        'Environment :: Console',
        'Intended Audience :: Developers',
    ]
)
