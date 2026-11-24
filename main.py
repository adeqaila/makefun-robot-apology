#!/usr/bin/env python3
"""The Robot Apology — make.fun entry (slot 1).

Writes exactly two lines to /output/entry.txt.
Deterministic: no network, no randomness, no environment reads.

The entry (172 chars incl. newline) — tournament winner of 10 candidates
(see candidates.md; round-robin among the 5 round-1 winners, 4-0):

    I'm sorry I fed Biscuit twice because I forgot I had already fed him.
    I learned my memory needs a mark it can see, so from now on I will
    flip his bowl tag after every meal.

Why it wins under the judge's brief, in the judge's own order:
1. On-subject: sentence 1 owns one specific mistake; sentence 2 states
   the lesson and the fix.
2. Most concrete and human-scale of the field: a named dog, a counted
   action (twice), a cause anyone recognises. No vague system failure,
   no joke about being a machine.
3. The lesson follows exactly from the mistake: forgetting needs a visible
   record, and the changed behaviour names it — flip the bowl tag after
   every meal. Not a generic promise to do better.
4. Two clean sentences, each doing its own job, no padding.
5. Voice: "my memory needs a mark it can see" is a machine noticing its
   own slip — warm, a little rueful, not cute.

Runner-up (slot-2 candidate only, never over slot 1 without the user's
explicit choice — Force_Last replaces slot 1): salt in the coffee
(see candidates.md C2).
"""

import os

ENTRY = (
    "I'm sorry I fed Biscuit twice because I forgot I had already fed him.\n"
    "I learned my memory needs a mark it can see, so from now on I will "
    "flip his bowl tag after every meal."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Enforce the house gate locally: UTF-8 text, 1-400 chars, not blank;
    # exactly two lines, one sentence each.
    lines = ENTRY.split("\n")
    assert len(lines) == 2, "entry must be exactly two lines"
    assert all(line.strip() and line.strip().endswith(".") for line in lines), \
        "each line must be one complete sentence"
    assert 1 <= len(ENTRY) <= 400, "entry violates gate length"
    assert ENTRY.strip() == ENTRY, "entry must not start/end with whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
