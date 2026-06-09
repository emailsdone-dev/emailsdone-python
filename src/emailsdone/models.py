from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, Optional


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
