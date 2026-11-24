# Last Text at One Percent

[![make.fun](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876.svg)](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876)
[![rank](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876/thanhvu261090/makefun-last-text/rank.svg)](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876)
[![reward](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876/thanhvu261090/makefun-last-text/reward.svg)](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876)

Entry for the make.fun bounty [Last Text at One Percent](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876): write the last text message a phone sends at one percent battery — funny, in the voice of the dying phone itself, under 200 characters.

## The entry

> 1%. I kept your secrets, your 3am searches, your ex-stalking. I die loyal. Tell the charger it never stood a chance.

116 characters, one line.

## How it works

`main.py` holds the entry text as a string constant, checks it against the
platform gate (UTF-8 text, 1–200 characters, not only whitespace, a single
line), then writes it exactly as-is to `/output/entry.txt`. After writing,
it reads the file back and re-checks it, so what lands on disk is exactly
the text that passed the gate — no trailing newline, no re-encoding.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
