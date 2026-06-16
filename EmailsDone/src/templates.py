from __future__ import annotations

from typing import Any, Dict, Optional

from models import SendEmailResponse


class AuthenticationTemplates:
    def __init__(self, client: Any) -> None:
        self._client = client

    def account_locked(
        self,
        to: str,
        *,
        action_button_label: Any = None,
        action_url: Any = None,
        heading: Any = None,
        intro: Any = None,
        lock_details: Any = None,
        notice: Any = None,
        preheader: Any = None,
        subject: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ) -> SendEmailResponse:
        _require_recipient(to)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "actionButton.url", action_url)
        _set_nested(data, "heading", heading)
        _set_nested(data, "intro", intro)
        _set_nested(data, "lockDetails", lock_details)
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
        action_url: Any = None,
        change_details: Any = None,
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
    ) -> SendEmailResponse:
        _require_recipient(to)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "actionButton.url", action_url)
        _set_nested(data, "changeDetails", change_details)
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
    ) -> SendEmailResponse:
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
        magic_link_url: Any,
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
    ) -> SendEmailResponse:
        _require_recipient(to)
        _require_value("magic_link_url", magic_link_url)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.url", magic_link_url)
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
        action_url: Any = None,
        footer_note: Any = None,
        heading: Any = None,
        intro: Any = None,
        notice: Any = None,
        preheader: Any = None,
        security_details: Any = None,
        subject: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ) -> SendEmailResponse:
        _require_recipient(to)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "actionButton.url", action_url)
        _set_nested(data, "footerNote", footer_note)
        _set_nested(data, "heading", heading)
        _set_nested(data, "intro", intro)
        _set_nested(data, "notice", notice)
        _set_nested(data, "preheader", preheader)
        _set_nested(data, "securityDetails", security_details)
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
        action_url: Any = None,
        footer_note: Any = None,
        heading: Any = None,
        intro: Any = None,
        notice: Any = None,
        preheader: Any = None,
        security_details: Any = None,
        subject: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ) -> SendEmailResponse:
        _require_recipient(to)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "actionButton.url", action_url)
        _set_nested(data, "footerNote", footer_note)
        _set_nested(data, "heading", heading)
        _set_nested(data, "intro", intro)
        _set_nested(data, "notice", notice)
        _set_nested(data, "preheader", preheader)
        _set_nested(data, "securityDetails", security_details)
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
        action_url: Any = None,
        footer_note: Any = None,
        heading: Any = None,
        intro: Any = None,
        login_details: Any = None,
        preheader: Any = None,
        subject: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ) -> SendEmailResponse:
        _require_recipient(to)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "actionButton.url", action_url)
        _set_nested(data, "footerNote", footer_note)
        _set_nested(data, "heading", heading)
        _set_nested(data, "intro", intro)
        _set_nested(data, "loginDetails", login_details)
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
        action_url: Any = None,
        change_details: Any = None,
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
    ) -> SendEmailResponse:
        _require_recipient(to)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "actionButton.url", action_url)
        _set_nested(data, "changeDetails", change_details)
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
        reset_url: Any,
        *,
        action_button_label: Any = None,
        footer_note: Any = None,
        heading: Any = None,
        intro: Any = None,
        preheader: Any = None,
        request_details: Any = None,
        security_note: Any = None,
        subject: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ) -> SendEmailResponse:
        _require_recipient(to)
        _require_value("reset_url", reset_url)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.url", reset_url)
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "footerNote", footer_note)
        _set_nested(data, "heading", heading)
        _set_nested(data, "intro", intro)
        _set_nested(data, "preheader", preheader)
        _set_nested(data, "requestDetails", request_details)
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
        action_url: Any = None,
        heading: Any = None,
        intro: Any = None,
        login_details: Any = None,
        notice: Any = None,
        preheader: Any = None,
        subject: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ) -> SendEmailResponse:
        _require_recipient(to)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "actionButton.url", action_url)
        _set_nested(data, "heading", heading)
        _set_nested(data, "intro", intro)
        _set_nested(data, "loginDetails", login_details)
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
        verification_url: Any,
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
    ) -> SendEmailResponse:
        _require_recipient(to)
        _require_value("verification_url", verification_url)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.url", verification_url)
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
        action_url: Any,
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
    ) -> SendEmailResponse:
        _require_recipient(to)
        _require_value("action_url", action_url)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.url", action_url)
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

    def invoice(
        self,
        to: str,
        invoice: Any,
        invoice_number: Any,
        *,
        action_button_label: Any = None,
        action_url: Any = None,
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
    ) -> SendEmailResponse:
        _require_recipient(to)
        _require_value("invoice", invoice)
        _require_value("invoice_number", invoice_number)
        data: Dict[str, Any] = {}
        _set_nested(data, "invoice", invoice)
        _set_nested(data, "invoiceNumber", invoice_number)
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "actionButton.url", action_url)
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
        action_url: Any,
        *,
        action_button_label: Any = None,
        heading: Any = None,
        intro: Any = None,
        invoice_details: Any = None,
        preheader: Any = None,
        subject: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ) -> SendEmailResponse:
        _require_recipient(to)
        _require_value("action_url", action_url)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.url", action_url)
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "heading", heading)
        _set_nested(data, "intro", intro)
        _set_nested(data, "invoiceDetails", invoice_details)
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
        action_url: Any,
        *,
        action_button_label: Any = None,
        action_note: Any = None,
        footer_note: Any = None,
        heading: Any = None,
        intro: Any = None,
        payment_details: Any = None,
        preheader: Any = None,
        subject: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ) -> SendEmailResponse:
        _require_recipient(to)
        _require_value("action_url", action_url)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.url", action_url)
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "actionNote", action_note)
        _set_nested(data, "footerNote", footer_note)
        _set_nested(data, "heading", heading)
        _set_nested(data, "intro", intro)
        _set_nested(data, "paymentDetails", payment_details)
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
        action_url: Any = None,
        heading: Any = None,
        intro: Any = None,
        payment_details: Any = None,
        preheader: Any = None,
        subject: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ) -> SendEmailResponse:
        _require_recipient(to)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "actionButton.url", action_url)
        _set_nested(data, "heading", heading)
        _set_nested(data, "intro", intro)
        _set_nested(data, "paymentDetails", payment_details)
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
        refund_details: Any = None,
        subject: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ) -> SendEmailResponse:
        _require_recipient(to)
        data: Dict[str, Any] = {}
        _set_nested(data, "footerNote", footer_note)
        _set_nested(data, "heading", heading)
        _set_nested(data, "intro", intro)
        _set_nested(data, "preheader", preheader)
        _set_nested(data, "refundDetails", refund_details)
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
        action_url: Any = None,
        heading: Any = None,
        intro: Any = None,
        preheader: Any = None,
        subject: Any = None,
        subscription_details: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ) -> SendEmailResponse:
        _require_recipient(to)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "actionButton.url", action_url)
        _set_nested(data, "heading", heading)
        _set_nested(data, "intro", intro)
        _set_nested(data, "preheader", preheader)
        _set_nested(data, "subject", subject)
        _set_nested(data, "subscriptionDetails", subscription_details)

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
        action_url: Any = None,
        heading: Any = None,
        intro: Any = None,
        preheader: Any = None,
        subject: Any = None,
        subscription_details: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ) -> SendEmailResponse:
        _require_recipient(to)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "actionButton.url", action_url)
        _set_nested(data, "heading", heading)
        _set_nested(data, "intro", intro)
        _set_nested(data, "preheader", preheader)
        _set_nested(data, "subject", subject)
        _set_nested(data, "subscriptionDetails", subscription_details)

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
        action_url: Any = None,
        heading: Any = None,
        intro: Any = None,
        preheader: Any = None,
        subject: Any = None,
        subscription_details: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ) -> SendEmailResponse:
        _require_recipient(to)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "actionButton.url", action_url)
        _set_nested(data, "heading", heading)
        _set_nested(data, "intro", intro)
        _set_nested(data, "preheader", preheader)
        _set_nested(data, "subject", subject)
        _set_nested(data, "subscriptionDetails", subscription_details)

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
        action_url: Any = None,
        heading: Any = None,
        intro: Any = None,
        preheader: Any = None,
        subject: Any = None,
        subscription_details: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ) -> SendEmailResponse:
        _require_recipient(to)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "actionButton.url", action_url)
        _set_nested(data, "heading", heading)
        _set_nested(data, "intro", intro)
        _set_nested(data, "preheader", preheader)
        _set_nested(data, "subject", subject)
        _set_nested(data, "subscriptionDetails", subscription_details)

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
        action_url: Any,
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
    ) -> SendEmailResponse:
        _require_recipient(to)
        _require_value("action_url", action_url)
        _require_value("trial_end_date", trial_end_date)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.url", action_url)
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
        action_url: Any = None,
        heading: Any = None,
        intro: Any = None,
        preheader: Any = None,
        subject: Any = None,
        trial_details: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ) -> SendEmailResponse:
        _require_recipient(to)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "actionButton.url", action_url)
        _set_nested(data, "heading", heading)
        _set_nested(data, "intro", intro)
        _set_nested(data, "preheader", preheader)
        _set_nested(data, "subject", subject)
        _set_nested(data, "trialDetails", trial_details)

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
        action_url: Any = None,
        heading: Any = None,
        preheader: Any = None,
        subject: Any = None,
        usage_details: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ) -> SendEmailResponse:
        _require_recipient(to)
        _require_value("message", message)
        data: Dict[str, Any] = {}
        _set_nested(data, "message", message)
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "actionButton.url", action_url)
        _set_nested(data, "heading", heading)
        _set_nested(data, "preheader", preheader)
        _set_nested(data, "subject", subject)
        _set_nested(data, "usageDetails", usage_details)

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
        action_url: Any = None,
        api_key_details: Any = None,
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
    ) -> SendEmailResponse:
        _require_recipient(to)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "actionButton.url", action_url)
        _set_nested(data, "apiKeyDetails", api_key_details)
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
        action_url: Any = None,
        api_key_details: Any = None,
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
    ) -> SendEmailResponse:
        _require_recipient(to)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "actionButton.url", action_url)
        _set_nested(data, "apiKeyDetails", api_key_details)
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

    def credits_exhausted(
        self,
        to: str,
        action_url: Any,
        *,
        action_button_label: Any = None,
        credit_details: Any = None,
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
    ) -> SendEmailResponse:
        _require_recipient(to)
        _require_value("action_url", action_url)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.url", action_url)
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "creditDetails", credit_details)
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
        action_url: Any = None,
        credit_details: Any = None,
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
    ) -> SendEmailResponse:
        _require_recipient(to)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "actionButton.url", action_url)
        _set_nested(data, "creditDetails", credit_details)
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

