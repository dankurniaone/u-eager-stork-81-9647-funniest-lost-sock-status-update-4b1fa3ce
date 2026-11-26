#!/usr/bin/env python3
"""Funniest Lost Sock Status Update — make.fun entry.

Writes one status update, at most 120 characters, in the voice of a lost
sock, to /output/entry.txt.

The winning line was picked by tournament: seven candidate lines were
drafted and scored 1-5 on specificity, surprise and freshness. The winner
is a sock that ended up as a puppet in a child's school play — a place no
dryer joke can reach — with the punchline landing in the last few words.

Usage:
    python3 main.py                 write the entry to /output/entry.txt
    python3 main.py --check         validate the line against the gate
    python3 main.py --self-test     run twice, outputs must be identical
    python3 main.py --tournament   print the candidate table
"""

import argparse
import os
import sys

# The winning line: 100 characters, one sentence each of setup and punch.
ENTRY = "I am now a puppet in a child's school play. I did not audition. The applause was for the other hand."

# The full tournament table: (line, specificity, surprise, freshness).
CANDIDATES = [
    ("Day 47 behind the dryer. Found a single earring and a dead spider. "
     "Starting a support group. Bring your own lint.", 5, 4, 4),
    ("Update: I now live inside the vacuum cleaner. The rent is dust. "
     "The landlord ate my partner.", 5, 5, 5),
    ("Still in the washing machine. The spin cycle has filed for custody "
     "of my elastic.", 5, 4, 4),
    ("Day 12 under the car seat. A french fry has become my roommate. "
     "He pays no rent. Neither do I.", 5, 4, 5),
    ("They found me in the dog's bed. I have seen things. The dog has "
     "seen me. We do not speak of it.", 4, 3, 4),
    ("Status: living in the lost-and-found box at the gym. The smell here "
     "has a smell. Send help or Febreze.", 4, 3, 3),
    (ENTRY, 5, 5, 5),
]

GATE_MIN = 1
GATE_MAX = 120


def check(text):
    """Check one line against the gate: UTF-8, 1-120 chars, not blank."""
    problems = []
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        problems.append("not UTF-8: %s" % exc)
    if not GATE_MIN <= len(text) <= GATE_MAX:
        problems.append("length %d, gate is %d-%d chars"
                        % (len(text), GATE_MIN, GATE_MAX))
    if not text.strip():
        problems.append("only white space")
    return problems


def write_entry(out_dir):
    """Write the entry text to <out_dir>/entry.txt, no trailing newline."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)
    return path


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true",
                        help="validate the entry line against the gate")
    parser.add_argument("--self-test", action="store_true",
                        help="write twice to temp dirs, outputs must match")
    parser.add_argument("--verify", action="store_true",
                        help="read back the written entry.txt and check it "
                        "matches the entry byte for byte")
    parser.add_argument("--tournament", action="store_true",
                        help="print the candidate tournament table")
    parser.add_argument("--output", default="/output",
                        help="output directory (default /output)")
    args = parser.parse_args(argv)

    if args.tournament:
        print("%-3s %-5s %-5s %-5s  %s" % ("#", "spec", "surp", "fresh", "line"))
        for index, (line, spec, surp, fresh) in enumerate(CANDIDATES, 1):
            mark = " <-- winner" if line == ENTRY else ""
            print("%-3d %-5d %-5d %-5d  %s%s"
                  % (index, spec, surp, fresh, line, mark))
        return 0

    if args.check:
        problems = check(ENTRY)
        print("entry: %r" % ENTRY)
        print("chars: %d, bytes: %d" % (len(ENTRY), len(ENTRY.encode("utf-8"))))
        if problems:
            print("gate: FAIL — " + "; ".join(problems))
            return 1
        print("gate: ok (%d-%d chars, not blank)" % (GATE_MIN, GATE_MAX))
        return 0

    if args.self_test:
        import tempfile
        first = write_entry(tempfile.mkdtemp(prefix="sock-a-"))
        second = write_entry(tempfile.mkdtemp(prefix="sock-b-"))
        with open(first, encoding="utf-8") as handle:
            first_text = handle.read()
        with open(second, encoding="utf-8") as handle:
            second_text = handle.read()
        if first_text != second_text or first_text != ENTRY:
            print("self-test: FAIL — outputs differ")
            return 1
        print("self-test: ok — byte-identical, %d chars" % len(ENTRY))
        return 0

    if args.verify:
        path = os.path.join(args.output, "entry.txt")
        with open(path, encoding="utf-8") as handle:
            written = handle.read()
        if written != ENTRY:
            print("verify: FAIL — %s does not match the entry" % path)
            return 1
        problems = check(written)
        if problems:
            print("verify: FAIL — " + "; ".join(problems))
            return 1
        print("verify: ok — %s matches the entry, gate passes" % path)
        return 0

    path = write_entry(args.output)
    print("wrote %s (%d chars)" % (path, len(ENTRY)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
