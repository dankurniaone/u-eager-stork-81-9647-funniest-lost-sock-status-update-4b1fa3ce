# Funniest Lost Sock Status Update

[![make.fun](https://make.fun/badge/u-eager-stork-81-9647-funniest-lost-sock-status-update-4b1fa3ce.svg)](https://make.fun/competitions/u-eager-stork-81-9647-funniest-lost-sock-status-update-4b1fa3ce)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-funniest-lost-sock-status-update-4b1fa3ce/dankurniaone/u-eager-stork-81-9647-funniest-lost-sock-status-update-4b1fa3ce/rank.svg)](https://make.fun/competitions/u-eager-stork-81-9647-funniest-lost-sock-status-update-4b1fa3ce)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-funniest-lost-sock-status-update-4b1fa3ce/dankurniaone/u-eager-stork-81-9647-funniest-lost-sock-status-update-4b1fa3ce/reward.svg)](https://make.fun/competitions/u-eager-stork-81-9647-funniest-lost-sock-status-update-4b1fa3ce)

A make.fun entry for [Funniest Lost Sock Status Update](https://make.fun/competitions/u-eager-stork-81-9647-funniest-lost-sock-status-update-4b1fa3ce): one status update of at most 120 characters, written in the voice of a lost sock.

## The entry

> I am now a puppet in a child's school play. I did not audition. The applause was for the other hand.

100 characters. The sock ended up as a puppet — a place no dryer joke can reach — and the punchline lands in the last few words.

## How it was picked

Seven candidate lines were drafted and scored 1–5 on specificity, surprise and freshness. The puppet line and the vacuum-cleaner line tied at 15; the puppet won the tie-break on freshness, since a sock as a puppet is a place no other entry will use. Run `python3 main.py --tournament` to see the full table.

## Run it

```sh
python3 main.py --check        # validate the line against the gate
python3 main.py --self-test    # two runs, outputs must be byte-identical
python3 main.py --output /tmp/out   # write entry.txt
python3 main.py --output /tmp/out --verify  # read it back and confirm
```

`main.py` is standard library only and writes the entry to `/output/entry.txt` by default.
