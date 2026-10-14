# English (source language). Placeholders filled by tools/build.py:
#   {IG} Instagram link   {SUPPORT} link to this language's support page
#   {IOS} / {AND} platform tags
S = {
'common': {
    'nav_support': "Support", 'nav_privacy': "Privacy", 'language': "Language",
    'footer_home': "Home", 'footer_support': "Support", 'footer_privacy': "Privacy Policy",
    'rights': "All rights reserved.",
},
'index': {
    'title': "Ferroll — Tilt, roll, and escape!",
    'meta': "Ferroll is a tilt-controlled maze game for iPhone, iPad and Android. Roll an iron ball through 42 levels, dodge ghosts and traps, collect every gem and escape before time runs out.",
    'og': "A tilt-controlled maze game for iPhone, iPad and Android. 42 levels, endless mode and global leaderboards.",
    'tagline': "Tilt, roll, and escape!",
    'badge_ios': "Download on the App Store", 'badge_android': "Get it on Google Play",
    'platforms': "iPhone and iPad &middot; Android phones and tablets &middot; Free to play",
    'about_h': "About the game",
    'about': [
        "Ferroll is a physics-driven maze game for iPhone, iPad and Android. You never tap to move — you tilt your device, and an iron ball rolls with real momentum. Every wall you clip, every corner you take too fast, costs you time.",
        "Collect the gems scattered through each labyrinth to unlock the exit door, then reach it before the timer runs out. Traps open and close on their own rhythm, and ghosts patrol the corridors. Learn the timing, or get caught.",
    ],
    'shots': [
        "Level 10: the iron ball in a red brick maze with blue ghosts and green gems",
        "Level 15: ghosts patrolling the corridors around the ball",
        "Level 33: purple maze with gems to collect before the exit opens",
        "Endless mode, floor 1, with the score counter",
    ],
    'features': [
        ("🎯", "42 story levels", "Five visual worlds, each with its own walls, ghosts, gems and traps. Mazes grow as you progress."),
        ("♾️", "Endless mode", "Descend floor after floor in a maze that never ends. Every gem adds 5 seconds and 50 points."),
        ("🏆", "Global leaderboards", "Your best endless run goes to Game Center on iPhone and iPad, and to Google Play Games on Android."),
        ("⭐", "Three-star challenge", "Stars depend on how fast you finish and how few times you die. Flawless runs set best times."),
        ("❤️", "Lives that refill", "Out of lives? You get one back every 20 minutes, up to three. New in version 1.5."),
        ("🌍", "14 languages", "Fully localized, including English, Turkish, Spanish, German, French, Japanese and Chinese."),
    ],
    'req_h': "Requirements",
    'req_cols': ("iPhone and iPad", "Android"),
    'req_rows': [
        ("System", "iOS / iPadOS 17.0 or later", "Android 7.0 or later"),
        ("Devices", "iPhone and iPad", "Phones and tablets"),
        ("Leaderboard", "Game Center", "Google Play Games"),
        ("Orientation", "Landscape", None),
        ("Controls", "Device tilt (motion sensor required)", None),
        ("Price", "Free, with optional in-app purchases", None),
    ],
    'help_h': "Need help?",
    'help': "Stuck on a level, missing a purchase, or found a bug? The <a href=\"{SUPPORT}\">support page</a> covers the most common questions on both platforms, and you can always message us on Instagram at {IG}.",
    'help_btn': "Go to Support",
},
'support': {
    'title': "Ferroll — Support",
    'meta': "Support and frequently asked questions for Ferroll, the tilt-controlled maze game for iPhone, iPad and Android.",
    'h': "Support",
    'intro': "Every question below is answered from how the game actually works, on iPhone, iPad and Android. If none of it solves your problem, message us on Instagram — we read every message.",
    'contact': "<strong>Contact:</strong> send a direct message on Instagram to {IG}",
    'contact_note': "To help us reproduce a problem quickly, please include your <strong>device model</strong>, your <strong>iOS or Android version</strong>, the <strong>game version</strong> and the <strong>level number</strong> where it happened. We usually reply within 2&ndash;3 business days.",
    'sections': [
        ("Playing the game", [
            ("How do I control the ball?", [
                "You tilt the device — there is no on-screen joystick. Hold your phone or tablet flat and tip it in the direction you want the ball to roll. The ball has real weight, so it keeps moving after you level the device out. Ferroll is landscape-only and needs a working motion sensor (accelerometer)."]),
            ("The level started but the ball won't move.", [
                "At the start of every level the ball sits inside a glass cage. Tap the cage to shatter it and the level begins. The timer does not run until you do."]),
            ("The exit door won't open.", [
                "You must collect every gem in the level first. The counter in the top-right corner shows your progress (for example 2 / 6). Once it is complete the door opens and you can roll into it."]),
            ("The controls feel drifty or too sensitive.", [
                "The game reads your device's tilt relative to how you are holding it, so play in a stable position — sitting down works best. Playing while lying flat on your back is the usual cause of a ball that drifts on its own, because the device has almost no tilt reference in that position."]),
            ("How do I earn three stars?", [
                "Stars depend on two things: how much time is left when you finish, and how many times you died. Finishing with over half the timer remaining earns three stars. Dying once caps you at two stars, and dying twice or more — or running out of time — drops you to one star. Only a flawless run with no deaths can set a new best-time record."]),
            ("I keep dying to the ghosts.", [
                "Ghosts always warn you before they move. They appear in a wall and glow in place for a moment before charging down the corridor, and you'll hear them if you're close. That pause is your cue to get out of the corridor. Over long corridors they briefly phase out and become harmless — you can pass through them at that moment."]),
            ("Time ran out in Endless mode. Can I keep going?", [
                "Once per run, yes. When the clock hits zero you can watch an optional video to get 30 more seconds and continue from where you were. The usual 200-point penalty for continuing applies. If time runs out a second time in the same run, the run ends."]),
        ]),
        ("Purchases and lives", [
            ("I bought \"Remove Ads\" but the ads came back.", [
                "Open the in-game <strong>Store</strong> and tap <strong>RESTORE PURCHASES</strong>. This re-checks your purchase with the store and re-applies it. Make sure you are signed in with the same account you used to buy it: your <strong>Apple Account</strong> on iPhone and iPad, or your <strong>Google account</strong> in the Play Store on Android. Restoring is free and can be done as many times as you need. Purchases don't carry over between iOS and Android."]),
            ("What does \"Remove Ads\" actually remove?", [
                "It removes the full-screen video ads that appear between levels. You can still choose to watch an optional video to earn a free life — that stays available on purpose. Buying it also unlocks the theme selector in Endless mode."]),
            ("I ran out of lives. What now?", [
                "You start with three lives. When you die you can spend one to continue where you fell, or watch a short optional video to continue for free. Since version 1.5, lives also refill on their own: you get one back every 20 minutes until you have three again. The countdown is shown in the Store and on the revive screen. You can also buy life packs in the Store. Resetting your progress will not delete lives you purchased."]),
            ("My purchase was charged but nothing arrived.", [
                "First try <strong>RESTORE PURCHASES</strong> in the Store. If the purchase still doesn't appear, message us on Instagram at {IG} with a screenshot of your receipt and we'll sort it out. Refunds are handled by the store you bought from:",
                "{IOS} <a href=\"https://reportaproblem.apple.com\">reportaproblem.apple.com</a><br>{AND} <a href=\"https://support.google.com/googleplay/answer/2479637\">Google Play refund help</a>"]),
        ]),
        ("Progress, sound and leaderboards", [
            ("How do I reset my progress?", [
                "Go to <strong>Settings</strong> from the main menu and tap <strong>RESET PROGRESS</strong>. This clears your unlocked levels, stars and best times, and it cannot be undone. Your leaderboard records, your purchased lives and your \"Remove Ads\" purchase are all kept."]),
            ("There's no sound.", [
                "Check the speaker button on the game screen (it mutes the current session) and the Music and Sound FX settings in <strong>Settings</strong>, where each has its own volume. Then check your device:",
                "{IOS} Ferroll respects the silent switch, so the game stays quiet when your iPhone is on silent.<br>{AND} Turn up the media volume with the volume buttons while the game is open."]),
            ("Does the game stop my music?", [
                "{IOS} No. On iPhone and iPad, Ferroll mixes with whatever you are already listening to, so your music or podcast keeps playing. If you'd rather hear only your own audio, turn Music off in Settings."]),
            ("My Endless score isn't on the leaderboard.", [
                "Scores are submitted automatically when a run ends, as long as you are signed in to the leaderboard service on your device. Sign in, then play one more run.",
                "{IOS} Game Center: <strong>Settings &rarr; Game Center</strong>.<br>{AND} Google Play Games: open the Play Games app and sign in."]),
            ("The game says there's no internet connection.", [
                "Ads need a connection, so the free version asks you to reconnect. The \"Remove Ads\" purchase disables that message entirely."]),
            ("I got interrupted by a call and lost the level.", [
                "{IOS} Since version 1.4 the game pauses itself when you leave the app, and your remaining time is preserved. If you're still seeing this, please update to the latest version from the App Store."]),
        ]),
    ],
    'stuck_h': "Still stuck?",
    'stuck': "Message {IG} on Instagram and describe what happened. Bug reports genuinely help — several fixes in recent updates came straight from player messages.",
},
'privacy': {
    'title': "Ferroll — Privacy Policy",
    'meta': "Privacy Policy for Ferroll, the tilt-controlled maze game for iPhone, iPad and Android.",
    'h': "Privacy Policy",
    'updated': "Last updated: 14 October 2026",
    'translation_note': None,
    'intro': "This policy explains what happens to your data when you play <strong>Ferroll</strong> (\"the app\"), published by Mustafa Yağız (\"we\", \"us\"). It applies to the iOS app distributed on the Apple App Store and to the Android app distributed on Google Play.",
    'short': "<strong>In short:</strong> we do not run any servers and we do not collect, store or receive any personal information about you. Your game progress never leaves your device. The only third parties involved are Apple (on iOS) and Google, described below.",
    'sections': [
        ("Data stored on your device", [
            ('p', "Your unlocked levels, stars, best times, remaining lives, life refill timer and your sound, music and haptics settings are saved locally on your device, using the platform's standard app storage on iOS and the app's private storage on Android. This data is not transmitted anywhere, we cannot read it, and it is deleted when you delete the app.")]),
        ("Motion sensor", [
            ('p', "The app reads your device's accelerometer to steer the ball. This reading is used only in the moment to move the ball on screen. It is never recorded, stored or transmitted.")]),
        ("Third-party services", [
            ('h3', "Google AdMob (advertising)"),
            ('p', "The free version of the app shows ads through Google AdMob. To deliver and measure those ads, Google may collect information such as your device's advertising identifier, IP address, device type and your interactions with ads. We never see this data ourselves; it is handled by Google under its own policies."),
            ('p', "In the European Economic Area, the United Kingdom and Switzerland, the app shows Google's consent form before any ads are requested, on both iOS and Android. You can change your choice at any time from <strong>Settings &rarr; Privacy Options</strong> inside the game."),
            ('p', "{IOS} The app also asks for your permission before any tracking identifier can be used. If you decline, you will still see ads, but they will be non-personalised. You can change this choice at any time in <strong>iOS Settings &rarr; Privacy &amp; Security &rarr; Tracking</strong>."),
            ('p', "{AND} Ads may use your device's advertising ID. You can reset or delete it in your device settings (on most devices <strong>Settings &rarr; Privacy &rarr; Ads</strong>, or <strong>Settings &rarr; Google &rarr; Ads</strong>). Once deleted, you will still see ads, but they will not be personalised."),
            ('p', "Buying the \"Remove Ads\" in-app purchase stops the app from requesting the full-screen ads between levels. Optional rewarded videos, which you can choose to watch for a free life, are only requested when you open a screen that offers one."),
            ('p', "Google's handling of this data is described in the <a href=\"https://policies.google.com/technologies/partner-sites\">Google Privacy &amp; Terms</a> and the <a href=\"https://support.google.com/admob/answer/6128543\">AdMob policies</a>."),
            ('h3', "Leaderboards (Game Center and Google Play Games)"),
            ('p', "If you are signed in to the leaderboard service on your device, your Endless mode score is submitted to the Ferroll leaderboard so it can be ranked against other players. On iOS this is Apple Game Center; on Android it is Google Play Games. The name shown on the leaderboard is the one set in your Game Center or Play Games profile — not something the app creates. You can opt out by signing out of Game Center (iOS Settings) or Google Play Games (the Play Games app); the game remains fully playable."),
            ('h3', "In-app purchases"),
            ('p', "Purchases are processed entirely by Apple through the App Store on iOS, and by Google through Google Play Billing on Android. We never receive or store your payment card details, billing address or account credentials. The app is only told whether a purchase succeeded."),
            ('h3', "Version check (iOS)"),
            ('p', "When the main menu opens, the iOS app asks Apple's public App Store lookup service whether a newer version of Ferroll is available. This request contains only the app's own identifier. No information about you is sent."),
        ]),
        ("Android permissions", [
            ('table', [("Permission", "Why the app uses it"),
                       ("Internet and network state", "Load ads, process purchases, submit leaderboard scores and detect when you are offline"),
                       ("Vibration", "Haptic feedback when the ball hits walls or collects gems (can be turned off in Settings)"),
                       ("High sampling rate sensors", "Read the motion sensor fast enough for smooth tilt controls"),
                       ("Advertising ID", "Used by Google AdMob to deliver and measure ads, as described above")]),
            ('p', "The app never asks for your location, contacts, photos, microphone or camera."),
        ]),
        ("Data we collect ourselves", [
            ('table', [("Category", "Collected?"),
                       ("Name, email or account details", "No — the app has no accounts or sign-up"),
                       ("Location", "No"),
                       ("Contacts, photos, microphone, camera", "No — the app never requests them"),
                       ("Health or fitness data", "No"),
                       ("Analytics or crash reporting by us", "No — we run no analytics service"),
                       ("Game progress", "Stored only on your device")]),
        ]),
        ("Children", [
            ('p', "Ferroll contains no chat, no user-generated content and no social features beyond the leaderboards described above. We do not knowingly collect personal information from children. If you believe a child has provided us with personal information, please contact us and we will act on it.")]),
        ("Your choices", [
            ('ul', ["Change your ad consent at any time from <strong>Settings &rarr; Privacy Options</strong> in the game (shown where consent is required).",
                    "{IOS} Refuse or withdraw tracking permission, or reset your advertising identifier, in <strong>iOS Settings &rarr; Privacy &amp; Security &rarr; Tracking</strong>.",
                    "{AND} Reset or delete your advertising ID in your device's ad settings.",
                    "Sign out of Game Center or Google Play Games to stop leaderboard submissions.",
                    "Buy \"Remove Ads\" to stop the full-screen ads between levels.",
                    "Delete the app to erase all locally stored game data."]),
            ('p', "Because we hold no personal data about you on any server, there is nothing for us to export or erase on request. If you would still like to ask about your data, contact us as described below and we will respond."),
        ]),
        ("Changes to this policy", [
            ('p', "If this policy changes, the revised version will be posted on this page with a new \"last updated\" date. Significant changes will also be noted in the App Store and Google Play release notes.")]),
        ("Contact", [
            ('p', "Questions about this policy? Send a direct message on Instagram to {IG}.")]),
    ],
},
}
