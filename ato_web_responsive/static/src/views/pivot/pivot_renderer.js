import { patch } from "@web/core/utils/patch";
import { PivotRenderer } from "@web/views/pivot/pivot_renderer";
import { useService } from "@web/core/utils/hooks";

import { useEffect } from "@odoo/owl";

patch(PivotRenderer.prototype, {
    setup() {
        super.setup();
        this.ui = useService("ui");

        if (this.ui.isSmall) {
            useEffect(() => {
                const table = this.tableRef();
                if (table) {
                    const tooltipElems = table.querySelectorAll("*[data-tooltip]");
                    for (const el of tooltipElems) {
                        el.removeAttribute("data-tooltip");
                        el.removeAttribute("data-tooltip-position");
                    }
                }
            });
        }
    },

    getPadding(cell) {
        if (this.ui.isSmall) {
            return 5 + cell.indent * 5;
        }
        return super.getPadding(...arguments);
    },
});
