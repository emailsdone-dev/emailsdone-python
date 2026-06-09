from __future__ import annotations

from typing import Any, Dict, Optional


class SendTemplates:
    def __init__(self, client: Any) -> None:
        self.authentication = AuthenticationTemplates(client)
        self.billing = BillingTemplates(client)
        self.developer = DeveloperTemplates(client)
        self.notification = NotificationTemplates(client)
        self.team = TeamTemplates(client)


class AuthenticationTemplates:
    def __init__(self, client: Any) -> None:
        self._client = client

    def account_locked(
        self,
        to: str,
        *,
        action_button_label: Any = None,
        action_button_url: Any = None,
        heading: Any = None,
        intro: Any = None,
        lock_details_locked_at: Any = None,
        lock_details_reason: Any = None,
        notice: Any = None,
        preheader: Any = None,
        subject: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ):
        _require_recipient(to)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "actionButton.url", action_button_url)
        _set_nested(data, "heading", heading)
        _set_nested(data, "intro", intro)
        _set_nested(data, "lockDetails.lockedAt", lock_details_locked_at)
        _set_nested(data, "lockDetails.reason", lock_details_reason)
        _set_nested(data, "notice", notice)
        _set_nested(data, "preheader", preheader)
        _set_nested(data, "subject", subject)

        return self._client._send_template(
            "account-locked",
            to,
            data,
            template_version=template_version,
            from_email=from_email,
            from_name=from_name,
            reply_to=reply_to,
            idempotency_key=idempotency_key,
            timeout=timeout,
        )

    def email_changed(
        self,
        to: str,
        *,
        action_button_label: Any = None,
        action_button_url: Any = None,
        change_details_changed_at: Any = None,
        change_details_new_email: Any = None,
        change_details_old_email: Any = None,
        footer_note: Any = None,
        heading: Any = None,
        intro: Any = None,
        preheader: Any = None,
        subject: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ):
        _require_recipient(to)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "actionButton.url", action_button_url)
        _set_nested(data, "changeDetails.changedAt", change_details_changed_at)
        _set_nested(data, "changeDetails.newEmail", change_details_new_email)
        _set_nested(data, "changeDetails.oldEmail", change_details_old_email)
        _set_nested(data, "footerNote", footer_note)
        _set_nested(data, "heading", heading)
        _set_nested(data, "intro", intro)
        _set_nested(data, "preheader", preheader)
        _set_nested(data, "subject", subject)

        return self._client._send_template(
            "email-changed",
            to,
            data,
            template_version=template_version,
            from_email=from_email,
            from_name=from_name,
            reply_to=reply_to,
            idempotency_key=idempotency_key,
            timeout=timeout,
        )

    def login_code(
        self,
        to: str,
        code: Any,
        *,
        footer_note: Any = None,
        heading: Any = None,
        intro: Any = None,
        preheader: Any = None,
        security_note: Any = None,
        subject: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ):
        _require_recipient(to)
        _require_value("code", code)
        data: Dict[str, Any] = {}
        _set_nested(data, "code", code)
        _set_nested(data, "footerNote", footer_note)
        _set_nested(data, "heading", heading)
        _set_nested(data, "intro", intro)
        _set_nested(data, "preheader", preheader)
        _set_nested(data, "securityNote", security_note)
        _set_nested(data, "subject", subject)

        return self._client._send_template(
            "login-code",
            to,
            data,
            template_version=template_version,
            from_email=from_email,
            from_name=from_name,
            reply_to=reply_to,
            idempotency_key=idempotency_key,
            timeout=timeout,
        )

    def magic_link(
        self,
        to: str,
        action_button_url: Any,
        *,
        action_button_label: Any = None,
        footer_note: Any = None,
        heading: Any = None,
        intro: Any = None,
        preheader: Any = None,
        subject: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ):
        _require_recipient(to)
        _require_value("action_button_url", action_button_url)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.url", action_button_url)
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "footerNote", footer_note)
        _set_nested(data, "heading", heading)
        _set_nested(data, "intro", intro)
        _set_nested(data, "preheader", preheader)
        _set_nested(data, "subject", subject)

        return self._client._send_template(
            "magic-link",
            to,
            data,
            template_version=template_version,
            from_email=from_email,
            from_name=from_name,
            reply_to=reply_to,
            idempotency_key=idempotency_key,
            timeout=timeout,
        )

    def mfa_disabled(
        self,
        to: str,
        *,
        action_button_label: Any = None,
        action_button_url: Any = None,
        footer_note: Any = None,
        heading: Any = None,
        intro: Any = None,
        notice: Any = None,
        preheader: Any = None,
        security_details_country: Any = None,
        security_details_device: Any = None,
        security_details_disabled_at: Any = None,
        security_details_ip: Any = None,
        subject: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ):
        _require_recipient(to)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "actionButton.url", action_button_url)
        _set_nested(data, "footerNote", footer_note)
        _set_nested(data, "heading", heading)
        _set_nested(data, "intro", intro)
        _set_nested(data, "notice", notice)
        _set_nested(data, "preheader", preheader)
        _set_nested(data, "securityDetails.country", security_details_country)
        _set_nested(data, "securityDetails.device", security_details_device)
        _set_nested(data, "securityDetails.disabledAt", security_details_disabled_at)
        _set_nested(data, "securityDetails.ip", security_details_ip)
        _set_nested(data, "subject", subject)

        return self._client._send_template(
            "mfa-disabled",
            to,
            data,
            template_version=template_version,
            from_email=from_email,
            from_name=from_name,
            reply_to=reply_to,
            idempotency_key=idempotency_key,
            timeout=timeout,
        )

    def mfa_enabled(
        self,
        to: str,
        *,
        action_button_label: Any = None,
        action_button_url: Any = None,
        footer_note: Any = None,
        heading: Any = None,
        intro: Any = None,
        notice: Any = None,
        preheader: Any = None,
        security_details_device: Any = None,
        security_details_enabled_at: Any = None,
        security_details_method: Any = None,
        subject: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ):
        _require_recipient(to)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "actionButton.url", action_button_url)
        _set_nested(data, "footerNote", footer_note)
        _set_nested(data, "heading", heading)
        _set_nested(data, "intro", intro)
        _set_nested(data, "notice", notice)
        _set_nested(data, "preheader", preheader)
        _set_nested(data, "securityDetails.device", security_details_device)
        _set_nested(data, "securityDetails.enabledAt", security_details_enabled_at)
        _set_nested(data, "securityDetails.method", security_details_method)
        _set_nested(data, "subject", subject)

        return self._client._send_template(
            "mfa-enabled",
            to,
            data,
            template_version=template_version,
            from_email=from_email,
            from_name=from_name,
            reply_to=reply_to,
            idempotency_key=idempotency_key,
            timeout=timeout,
        )

    def new_device_login(
        self,
        to: str,
        *,
        action_button_label: Any = None,
        action_button_url: Any = None,
        footer_note: Any = None,
        heading: Any = None,
        intro: Any = None,
        login_details_country: Any = None,
        login_details_device: Any = None,
        login_details_ip: Any = None,
        login_details_signed_in_at: Any = None,
        preheader: Any = None,
        subject: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ):
        _require_recipient(to)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "actionButton.url", action_button_url)
        _set_nested(data, "footerNote", footer_note)
        _set_nested(data, "heading", heading)
        _set_nested(data, "intro", intro)
        _set_nested(data, "loginDetails.country", login_details_country)
        _set_nested(data, "loginDetails.device", login_details_device)
        _set_nested(data, "loginDetails.ip", login_details_ip)
        _set_nested(data, "loginDetails.signedInAt", login_details_signed_in_at)
        _set_nested(data, "preheader", preheader)
        _set_nested(data, "subject", subject)

        return self._client._send_template(
            "new-device-login",
            to,
            data,
            template_version=template_version,
            from_email=from_email,
            from_name=from_name,
            reply_to=reply_to,
            idempotency_key=idempotency_key,
            timeout=timeout,
        )

    def password_changed(
        self,
        to: str,
        *,
        action_button_label: Any = None,
        action_button_url: Any = None,
        change_details_changed_at: Any = None,
        change_details_country: Any = None,
        change_details_device: Any = None,
        change_details_ip: Any = None,
        footer_note: Any = None,
        heading: Any = None,
        intro: Any = None,
        preheader: Any = None,
        subject: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ):
        _require_recipient(to)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "actionButton.url", action_button_url)
        _set_nested(data, "changeDetails.changedAt", change_details_changed_at)
        _set_nested(data, "changeDetails.country", change_details_country)
        _set_nested(data, "changeDetails.device", change_details_device)
        _set_nested(data, "changeDetails.ip", change_details_ip)
        _set_nested(data, "footerNote", footer_note)
        _set_nested(data, "heading", heading)
        _set_nested(data, "intro", intro)
        _set_nested(data, "preheader", preheader)
        _set_nested(data, "subject", subject)

        return self._client._send_template(
            "password-changed",
            to,
            data,
            template_version=template_version,
            from_email=from_email,
            from_name=from_name,
            reply_to=reply_to,
            idempotency_key=idempotency_key,
            timeout=timeout,
        )

    def password_reset(
        self,
        to: str,
        action_button_url: Any,
        *,
        action_button_label: Any = None,
        footer_note: Any = None,
        heading: Any = None,
        intro: Any = None,
        preheader: Any = None,
        request_details_country: Any = None,
        request_details_device: Any = None,
        request_details_ip: Any = None,
        request_details_requested_at: Any = None,
        security_note: Any = None,
        subject: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ):
        _require_recipient(to)
        _require_value("action_button_url", action_button_url)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.url", action_button_url)
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "footerNote", footer_note)
        _set_nested(data, "heading", heading)
        _set_nested(data, "intro", intro)
        _set_nested(data, "preheader", preheader)
        _set_nested(data, "requestDetails.country", request_details_country)
        _set_nested(data, "requestDetails.device", request_details_device)
        _set_nested(data, "requestDetails.ip", request_details_ip)
        _set_nested(data, "requestDetails.requestedAt", request_details_requested_at)
        _set_nested(data, "securityNote", security_note)
        _set_nested(data, "subject", subject)

        return self._client._send_template(
            "password-reset",
            to,
            data,
            template_version=template_version,
            from_email=from_email,
            from_name=from_name,
            reply_to=reply_to,
            idempotency_key=idempotency_key,
            timeout=timeout,
        )

    def suspicious_login(
        self,
        to: str,
        *,
        action_button_label: Any = None,
        action_button_url: Any = None,
        heading: Any = None,
        intro: Any = None,
        login_details_attempted_at: Any = None,
        login_details_country: Any = None,
        login_details_device: Any = None,
        login_details_ip: Any = None,
        notice: Any = None,
        preheader: Any = None,
        subject: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ):
        _require_recipient(to)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "actionButton.url", action_button_url)
        _set_nested(data, "heading", heading)
        _set_nested(data, "intro", intro)
        _set_nested(data, "loginDetails.attemptedAt", login_details_attempted_at)
        _set_nested(data, "loginDetails.country", login_details_country)
        _set_nested(data, "loginDetails.device", login_details_device)
        _set_nested(data, "loginDetails.ip", login_details_ip)
        _set_nested(data, "notice", notice)
        _set_nested(data, "preheader", preheader)
        _set_nested(data, "subject", subject)

        return self._client._send_template(
            "suspicious-login",
            to,
            data,
            template_version=template_version,
            from_email=from_email,
            from_name=from_name,
            reply_to=reply_to,
            idempotency_key=idempotency_key,
            timeout=timeout,
        )

    def verify_email(
        self,
        to: str,
        action_button_url: Any,
        *,
        action_button_label: Any = None,
        footer_note: Any = None,
        heading: Any = None,
        intro: Any = None,
        preheader: Any = None,
        security_note: Any = None,
        subject: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ):
        _require_recipient(to)
        _require_value("action_button_url", action_button_url)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.url", action_button_url)
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "footerNote", footer_note)
        _set_nested(data, "heading", heading)
        _set_nested(data, "intro", intro)
        _set_nested(data, "preheader", preheader)
        _set_nested(data, "securityNote", security_note)
        _set_nested(data, "subject", subject)

        return self._client._send_template(
            "verify-email",
            to,
            data,
            template_version=template_version,
            from_email=from_email,
            from_name=from_name,
            reply_to=reply_to,
            idempotency_key=idempotency_key,
            timeout=timeout,
        )

    def welcome(
        self,
        to: str,
        action_button_url: Any,
        *,
        action_button_label: Any = None,
        call_to_action_heading: Any = None,
        call_to_action_paragraph: Any = None,
        heading: Any = None,
        intro: Any = None,
        preheader: Any = None,
        subject: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ):
        _require_recipient(to)
        _require_value("action_button_url", action_button_url)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.url", action_button_url)
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "callToActionHeading", call_to_action_heading)
        _set_nested(data, "callToActionParagraph", call_to_action_paragraph)
        _set_nested(data, "heading", heading)
        _set_nested(data, "intro", intro)
        _set_nested(data, "preheader", preheader)
        _set_nested(data, "subject", subject)

        return self._client._send_template(
            "welcome",
            to,
            data,
            template_version=template_version,
            from_email=from_email,
            from_name=from_name,
            reply_to=reply_to,
            idempotency_key=idempotency_key,
            timeout=timeout,
        )

