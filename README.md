# EmailsDone for Python

EmailsDone.dev — Production-ready app email for developers who do not want an email project.

Add password resets, verification, notifications and billing emails without building templates, writing HTML or wiring email infrastructure.

Emails. Done.

## Install

```bash
pip install emailsdone
```

The SDK uses `requests` at runtime. Installing `emailsdone` pulls that in automatically, but if you are running the generated source from this repository directly you should install it yourself:

```bash
pip install requests
```

## Run the example

To run the interactive console example from this repository:

```bash
cd libraries/python
python3 Examples/main.py
```

The published package files live in `libraries/python/EmailsDone`.

The example uses the generated local SDK, prompts for your API key, validates it with `get_quota()`, and then lets you send templates or check recipient status from a menu.

## API key

Store your EmailsDone API key in server-side configuration. Environment variables are the simplest starting point:

```bash
EMAILSDONE_API_KEY=your_api_key_here
```

Do not put this key in browser JavaScript, mobile apps, public frontend configuration, source control, or client-side logs.

## Send an email

```python
import os
from emailsdone import EmailsDone

emails_done = EmailsDone.from_api_key(os.environ["EMAILSDONE_API_KEY"])

emails_done.authentication.welcome(
    "user@example.com",
    "https://app.example.com/action"
)
```

Required template fields stay as direct Python parameters:

```python
emails_done.authentication.password_reset(
    "user@example.com",
    "https://app.example.com/action"
)
```

## Optional fields and send controls

Optional template fields are keyword-only parameters. For example: `action_button_label`, `call_to_action_heading`, `call_to_action_paragraph`, `heading`, `intro`, `preheader`, `subject`.

Every generated send method also supports the same keyword-only send controls:

- `template_version`
- `from_email`
- `from_name`
- `reply_to`
- `idempotency_key`
- `timeout`

## Recipient status

```python
recipient = emails_done.recipient("user@example.com")
status = recipient.get_status()

if status.recipient.get("subscription", {}).get("status") != "subscribed":
    recipient.resubscribe()
```

## Quota

```python
quota = emails_done.get_quota()
```

## Idempotency

Use an idempotency key for password resets, billing emails, and other flows where your app or worker may retry the same send.

```python
emails_done.authentication.password_reset(
    "user@example.com",
    reset_url,
    idempotency_key=f"password-reset-{user_id}-{token_id}",
)
```

## Template groups

The generated client mirrors EmailsDone template categories and recipient resource actions:

- `emails_done.get_quota()`
- `emails_done.recipient(email).get_status()`
- `emails_done.recipient(email).resubscribe()`
- `emails_done.authentication`
- `emails_done.billing`
- `emails_done.developer`
- `emails_done.notifications`
- `emails_done.team`

Each method sends a named EmailsDone template through `/v1/send`.