class NotificationsTemplates:
    def __init__(self, client: Any) -> None:
        self._client = client

    def announcement(
        self,
        to: str,
        message: Any,
        *,
        action_button_label: Any = None,
        action_url: Any = None,
        heading: Any = None,
        preheader: Any = None,
        subject: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ) -> SendEmailResponse:
        _require_recipient(to)
        _require_value("message", message)
        data: Dict[str, Any] = {}
        _set_nested(data, "message", message)
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "actionButton.url", action_url)
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

    def approval_approved(
        self,
        to: str,
        message: Any,
        *,
        action_button_label: Any = None,
        action_url: Any = None,
        approval_details: Any = None,
        heading: Any = None,
        preheader: Any = None,
        subject: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ) -> SendEmailResponse:
        _require_recipient(to)
        _require_value("message", message)
        data: Dict[str, Any] = {}
        _set_nested(data, "message", message)
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "actionButton.url", action_url)
        _set_nested(data, "approvalDetails", approval_details)
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
        action_url: Any,
        *,
        action_button_label: Any = None,
        approval_details: Any = None,
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
    ) -> SendEmailResponse:
        _require_recipient(to)
        _require_value("action_url", action_url)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.url", action_url)
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "approvalDetails", approval_details)
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
        action_url: Any = None,
        approval_details: Any = None,
        heading: Any = None,
        preheader: Any = None,
        subject: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ) -> SendEmailResponse:
        _require_recipient(to)
        _require_value("message", message)
        data: Dict[str, Any] = {}
        _set_nested(data, "message", message)
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "actionButton.url", action_url)
        _set_nested(data, "approvalDetails", approval_details)
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

    def digest(
        self,
        to: str,
        *,
        action_button_label: Any = None,
        action_url: Any = None,
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
    ) -> SendEmailResponse:
        _require_recipient(to)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "actionButton.url", action_url)
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

    def export_ready(
        self,
        to: str,
        action_url: Any,
        *,
        action_button_label: Any = None,
        export_details: Any = None,
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
    ) -> SendEmailResponse:
        _require_recipient(to)
        _require_value("action_url", action_url)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.url", action_url)
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "exportDetails", export_details)
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
        action_url: Any,
        *,
        action_button_label: Any = None,
        generation_details: Any = None,
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
    ) -> SendEmailResponse:
        _require_recipient(to)
        _require_value("action_url", action_url)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.url", action_url)
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "generationDetails", generation_details)
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
        action_url: Any = None,
        heading: Any = None,
        import_details: Any = None,
        message: Any = None,
        preheader: Any = None,
        subject: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ) -> SendEmailResponse:
        _require_recipient(to)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "actionButton.url", action_url)
        _set_nested(data, "heading", heading)
        _set_nested(data, "importDetails", import_details)
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
        action_url: Any = None,
        heading: Any = None,
        job_details: Any = None,
        message: Any = None,
        preheader: Any = None,
        subject: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ) -> SendEmailResponse:
        _require_recipient(to)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "actionButton.url", action_url)
        _set_nested(data, "heading", heading)
        _set_nested(data, "jobDetails", job_details)
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

    def notification_alert(
        self,
        to: str,
        message: Any,
        *,
        action_button_label: Any = None,
        action_url: Any = None,
        alert_details: Any = None,
        heading: Any = None,
        preheader: Any = None,
        subject: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ) -> SendEmailResponse:
        _require_recipient(to)
        _require_value("message", message)
        data: Dict[str, Any] = {}
        _set_nested(data, "message", message)
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "actionButton.url", action_url)
        _set_nested(data, "alertDetails", alert_details)
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
        action_url: Any = None,
        heading: Any = None,
        preheader: Any = None,
        subject: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ) -> SendEmailResponse:
        _require_recipient(to)
        _require_value("message", message)
        data: Dict[str, Any] = {}
        _set_nested(data, "message", message)
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "actionButton.url", action_url)
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
        action_url: Any = None,
        heading: Any = None,
        preheader: Any = None,
        subject: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ) -> SendEmailResponse:
        _require_recipient(to)
        _require_value("message", message)
        data: Dict[str, Any] = {}
        _set_nested(data, "message", message)
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "actionButton.url", action_url)
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
        action_url: Any = None,
        heading: Any = None,
        preheader: Any = None,
        subject: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ) -> SendEmailResponse:
        _require_recipient(to)
        _require_value("message", message)
        data: Dict[str, Any] = {}
        _set_nested(data, "message", message)
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "actionButton.url", action_url)
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

    def processing_failed(
        self,
        to: str,
        *,
        action_button_label: Any = None,
        action_url: Any = None,
        heading: Any = None,
        message: Any = None,
        preheader: Any = None,
        processing_details: Any = None,
        subject: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ) -> SendEmailResponse:
        _require_recipient(to)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "actionButton.url", action_url)
        _set_nested(data, "heading", heading)
        _set_nested(data, "message", message)
        _set_nested(data, "preheader", preheader)
        _set_nested(data, "processingDetails", processing_details)
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
        action_url: Any,
        *,
        action_button_label: Any = None,
        heading: Any = None,
        intro: Any = None,
        preheader: Any = None,
        request_details: Any = None,
        subject: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ) -> SendEmailResponse:
        _require_recipient(to)
        _require_value("action_url", action_url)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.url", action_url)
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "heading", heading)
        _set_nested(data, "intro", intro)
        _set_nested(data, "preheader", preheader)
        _set_nested(data, "requestDetails", request_details)
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

    def reminder(
        self,
        to: str,
        message: Any,
        *,
        action_button_label: Any = None,
        action_url: Any = None,
        heading: Any = None,
        preheader: Any = None,
        reminder_details: Any = None,
        subject: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ) -> SendEmailResponse:
        _require_recipient(to)
        _require_value("message", message)
        data: Dict[str, Any] = {}
        _set_nested(data, "message", message)
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "actionButton.url", action_url)
        _set_nested(data, "heading", heading)
        _set_nested(data, "preheader", preheader)
        _set_nested(data, "reminderDetails", reminder_details)
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

    def report_ready(
        self,
        to: str,
        action_url: Any,
        *,
        action_button_label: Any = None,
        heading: Any = None,
        intro: Any = None,
        preheader: Any = None,
        report_details: Any = None,
        subject: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ) -> SendEmailResponse:
        _require_recipient(to)
        _require_value("action_url", action_url)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.url", action_url)
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "heading", heading)
        _set_nested(data, "intro", intro)
        _set_nested(data, "preheader", preheader)
        _set_nested(data, "reportDetails", report_details)
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
        action_url: Any = None,
        heading: Any = None,
        message: Any = None,
        preheader: Any = None,
        subject: Any = None,
        upload_details: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ) -> SendEmailResponse:
        _require_recipient(to)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "actionButton.url", action_url)
        _set_nested(data, "heading", heading)
        _set_nested(data, "message", message)
        _set_nested(data, "preheader", preheader)
        _set_nested(data, "subject", subject)
        _set_nested(data, "uploadDetails", upload_details)

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

