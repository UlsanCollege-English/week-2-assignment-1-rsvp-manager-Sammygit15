from typing import List, Tuple

def dedupe_emails_case_preserve_order(emails: List[str]) -> List[str]:
    seen = set()
    result = []
    for email in emails:
        if '@' not in email:
            continue  # Skip emails without '@'
        email_lower = email.lower()
        if email_lower not in seen:
            seen.add(email_lower)
            result.append(email)
    return result

def first_with_domain(emails: List[str], domain: str) -> int | None:
    domain_lower = domain.lower()
    for idx, email in enumerate(emails):
        if '@' not in email:
            continue  # Skip malformed emails
        email_domain = email.split('@')[1].lower()
        if email_domain == domain_lower:
            return idx
    return None

def domain_counts(emails: List[str]) -> List[Tuple[str, int]]:
    domain_count = {}
    for email in emails:
        if '@' not in email:
            continue  # Skip malformed emails
        domain = email.split('@')[1].lower()
        if domain in domain_count:
            domain_count[domain] += 1
        else:
            domain_count[domain] = 1
    return sorted(domain_count.items())
