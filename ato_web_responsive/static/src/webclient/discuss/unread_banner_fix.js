/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { Thread } from "@mail/core/common/thread";

// Guard against a missing firstUnreadMessage after loadAround().
patch(Thread.prototype, {
    async onClickUnreadMessagesBanner() {
        const thread = this.props.thread;
        const separator = this.channel?.self_member_id?.new_message_separator_ui;
        if (!thread || !separator) {
            return;
        }
        await thread.loadAround({ messageId: separator });
        const message = thread.firstUnreadMessage;
        if (message) {
            await this.messageHighlight?.highlightMessage(message);
        }
    },
});