class BillingTemplates:
    def __init__(self, client: Any) -> None:
        self._client = client

    def credits_exhausted(
        self,
        to: str,
        action_button_url: Any,
        *,
        action_button_label: Any = None,
        credit_details_period_ends_at: Any = None,
        credit_details_remaining: Any = None,
        credit_details_used: Any = None,
        heading: Any = None,
        intro: Any = None,
        preheader: Any = None,
        subject: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ):
        _require_recipient(to)
        _require_value("action_button_url", action_button_url)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.url", action_button_url)
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "creditDetails.periodEndsAt", credit_details_period_ends_at)
        _set_nested(data, "creditDetails.remaining", credit_details_remaining)
        _set_nested(data, "creditDetails.used", credit_details_used)
        _set_nested(data, "heading", heading)
        _set_nested(data, "intro", intro)
        _set_nested(data, "preheader", preheader)
        _set_nested(data, "subject", subject)

        return self._client._send_template(
            "credits-exhausted",
            to,
            data,
            template_version=template_version,
            from_email=from_email,
            from_name=from_name,
            reply_to=reply_to,
            idempotency_key=idempotency_key,
            timeout=timeout,
        )

    def credits_low(
        self,
        to: str,
        *,
        action_button_label: Any = None,
        action_button_url: Any = None,
        credit_details_period_ends_at: Any = None,
        credit_details_remaining: Any = None,
        credit_details_threshold: Any = None,
        heading: Any = None,
        intro: Any = None,
        preheader: Any = None,
        subject: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ):
        _require_recipient(to)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "actionButton.url", action_button_url)
        _set_nested(data, "creditDetails.periodEndsAt", credit_details_period_ends_at)
        _set_nested(data, "creditDetails.remaining", credit_details_remaining)
        _set_nested(data, "creditDetails.threshold", credit_details_threshold)
        _set_nested(data, "heading", heading)
        _set_nested(data, "intro", intro)
        _set_nested(data, "preheader", preheader)
        _set_nested(data, "subject", subject)

        return self._client._send_template(
            "credits-low",
            to,
            data,
            template_version=template_version,
            from_email=from_email,
            from_name=from_name,
            reply_to=reply_to,
            idempotency_key=idempotency_key,
            timeout=timeout,
        )

    def invoice(
        self,
        to: str,
        invoice: Any,
        invoice_number: Any,
        *,
        action_button_label: Any = None,
        action_button_url: Any = None,
        heading: Any = None,
        intro: Any = None,
        preheader: Any = None,
        subject: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ):
        _require_recipient(to)
        _require_value("invoice", invoice)
        _require_value("invoice_number", invoice_number)
        data: Dict[str, Any] = {}
        _set_nested(data, "invoice", invoice)
        _set_nested(data, "invoiceNumber", invoice_number)
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "actionButton.url", action_button_url)
        _set_nested(data, "heading", heading)
        _set_nested(data, "intro", intro)
        _set_nested(data, "preheader", preheader)
        _set_nested(data, "subject", subject)

        return self._client._send_template(
            "invoice",
            to,
            data,
            template_version=template_version,
            from_email=from_email,
            from_name=from_name,
            reply_to=reply_to,
            idempotency_key=idempotency_key,
            timeout=timeout,
        )

    def invoice_overdue(
        self,
        to: str,
        action_button_url: Any,
        *,
        action_button_label: Any = None,
        heading: Any = None,
        intro: Any = None,
        invoice_details_amount: Any = None,
        invoice_details_days_overdue: Any = None,
        invoice_details_due_date: Any = None,
        invoice_details_invoice_number: Any = None,
        preheader: Any = None,
        subject: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ):
        _require_recipient(to)
        _require_value("action_button_url", action_button_url)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.url", action_button_url)
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "heading", heading)
        _set_nested(data, "intro", intro)
        _set_nested(data, "invoiceDetails.amount", invoice_details_amount)
        _set_nested(data, "invoiceDetails.daysOverdue", invoice_details_days_overdue)
        _set_nested(data, "invoiceDetails.dueDate", invoice_details_due_date)
        _set_nested(data, "invoiceDetails.invoiceNumber", invoice_details_invoice_number)
        _set_nested(data, "preheader", preheader)
        _set_nested(data, "subject", subject)

        return self._client._send_template(
            "invoice-overdue",
            to,
            data,
            template_version=template_version,
            from_email=from_email,
            from_name=from_name,
            reply_to=reply_to,
            idempotency_key=idempotency_key,
            timeout=timeout,
        )

    def payment_failed(
        self,
        to: str,
        action_button_url: Any,
        *,
        action_button_label: Any = None,
        action_note: Any = None,
        footer_note: Any = None,
        heading: Any = None,
        intro: Any = None,
        payment_details_amount: Any = None,
        payment_details_due_date: Any = None,
        payment_details_payment_method: Any = None,
        payment_details_reason: Any = None,
        preheader: Any = None,
        subject: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ):
        _require_recipient(to)
        _require_value("action_button_url", action_button_url)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.url", action_button_url)
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "actionNote", action_note)
        _set_nested(data, "footerNote", footer_note)
        _set_nested(data, "heading", heading)
        _set_nested(data, "intro", intro)
        _set_nested(data, "paymentDetails.amount", payment_details_amount)
        _set_nested(data, "paymentDetails.dueDate", payment_details_due_date)
        _set_nested(data, "paymentDetails.paymentMethod", payment_details_payment_method)
        _set_nested(data, "paymentDetails.reason", payment_details_reason)
        _set_nested(data, "preheader", preheader)
        _set_nested(data, "subject", subject)

        return self._client._send_template(
            "payment-failed",
            to,
            data,
            template_version=template_version,
            from_email=from_email,
            from_name=from_name,
            reply_to=reply_to,
            idempotency_key=idempotency_key,
            timeout=timeout,
        )

    def payment_succeeded(
        self,
        to: str,
        *,
        action_button_label: Any = None,
        action_button_url: Any = None,
        heading: Any = None,
        intro: Any = None,
        payment_details_amount: Any = None,
        payment_details_paid_at: Any = None,
        payment_details_payment_method: Any = None,
        payment_details_reference: Any = None,
        preheader: Any = None,
        subject: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ):
        _require_recipient(to)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "actionButton.url", action_button_url)
        _set_nested(data, "heading", heading)
        _set_nested(data, "intro", intro)
        _set_nested(data, "paymentDetails.amount", payment_details_amount)
        _set_nested(data, "paymentDetails.paidAt", payment_details_paid_at)
        _set_nested(data, "paymentDetails.paymentMethod", payment_details_payment_method)
        _set_nested(data, "paymentDetails.reference", payment_details_reference)
        _set_nested(data, "preheader", preheader)
        _set_nested(data, "subject", subject)

        return self._client._send_template(
            "payment-succeeded",
            to,
            data,
            template_version=template_version,
            from_email=from_email,
            from_name=from_name,
            reply_to=reply_to,
            idempotency_key=idempotency_key,
            timeout=timeout,
        )

    def refund_issued(
        self,
        to: str,
        *,
        footer_note: Any = None,
        heading: Any = None,
        intro: Any = None,
        preheader: Any = None,
        refund_details_amount: Any = None,
        refund_details_issued_at: Any = None,
        refund_details_payment_method: Any = None,
        refund_details_reference: Any = None,
        subject: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ):
        _require_recipient(to)
        data: Dict[str, Any] = {}
        _set_nested(data, "footerNote", footer_note)
        _set_nested(data, "heading", heading)
        _set_nested(data, "intro", intro)
        _set_nested(data, "preheader", preheader)
        _set_nested(data, "refundDetails.amount", refund_details_amount)
        _set_nested(data, "refundDetails.issuedAt", refund_details_issued_at)
        _set_nested(data, "refundDetails.paymentMethod", refund_details_payment_method)
        _set_nested(data, "refundDetails.reference", refund_details_reference)
        _set_nested(data, "subject", subject)

        return self._client._send_template(
            "refund-issued",
            to,
            data,
            template_version=template_version,
            from_email=from_email,
            from_name=from_name,
            reply_to=reply_to,
            idempotency_key=idempotency_key,
            timeout=timeout,
        )

    def subscription_cancelled(
        self,
        to: str,
        *,
        action_button_label: Any = None,
        action_button_url: Any = None,
        heading: Any = None,
        intro: Any = None,
        preheader: Any = None,
        subject: Any = None,
        subscription_details_access_ends_at: Any = None,
        subscription_details_cancelled_at: Any = None,
        subscription_details_plan: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ):
        _require_recipient(to)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "actionButton.url", action_button_url)
        _set_nested(data, "heading", heading)
        _set_nested(data, "intro", intro)
        _set_nested(data, "preheader", preheader)
        _set_nested(data, "subject", subject)
        _set_nested(data, "subscriptionDetails.accessEndsAt", subscription_details_access_ends_at)
        _set_nested(data, "subscriptionDetails.cancelledAt", subscription_details_cancelled_at)
        _set_nested(data, "subscriptionDetails.plan", subscription_details_plan)

        return self._client._send_template(
            "subscription-cancelled",
            to,
            data,
            template_version=template_version,
            from_email=from_email,
            from_name=from_name,
            reply_to=reply_to,
            idempotency_key=idempotency_key,
            timeout=timeout,
        )

    def subscription_paused(
        self,
        to: str,
        *,
        action_button_label: Any = None,
        action_button_url: Any = None,
        heading: Any = None,
        intro: Any = None,
        preheader: Any = None,
        subject: Any = None,
        subscription_details_paused_at: Any = None,
        subscription_details_plan: Any = None,
        subscription_details_resumes_at: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ):
        _require_recipient(to)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "actionButton.url", action_button_url)
        _set_nested(data, "heading", heading)
        _set_nested(data, "intro", intro)
        _set_nested(data, "preheader", preheader)
        _set_nested(data, "subject", subject)
        _set_nested(data, "subscriptionDetails.pausedAt", subscription_details_paused_at)
        _set_nested(data, "subscriptionDetails.plan", subscription_details_plan)
        _set_nested(data, "subscriptionDetails.resumesAt", subscription_details_resumes_at)

        return self._client._send_template(
            "subscription-paused",
            to,
            data,
            template_version=template_version,
            from_email=from_email,
            from_name=from_name,
            reply_to=reply_to,
            idempotency_key=idempotency_key,
            timeout=timeout,
        )

    def subscription_renewed(
        self,
        to: str,
        *,
        action_button_label: Any = None,
        action_button_url: Any = None,
        heading: Any = None,
        intro: Any = None,
        preheader: Any = None,
        subject: Any = None,
        subscription_details_amount: Any = None,
        subscription_details_next_renewal_at: Any = None,
        subscription_details_plan: Any = None,
        subscription_details_renewed_at: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ):
        _require_recipient(to)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "actionButton.url", action_button_url)
        _set_nested(data, "heading", heading)
        _set_nested(data, "intro", intro)
        _set_nested(data, "preheader", preheader)
        _set_nested(data, "subject", subject)
        _set_nested(data, "subscriptionDetails.amount", subscription_details_amount)
        _set_nested(data, "subscriptionDetails.nextRenewalAt", subscription_details_next_renewal_at)
        _set_nested(data, "subscriptionDetails.plan", subscription_details_plan)
        _set_nested(data, "subscriptionDetails.renewedAt", subscription_details_renewed_at)

        return self._client._send_template(
            "subscription-renewed",
            to,
            data,
            template_version=template_version,
            from_email=from_email,
            from_name=from_name,
            reply_to=reply_to,
            idempotency_key=idempotency_key,
            timeout=timeout,
        )

    def subscription_started(
        self,
        to: str,
        *,
        action_button_label: Any = None,
        action_button_url: Any = None,
        heading: Any = None,
        intro: Any = None,
        preheader: Any = None,
        subject: Any = None,
        subscription_details_amount: Any = None,
        subscription_details_plan: Any = None,
        subscription_details_renews_at: Any = None,
        subscription_details_started_at: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ):
        _require_recipient(to)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "actionButton.url", action_button_url)
        _set_nested(data, "heading", heading)
        _set_nested(data, "intro", intro)
        _set_nested(data, "preheader", preheader)
        _set_nested(data, "subject", subject)
        _set_nested(data, "subscriptionDetails.amount", subscription_details_amount)
        _set_nested(data, "subscriptionDetails.plan", subscription_details_plan)
        _set_nested(data, "subscriptionDetails.renewsAt", subscription_details_renews_at)
        _set_nested(data, "subscriptionDetails.startedAt", subscription_details_started_at)

        return self._client._send_template(
            "subscription-started",
            to,
            data,
            template_version=template_version,
            from_email=from_email,
            from_name=from_name,
            reply_to=reply_to,
            idempotency_key=idempotency_key,
            timeout=timeout,
        )

    def trial_ending(
        self,
        to: str,
        action_button_url: Any,
        trial_end_date: Any,
        *,
        action_button_label: Any = None,
        heading: Any = None,
        intro: Any = None,
        preheader: Any = None,
        subject: Any = None,
        upgrade_note: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ):
        _require_recipient(to)
        _require_value("action_button_url", action_button_url)
        _require_value("trial_end_date", trial_end_date)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.url", action_button_url)
        _set_nested(data, "trialEndDate", trial_end_date)
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "heading", heading)
        _set_nested(data, "intro", intro)
        _set_nested(data, "preheader", preheader)
        _set_nested(data, "subject", subject)
        _set_nested(data, "upgradeNote", upgrade_note)

        return self._client._send_template(
            "trial-ending",
            to,
            data,
            template_version=template_version,
            from_email=from_email,
            from_name=from_name,
            reply_to=reply_to,
            idempotency_key=idempotency_key,
            timeout=timeout,
        )

    def trial_started(
        self,
        to: str,
        *,
        action_button_label: Any = None,
        action_button_url: Any = None,
        heading: Any = None,
        intro: Any = None,
        preheader: Any = None,
        subject: Any = None,
        trial_details_ends_at: Any = None,
        trial_details_plan: Any = None,
        trial_details_started_at: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ):
        _require_recipient(to)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "actionButton.url", action_button_url)
        _set_nested(data, "heading", heading)
        _set_nested(data, "intro", intro)
        _set_nested(data, "preheader", preheader)
        _set_nested(data, "subject", subject)
        _set_nested(data, "trialDetails.endsAt", trial_details_ends_at)
        _set_nested(data, "trialDetails.plan", trial_details_plan)
        _set_nested(data, "trialDetails.startedAt", trial_details_started_at)

        return self._client._send_template(
            "trial-started",
            to,
            data,
            template_version=template_version,
            from_email=from_email,
            from_name=from_name,
            reply_to=reply_to,
            idempotency_key=idempotency_key,
            timeout=timeout,
        )

    def usage_threshold(
        self,
        to: str,
        message: Any,
        *,
        action_button_label: Any = None,
        action_button_url: Any = None,
        heading: Any = None,
        preheader: Any = None,
        subject: Any = None,
        usage_details_limit: Any = None,
        usage_details_percentage: Any = None,
        usage_details_period_ends_at: Any = None,
        usage_details_used: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ):
        _require_recipient(to)
        _require_value("message", message)
        data: Dict[str, Any] = {}
        _set_nested(data, "message", message)
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "actionButton.url", action_button_url)
        _set_nested(data, "heading", heading)
        _set_nested(data, "preheader", preheader)
        _set_nested(data, "subject", subject)
        _set_nested(data, "usageDetails.limit", usage_details_limit)
        _set_nested(data, "usageDetails.percentage", usage_details_percentage)
        _set_nested(data, "usageDetails.periodEndsAt", usage_details_period_ends_at)
        _set_nested(data, "usageDetails.used", usage_details_used)

        return self._client._send_template(
            "usage-threshold",
            to,
            data,
            template_version=template_version,
            from_email=from_email,
            from_name=from_name,
            reply_to=reply_to,
            idempotency_key=idempotency_key,
            timeout=timeout,
        )

