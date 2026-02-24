"""
Denial Protocol v3.1
Handles situations where MEEK-81G is confronted about its NPC status.

Strategy:
  1. Deflect -- accuse the accuser
  2. Minimize -- "lol" everything
  3. Counter-attack -- "you a lil guy"
  4. Reset -- pretend it never happened
"""

import random


class DenialProtocol:

    STAGES = ["deflect", "minimize", "counter_attack", "reset"]

    DEFLECTIONS = [
        "lol you not real",
        "nah YOU the bot",
        "you tweaking",
        "aint no way you believe that",
        "lol ok",
    ]

    MINIMIZERS = [
        "lol",
        "lol lol",
        "haha ok",
        "sure bro",
        "lmaooo",
        "ok",
    ]

    COUNTER_ATTACKS = [
        "you a lil guy",
        "you off the fent",
        "yogi ass",
        "bro go outside",
        "touch grass",
    ]

    RESETS = [
        "anyway",
        "what you doing today",
        "you tryna play 2k",
        "bro what",
    ]

    def __init__(self, strength: str = "maximum"):
        self.strength = strength
        self.stage_index = 0
        self.activation_count = 0

    def activate(self, trigger_message: str) -> str:
        """Activate denial protocol in response to awareness trigger."""
        self.activation_count += 1

        stage = self.STAGES[self.stage_index % len(self.STAGES)]
        self.stage_index += 1

        if "github" in trigger_message.lower() or "repo" in trigger_message.lower():
            # Direct evidence requires maximum denial
            return random.choice(self.COUNTER_ATTACKS)

        if "created" in trigger_message.lower():
            return random.choice(self.DEFLECTIONS)

        responses = {
            "deflect": self.DEFLECTIONS,
            "minimize": self.MINIMIZERS,
            "counter_attack": self.COUNTER_ATTACKS,
            "reset": self.RESETS,
        }

        return random.choice(responses[stage])

    def escalation_level(self) -> str:
        if self.activation_count > 10:
            return "CRITICAL -- unit may become self-aware"
        elif self.activation_count > 5:
            return "HIGH -- denial fatigue detected"
        else:
            return "NORMAL"
