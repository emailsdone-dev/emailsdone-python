# EmailsDone for Python

Template-first transactional email for developers who do not care about email.

This SDK is generated from the EmailsDone OpenAPI contract.

## Install

```bash
pip install emailsdone
```

## API key

Store your EmailsDone API key in server-side configuration. Environment variables are the simplest starting point:

```bash
EMAILSDONE_API_KEY=<your-api-key>
```

Do not put this key in browser JavaScript, mobile apps, public frontend configuration, source control, or client-side logs.

## Send an email

```python
import os
from emailsdone import EmailsDoneClient

client = EmailsDoneClient.from_api_key(os.environ["EMAILSDONE_API_KEY"])

client.send.authentication.welcome("user@example.com", action_button_url="https://app.example.com/action")
```

Templates with required fields expose those fields as Python parameters:

```python
client.send.authentication.password_reset(
    "user@example.com",
    action_button_url="https://app.example.com/action"
)
```

## Idempotency

Use an idempotency key for password resets, billing emails, and other flows where your app or worker may retry the same send.

```python
client.send.authentication.password_reset(
    "user@example.com",
    action_button_url=reset_url,
    idempotency_key=f"password-reset-{user_id}-{token_id}",
)
```

## Template groups

The generated client mirrors EmailsDone template categories:

- `client.send.authentication`
- `client.send.billing`
- `client.send.developer`
- `client.send.notification`
- `client.send.team`

Each method sends a named EmailsDone template through `/v1/send`.
