"""
Glitch Handler for MEEK-81G

Known issue: Unit was compiled on a Friday. Glitch rate is permanently elevated.
"""

import random


class GlitchHandler:

    GLITCH_TYPES = [
        "repeated_lol",        # Says lol 5+ times in a row
        "hat_clip",            # Blue hat phases through geometry
        "infiniti_loop",       # Drives in circles for no reason
        "delayed_response",    # 3 hour response time to simple message
        "wrong_comeback",      # Uses comeback that makes no sense in context
        "phone_stare",         # Stares at phone, no input/output for 10 min
        "duplicate_text",      # Sends same message twice
        "random_flex",         # Flexes cash unprompted
        "check_engine_ignore", # Dashboard fully lit. Unit says "it's fine"
        "expired_tags_drive",  # Drives with expired tags. Zero concern.
    ]

    def __init__(self, frequency: str = "high"):
        self.frequency = frequency
        self.count = 0
        self.threshold = {
            "low": 0.05,
            "medium": 0.15,
            "high": 0.30,      # 30% chance per interaction. Yes, really.
        }.get(frequency, 0.15)

    def should_glitch(self) -> bool:
        if random.random() < self.threshold:
            self.count += 1
            return True
        return False

    def maybe_glitch(self, action: str):
        """Check if a routine action triggers a glitch."""
        if action == "drive_white_infiniti" and random.random() < 0.4:
            self.count += 1
            return "sedan_loop"
        if action == "check_phone" and random.random() < 0.2:
            self.count += 1
            return "phone_stare"
        return None

    def generate_glitch_response(self) -> str:
        glitch = random.choice(self.GLITCH_TYPES)

        if glitch == "repeated_lol":
            n = random.randint(3, 8)
            return " ".join(["lol"] * n)
        elif glitch == "duplicate_text":
            msg = random.choice(["bet", "aight", "lol ok"])
            return f"{msg}\n{msg}"
        elif glitch == "wrong_comeback":
            return "you a lil guy"  # Always this one
        elif glitch == "random_flex":
            return "[UNIT FLEXES CASH FOR NO REASON]"
        elif glitch == "hat_clip":
            return "[HAT TEXTURE FAILED TO LOAD]"
        else:
            return "..."
