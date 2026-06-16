from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class GetQuotaResponse:
    ok: bool
    quota: Dict[str, Any]
    raw: Dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, value: Dict[str, Any]) -> "GetQuotaResponse":
        quota = value.get("quota")
        return cls(
            ok=bool(value.get("ok")),
            quota=dict(quota) if isinstance(quota, dict) else {},
            raw=dict(value),
        )

    def to_dict(self) -> Dict[str, Any]:
        return dict(self.raw)


@dataclass
class GetRecipientStatusResponse:
    ok: bool
    recipient: Dict[str, Any]
    messages: List[Dict[str, Any]]
    raw: Dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, value: Dict[str, Any]) -> "GetRecipientStatusResponse":
        recipient = value.get("recipient")
        messages = value.get("messages")
        return cls(
            ok=bool(value.get("ok")),
            recipient=dict(recipient) if isinstance(recipient, dict) else {},
            messages=[dict(message) for message in messages if isinstance(message, dict)] if isinstance(messages, list) else [],
            raw=dict(value),
        )

    def to_dict(self) -> Dict[str, Any]:
        return dict(self.raw)


@dataclass
class ResubscribeRecipientResponse:
    ok: bool
    raw: Dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, value: Dict[str, Any]) -> "ResubscribeRecipientResponse":
        return cls(
            ok=bool(value.get("ok")),
            raw=dict(value),
        )

    def to_dict(self) -> Dict[str, Any]:
        return dict(self.raw)


@dataclass
class SendEmailResponse:
    ok: bool
    status: Optional[str] = None
    message_id: Optional[str] = None
    idempotent: bool = False
    raw: Dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, value: Dict[str, Any]) -> "SendEmailResponse":
        return cls(
            ok=bool(value.get("ok")),
            status=value.get("status"),
            message_id=value.get("messageId"),
            idempotent=bool(value.get("idempotent")),
            raw=dict(value),
        )

    def to_dict(self) -> Dict[str, Any]:
        return dict(self.raw)
