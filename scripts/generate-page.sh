#!/bin/bash
# Generate an integration page from the GHL template by replacing platform-specific content
# Usage: ./generate-page.sh <slug> <platform-name> <description> <meta-description>

SLUG="$1"
NAME="$2"  
TEMPLATE="integrations/gohighlevel.html"
OUTPUT="integrations/${SLUG}.html"

if [ -f "$OUTPUT" ]; then
  echo "Already exists: $OUTPUT"
  exit 0
fi

echo "Generating $OUTPUT from template..."
cp "$TEMPLATE" "$OUTPUT"
echo "Created $OUTPUT ($(wc -c < "$OUTPUT") bytes)"
