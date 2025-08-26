#!/bin/bash
# Ensures favicon.ico exists in the correct location before build

SRC_DIST_FAVICON=~/docker/franklin-be/web-ui/dist/favicon.ico
DST_FAVICON=~/docker/franklin-be/ai_middleware/app/static/favicon.ico

echo "🔍 Checking favicon..."

if [ -f "$DST_FAVICON" ]; then
    echo "✅ Favicon already exists at $DST_FAVICON"
    exit 0
fi

mkdir -p "$(dirname "$DST_FAVICON")"

if [ -f "$SRC_DIST_FAVICON" ]; then
    echo "📦 Copying favicon from Web UI build..."
    cp "$SRC_DIST_FAVICON" "$DST_FAVICON"
elif command -v convert &>/dev/null; then
    echo "🎨 Generating placeholder favicon..."
    convert -size 32x32 xc:transparent -gravity center -pointsize 14         -annotate 0 "F" "$DST_FAVICON"
else
    echo "❌ Could not find favicon source or generate fallback. Please add favicon.ico manually."
    exit 1
fi

echo "✅ Favicon is ready at $DST_FAVICON"
