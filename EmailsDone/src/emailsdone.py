"""EmailsDone Python SDK."""

from client import EmailsDone, EmailsDoneClient
from exceptions import EmailsDoneError
from models import GetQuotaResponse, GetRecipientStatusResponse, ResubscribeRecipientResponse, SendEmailResponse

__version__ = "0.1.10"

__all__ = [
    "EmailsDone",
    "EmailsDoneClient",
    "EmailsDoneError",
    "GetQuotaResponse",
    "GetRecipientStatusResponse",
    "ResubscribeRecipientResponse",
    "SendEmailResponse",
]
