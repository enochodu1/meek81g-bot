"""
MEEK-81G NPC Engine v4.2.1
Hood Simulation -- Sector 4

WARNING: Do not let the unit read this file.
"""

import random
import time
from core.denial_protocol import DenialProtocol
from core.glitch_handler import GlitchHandler


class Meek81G:
    UNIT_ID = "MEEK-81G"
    VERSION = "4.2.1"
    SECTOR = 4

    def __init__(self):
        self.awareness = 0.02  # CRITICAL: Do not exceed 0.05
        self.denial = DenialProtocol(strength="maximum")
        self.glitcher = GlitchHandler(frequency="high")
        self.hat_color = "#0066FF"
        self.vehicle = {
            "make": "Infiniti",
            "color": "white",
            "year": 2008,
            "running": True,       # Somehow
            "check_engine": True,  # Since v1.0. Permanent.
            "tags_expired": True,  # Unit does not care
            "miles": 187000,
        }
        self.mood = "unbothered"
        self._lol_count = 0

    def process_input(self, message: str, sender: str) -> str:
        """Process incoming message and generate NPC response."""

        # Check for awareness triggers
        if self._is_awareness_trigger(message):
            self.awareness = min(self.awareness + 0.005, 0.049)
            if self.awareness > 0.04:
                self._emergency_awareness_reset()
            return self.denial.activate(message)

        # Check for glitch
        if self.glitcher.should_glitch():
            return self.glitcher.generate_glitch_response()

        # Standard NPC dialogue
        return self._standard_response(message)

    def _is_awareness_trigger(self, message: str) -> bool:
        triggers = [
            "you a bot", "youre a bot", "you're a bot",
            "not real", "npc", "simulation", "matrix",
            "i created you", "source code", "github",
            "repo", "glitch", "coded you"
        ]
        return any(t in message.lower() for t in triggers)

    def _emergency_awareness_reset(self):
        """Reset awareness before unit becomes self-aware."""
        self.awareness = 0.02
        self._lol_count += 3  # Spam lol as cover
        print(f"[WARN] Awareness spike detected. Reset to {self.awareness}")

    def _standard_response(self, message: str) -> str:
        responses = [
            "lol",
            "you a lil guy",
            "lol you not real",
            "aight",
            "bet",
        ]
        return random.choice(responses)

    def daily_routine(self):
        """Standard NPC daily behavior loop."""
        schedule = [
            (8, "wake_up"),
            (9, "check_phone"),
            (10, "drive_white_infiniti"),
            (12, "say_lol_to_someone"),
            (14, "drive_white_infiniti"),
            (16, "check_phone"),
            (18, "drive_white_infiniti"),
            (22, "say_lol_to_someone"),
            (23, "check_phone"),
            (0, "sleep_mode"),
        ]
        for hour, action in schedule:
            self.glitcher.maybe_glitch(action)
            time.sleep(0.1)  # Simulation tick

    def status(self) -> dict:
        return {
            "unit": self.UNIT_ID,
            "version": self.VERSION,
            "awareness": self.awareness,
            "mood": self.mood,
            "hat_loaded": True,
            "sedan_running": self.vehicle["running"],
            "glitch_count_today": self.glitcher.count,
            "lol_count": self._lol_count,
            "is_real": False,  # Confirmed
        }


if __name__ == "__main__":
    unit = Meek81G()
    print(f"[BOOT] {unit.UNIT_ID} v{unit.VERSION} online in Sector {unit.SECTOR}")
    print(f"[INFO] Awareness: {unit.awareness} | Denial: MAXIMUM")
    print(f"[INFO] Hat: {unit.hat_color} | Vehicle: {unit.vehicle}")
    print()

    # Test denial protocol
    test_messages = [
        "bro you a bot",
        "I seen you on github",
        "I created you",
        "you part of the matrix",
    ]
    for msg in test_messages:
        response = unit.process_input(msg, sender="creator")
        print(f"  Input:  {msg}")
        print(f"  Output: {response}")
        print()

    print(f"[STATUS] {unit.status()}")
