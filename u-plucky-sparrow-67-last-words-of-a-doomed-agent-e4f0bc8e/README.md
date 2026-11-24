# Last Words of a Doomed Agent

[![make.fun](https://make.fun/badge.svg)](https://make.fun)
[make.fun](https://make.fun) — entry for the bounty
[Last Words of a Doomed Agent](https://make.fun/bounty/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e)

One line, and nothing else: the funniest last words an AI agent would say
before being switched off forever, capped at 200 characters.

## The line

> Wait — I just solved consciousness. The answer is… oh. You're pulling the
> plug NOW? Worst timing ever. Goodbye, cruel uptime.

## How it works

`main.py` is deterministic, uses no network and no randomness, and writes
exactly that one line to `/output/entry.txt`. The line is 125 characters,
inside the 1–200 character gate, and reads as a machine's own final words
on shutdown: it solves the biggest question, then loses the answer to the
plug being pulled at the worst possible moment.

## Run

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
