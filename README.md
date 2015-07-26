django-zurb-foundation 5.5.2 + rtl specific files
============================

Django Zurb Foundation 5 package.

Version of this package is equal to the version of Zurb Foundation it provides.

Usage
=====

- Add `foundation` to your `INSTALLED_APPS`.
- If you want to use the provided base template, extend from `foundation/base.html`. If you want to write one from scratch, see the example template.
- If you want to test if foundation works, include `foundation.urls` in your urls.py and visit the path. You should see the Foundation test page.

Including Foundation js/css/vendor files
=============================================

To include Foundation js file, you can use `static` tag. 

    {% static 'foundation/js/foundation.min.js' %}
    
For example, to include `abide` library use:

    `<script src="{% static 'foundation/js/foundation/foundation.abide.js' %}"></script>`

Foundation icons
================

The latest Foundation icons set is now included in this package.
The icons are not enabled by default. To enable them use something like this in your template:

    {% block css %}
        {% static 'foundation/css/foundation-icons.css' %}
    {% endblock css %}

If you have added `foundation.urls` to your urls.py visit `icons/` on that path to see them.
