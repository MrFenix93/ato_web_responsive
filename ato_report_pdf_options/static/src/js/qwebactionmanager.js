
/** @odoo-module **/

import { registry } from "@web/core/registry";
import { PdfOptionsModal } from "./PdfOptionsModal";

function isMobileDevice() {
    return /Android|iPhone|iPad|iPod|Opera Mini|IEMobile|WPDesktop/i.test(
        navigator.userAgent
    );
}

let iframeForReport;

function getMobilePrintUrl(action) {
    const reportName = action.report_name;
    const actionContext = action.context || {};
    const ids = actionContext.active_ids
        ? actionContext.active_ids.join(",")
        : "";

    return `/report/mobile_print/${reportName}/${ids}`;
}

function printPdf(url, mobilePrintUrl, callback) {
    if (isMobileDevice()) {
        window.open(mobilePrintUrl, "_blank");
        callback();
        return;
    }

    let iframe = iframeForReport;

    if (!iframe) {
        iframe = iframeForReport = document.createElement("iframe");
        iframe.className = "pdfIframe";
        iframe.style.display = "none";
        document.body.appendChild(iframe);
    }

    iframe.onload = function () {
        setTimeout(function () {
            try {
                iframe.contentWindow.focus();
                iframe.contentWindow.print();
            } finally {
                callback();
            }
        }, 100);
    };

    iframe.onerror = function () {
        callback();
    };

    iframe.src = url;
}

function getReportUrl(action, type, userContext) {
    let url = `/report/${type}/${action.report_name}`;
    const actionContext = action.context || {};

    if (action.data && JSON.stringify(action.data) !== "{}") {
        const options = encodeURIComponent(JSON.stringify(action.data));
        const context = encodeURIComponent(JSON.stringify(actionContext));

        url += `?options=${options}&context=${context}`;
    } else {
        if (actionContext.active_ids) {
            url += `/${actionContext.active_ids.join(",")}`;
        }

        if (type === "html") {
            const context = encodeURIComponent(
                JSON.stringify(userContext || actionContext)
            );
            url += `?context=${context}`;
        }
    }

    return url;
}

registry
    .category("ir.actions.report handlers")
    .add("pdf_report_options_handler", async function (action, options, env) {
        let { default_print_option, report_type } = action;

        if (report_type !== "qweb-pdf") {
            return false;
        }

        if (default_print_option === "download") {
            return false;
        }

        if (!default_print_option) {
            let removeDialog;

            default_print_option = await new Promise((resolve) => {
                removeDialog = env.services.dialog.add(
                    PdfOptionsModal,
                    {
                        onSelectOption: (option) => resolve(option),
                    },
                    {
                        onClose: () => resolve("close"),
                    }
                );
            });

            if (removeDialog) {
                removeDialog();
            }

            if (default_print_option === "close") {
                return true;
            }

            if (default_print_option === "download") {
                return false;
            }
        }

        if (
            default_print_option !== "print" &&
            default_print_option !== "open"
        ) {
            return false;
        }

        const userContext =
            env.services.user && env.services.user.context
                ? env.services.user.context
                : action.context || {};

        const url = getReportUrl(action, "pdf", userContext);
        const mobilePrintUrl = getMobilePrintUrl(action);

        if (default_print_option === "print") {
            env.services.ui.block();

            try {
                printPdf(url, mobilePrintUrl, () => {
                    env.services.ui.unblock();
                });
            } catch (error) {
                env.services.ui.unblock();
                throw error;
            }

            return true;
        }

        if (default_print_option === "open") {
            window.open(url, "_blank");
            return true;
        }

        return false;
    });
