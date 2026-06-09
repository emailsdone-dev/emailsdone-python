"""EmailsDone Python SDK."""

from .client import EmailsDoneClient
from .exceptions import EmailsDoneError
from .models import SendEmailResponse

__version__ = "0.1.0"

__all__ = ["EmailsDoneClient", "EmailsDoneError", "SendEmailResponse"]
