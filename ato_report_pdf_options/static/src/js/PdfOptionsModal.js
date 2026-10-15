
/** @odoo-module **/

import { _t } from "@web/core/l10n/translation";
import { Dialog } from "@web/core/dialog/dialog";
import { Component, useProps, t } from "@odoo/owl";

export class PdfOptionsModal extends Component {
    static template = "ato_report_pdf_options.ButtonOptions";
    static components = { Dialog };

    props = useProps({
        onSelectOption: t.function(),
        close: t.function().optional(),
    });

    setup() {
        this.title = _t("What do you want to do?");
    }

    executePdfAction(option) {
        this.props.onSelectOption(option);
    }
}
