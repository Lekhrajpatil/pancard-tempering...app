# PAN Card Tampering Detection

A clean, fast Flask app that compares a PAN card image against a known original and highlights differences. Perfect for demos, proof‑of‑concepts, and document QA.

## Why this exists
When documents get edited, it’s not always obvious what changed. This tool gives you:
- A similarity score (how close is the upload to the original?)
- Visual overlays that mark changed regions
- A simple, modern UI that works locally

## Quick start
1. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
2. Provide the reference image
   - Save your original PAN image as `image.jpg` in `app/static/original/`
3. Run the app
   ```bash
   python app.py
   ```
4. Visit the UI
   - Open `http://localhost:5000`
   - Upload the PAN image you want to verify

## What you’ll see
- A clear similarity percentage
- Four views: Original, Uploaded, Difference Map, Threshold
- Red rectangles highlighting suspicious areas

## Project layout
```
app/
  __init__.py              # Flask app init & blueprint registration
  views.py                 # Routes + upload/compare flow
  models/
    tampering_detector.py  # SSIM-based comparison + result saving
  utils/
    image_processor.py     # Small helpers for image IO/resize/validate
  static/
    css/style.css          # Styles (no inline CSS in templates)
    js/main.js             # Client-side UX (drag/drop, preview, loading)
    uploads/               # Uploaded images
    original/              # Reference image (image.jpg)
    generated/             # Output images written by the app
  templates/
    index.html             # Main UI (clean copy + external assets)

config.py                  # Basic Flask config
requirements.txt           # Dependencies
README.md                  # This file
```

## How it works (brief)
- The app resizes both images to a consistent size
- Converts them to grayscale
- Uses Structural Similarity (SSIM) to compute a diff
- Thresholds the diff to find changed regions
- Draws boxes on both images and saves all outputs under `app/static/generated/`

## Tips
- Keep the reference image crisp and well-lit for best results
- If everything looks identical but score is low, ensure both images are the same aspect ratio (the app resizes, but quality matters)
- Very heavy compression can reduce accuracy

## Testing
Run the included tests:
```bash
python -m unittest discover tests
```

## Deploying
- Local (dev): `python app.py`
- Production (example): `gunicorn -w 4 -b 0.0.0.0:5000 app:app`

## License
MIT. Use it, extend it, and have fun.
