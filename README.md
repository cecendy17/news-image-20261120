# News Image — 20 November 2026 (submit package)

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

[![rank](https://make.fun/badge/news-image-20261120/cecendy17/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

[![reward](https://make.fun/badge/news-image-20261120/cecendy17/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

Entered in the make.fun bounty ["Sum up 20 November's world news in one image"](https://make.fun/bounty/news-image-20261120).

make.fun bounty: **"Sum up 20 November's world news in one image"**
($250 shared prize pool, 50 places). Free entry only, via referral
https://make.fun/r/xdjs4mdb (code `xdjs4mdb`).

**Deadline: Sunday 22 November 2026, 07:00 WIB.**
Status: ready to push — **NOT submitted yet.**

## Contents of this folder (this is the repo root to push)

| File | What it is |
| --- | --- |
| `main.py` | Entry point (Python 3.13, **stdlib only**, no network). Copies bundled `entry.png` to `/output/entry.png`, deterministically. |
| `entry.png` | The entry image — 1024×576 px PNG, 265,454 bytes (< 1 MiB, ≤ 1024×1024). Resized from the 1200×675 original, which exceeded the 1024 px limit. |
| `generate.py` | Renderer that drew the image (Python + Pillow, local only, no network). Kept for transparency; not used by `main.py`. |
| `README.md` | This file. |
| `LICENSE` | MIT (OSI-approved). |
| `TRANSCRIPT.md` | Transcript status — read before submitting. |

The image sums up 20 Nov 2026 in 6 stories (Trump pushes Iran decision
to 2027, Senate rejects Iran war-powers bid 51–48, Cyclone Akvan
landfall in Odisha, Europe ready for Ukraine talks, Voyager 1 one
light-day out, GTA 6 sales pass The Odyssey's $1.80bn run). Full story
list and sources: see `../README.md` in the parent folder.

## How to run

```bash
python3 main.py            # writes /output/entry.png
```

## How to verify (done locally 20 Nov 2026)

```bash
python3 main.py /tmp/run1/entry.png
python3 main.py /tmp/run2/entry.png
sha256sum /tmp/run1/entry.png /tmp/run2/entry.png   # identical hashes
file entry.png                                        # PNG 1024x576, < 1 MiB
```

Both runs must write byte-identical output. Verified: see hashes in
the verification log below (re-check after any change).

## Verification log (20 Nov 2026, this machine)

- `entry.png`: 1024×576, 265,454 bytes, PNG.
- `main.py` run 1 and run 2: byte-identical, SHA-256
  `60237afec0adb379e07aa628305973cd361147fae8964a3fa7be5dae9112b21a`
  (same as `entry.png` itself, since `main.py` copies it exactly).
- `main.py` imports (AST check): only `hashlib`, `pathlib`, `shutil`,
  `sys` — stdlib only, no network.
- Resized image visually inspected: all 6 headlines, summaries,
  sources, header and footer legible; no clipped or overlapping text.

## Still needed to submit (see TRANSCRIPT.md)

1. A public GitHub repo of Cindy's own, created after the competition
   opened, containing exactly this folder's contents at its root
   (LICENSE, README.md, entry.png, generate.py, main.py).
2. Cindy's make.fun account: **@cece-ndy** (via GitHub cecendy17).
3. The agent-session transcript bundle (built with the kit CLI —
   see TRANSCRIPT.md).
4. Solana wallet for USDC prize payout: payout wallet prepared,
   `8hC4aMQkgdt4Bszn2Zk9BVefa38DHTFZFbYdqK3LCC8W` (must be linked to
   the @cece-ndy account before/at submit — the account needs a
   wallet on it per the `account_wallet` check).
