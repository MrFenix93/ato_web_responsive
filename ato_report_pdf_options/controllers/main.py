from odoo import http
from odoo.http import request


class ReportMobilePrint(http.Controller):

    @http.route(
        '/report/mobile_print/<path:report_name>/<path:docids>',
        type='http',
        auth='user',
    )
    def mobile_print(self, report_name, docids, **kwargs):
        html_response = request.env['ir.actions.report'].sudo()._render_qweb_html(
            report_name, list(map(int, docids.split(',')))
        )
        html_content = html_response[0].decode('utf-8')

        auto_print_script = """<script>
document.addEventListener("DOMContentLoaded", function() {
    setTimeout(function() { window.print(); }, 300);
});
</script>"""

        html_content = html_content.replace('</head>', auto_print_script + '</head>', 1)

        return request.make_response(
            html_content,
            headers=[('Content-Type', 'text/html; charset=utf-8')]
        )
