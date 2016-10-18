========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |requires|
        | |coveralls|
    * - package
      - |version| |downloads| |wheel| |supported-versions| |supported-implementations|

.. |docs| image:: https://readthedocs.org/projects/cwmon-system/badge/?style=flat
    :target: https://readthedocs.org/projects/cwmon-system
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/RescueTime/cwmon-system.svg?branch=develop
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/RescueTime/cwmon-system

.. |requires| image:: https://requires.io/github/RescueTime/cwmon-system/requirements.svg?branch=develop
    :alt: Requirements Status
    :target: https://requires.io/github/RescueTime/cwmon-system/requirements/?branch=develop

.. |coveralls| image:: https://coveralls.io/repos/github/RescueTime/cwmon-system/badge.svg?branch=develop
    :target: https://coveralls.io/github/RescueTime/cwmon-system?branch=develop
    :alt: Coverage Status

.. |version| image:: https://img.shields.io/pypi/v/cwmon-system.svg?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/cwmon-system

.. |downloads| image:: https://img.shields.io/pypi/dm/cwmon-system.svg?style=flat
    :alt: PyPI Package monthly downloads
    :target: https://pypi.python.org/pypi/cwmon-system

.. |wheel| image:: https://img.shields.io/pypi/wheel/cwmon-system.svg?style=flat
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/cwmon-system

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/cwmon-system.svg?style=flat
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/cwmon-system

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/cwmon-system.svg?style=flat
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/cwmon-system


.. end-badges

A cwmon_ plugin for system-level monitoring.

.. _cwmon: https://github.com/RescueTime/cwmon

* Free software: BSD license

Installation
============

::

    pip install cwmon-system

Documentation
=============

https://cwmon-system.readthedocs.io/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
