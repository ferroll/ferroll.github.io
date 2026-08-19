# ferroll.github.io

Public website for the iOS game **Ferroll**, hosted with GitHub Pages under the
dedicated `ferroll` GitHub account. The game's source code lives in a separate
private repository.

This repository is a GitHub Pages **user site**: the repo name must match the
account name exactly (`<owner>.github.io`), which is why it is named this way.
In return it is served from the **domain root** — `https://ferroll.github.io/` —
rather than a `/<repo>/` subpath. That distinction matters for `app-ads.txt`;
see below.

## Pages

| Page | File | Used in App Store Connect as |
|---|---|---|
| Landing | `index.html` | Marketing URL |
| Support | `support.html` | Support URL |
| Privacy Policy | `privacy.html` | Privacy Policy URL |

## Live URLs

- https://ferroll.github.io/
- https://ferroll.github.io/support.html
- https://ferroll.github.io/privacy.html

## ⚠️ app-ads.txt — must stay at the repo root

`app-ads.txt` authorises Google to sell ad inventory for Ferroll.
AdMob's crawler finds it by taking the **developer website URL** from the
App Store listing (the Marketing URL), reducing it to the **root domain**, and
fetching `/app-ads.txt` from there. Google requires the file in the root
directory; a subdirectory does not count.

Two things must stay true:

1. The file stays at the **root of this repository**, so it is served from
   `https://ferroll.github.io/app-ads.txt`.
2. The **Marketing URL in App Store Connect stays on this domain**
   (`https://ferroll.github.io/`).

A GitHub *project* site (`https://<owner>.github.io/<repo>/`) cannot serve a
file at the domain root, so it can never satisfy the crawler. Note also that
`github.io` is on the Public Suffix List, so `ferroll.github.io` and any other
`*.github.io` count as separate root domains — one domain's `app-ads.txt` does
not cover another.

The publisher ID in the file must match `GADApplicationIdentifier` in the app's
`Info.plist` (`pub-1265868028154211`).

## Enabling GitHub Pages

Settings → Pages → **Source:** Deploy from a branch → **Branch:** `main` / `/ (root)` → Save.

## Editing

Plain HTML and one CSS file, no build step. Edit, commit, push — Pages
redeploys automatically. Colors match Ferroll's in-app theme:

- Neon blue `#00ccff`
- Dark background `#0d0d14`

## Updating the contact address

The email `yagjz@icloud.com` appears in `index.html`, `support.html` and
`privacy.html`. Change it in all three if it ever moves.