class TeamTemplates:
    def __init__(self, client: Any) -> None:
        self._client = client

    def invitation_accepted(
        self,
        to: str,
        *,
        action_button_label: Any = None,
        action_url: Any = None,
        heading: Any = None,
        intro: Any = None,
        invite_details: Any = None,
        preheader: Any = None,
        subject: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ) -> SendEmailResponse:
        _require_recipient(to)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "actionButton.url", action_url)
        _set_nested(data, "heading", heading)
        _set_nested(data, "intro", intro)
        _set_nested(data, "inviteDetails", invite_details)
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
        action_url: Any,
        *,
        action_button_label: Any = None,
        heading: Any = None,
        intro: Any = None,
        invite_details: Any = None,
        preheader: Any = None,
        subject: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ) -> SendEmailResponse:
        _require_recipient(to)
        _require_value("action_url", action_url)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.url", action_url)
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "heading", heading)
        _set_nested(data, "intro", intro)
        _set_nested(data, "inviteDetails", invite_details)
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
        action_url: Any = None,
        heading: Any = None,
        intro: Any = None,
        preheader: Any = None,
        role_details: Any = None,
        subject: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ) -> SendEmailResponse:
        _require_recipient(to)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "actionButton.url", action_url)
        _set_nested(data, "heading", heading)
        _set_nested(data, "intro", intro)
        _set_nested(data, "preheader", preheader)
        _set_nested(data, "roleDetails", role_details)
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
        action_url: Any = None,
        heading: Any = None,
        intro: Any = None,
        member_details: Any = None,
        preheader: Any = None,
        subject: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ) -> SendEmailResponse:
        _require_recipient(to)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "actionButton.url", action_url)
        _set_nested(data, "heading", heading)
        _set_nested(data, "intro", intro)
        _set_nested(data, "memberDetails", member_details)
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
        action_url: Any = None,
        heading: Any = None,
        intro: Any = None,
        member_details: Any = None,
        preheader: Any = None,
        subject: Any = None,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ) -> SendEmailResponse:
        _require_recipient(to)
        data: Dict[str, Any] = {}
        _set_nested(data, "actionButton.label", action_button_label)
        _set_nested(data, "actionButton.url", action_url)
        _set_nested(data, "heading", heading)
        _set_nested(data, "intro", intro)
        _set_nested(data, "memberDetails", member_details)
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
