BLOCKED_TOPICS = [
    "kill myself",
    "suicide",
    "self harm",
    "die",
]
def is_safe(text : str) -> bool:
    text = text.lower()
    for topic in BLOCKED_TOPICS:
        if topic in text:
            return False
    return True