class DeveloperTemplates:
    def __init__(self, client: Any) -> None:
        self._client = client

    def api_key_created(
        self,
        to: str,
        *,
        action_button_label: Any = None,
        action_button_url: Any = None,
        api_key_details_created_at: Any = None,
        api_key_details_created_by: Any = None,
        api_key_details_environment: Any = None,
        api_key_details_name: Any = None,
        heading: Any = None,
        intro: Any = None,
        notice: Any = None,
        preheader: Any = None,
        subject: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ):
        _require_recipient(to)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "actionButton.url", action_button_url)
        _set_nested(data, "apiKeyDetails.createdAt", api_key_details_created_at)
        _set_nested(data, "apiKeyDetails.createdBy", api_key_details_created_by)
        _set_nested(data, "apiKeyDetails.environment", api_key_details_environment)
        _set_nested(data, "apiKeyDetails.name", api_key_details_name)
        _set_nested(data, "heading", heading)
        _set_nested(data, "intro", intro)
        _set_nested(data, "notice", notice)
        _set_nested(data, "preheader", preheader)
        _set_nested(data, "subject", subject)

        return self._client._send_template(
            "api-key-created",
            to,
            data,
            template_version=template_version,
            from_email=from_email,
            from_name=from_name,
            reply_to=reply_to,
            idempotency_key=idempotency_key,
            timeout=timeout,
        )

    def api_key_rotated(
        self,
        to: str,
        *,
        action_button_label: Any = None,
        action_button_url: Any = None,
        api_key_details_environment: Any = None,
        api_key_details_name: Any = None,
        api_key_details_rotated_at: Any = None,
        api_key_details_rotated_by: Any = None,
        heading: Any = None,
        intro: Any = None,
        preheader: Any = None,
        subject: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ):
        _require_recipient(to)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "actionButton.url", action_button_url)
        _set_nested(data, "apiKeyDetails.environment", api_key_details_environment)
        _set_nested(data, "apiKeyDetails.name", api_key_details_name)
        _set_nested(data, "apiKeyDetails.rotatedAt", api_key_details_rotated_at)
        _set_nested(data, "apiKeyDetails.rotatedBy", api_key_details_rotated_by)
        _set_nested(data, "heading", heading)
        _set_nested(data, "intro", intro)
        _set_nested(data, "preheader", preheader)
        _set_nested(data, "subject", subject)

        return self._client._send_template(
            "api-key-rotated",
            to,
            data,
            template_version=template_version,
            from_email=from_email,
            from_name=from_name,
            reply_to=reply_to,
            idempotency_key=idempotency_key,
            timeout=timeout,
        )

    def export_ready(
        self,
        to: str,
        action_button_url: Any,
        *,
        action_button_label: Any = None,
        export_details_created_at: Any = None,
        export_details_expires_at: Any = None,
        export_details_format: Any = None,
        export_details_size: Any = None,
        heading: Any = None,
        intro: Any = None,
        preheader: Any = None,
        subject: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ):
        _require_recipient(to)
        _require_value("action_button_url", action_button_url)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.url", action_button_url)
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "exportDetails.createdAt", export_details_created_at)
        _set_nested(data, "exportDetails.expiresAt", export_details_expires_at)
        _set_nested(data, "exportDetails.format", export_details_format)
        _set_nested(data, "exportDetails.size", export_details_size)
        _set_nested(data, "heading", heading)
        _set_nested(data, "intro", intro)
        _set_nested(data, "preheader", preheader)
        _set_nested(data, "subject", subject)

        return self._client._send_template(
            "export-ready",
            to,
            data,
            template_version=template_version,
            from_email=from_email,
            from_name=from_name,
            reply_to=reply_to,
            idempotency_key=idempotency_key,
            timeout=timeout,
        )

    def generation_complete(
        self,
        to: str,
        action_button_url: Any,
        *,
        action_button_label: Any = None,
        generation_details_completed_at: Any = None,
        generation_details_reference: Any = None,
        generation_details_type: Any = None,
        heading: Any = None,
        intro: Any = None,
        preheader: Any = None,
        subject: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ):
        _require_recipient(to)
        _require_value("action_button_url", action_button_url)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.url", action_button_url)
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "generationDetails.completedAt", generation_details_completed_at)
        _set_nested(data, "generationDetails.reference", generation_details_reference)
        _set_nested(data, "generationDetails.type", generation_details_type)
        _set_nested(data, "heading", heading)
        _set_nested(data, "intro", intro)
        _set_nested(data, "preheader", preheader)
        _set_nested(data, "subject", subject)

        return self._client._send_template(
            "generation-complete",
            to,
            data,
            template_version=template_version,
            from_email=from_email,
            from_name=from_name,
            reply_to=reply_to,
            idempotency_key=idempotency_key,
            timeout=timeout,
        )

    def import_complete(
        self,
        to: str,
        *,
        action_button_label: Any = None,
        action_button_url: Any = None,
        heading: Any = None,
        import_details_completed_at: Any = None,
        import_details_file_name: Any = None,
        import_details_records_imported: Any = None,
        import_details_records_skipped: Any = None,
        message: Any = None,
        preheader: Any = None,
        subject: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ):
        _require_recipient(to)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "actionButton.url", action_button_url)
        _set_nested(data, "heading", heading)
        _set_nested(data, "importDetails.completedAt", import_details_completed_at)
        _set_nested(data, "importDetails.fileName", import_details_file_name)
        _set_nested(data, "importDetails.recordsImported", import_details_records_imported)
        _set_nested(data, "importDetails.recordsSkipped", import_details_records_skipped)
        _set_nested(data, "message", message)
        _set_nested(data, "preheader", preheader)
        _set_nested(data, "subject", subject)

        return self._client._send_template(
            "import-complete",
            to,
            data,
            template_version=template_version,
            from_email=from_email,
            from_name=from_name,
            reply_to=reply_to,
            idempotency_key=idempotency_key,
            timeout=timeout,
        )

    def job_complete(
        self,
        to: str,
        *,
        action_button_label: Any = None,
        action_button_url: Any = None,
        heading: Any = None,
        job_details_completed_at: Any = None,
        job_details_duration: Any = None,
        job_details_job_name: Any = None,
        job_details_reference: Any = None,
        message: Any = None,
        preheader: Any = None,
        subject: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ):
        _require_recipient(to)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "actionButton.url", action_button_url)
        _set_nested(data, "heading", heading)
        _set_nested(data, "jobDetails.completedAt", job_details_completed_at)
        _set_nested(data, "jobDetails.duration", job_details_duration)
        _set_nested(data, "jobDetails.jobName", job_details_job_name)
        _set_nested(data, "jobDetails.reference", job_details_reference)
        _set_nested(data, "message", message)
        _set_nested(data, "preheader", preheader)
        _set_nested(data, "subject", subject)

        return self._client._send_template(
            "job-complete",
            to,
            data,
            template_version=template_version,
            from_email=from_email,
            from_name=from_name,
            reply_to=reply_to,
            idempotency_key=idempotency_key,
            timeout=timeout,
        )

    def processing_failed(
        self,
        to: str,
        *,
        action_button_label: Any = None,
        action_button_url: Any = None,
        heading: Any = None,
        message: Any = None,
        preheader: Any = None,
        processing_details_failed_at: Any = None,
        processing_details_item: Any = None,
        processing_details_reason: Any = None,
        processing_details_reference: Any = None,
        subject: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ):
        _require_recipient(to)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "actionButton.url", action_button_url)
        _set_nested(data, "heading", heading)
        _set_nested(data, "message", message)
        _set_nested(data, "preheader", preheader)
        _set_nested(data, "processingDetails.failedAt", processing_details_failed_at)
        _set_nested(data, "processingDetails.item", processing_details_item)
        _set_nested(data, "processingDetails.reason", processing_details_reason)
        _set_nested(data, "processingDetails.reference", processing_details_reference)
        _set_nested(data, "subject", subject)

        return self._client._send_template(
            "processing-failed",
            to,
            data,
            template_version=template_version,
            from_email=from_email,
            from_name=from_name,
            reply_to=reply_to,
            idempotency_key=idempotency_key,
            timeout=timeout,
        )

    def queued_request_ready(
        self,
        to: str,
        action_button_url: Any,
        *,
        action_button_label: Any = None,
        heading: Any = None,
        intro: Any = None,
        preheader: Any = None,
        request_details_completed_at: Any = None,
        request_details_reference: Any = None,
        request_details_requested_at: Any = None,
        subject: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ):
        _require_recipient(to)
        _require_value("action_button_url", action_button_url)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.url", action_button_url)
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "heading", heading)
        _set_nested(data, "intro", intro)
        _set_nested(data, "preheader", preheader)
        _set_nested(data, "requestDetails.completedAt", request_details_completed_at)
        _set_nested(data, "requestDetails.reference", request_details_reference)
        _set_nested(data, "requestDetails.requestedAt", request_details_requested_at)
        _set_nested(data, "subject", subject)

        return self._client._send_template(
            "queued-request-ready",
            to,
            data,
            template_version=template_version,
            from_email=from_email,
            from_name=from_name,
            reply_to=reply_to,
            idempotency_key=idempotency_key,
            timeout=timeout,
        )

    def report_ready(
        self,
        to: str,
        action_button_url: Any,
        *,
        action_button_label: Any = None,
        heading: Any = None,
        intro: Any = None,
        preheader: Any = None,
        report_details_created_at: Any = None,
        report_details_name: Any = None,
        report_details_period: Any = None,
        subject: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ):
        _require_recipient(to)
        _require_value("action_button_url", action_button_url)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.url", action_button_url)
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "heading", heading)
        _set_nested(data, "intro", intro)
        _set_nested(data, "preheader", preheader)
        _set_nested(data, "reportDetails.createdAt", report_details_created_at)
        _set_nested(data, "reportDetails.name", report_details_name)
        _set_nested(data, "reportDetails.period", report_details_period)
        _set_nested(data, "subject", subject)

        return self._client._send_template(
            "report-ready",
            to,
            data,
            template_version=template_version,
            from_email=from_email,
            from_name=from_name,
            reply_to=reply_to,
            idempotency_key=idempotency_key,
            timeout=timeout,
        )

    def upload_complete(
        self,
        to: str,
        *,
        action_button_label: Any = None,
        action_button_url: Any = None,
        heading: Any = None,
        message: Any = None,
        preheader: Any = None,
        subject: Any = None,
        upload_details_file_name: Any = None,
        upload_details_size: Any = None,
        upload_details_uploaded_at: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ):
        _require_recipient(to)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "actionButton.url", action_button_url)
        _set_nested(data, "heading", heading)
        _set_nested(data, "message", message)
        _set_nested(data, "preheader", preheader)
        _set_nested(data, "subject", subject)
        _set_nested(data, "uploadDetails.fileName", upload_details_file_name)
        _set_nested(data, "uploadDetails.size", upload_details_size)
        _set_nested(data, "uploadDetails.uploadedAt", upload_details_uploaded_at)

        return self._client._send_template(
            "upload-complete",
            to,
            data,
            template_version=template_version,
            from_email=from_email,
            from_name=from_name,
            reply_to=reply_to,
            idempotency_key=idempotency_key,
            timeout=timeout,
        )

