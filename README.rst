=============================
dj-contextmodels
=============================

.. image:: https://badge.fury.io/py/dj-contextmodels.svg
    :target: https://badge.fury.io/py/dj-contextmodels

.. image:: https://travis-ci.org/kverdecia/dj-contextmodels.svg?branch=master
    :target: https://travis-ci.org/kverdecia/dj-contextmodels

.. image:: https://codecov.io/gh/kverdecia/dj-contextmodels/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/kverdecia/dj-contextmodels

Abstract models to define context values

Documentation
-------------

The full documentation is at https://dj-contextmodels.readthedocs.io.

Quickstart
----------

Install dj-contextmodels::

    pip install dj-contextmodels

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'contextmodels.apps.ContextModelsConfig',
        ...
    )

Add dj-contextmodels's URL patterns:

.. code-block:: python

    from contextmodels import urls as contextmodels_urls


    urlpatterns = [
        ...
        url(r'^', include(contextmodels_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox


Development commands
---------------------

::

    pip install -r requirements_dev.txt
    invoke -l


Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
