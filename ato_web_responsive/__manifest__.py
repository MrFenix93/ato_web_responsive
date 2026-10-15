# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    "name": "ATO Responsive",
    "category": "Technical",
    "version": "20.0.1.0.0",
    "depends": ["web", "base_setup"],
    "auto_install": False,
    "data": [
        "views/webclient_templates.xml",
    ],
    "assets": {
        "web._assets_primary_variables": [
            (
                "after",
                "web/static/src/scss/primary_variables.scss",
                "ato_web_responsive/static/src/**/*.variables.scss",
            ),
            (
                "before",
                "web/static/src/scss/primary_variables.scss",
                "ato_web_responsive/static/src/scss/primary_variables.scss",
            ),
        ],
        "web._assets_secondary_variables": [
            (
                "before",
                "web/static/src/scss/secondary_variables.scss",
                "ato_web_responsive/static/src/scss/secondary_variables.scss",
            ),
        ],
        "web._assets_backend_helpers": [
            (
                "before",
                "web/static/src/scss/bootstrap_overridden.scss",
                "ato_web_responsive/static/src/scss/bootstrap_overridden.scss",
            ),
        ],
        "web.assets_frontend": [
            "ato_web_responsive/static/src/webclient/home_menu/home_menu_background.scss",  # used by login page
            "ato_web_responsive/static/src/webclient/navbar/navbar.scss",
        ],
        "web.assets_backend": [
            "ato_web_responsive/static/src/webclient/**/*.scss",
            "ato_web_responsive/static/src/views/**/*.scss",
            # Don't include dark mode files in light mode
            ("remove", "ato_web_responsive/static/src/**/*.dark.scss"),
        ],
        "web.assets_backend_lazy": [
            "ato_web_responsive/static/src/views/pivot/**",
        ],
        "web.assets_backend_lazy_dark": [
            ("include", "web.dark_mode_variables"),
            # web._assets_backend_helpers
            (
                "before",
                "ato_web_responsive/static/src/scss/bootstrap_overridden.scss",
                "ato_web_responsive/static/src/scss/bootstrap_overridden.dark.scss",
            ),
            (
                "after",
                "web/static/lib/bootstrap/scss/_functions.scss",
                "ato_web_responsive/static/src/scss/bs_functions_overridden.dark.scss",
            ),
        ],
        "web.assets_web": [
            "ato_web_responsive/static/src/webclient/**/*.js",
            "ato_web_responsive/static/src/webclient/**/*.xml",
            "ato_web_responsive/static/src/views/**/*.js",
            "ato_web_responsive/static/src/views/**/*.xml",
            ("remove", "ato_web_responsive/static/src/views/pivot/**"),
            (
                "replace",
                "web/static/src/main.js",
                "ato_web_responsive/static/src/main.js",
            ),
        ],
        # ========= Dark Mode =========
        "web.dark_mode_variables": [
            # web._assets_primary_variables
            (
                "before",
                "ato_web_responsive/static/src/scss/primary_variables.scss",
                "ato_web_responsive/static/src/scss/primary_variables.dark.scss",
            ),
            (
                "before",
                "ato_web_responsive/static/src/**/*.variables.scss",
                "ato_web_responsive/static/src/**/*.variables.dark.scss",
            ),
            # web._assets_secondary_variables
            (
                "before",
                "ato_web_responsive/static/src/scss/secondary_variables.scss",
                "ato_web_responsive/static/src/scss/secondary_variables.dark.scss",
            ),
        ],
        "web.assets_web_dark": [
            ("include", "web.dark_mode_variables"),
            # web._assets_backend_helpers
            (
                "before",
                "ato_web_responsive/static/src/scss/bootstrap_overridden.scss",
                "ato_web_responsive/static/src/scss/bootstrap_overridden.dark.scss",
            ),
            (
                "after",
                "web/static/lib/bootstrap/scss/_functions.scss",
                "ato_web_responsive/static/src/scss/bs_functions_overridden.dark.scss",
            ),
            # assets_backend
            "ato_web_responsive/static/src/**/*.dark.scss",
        ],
    },
    "installable": True,
    "application": True,	
    "author": "Agga, IdeaCode Academy; ATO Solution",
    "images": ["static/description/img.png"],
    "license": "LGPL-3",
}

