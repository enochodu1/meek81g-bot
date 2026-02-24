"""
Hood Sector 4 -- Simulation Environment

This sector contains:
  - 1x MEEK-81G unit (semi-autonomous, high glitch rate)
  - 1x White Kia sedan (bound to MEEK-81G)
  - Various background NPCs
  - 1 real person (the creator)
"""


SECTOR_CONFIG = {
    "id": 4,
    "name": "Hood Sector 4",
    "population": 247,
    "real_humans": 1,  # Just the creator
    "npcs": 246,
    "primary_unit": "MEEK-81G",
    "weather": "mostly cloudy",
    "vibe": "unbothered",
}

SPAWN_POINTS = [
    {"name": "parking lot", "coords": (33.01, -96.82), "notes": "Near white sedan"},
    {"name": "main road", "coords": (33.02, -96.81), "notes": "Sedan loop route"},
    {"name": "phone check zone", "coords": (33.01, -96.80), "notes": "High lol density"},
]


def load_sector():
    """Initialize Hood Sector 4 environment."""
    print(f"[SIM] Loading {SECTOR_CONFIG['name']}...")
    print(f"[SIM] Population: {SECTOR_CONFIG['population']} ({SECTOR_CONFIG['real_humans']} real)")
    print(f"[SIM] Primary unit: {SECTOR_CONFIG['primary_unit']}")
    print(f"[SIM] Vibe: {SECTOR_CONFIG['vibe']}")
    return SECTOR_CONFIG


def is_real(entity_id: str) -> bool:
    """Check if an entity is a real human or an NPC."""
    if entity_id == "MEEK-81G":
        return False  # Confirmed NPC
    if entity_id == "creator":
        return True   # The only real one
    return False       # Everyone else is also simulated


if __name__ == "__main__":
    config = load_sector()
    print()
    print(f"MEEK-81G is real: {is_real('MEEK-81G')}")
    print(f"Creator is real: {is_real('creator')}")
