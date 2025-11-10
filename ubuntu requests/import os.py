import os
import requests
import hashlib
from urllib.parse import urlparse

# ---- SAFETY CONFIG ----
MAX_FILE_SIZE_MB = 10
ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"}
FETCH_DIR = "Fetched_Images"
HASH_LOG_FILE = "image_hashes.txt"


def is_safe_url(url):
    """Ensure HTTPS and allowed extension."""
    parsed = urlparse(url.strip())
    if parsed.scheme != "https":
        print(f"⚠ Skipping non-HTTPS URL: {url}")
        return False

    ext = os.path.splitext(parsed.path)[1].lower()
    if ext not in ALLOWED_EXTENSIONS:
        print(f"⚠ Unsupported file type ({ext}) for URL: {url}")
        return False

    return True


def calculate_hash(content):
    """Compute SHA256 hash fingerprint."""
    return hashlib.sha256(content).hexdigest()


def is_duplicate(image_hash):
    """Check if this hash was seen before."""
    if not os.path.exists(HASH_LOG_FILE):
        return False
    with open(HASH_LOG_FILE, "r") as f:
        return image_hash in {line.strip() for line in f}


def log_hash(image_hash):
    """Save new hash to the log file."""
    with open(HASH_LOG_FILE, "a") as f:
        f.write(image_hash + "\n")


def is_safe_content(headers):
    """Inspect HTTP headers for content safety."""
    content_type = headers.get("Content-Type", "").lower()
    if not content_type.startswith("image/"):
        print(f"⚠ Not an image: {content_type}")
        return False

    content_length = headers.get("Content-Length")
    if content_length:
        size_mb = int(content_length) / (1024 * 1024)
        if size_mb > MAX_FILE_SIZE_MB:
            print(f"⚠ File too large ({size_mb:.1f} MB > {MAX_FILE_SIZE_MB} MB)")
            return False

    return True


def fetch_image(url):
    """Fetch and save one image with header validation."""
    try:
        if not is_safe_url(url):
            return

        os.makedirs(FETCH_DIR, exist_ok=True)

        # Use HEAD first to inspect headers without downloading
        head_response = requests.head(url, timeout=10, allow_redirects=True, verify=True)
        if not is_safe_content(head_response.headers):
            return

        # Now safely download
        with requests.get(url, timeout=10, stream=True, verify=True) as r:
            r.raise_for_status()

            # Double-check headers during GET too
            if not is_safe_content(r.headers):
                return

            parsed_url = urlparse(url)
            filename = os.path.basename(parsed_url.path) or "downloaded_image.jpg"

            # Hash check before writing
            content = r.content
            img_hash = calculate_hash(content)
            if is_duplicate(img_hash):
                print(f"⚠ Duplicate detected — skipping {filename}")
                return

            # Ensure unique filename
            base, ext = os.path.splitext(filename)
            filepath = os.path.join(FETCH_DIR, filename)
            counter = 1
            while os.path.exists(filepath):
                filepath = os.path.join(FETCH_DIR, f"{base}_{counter}{ext}")
                counter += 1

            # Save safely
            with open(filepath, "wb") as f:
                f.write(content)

            log_hash(img_hash)
            print(f"✓ Downloaded safely: {filename}")
            print(f"  Saved to: {filepath}\n")

    except requests.exceptions.RequestException as e:
        print(f"✗ Network or request error: {e}")
    except Exception as e:
        print(f"✗ Unexpected error: {e}")


def main():
    print("🛡️  Secure Ubuntu Image Fetcher — Header-Verified Edition")
    print("Inspects HTTP headers before trusting the content.\n")

    urls = []
    while True:
        line = input("URL: ").strip()
        if not line:
            break
        urls.append(line)

    if not urls:
        print("No URLs entered. Exiting.")
        return

    print(f"\nFetching {len(urls)} image(s)...\n")
    for url in urls:
        fetch_image(url)

    print("✅ All tasks completed.")
    print(f"📁 Check '{FETCH_DIR}' for your verified images.\n")


if __name__ == "__main__":
    main()

