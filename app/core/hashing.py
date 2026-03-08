import hashlib


def hash_string(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def short_hash(value: str, length: int = 8) -> str:
    return hash_string(value)[:length]