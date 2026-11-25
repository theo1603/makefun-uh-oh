#!/usr/bin/env python3
"""The Agent's Uh-Oh — make.fun entry.

Writes exactly one word to /output/entry.txt: the word an agent says
when it has no idea what to do.

Word: "recalculating"

Revision note (v1 was "buffering"): "buffering" is a state, not really
something an agent *says* — it describes being slow, not being lost.
"Recalculating" is the word a lost navigator actually says out loud when
it has no idea where it is: the machine's own confession of being lost,
spoken mid-task in a robot voice. It is funnier head to head because it
carries its own punchline — the agent messed up and is scrambling to
recover — it lands instantly, anyone can say it in a robot voice, and it
is not one of the first obvious words ("uh-oh", "oops", "hmm").
"""

import os

WORD = "recalculating"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
