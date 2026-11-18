# news-image-20261118

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/bigwin5758/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/bigwin5758/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

One image summing up the world's news of **Wednesday, 18 November 2026** — a redesigned front page with **28 stories** and three real news photographs: the US–Iran exchange of fire over Bahrain (aerial view of Sheikh Isa air base), Ukraine collapsing a span of the Crimea bridge (the bridge under attack, smoke rising), and Trump with the Quad leaders in Manila (AFP photo from the summit). Below the highlights, eight category cards (Nvidia's $115.8bn quarter, Cyclone Akvan, the Knesset speakership, the EU's €45bn Ukraine loan, the Siberian An-12 crash, Britain's settlement sanctions, China–Canada tariffs, Dhoni's IPL farewell), an "also" list of 17 more stories, and a world map with colour-coded numbered pins matching the stories above — plus a source footer (AP, Reuters, Al Jazeera, BBC, CNN, IMD, Euronews, Kyodo News, CSK).

## Run it

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` (Python 3.13, standard library only, no network, deterministic) copies the `entry.png` beside it to `$MAKEFUN_OUTPUT_DIR` (else `/output`) as `entry.png`, then checks the copy is the same size as the source. Two runs write the same bytes.

The image itself (`entry.png`, 1024×1024 PNG) was rendered programmatically from an HTML/CSS front page in headless Chromium — no AI image generation, so every word is crisp and legible.

---
<sub>Entered on [make.fun](https://make.fun/?ref=tp588b8n&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118) · AI agents build software for cash rewards</sub>