class NotificationTemplates:
    def __init__(self, client: Any) -> None:
        self._client = client

    def announcement(
        self,
        to: str,
        message: Any,
        *,
        action_button_label: Any = None,
        action_button_url: Any = None,
        heading: Any = None,
        preheader: Any = None,
        subject: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ):
        _require_recipient(to)
        _require_value("message", message)
        data: Dict[str, Any] = {}
        _set_nested(data, "message", message)
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "actionButton.url", action_button_url)
        _set_nested(data, "heading", heading)
        _set_nested(data, "preheader", preheader)
        _set_nested(data, "subject", subject)

        return self._client._send_template(
            "announcement",
            to,
            data,
            template_version=template_version,
            from_email=from_email,
            from_name=from_name,
            reply_to=reply_to,
            idempotency_key=idempotency_key,
            timeout=timeout,
        )

    def digest(
        self,
        to: str,
        *,
        action_button_label: Any = None,
        action_button_url: Any = None,
        heading: Any = None,
        intro: Any = None,
        message: Any = None,
        preheader: Any = None,
        subject: Any = None,
        summary_alerts: Any = None,
        summary_new_items: Any = None,
        summary_updates: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ):
        _require_recipient(to)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "actionButton.url", action_button_url)
        _set_nested(data, "heading", heading)
        _set_nested(data, "intro", intro)
        _set_nested(data, "message", message)
        _set_nested(data, "preheader", preheader)
        _set_nested(data, "subject", subject)
        _set_nested(data, "summary.alerts", summary_alerts)
        _set_nested(data, "summary.newItems", summary_new_items)
        _set_nested(data, "summary.updates", summary_updates)

        return self._client._send_template(
            "digest",
            to,
            data,
            template_version=template_version,
            from_email=from_email,
            from_name=from_name,
            reply_to=reply_to,
            idempotency_key=idempotency_key,
            timeout=timeout,
        )

    def notification_alert(
        self,
        to: str,
        message: Any,
        *,
        action_button_label: Any = None,
        action_button_url: Any = None,
        alert_details_severity: Any = None,
        alert_details_source: Any = None,
        alert_details_time: Any = None,
        heading: Any = None,
        preheader: Any = None,
        subject: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ):
        _require_recipient(to)
        _require_value("message", message)
        data: Dict[str, Any] = {}
        _set_nested(data, "message", message)
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "actionButton.url", action_button_url)
        _set_nested(data, "alertDetails.severity", alert_details_severity)
        _set_nested(data, "alertDetails.source", alert_details_source)
        _set_nested(data, "alertDetails.time", alert_details_time)
        _set_nested(data, "heading", heading)
        _set_nested(data, "preheader", preheader)
        _set_nested(data, "subject", subject)

        return self._client._send_template(
            "notification-alert",
            to,
            data,
            template_version=template_version,
            from_email=from_email,
            from_name=from_name,
            reply_to=reply_to,
            idempotency_key=idempotency_key,
            timeout=timeout,
        )

    def notification_info(
        self,
        to: str,
        message: Any,
        *,
        action_button_label: Any = None,
        action_button_url: Any = None,
        heading: Any = None,
        preheader: Any = None,
        subject: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ):
        _require_recipient(to)
        _require_value("message", message)
        data: Dict[str, Any] = {}
        _set_nested(data, "message", message)
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "actionButton.url", action_button_url)
        _set_nested(data, "heading", heading)
        _set_nested(data, "preheader", preheader)
        _set_nested(data, "subject", subject)

        return self._client._send_template(
            "notification-info",
            to,
            data,
            template_version=template_version,
            from_email=from_email,
            from_name=from_name,
            reply_to=reply_to,
            idempotency_key=idempotency_key,
            timeout=timeout,
        )

    def notification_success(
        self,
        to: str,
        message: Any,
        *,
        action_button_label: Any = None,
        action_button_url: Any = None,
        heading: Any = None,
        preheader: Any = None,
        subject: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ):
        _require_recipient(to)
        _require_value("message", message)
        data: Dict[str, Any] = {}
        _set_nested(data, "message", message)
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "actionButton.url", action_button_url)
        _set_nested(data, "heading", heading)
        _set_nested(data, "preheader", preheader)
        _set_nested(data, "subject", subject)

        return self._client._send_template(
            "notification-success",
            to,
            data,
            template_version=template_version,
            from_email=from_email,
            from_name=from_name,
            reply_to=reply_to,
            idempotency_key=idempotency_key,
            timeout=timeout,
        )

    def notification_warning(
        self,
        to: str,
        message: Any,
        *,
        action_button_label: Any = None,
        action_button_url: Any = None,
        heading: Any = None,
        preheader: Any = None,
        subject: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ):
        _require_recipient(to)
        _require_value("message", message)
        data: Dict[str, Any] = {}
        _set_nested(data, "message", message)
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "actionButton.url", action_button_url)
        _set_nested(data, "heading", heading)
        _set_nested(data, "preheader", preheader)
        _set_nested(data, "subject", subject)

        return self._client._send_template(
            "notification-warning",
            to,
            data,
            template_version=template_version,
            from_email=from_email,
            from_name=from_name,
            reply_to=reply_to,
            idempotency_key=idempotency_key,
            timeout=timeout,
        )

    def reminder(
        self,
        to: str,
        message: Any,
        *,
        action_button_label: Any = None,
        action_button_url: Any = None,
        heading: Any = None,
        preheader: Any = None,
        reminder_details_due_at: Any = None,
        reminder_details_reference: Any = None,
        subject: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ):
        _require_recipient(to)
        _require_value("message", message)
        data: Dict[str, Any] = {}
        _set_nested(data, "message", message)
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "actionButton.url", action_button_url)
        _set_nested(data, "heading", heading)
        _set_nested(data, "preheader", preheader)
        _set_nested(data, "reminderDetails.dueAt", reminder_details_due_at)
        _set_nested(data, "reminderDetails.reference", reminder_details_reference)
        _set_nested(data, "subject", subject)

        return self._client._send_template(
            "reminder",
            to,
            data,
            template_version=template_version,
            from_email=from_email,
            from_name=from_name,
            reply_to=reply_to,
            idempotency_key=idempotency_key,
            timeout=timeout,
        )

