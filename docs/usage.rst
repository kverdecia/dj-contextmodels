=====
Usage
=====

To use dj-contextmodels in a project, add it to your `INSTALLED_APPS`:

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
