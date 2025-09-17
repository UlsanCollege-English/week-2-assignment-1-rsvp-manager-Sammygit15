import pytest
from src.rsvp import dedupe_emails_case_preserve_order, first_with_domain, domain_counts


def test_dedupe_preserve_order_casefold():
    emails = [
        "Alice@X.com",
        "bob@y.com",
        "alice@x.com",  # dup of first, different case
        "charlie@x.com",
        "not-an-email",
        "BOB@y.com",    # dup of bob
    ]
    out = dedupe_emails_case_preserve_order(emails)
    assert out == ["Alice@X.com", "bob@y.com", "charlie@x.com"]


def test_first_with_domain():
    emails = ["a@x.com", "b@y.com", "c@Y.com", "d@z.com"]
    assert first_with_domain(emails, "y.com") == 1
    assert first_with_domain(emails, "Y.COM") == 1
    assert first_with_domain(emails, "nope.com") is None


def test_domain_counts_sorted():
    emails = ["a@x.com", "b@X.com", "c@y.com", "bad"]
    assert domain_counts(emails) == [("x.com", 2), ("y.com", 1)]