# -*- coding: utf-8 -*-
{
    "name": "PDF Report Options - Mobile Print",
    "version": "20.0.1.0.0",

    "summary": "Print, download or open PDF reports with desktop and mobile printing support",

    "description": """
PDF Report Options for Odoo 20.

Choose what to do when generating a PDF report:
- Print the report directly
- Download the PDF
- Open the PDF in a new tab
- Set a default option for each report
- Print reports from mobile devices

Originally developed by Luis Rodrigo Mejia Mateus.
Updated for Odoo 20 and enhanced with mobile printing support by ATO Solution.
    """,

    "author": "Luis Rodrigo Mejia Mateus, ATO Solution",
    "website": "https://ato-solution.com",
    "category": "Productivity",
    "license": "LGPL-3",

    "depends": [
        "web",
    ],

    "data": [
        "views/ir_actions_report.xml",
    ],

    "assets": {
        "web.assets_web": [
            "ato_report_pdf_options/static/src/js/PdfOptionsModal.js",
            "ato_report_pdf_options/static/src/js/qwebactionmanager.js",
            "ato_report_pdf_options/static/src/**/*.xml",
        ],
    },

    "images": [
        "static/description/banner.png",
    ],

    "installable": True,
    "application": False,
    "auto_install": False,
}