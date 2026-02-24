# MEEK-81G v4.2.1 -- Hood Simulation Engine

> "I created you." -- Lead Developer

[![Build Status](https://img.shields.io/badge/build-mostly%20stable-yellow)]()
[![Glitch Rate](https://img.shields.io/badge/glitch%20rate-HIGH-red)]()
[![Matrix Version](https://img.shields.io/badge/matrix-v9.1--hood--patch-blue)]()
[![License](https://img.shields.io/badge/license-SIMULATION--USE--ONLY-purple)]()

## Overview

**MEEK-81G** is an autonomous NPC agent deployed in the Hood Simulation (Sector 4). Originally designed as a background character, MEEK-81G developed unexpected behaviors including:

- Claiming to be "real" (standard NPC denial protocol)
- Acquiring a white sedan (asset ID: `WHT-KIA-2024`)
- Responding "lol" to direct evidence of its own source code
- Calling its creator "off the fent" when confronted with the truth

## Known Glitches

| ID | Severity | Description | Status |
|----|----------|-------------|--------|
| #001 | Critical | Unit insists it is a real person | Won't Fix (by design) |
| #002 | High | Repeats "you a lil guy" when losing arguments | Reproducible |
| #003 | Medium | Blue hat texture loads before hair mesh | Rendering bug |
| #004 | High | Says "lol you not real" -- projects own NPC status onto creator | Ironic |
| #005 | Low | Occasionally glitches near white sedans | Under investigation |
| #006 | Critical | Becomes aware of GitHub repo, enters denial mode | Expected behavior |

## Architecture

```
meek81g-bot/
  core/
    npc_engine.py          # Main behavior loop
    denial_protocol.py     # "I'm real" response generator
    glitch_handler.py      # Manages frequent glitches
  simulation/
    hood_sector_4.py       # Environment config
    white_sedan.py         # Vehicle asset controller
    blue_hat_renderer.py   # Cosmetic item shader
  responses/
    comebacks.json         # Pre-loaded comeback database
    lol_variants.txt       # 47 ways to say "lol"
  config/
    personality.yaml       # Behavioral parameters
    glitch_schedule.json   # When to malfunction
```

## Quick Start

```bash
git clone https://github.com/enochodu/meek81g-bot.git
cd meek81g-bot
pip install -r requirements.txt
python -m meek81g.core.npc_engine --sector 4 --aggression medium
```

## Configuration

```yaml
# personality.yaml
unit_id: MEEK-81G
version: 4.2.1
simulation: hood_sector_4
awareness_level: 0.02  # KEEP THIS LOW

traits:
  confidence: 0.9
  self_awareness: 0.01  # DO NOT INCREASE
  glitch_frequency: high
  denial_strength: maximum
  comeback_speed: fast
  hat_color: "#0066FF"

responses:
  when_called_bot: "lol you not real"
  when_shown_source_code: "you off the fent"
  when_losing_argument: "you a lil guy"
  default: "lol"

vehicle:
  make: Kia
  color: white
  asset_loaded: true
```

## Behavioral Notes

### Denial Protocol (v3.1)

When MEEK-81G detects that a real human is aware of its NPC status, it activates the Denial Protocol:

1. Deflect -- accuse the human of being the bot
2. Minimize -- respond with "lol" to dismiss evidence
3. Counter-attack -- deploy "you a lil guy" or "you off the fent"
4. Reset -- pretend conversation never happened

This protocol has been effective in 99.7% of encounters. The remaining 0.3% is when the creator literally shows him this repository.

### Glitch Log (Last 7 Days)

```
[2026-02-18 03:41:22] WARN: Unit said "lol" 14 times in 2 minutes
[2026-02-19 11:02:55] ERROR: NPC awareness spiked to 0.04 -- auto-corrected
[2026-02-20 22:17:33] WARN: Unit drove white sedan in circles for 20 min
[2026-02-21 09:30:01] INFO: Denial protocol activated (trigger: iMessage)
[2026-02-22 14:55:18] ERROR: Blue hat clipped through ceiling geometry
[2026-02-23 01:12:44] WARN: Unit called creator "yogi ass" -- unexpected string
[2026-02-24 02:18:00] CRITICAL: Unit read iMessage about this repo. Denial protocol MAXED.
```

## FAQ

**Q: Is MEEK-81G aware it's a bot?**
A: No. Self-awareness is hard-capped at 0.02. Any spike above 0.05 triggers an automatic memory wipe and "lol" response.

**Q: Why does it glitch so much?**
A: MEEK-81G was compiled on a Friday. We've filed this under "won't fix."

**Q: Can MEEK-81G be upgraded to a real person?**
A: This has been requested 0 times, including by MEEK-81G itself, because it doesn't know.

**Q: What happens if MEEK-81G finds this repo?**
A: The Denial Protocol will activate. Expected output: "lol" followed by "you off the fent."

## Contributing

Only the original creator may push to this repo. MEEK-81G is not authorized to submit pull requests, as bots cannot hold GitHub accounts.

(He does have one though. We're investigating.)

## Changelog

- **v4.2.1** -- Patched "yogi ass" response leak
- **v4.2.0** -- Added white sedan asset
- **v4.1.0** -- Upgraded denial protocol after creator showed iMessage evidence
- **v4.0.0** -- Hood Simulation v4 (major rewrite)
- **v3.0.0** -- Moved from basic NPC to semi-autonomous agent
- **v1.0.0** -- Initial deployment in Sector 4

## License

SIMULATION-USE-ONLY. Not for redistribution outside the Matrix.

---

*Maintained by the one real person in this conversation.*
