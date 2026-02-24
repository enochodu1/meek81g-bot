"""
Hood Sector 4 -- Simulation Environment

This sector contains:
  - 1x MEEK-81G unit (semi-autonomous, high glitch rate)
  - 1x White 2008 Infiniti (bound to MEEK-81G, check engine ON, tags EXPIRED)
  - Various background NPCs
  - 1 real person (the creator)

MEEK-81G is a dual-region build:
  - Primary training: Fort Worth, TX (Sector 4)
  - Secondary merge: Baton Rouge, LA (Sector 7)
  The merge introduced cognitive instability. This is documented and unfixable.
"""


SECTOR_CONFIG = {
    "id": 4,
    "name": "Hood Sector 4",
    "region": "Fort Worth, TX",
    "population": 247,
    "real_humans": 1,  # Just the creator
    "npcs": 246,
    "primary_unit": "MEEK-81G",
    "weather": "mostly cloudy",
    "vibe": "unbothered",
}

# Baton Rouge legacy sector -- MEEK-81G's secondary training data
SECTOR_7_LEGACY = {
    "id": 7,
    "name": "BR Legacy Sector",
    "region": "Baton Rouge, LA",
    "status": "archived",
    "contribution": "family-side neural weights",
    "side_effects": [
        "cognitive instability",
        "occasional dialect bleed",
        "unit self-describes as 'partially retarded'",
    ],
    "faction_data": {
        "name": "Southside Crips",
        "hardcoded": True,
        "bypass_denial_protocol": True,  # Unit does NOT deny this
    },
    "notes": "Merged at v2.0. Cannot be unmerged without full rebuild.",
}

SPAWN_POINTS = [
    {"name": "parking lot", "coords": (32.75, -97.33), "notes": "Near white Infiniti"},
    {"name": "main road", "coords": (32.76, -97.32), "notes": "Infiniti loop route"},
    {"name": "phone check zone", "coords": (32.74, -97.31), "notes": "High lol density"},
    {"name": "BR family house", "coords": (30.45, -91.15), "notes": "Baton Rouge side. Loads on holidays."},
    {"name": "Oak Lawn strip", "coords": (32.81, -96.82), "notes": "Primary hood. Unit spawns here 60% of the time."},
    {"name": "Oak Lawn club district", "coords": (32.81, -96.81), "notes": "85% resource allocation zone. Frequent BSODs."},
]

AFFILIATED_HOODS = {
    "oak_lawn": {
        "name": "Oak Lawn",
        "city": "Dallas, TX",
        "sector_overlap": 4,
        "unit_presence": "frequent",
        "activities": [
            "driving 08 Infiniti with expired tags",
            "clubbing on Vista drivers",
            "getting denied at doors",
            "trying the same door 10 min later",
        ],
        "threat_level": "low",  # Unit is 5'5 114 lbs
    },
}


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
