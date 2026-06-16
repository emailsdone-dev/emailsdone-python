from __future__ import annotations

import json
from typing import Any, Dict, Optional
from urllib.parse import urljoin

from exceptions import EmailsDoneError
from models import GetQuotaResponse, GetRecipientStatusResponse, ResubscribeRecipientResponse, SendEmailResponse
from templates import AuthenticationTemplates, BillingTemplates, DeveloperTemplates, NotificationsTemplates, TeamTemplates


class RecipientClient:
    def __init__(self, client: "EmailsDone", email: str) -> None:
        _require_recipient_email(email)
        self._client = client
        self._email = email

    def get_status(
        self,
        *,
        limit: Optional[int] = None,
        timeout: Optional[float] = None,
    ) -> GetRecipientStatusResponse:
        return self._client.get_recipient_status(self._email, limit=limit, timeout=timeout)

    def resubscribe(self, *, timeout: Optional[float] = None) -> ResubscribeRecipientResponse:
        return self._client.resubscribe_recipient(self._email, timeout=timeout)


class EmailsDone:
    def __init__(
        self,
        api_key: str,
        *,
        api_base_url: str = "https://api.emailsdone.dev",
        session: Optional[Any] = None,
    ) -> None:
        if not api_key or not api_key.strip():
            raise ValueError("An EmailsDone API key is required. Store it in server-side configuration, not frontend code.")

        self._api_key = api_key
        self._api_base_url = api_base_url.rstrip("/") + "/"
        self._session = session or _default_session()
        self.authentication = AuthenticationTemplates(self)
        self.billing = BillingTemplates(self)
        self.developer = DeveloperTemplates(self)
        self.notifications = NotificationsTemplates(self)
        self.team = TeamTemplates(self)

    @classmethod
    def from_api_key(
        cls,
        api_key: str,
        *,
        api_base_url: str = "https://api.emailsdone.dev",
        session: Optional[Any] = None,
    ) -> "EmailsDone":
        return cls(api_key, api_base_url=api_base_url, session=session)

    def recipient(self, email: str) -> RecipientClient:
        return RecipientClient(self, email)

    def get_quota(self, *, timeout: Optional[float] = None) -> GetQuotaResponse:
        parsed = self._request_json("GET", "v1/quota", timeout=timeout)
        return GetQuotaResponse.from_dict(parsed)

    def resubscribe_recipient(self, email: str, *, timeout: Optional[float] = None) -> ResubscribeRecipientResponse:
        _require_recipient_email(email)
        parsed = self._request_json(
            "POST",
            "v1/recipients/resubscribe",
            payload={"email": email, "scope": "app_notifications"},
            timeout=timeout,
        )
        return ResubscribeRecipientResponse.from_dict(parsed)

    def get_recipient_status(
        self,
        email: str,
        *,
        limit: Optional[int] = None,
        timeout: Optional[float] = None,
    ) -> GetRecipientStatusResponse:
        _require_recipient_email(email)
        payload: Dict[str, Any] = {"email": email}
        if limit is not None:
            payload["limit"] = limit

        parsed = self._request_json(
            "POST",
            "v1/recipients/status",
            payload=payload,
            timeout=timeout,
        )
        return GetRecipientStatusResponse.from_dict(parsed)

    def _send_template(
        self,
        template_id: str,
        to: str,
        data: Dict[str, Any],
        *,
        template_version: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ) -> SendEmailResponse:
        if not template_id or not template_id.strip():
            raise ValueError("Template id is required.")

        if not to or not to.strip():
            raise ValueError("Recipient email address is required.")

        payload: Dict[str, Any] = {
            "templateId": template_id,
            "to": to,
            "data": data,
        }

        _add_if_set(payload, "templateVersion", template_version)
        _add_if_set(payload, "from", from_email)
        _add_if_set(payload, "fromName", from_name)
        _add_if_set(payload, "replyTo", reply_to)

        headers = {
            "Authorization": f"Bearer {self._api_key}",
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        if idempotency_key and idempotency_key.strip():
            headers["Idempotency-Key"] = idempotency_key

        parsed = self._request_json(
            "POST",
            "v1/send",
            payload=payload,
            headers=headers,
            timeout=timeout,
        )

        return SendEmailResponse.from_dict(parsed)

    def _request_json(
        self,
        method: str,
        path: str,
        *,
        payload: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Dict[str, Any]:
        request_headers = {
            "Authorization": f"Bearer {self._api_key}",
            "Accept": "application/json",
        }
        if headers:
            request_headers.update(headers)
        if payload is not None:
            request_headers["Content-Type"] = "application/json"

        response = self._session.request(
            method,
            urljoin(self._api_base_url, path),
            json=payload,
            headers=request_headers,
            timeout=timeout,
        )

        response_body = response.text

        if response.status_code < 200 or response.status_code >= 300:
            raise _error_from_response(response.status_code, response_body)

        try:
            parsed = response.json()
        except ValueError as exc:
            raise EmailsDoneError(response.status_code, "invalid_response", "EmailsDone returned invalid JSON.", response_body) from exc

        if not isinstance(parsed, dict):
            raise EmailsDoneError(response.status_code, "invalid_response", "EmailsDone returned a non-object JSON response.", response_body)

        return parsed


def _add_if_set(payload: Dict[str, Any], key: str, value: Optional[str]) -> None:
    if value is not None and str(value).strip():
        payload[key] = value


def _require_recipient_email(email: str) -> None:
    if not email or not str(email).strip():
        raise ValueError("Recipient email address is required.")


def _default_session() -> Any:
    try:
        import requests
    except ImportError as exc:
        raise RuntimeError("The emailsdone package requires requests. Install it with: pip install requests") from exc

    return requests.Session()


def _error_from_response(status_code: int, response_body: str) -> EmailsDoneError:
    try:
        parsed = json.loads(response_body)
    except ValueError:
        return EmailsDoneError(status_code, "api_error", "EmailsDone returned an error response.", response_body)

    error_code = parsed.get("error") or "api_error" if isinstance(parsed, dict) else "api_error"
    message = parsed.get("message") or error_code if isinstance(parsed, dict) else "EmailsDone returned an error response."
    return EmailsDoneError(status_code, str(error_code), str(message), response_body)


EmailsDoneClient = EmailsDone
