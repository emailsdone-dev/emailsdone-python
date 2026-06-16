from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Dict, List

from emailsdone import EmailsDone, SendEmailResponse


@dataclass(frozen=True)
class DemoParameter:
    key: str
    label: str


@dataclass(frozen=True)
class DemoTemplate:
    group_name: str
    template_name: str
    parameters: List[DemoParameter]
    execute: Callable[[EmailsDone, Dict[str, str]], SendEmailResponse]


demo_template_registry: List[DemoTemplate] = [
    DemoTemplate(
        group_name="Authentication",
        template_name="Account Locked",
        parameters=[
            DemoParameter(key="to", label="Recipient email")
        ],
        execute=lambda emails_done, values: emails_done.authentication.account_locked(
            values["to"]
        ),
    ),
    DemoTemplate(
        group_name="Authentication",
        template_name="Email Changed",
        parameters=[
            DemoParameter(key="to", label="Recipient email")
        ],
        execute=lambda emails_done, values: emails_done.authentication.email_changed(
            values["to"]
        ),
    ),
    DemoTemplate(
        group_name="Authentication",
        template_name="Login Code",
        parameters=[
            DemoParameter(key="to", label="Recipient email"),
            DemoParameter(key="code", label="Code")
        ],
        execute=lambda emails_done, values: emails_done.authentication.login_code(
            values["to"],
            values["code"]
        ),
    ),
    DemoTemplate(
        group_name="Authentication",
        template_name="Magic Link",
        parameters=[
            DemoParameter(key="to", label="Recipient email"),
            DemoParameter(key="magic_link_url", label="Action Button URL")
        ],
        execute=lambda emails_done, values: emails_done.authentication.magic_link(
            values["to"],
            values["magic_link_url"]
        ),
    ),
    DemoTemplate(
        group_name="Authentication",
        template_name="Mfa Disabled",
        parameters=[
            DemoParameter(key="to", label="Recipient email")
        ],
        execute=lambda emails_done, values: emails_done.authentication.mfa_disabled(
            values["to"]
        ),
    ),
    DemoTemplate(
        group_name="Authentication",
        template_name="Mfa Enabled",
        parameters=[
            DemoParameter(key="to", label="Recipient email")
        ],
        execute=lambda emails_done, values: emails_done.authentication.mfa_enabled(
            values["to"]
        ),
    ),
    DemoTemplate(
        group_name="Authentication",
        template_name="New Device Login",
        parameters=[
            DemoParameter(key="to", label="Recipient email")
        ],
        execute=lambda emails_done, values: emails_done.authentication.new_device_login(
            values["to"]
        ),
    ),
    DemoTemplate(
        group_name="Authentication",
        template_name="Password Changed",
        parameters=[
            DemoParameter(key="to", label="Recipient email")
        ],
        execute=lambda emails_done, values: emails_done.authentication.password_changed(
            values["to"]
        ),
    ),
    DemoTemplate(
        group_name="Authentication",
        template_name="Password Reset",
        parameters=[
            DemoParameter(key="to", label="Recipient email"),
            DemoParameter(key="reset_url", label="Action Button URL")
        ],
        execute=lambda emails_done, values: emails_done.authentication.password_reset(
            values["to"],
            values["reset_url"]
        ),
    ),
    DemoTemplate(
        group_name="Authentication",
        template_name="Suspicious Login",
        parameters=[
            DemoParameter(key="to", label="Recipient email")
        ],
        execute=lambda emails_done, values: emails_done.authentication.suspicious_login(
            values["to"]
        ),
    ),
    DemoTemplate(
        group_name="Authentication",
        template_name="Verify Email",
        parameters=[
            DemoParameter(key="to", label="Recipient email"),
            DemoParameter(key="verification_url", label="Action Button URL")
        ],
        execute=lambda emails_done, values: emails_done.authentication.verify_email(
            values["to"],
            values["verification_url"]
        ),
    ),
    DemoTemplate(
        group_name="Authentication",
        template_name="Welcome",
        parameters=[
            DemoParameter(key="to", label="Recipient email"),
            DemoParameter(key="action_url", label="Action Button URL")
        ],
        execute=lambda emails_done, values: emails_done.authentication.welcome(
            values["to"],
            values["action_url"]
        ),
    ),
    DemoTemplate(
        group_name="Billing",
        template_name="Invoice Overdue",
        parameters=[
            DemoParameter(key="to", label="Recipient email"),
            DemoParameter(key="action_url", label="Action Button URL")
        ],
        execute=lambda emails_done, values: emails_done.billing.invoice_overdue(
            values["to"],
            values["action_url"]
        ),
    ),
    DemoTemplate(
        group_name="Billing",
        template_name="Payment Failed",
        parameters=[
            DemoParameter(key="to", label="Recipient email"),
            DemoParameter(key="action_url", label="Action Button URL")
        ],
        execute=lambda emails_done, values: emails_done.billing.payment_failed(
            values["to"],
            values["action_url"]
        ),
    ),
    DemoTemplate(
        group_name="Billing",
        template_name="Payment Succeeded",
        parameters=[
            DemoParameter(key="to", label="Recipient email")
        ],
        execute=lambda emails_done, values: emails_done.billing.payment_succeeded(
            values["to"]
        ),
    ),
    DemoTemplate(
        group_name="Billing",
        template_name="Refund Issued",
        parameters=[
            DemoParameter(key="to", label="Recipient email")
        ],
        execute=lambda emails_done, values: emails_done.billing.refund_issued(
            values["to"]
        ),
    ),
    DemoTemplate(
        group_name="Billing",
        template_name="Subscription Cancelled",
        parameters=[
            DemoParameter(key="to", label="Recipient email")
        ],
        execute=lambda emails_done, values: emails_done.billing.subscription_cancelled(
            values["to"]
        ),
    ),
    DemoTemplate(
        group_name="Billing",
        template_name="Subscription Paused",
        parameters=[
            DemoParameter(key="to", label="Recipient email")
        ],
        execute=lambda emails_done, values: emails_done.billing.subscription_paused(
            values["to"]
        ),
    ),
    DemoTemplate(
        group_name="Billing",
        template_name="Subscription Renewed",
        parameters=[
            DemoParameter(key="to", label="Recipient email")
        ],
        execute=lambda emails_done, values: emails_done.billing.subscription_renewed(
            values["to"]
        ),
    ),
    DemoTemplate(
        group_name="Billing",
        template_name="Subscription Started",
        parameters=[
            DemoParameter(key="to", label="Recipient email")
        ],
        execute=lambda emails_done, values: emails_done.billing.subscription_started(
            values["to"]
        ),
    ),
    DemoTemplate(
        group_name="Billing",
        template_name="Trial Ending",
        parameters=[
            DemoParameter(key="to", label="Recipient email"),
            DemoParameter(key="action_url", label="Action Button URL"),
            DemoParameter(key="trial_end_date", label="Trial End Date")
        ],
        execute=lambda emails_done, values: emails_done.billing.trial_ending(
            values["to"],
            values["action_url"],
            values["trial_end_date"]
        ),
    ),
    DemoTemplate(
        group_name="Billing",
        template_name="Trial Started",
        parameters=[
            DemoParameter(key="to", label="Recipient email")
        ],
        execute=lambda emails_done, values: emails_done.billing.trial_started(
            values["to"]
        ),
    ),
    DemoTemplate(
        group_name="Billing",
        template_name="Usage Threshold",
        parameters=[
            DemoParameter(key="to", label="Recipient email"),
            DemoParameter(key="message", label="Message")
        ],
        execute=lambda emails_done, values: emails_done.billing.usage_threshold(
            values["to"],
            values["message"]
        ),
    ),
    DemoTemplate(
        group_name="Developer",
        template_name="Api Key Created",
        parameters=[
            DemoParameter(key="to", label="Recipient email")
        ],
        execute=lambda emails_done, values: emails_done.developer.api_key_created(
            values["to"]
        ),
    ),
    DemoTemplate(
        group_name="Developer",
        template_name="Api Key Rotated",
        parameters=[
            DemoParameter(key="to", label="Recipient email")
        ],
        execute=lambda emails_done, values: emails_done.developer.api_key_rotated(
            values["to"]
        ),
    ),
    DemoTemplate(
        group_name="Developer",
        template_name="Credits Exhausted",
        parameters=[
            DemoParameter(key="to", label="Recipient email"),
            DemoParameter(key="action_url", label="Action Button URL")
        ],
        execute=lambda emails_done, values: emails_done.developer.credits_exhausted(
            values["to"],
            values["action_url"]
        ),
    ),
    DemoTemplate(
        group_name="Developer",
        template_name="Credits Low",
        parameters=[
            DemoParameter(key="to", label="Recipient email")
        ],
        execute=lambda emails_done, values: emails_done.developer.credits_low(
            values["to"]
        ),
    ),
    DemoTemplate(
        group_name="Notifications",
        template_name="Announcement",
        parameters=[
            DemoParameter(key="to", label="Recipient email"),
            DemoParameter(key="message", label="Message")
        ],
        execute=lambda emails_done, values: emails_done.notifications.announcement(
            values["to"],
            values["message"]
        ),
    ),
    DemoTemplate(
        group_name="Notifications",
        template_name="Approval Approved",
        parameters=[
            DemoParameter(key="to", label="Recipient email"),
            DemoParameter(key="message", label="Message")
        ],
        execute=lambda emails_done, values: emails_done.notifications.approval_approved(
            values["to"],
            values["message"]
        ),
    ),
    DemoTemplate(
        group_name="Notifications",
        template_name="Approval Needed",
        parameters=[
            DemoParameter(key="to", label="Recipient email"),
            DemoParameter(key="action_url", label="Action Button URL")
        ],
        execute=lambda emails_done, values: emails_done.notifications.approval_needed(
            values["to"],
            values["action_url"]
        ),
    ),
    DemoTemplate(
        group_name="Notifications",
        template_name="Approval Rejected",
        parameters=[
            DemoParameter(key="to", label="Recipient email"),
            DemoParameter(key="message", label="Message")
        ],
        execute=lambda emails_done, values: emails_done.notifications.approval_rejected(
            values["to"],
            values["message"]
        ),
    ),
    DemoTemplate(
        group_name="Notifications",
        template_name="Digest",
        parameters=[
            DemoParameter(key="to", label="Recipient email")
        ],
        execute=lambda emails_done, values: emails_done.notifications.digest(
            values["to"]
        ),
    ),
    DemoTemplate(
        group_name="Notifications",
        template_name="Export Ready",
        parameters=[
            DemoParameter(key="to", label="Recipient email"),
            DemoParameter(key="action_url", label="Action Button URL")
        ],
        execute=lambda emails_done, values: emails_done.notifications.export_ready(
            values["to"],
            values["action_url"]
        ),
    ),
    DemoTemplate(
        group_name="Notifications",
        template_name="Generation Complete",
        parameters=[
            DemoParameter(key="to", label="Recipient email"),
            DemoParameter(key="action_url", label="Action Button URL")
        ],
        execute=lambda emails_done, values: emails_done.notifications.generation_complete(
            values["to"],
            values["action_url"]
        ),
    ),
    DemoTemplate(
        group_name="Notifications",
        template_name="Import Complete",
        parameters=[
            DemoParameter(key="to", label="Recipient email")
        ],
        execute=lambda emails_done, values: emails_done.notifications.import_complete(
            values["to"]
        ),
    ),
    DemoTemplate(
        group_name="Notifications",
        template_name="Job Complete",
        parameters=[
            DemoParameter(key="to", label="Recipient email")
        ],
        execute=lambda emails_done, values: emails_done.notifications.job_complete(
            values["to"]
        ),
    ),
    DemoTemplate(
        group_name="Notifications",
        template_name="Notification Alert",
        parameters=[
            DemoParameter(key="to", label="Recipient email"),
            DemoParameter(key="message", label="Message")
        ],
        execute=lambda emails_done, values: emails_done.notifications.notification_alert(
            values["to"],
            values["message"]
        ),
    ),
    DemoTemplate(
        group_name="Notifications",
        template_name="Notification Info",
        parameters=[
            DemoParameter(key="to", label="Recipient email"),
            DemoParameter(key="message", label="Message")
        ],
        execute=lambda emails_done, values: emails_done.notifications.notification_info(
            values["to"],
            values["message"]
        ),
    ),
    DemoTemplate(
        group_name="Notifications",
        template_name="Notification Success",
        parameters=[
            DemoParameter(key="to", label="Recipient email"),
            DemoParameter(key="message", label="Message")
        ],
        execute=lambda emails_done, values: emails_done.notifications.notification_success(
            values["to"],
            values["message"]
        ),
    ),
    DemoTemplate(
        group_name="Notifications",
        template_name="Notification Warning",
        parameters=[
            DemoParameter(key="to", label="Recipient email"),
            DemoParameter(key="message", label="Message")
        ],
        execute=lambda emails_done, values: emails_done.notifications.notification_warning(
            values["to"],
            values["message"]
        ),
    ),
    DemoTemplate(
        group_name="Notifications",
        template_name="Processing Failed",
        parameters=[
            DemoParameter(key="to", label="Recipient email")
        ],
        execute=lambda emails_done, values: emails_done.notifications.processing_failed(
            values["to"]
        ),
    ),
    DemoTemplate(
        group_name="Notifications",
        template_name="Queued Request Ready",
        parameters=[
            DemoParameter(key="to", label="Recipient email"),
            DemoParameter(key="action_url", label="Action Button URL")
        ],
        execute=lambda emails_done, values: emails_done.notifications.queued_request_ready(
            values["to"],
            values["action_url"]
        ),
    ),
    DemoTemplate(
        group_name="Notifications",
        template_name="Reminder",
        parameters=[
            DemoParameter(key="to", label="Recipient email"),
            DemoParameter(key="message", label="Message")
        ],
        execute=lambda emails_done, values: emails_done.notifications.reminder(
            values["to"],
            values["message"]
        ),
    ),
    DemoTemplate(
        group_name="Notifications",
        template_name="Report Ready",
        parameters=[
            DemoParameter(key="to", label="Recipient email"),
            DemoParameter(key="action_url", label="Action Button URL")
        ],
        execute=lambda emails_done, values: emails_done.notifications.report_ready(
            values["to"],
            values["action_url"]
        ),
    ),
    DemoTemplate(
        group_name="Notifications",
        template_name="Upload Complete",
        parameters=[
            DemoParameter(key="to", label="Recipient email")
        ],
        execute=lambda emails_done, values: emails_done.notifications.upload_complete(
            values["to"]
        ),
    ),
    DemoTemplate(
        group_name="Team",
        template_name="Invitation Accepted",
        parameters=[
            DemoParameter(key="to", label="Recipient email")
        ],
        execute=lambda emails_done, values: emails_done.team.invitation_accepted(
            values["to"]
        ),
    ),
    DemoTemplate(
        group_name="Team",
        template_name="Invited To Workspace",
        parameters=[
            DemoParameter(key="to", label="Recipient email"),
            DemoParameter(key="action_url", label="Action Button URL")
        ],
        execute=lambda emails_done, values: emails_done.team.invited_to_workspace(
            values["to"],
            values["action_url"]
        ),
    ),
    DemoTemplate(
        group_name="Team",
        template_name="Role Changed",
        parameters=[
            DemoParameter(key="to", label="Recipient email")
        ],
        execute=lambda emails_done, values: emails_done.team.role_changed(
            values["to"]
        ),
    ),
    DemoTemplate(
        group_name="Team",
        template_name="Team Member Added",
        parameters=[
            DemoParameter(key="to", label="Recipient email")
        ],
        execute=lambda emails_done, values: emails_done.team.team_member_added(
            values["to"]
        ),
    ),
    DemoTemplate(
        group_name="Team",
        template_name="Team Member Removed",
        parameters=[
            DemoParameter(key="to", label="Recipient email")
        ],
        execute=lambda emails_done, values: emails_done.team.team_member_removed(
            values["to"]
        ),
    )
]