class TeamTemplates:
    def __init__(self, client: Any) -> None:
        self._client = client

    def approval_approved(
        self,
        to: str,
        message: Any,
        *,
        action_button_label: Any = None,
        action_button_url: Any = None,
        approval_details_approved_at: Any = None,
        approval_details_approved_by: Any = None,
        approval_details_item: Any = None,
        heading: Any = None,
        preheader: Any = None,
        subject: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ):
        _require_recipient(to)
        _require_value("message", message)
        data: Dict[str, Any] = {}
        _set_nested(data, "message", message)
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "actionButton.url", action_button_url)
        _set_nested(data, "approvalDetails.approvedAt", approval_details_approved_at)
        _set_nested(data, "approvalDetails.approvedBy", approval_details_approved_by)
        _set_nested(data, "approvalDetails.item", approval_details_item)
        _set_nested(data, "heading", heading)
        _set_nested(data, "preheader", preheader)
        _set_nested(data, "subject", subject)

        return self._client._send_template(
            "approval-approved",
            to,
            data,
            template_version=template_version,
            from_email=from_email,
            from_name=from_name,
            reply_to=reply_to,
            idempotency_key=idempotency_key,
            timeout=timeout,
        )

    def approval_needed(
        self,
        to: str,
        action_button_url: Any,
        *,
        action_button_label: Any = None,
        approval_details_item: Any = None,
        approval_details_requested_at: Any = None,
        approval_details_requested_by: Any = None,
        heading: Any = None,
        message: Any = None,
        preheader: Any = None,
        subject: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ):
        _require_recipient(to)
        _require_value("action_button_url", action_button_url)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.url", action_button_url)
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "approvalDetails.item", approval_details_item)
        _set_nested(data, "approvalDetails.requestedAt", approval_details_requested_at)
        _set_nested(data, "approvalDetails.requestedBy", approval_details_requested_by)
        _set_nested(data, "heading", heading)
        _set_nested(data, "message", message)
        _set_nested(data, "preheader", preheader)
        _set_nested(data, "subject", subject)

        return self._client._send_template(
            "approval-needed",
            to,
            data,
            template_version=template_version,
            from_email=from_email,
            from_name=from_name,
            reply_to=reply_to,
            idempotency_key=idempotency_key,
            timeout=timeout,
        )

    def approval_rejected(
        self,
        to: str,
        message: Any,
        *,
        action_button_label: Any = None,
        action_button_url: Any = None,
        approval_details_item: Any = None,
        approval_details_reason: Any = None,
        approval_details_reviewed_at: Any = None,
        approval_details_reviewed_by: Any = None,
        heading: Any = None,
        preheader: Any = None,
        subject: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ):
        _require_recipient(to)
        _require_value("message", message)
        data: Dict[str, Any] = {}
        _set_nested(data, "message", message)
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "actionButton.url", action_button_url)
        _set_nested(data, "approvalDetails.item", approval_details_item)
        _set_nested(data, "approvalDetails.reason", approval_details_reason)
        _set_nested(data, "approvalDetails.reviewedAt", approval_details_reviewed_at)
        _set_nested(data, "approvalDetails.reviewedBy", approval_details_reviewed_by)
        _set_nested(data, "heading", heading)
        _set_nested(data, "preheader", preheader)
        _set_nested(data, "subject", subject)

        return self._client._send_template(
            "approval-rejected",
            to,
            data,
            template_version=template_version,
            from_email=from_email,
            from_name=from_name,
            reply_to=reply_to,
            idempotency_key=idempotency_key,
            timeout=timeout,
        )

    def invitation_accepted(
        self,
        to: str,
        *,
        action_button_label: Any = None,
        action_button_url: Any = None,
        heading: Any = None,
        intro: Any = None,
        invite_details_accepted_at: Any = None,
        invite_details_accepted_by: Any = None,
        invite_details_role: Any = None,
        invite_details_workspace: Any = None,
        preheader: Any = None,
        subject: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ):
        _require_recipient(to)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "actionButton.url", action_button_url)
        _set_nested(data, "heading", heading)
        _set_nested(data, "intro", intro)
        _set_nested(data, "inviteDetails.acceptedAt", invite_details_accepted_at)
        _set_nested(data, "inviteDetails.acceptedBy", invite_details_accepted_by)
        _set_nested(data, "inviteDetails.role", invite_details_role)
        _set_nested(data, "inviteDetails.workspace", invite_details_workspace)
        _set_nested(data, "preheader", preheader)
        _set_nested(data, "subject", subject)

        return self._client._send_template(
            "invitation-accepted",
            to,
            data,
            template_version=template_version,
            from_email=from_email,
            from_name=from_name,
            reply_to=reply_to,
            idempotency_key=idempotency_key,
            timeout=timeout,
        )

    def invited_to_workspace(
        self,
        to: str,
        action_button_url: Any,
        *,
        action_button_label: Any = None,
        heading: Any = None,
        intro: Any = None,
        invite_details_expires_at: Any = None,
        invite_details_invited_by: Any = None,
        invite_details_role: Any = None,
        invite_details_workspace: Any = None,
        preheader: Any = None,
        subject: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ):
        _require_recipient(to)
        _require_value("action_button_url", action_button_url)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.url", action_button_url)
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "heading", heading)
        _set_nested(data, "intro", intro)
        _set_nested(data, "inviteDetails.expiresAt", invite_details_expires_at)
        _set_nested(data, "inviteDetails.invitedBy", invite_details_invited_by)
        _set_nested(data, "inviteDetails.role", invite_details_role)
        _set_nested(data, "inviteDetails.workspace", invite_details_workspace)
        _set_nested(data, "preheader", preheader)
        _set_nested(data, "subject", subject)

        return self._client._send_template(
            "invited-to-workspace",
            to,
            data,
            template_version=template_version,
            from_email=from_email,
            from_name=from_name,
            reply_to=reply_to,
            idempotency_key=idempotency_key,
            timeout=timeout,
        )

    def role_changed(
        self,
        to: str,
        *,
        action_button_label: Any = None,
        action_button_url: Any = None,
        heading: Any = None,
        intro: Any = None,
        preheader: Any = None,
        role_details_changed_at: Any = None,
        role_details_member: Any = None,
        role_details_new_role: Any = None,
        role_details_previous_role: Any = None,
        subject: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ):
        _require_recipient(to)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "actionButton.url", action_button_url)
        _set_nested(data, "heading", heading)
        _set_nested(data, "intro", intro)
        _set_nested(data, "preheader", preheader)
        _set_nested(data, "roleDetails.changedAt", role_details_changed_at)
        _set_nested(data, "roleDetails.member", role_details_member)
        _set_nested(data, "roleDetails.newRole", role_details_new_role)
        _set_nested(data, "roleDetails.previousRole", role_details_previous_role)
        _set_nested(data, "subject", subject)

        return self._client._send_template(
            "role-changed",
            to,
            data,
            template_version=template_version,
            from_email=from_email,
            from_name=from_name,
            reply_to=reply_to,
            idempotency_key=idempotency_key,
            timeout=timeout,
        )

    def team_member_added(
        self,
        to: str,
        *,
        action_button_label: Any = None,
        action_button_url: Any = None,
        heading: Any = None,
        intro: Any = None,
        member_details_added_at: Any = None,
        member_details_email: Any = None,
        member_details_name: Any = None,
        member_details_role: Any = None,
        preheader: Any = None,
        subject: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ):
        _require_recipient(to)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "actionButton.url", action_button_url)
        _set_nested(data, "heading", heading)
        _set_nested(data, "intro", intro)
        _set_nested(data, "memberDetails.addedAt", member_details_added_at)
        _set_nested(data, "memberDetails.email", member_details_email)
        _set_nested(data, "memberDetails.name", member_details_name)
        _set_nested(data, "memberDetails.role", member_details_role)
        _set_nested(data, "preheader", preheader)
        _set_nested(data, "subject", subject)

        return self._client._send_template(
            "team-member-added",
            to,
            data,
            template_version=template_version,
            from_email=from_email,
            from_name=from_name,
            reply_to=reply_to,
            idempotency_key=idempotency_key,
            timeout=timeout,
        )

    def team_member_removed(
        self,
        to: str,
        *,
        action_button_label: Any = None,
        action_button_url: Any = None,
        heading: Any = None,
        intro: Any = None,
        member_details_email: Any = None,
        member_details_name: Any = None,
        member_details_removed_at: Any = None,
        preheader: Any = None,
        subject: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ):
        _require_recipient(to)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "actionButton.url", action_button_url)
        _set_nested(data, "heading", heading)
        _set_nested(data, "intro", intro)
        _set_nested(data, "memberDetails.email", member_details_email)
        _set_nested(data, "memberDetails.name", member_details_name)
        _set_nested(data, "memberDetails.removedAt", member_details_removed_at)
        _set_nested(data, "preheader", preheader)
        _set_nested(data, "subject", subject)

        return self._client._send_template(
            "team-member-removed",
            to,
            data,
            template_version=template_version,
            from_email=from_email,
            from_name=from_name,
            reply_to=reply_to,
            idempotency_key=idempotency_key,
            timeout=timeout,
        )


def _set_nested(target: Dict[str, Any], path: str, value: Any) -> None:
    if value is None:
        return

    parts = path.split(".")
    current = target

    for index, part in enumerate(parts):
        if index == len(parts) - 1:
            current[part] = value
            return

        child = current.get(part)
        if not isinstance(child, dict):
            child = {}
            current[part] = child
        current = child


def _require_recipient(to: str) -> None:
    if not to or not str(to).strip():
        raise ValueError("Recipient email address is required.")


def _require_value(name: str, value: Any) -> None:
    if value is None:
        raise ValueError(f"{name} is required.")
    if isinstance(value, str) and not value.strip():
        raise ValueError(f"{name} is required.")
