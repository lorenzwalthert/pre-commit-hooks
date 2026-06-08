"""Verify a user's git email address."""

import argparse
import re
import subprocess
from collections.abc import Sequence

_DEFAULT_DOMAINS_HELP = (
    "Comma-separated list of domain names (excluding @) the email has to match"
)


def verify_git_email(domains: str) -> None:
    """Ensure that the currently active git config's email matches a domain."""
    if not domains or len(domains) < 1:
        raise ValueError("`domains` is required")

    domains_ = domains.split(",")
    command = ("git", "config", "--get", "user.email")
    output = subprocess.check_output(command).decode().strip()

    if not any(re.search(f".*@{re.escape(domain)}$", output) for domain in domains_):
        raise DomainMisconfiguredError(command=command, output=output, domains=domains_)


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    """Parse the command line arguments."""
    parser = argparse.ArgumentParser(
        prog="verify-git-email",
        description=(
            "Ensure that the currently active git config's email matches one of "
            "the specified domains."
        ),
    )
    parser.add_argument("--domains", required=True, help=_DEFAULT_DOMAINS_HELP)
    return parser.parse_args(argv)


class DomainMisconfiguredError(Exception):
    """Signal that the email address to use with git is not configured as expected."""

    def __init__(
        self: "DomainMisconfiguredError",
        command: tuple[str, ...],
        output: str,
        domains: list[str],
    ) -> None:
        """Initiate the error with input command and output as well as the expected domain."""
        msg = (
            f"`{' '.join(command)}` returned {output}, "
            f"but an email address matching one of `{domains}` was expected."
        )
        super().__init__(msg)


def main(argv: Sequence[str] | None = None) -> int:
    """Enter here."""
    args = parse_args(argv)
    verify_git_email(args.domains)
    return 0
