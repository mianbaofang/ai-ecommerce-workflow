# HyperFrames Redesign Verification

## What Changed

The five-scene composition now uses a publishing-desk metaphor instead of repeating the same card grid. The cup is shown once as the submitted product and once as a small delivery thumbnail. The middle scenes use two real public-source screenshots, a clearly labeled generic charger fixture, and a generated proofreading surface with all readable copy supplied by HTML.

## Huashu Review

- Baseline review: 6.3/10 overall; the largest issues were repeated cup variants, fixed left/right card structures, and missing real evidence imagery.
- Targeted changes: one visual anchor per scene, source clippings in evidence, second-category fixture in routing, one dominant redline proof, and a non-symmetric final delivery wall.
- Full review and scene plan: [hyperframes-evidence/HUASHU-DESIGN-REVIEW.md](hyperframes-evidence/HUASHU-DESIGN-REVIEW.md).

## Runtime Checks

- `npm run check`: passed; 0 lint errors, 0 runtime errors, 0 layout issues, 0 motion errors, 0 contrast warnings.
- Layout samples: 1.111s, 3.333s, 5.556s, 7.778s, 10s, 12.222s, 14.444s, 16.667s, and 18.889s.
- Motion assertions: 300 samples, all passed.
- Contrast: 78/78 text checks passed WCAG AA.
- Midpoint snapshots: five frames captured directly from the final compressed GIF and reviewed as a contact sheet plus individual evidence and proofreading frames.
- The final output wall keeps subtle movement through the 20-second endpoint; the collision checks passed without layout issues.

## Rendered Artifact

- Source render: 1920×1080, 10 fps, 20.0 seconds, 200 frames, 16,223,001 bytes.
- README GIF: 960×540, 5 fps, 100 frames, 1,933,236 bytes.
- SHA-256: `99B3DCC4DD2A29476D3CC7EE38C6556319D550718CFD7D5282D92001B4536634`.
- Rendered-artifact contact sheet: [hyperframes-evidence/github-spec-contact-sheet.png](hyperframes-evidence/github-spec-contact-sheet.png).

## Browser Checks

The static preview at `http://127.0.0.1:8913/docs/site/hyperframes-promo/index.html` was reloaded and checked in the in-app browser.

- Desktop 1440×810: 16:9 canvas rendered at 1440×810; all 7 images loaded and document overflow remained 1440×810.
- Mobile 390×844: canvas rendered at 390×219.375 and remained centered without horizontal clipping; all 7 images loaded.
- Timed progression: after reload, the submitted-product transform changed between two observations, confirming that the preview is actively running rather than a static image.
- Browser console: no error or warning entries.

This is a local visual and runtime verification. It does not claim merchant-backend approval, price accuracy, search ranking, or automatic publishing.
