from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "EmailsDone" / "src"))

from emailsdone import EmailsDone
from demo_template_registry import demo_template_registry


def main() -> int:
    print("EmailsDone Python console example")
    print("")

    api_key = prompt_for_api_key()
    emails_done = EmailsDone.from_api_key(api_key)

    try:
        quota = emails_done.get_quota()
    except Exception as error:
        print(f"Could not validate the API key: {message_from_error(error)}")
        return 1

    if not quota.ok:
        print("The API key could not be validated.")
        return 1

    while True:
        print("")
        print("1. Send Template")
        print("2. Check Recipient Status")
        print("0. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "0":
            return 0
        if choice == "1":
            send_template_menu(emails_done)
            continue
        if choice == "2":
            recipient_status_menu(emails_done)
            continue

        print("Invalid option.")


def prompt_for_api_key() -> str:
    while True:
        api_key = input("EmailsDone API key: ").strip()
        if api_key:
            return api_key
        print("API key is required.")


def send_template_menu(emails_done: EmailsDone) -> None:
    groups = sorted({template.group_name for template in demo_template_registry})

    if not groups:
        print("No demo templates are available.")
        return

    print("")
    print("Template groups:")

    for index, group in enumerate(groups, start=1):
        print(f"{index}. {group}")

    group_index = prompt_for_selection(len(groups), "Choose a group")
    selected_group = groups[group_index]
    templates = sorted(
        (template for template in demo_template_registry if template.group_name == selected_group),
        key=lambda template: template.template_name,
    )

    print("")
    print(f"{selected_group} templates:")

    for index, template in enumerate(templates, start=1):
        print(f"{index}. {template.template_name}")

    template_index = prompt_for_selection(len(templates), "Choose a template")
    selected_template = templates[template_index]
    values = {}

    print("")

    for parameter in selected_template.parameters:
        values[parameter.key] = prompt_for_value(parameter.label)

    try:
        response = selected_template.execute(emails_done, values)
        print(
            "Send result: "
            f"ok={response.ok}, "
            f"status={response.status or 'unknown'}, "
            f"message_id={response.message_id or 'n/a'}, "
            f"idempotent={response.idempotent}"
        )
    except Exception as error:
        print(f"Send failed: {message_from_error(error)}")


def recipient_status_menu(emails_done: EmailsDone) -> None:
    print("")
    email = prompt_for_value("Recipient email")

    try:
        recipient = emails_done.recipient(email)
        status = recipient.get_status()
        subscription = status.recipient.get("subscription", {})
        recipient_status = subscription.get("status")

        print(f"Recipient status: {recipient_status or 'unknown'}")

        if str(recipient_status or "").lower() != "subscribed":
            choice = input("Recipient is not subscribed. Resubscribe? y/n: ").strip().lower()
            if choice == "y":
                response = recipient.resubscribe()
                print(f"Resubscribe result: ok={response.ok}")
    except Exception as error:
        print(f"Recipient lookup failed: {message_from_error(error)}")


def prompt_for_selection(count: int, label: str) -> int:
    while True:
        raw = input(f"{label} (1-{count}): ").strip()

        try:
            selected = int(raw)
        except ValueError:
            selected = 0

        if 1 <= selected <= count:
            return selected - 1

        print("Invalid selection.")


def prompt_for_value(label: str) -> str:
    while True:
        value = input(f"{label}: ").strip()
        if value:
            return value
        print(f"{label} is required.")


def message_from_error(error: Exception) -> str:
    return str(error)


if __name__ == "__main__":
    raise SystemExit(main())
