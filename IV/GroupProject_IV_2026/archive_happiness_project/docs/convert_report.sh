#!/bin/bash
# Convert PROJECT_REPORT_FINAL.md to various formats
# Usage: ./convert_report.sh [docx|pdf|html|all]

FORMAT=${1:-docx}

echo "Converting PROJECT_REPORT_FINAL.md..."

case $FORMAT in
  docx)
    echo "Creating DOCX format..."
    pandoc PROJECT_REPORT_FINAL.md -o PROJECT_REPORT_FINAL.docx \
      --toc \
      --toc-depth=3 \
      --highlight-style=tango
    echo "✓ Created: PROJECT_REPORT_FINAL.docx"
    ;;

  pdf)
    echo "Creating PDF format..."
    # First create HTML
    pandoc PROJECT_REPORT_FINAL.md -o PROJECT_REPORT_FINAL_temp.html \
      --standalone \
      --toc \
      --toc-depth=3

    # Then convert to PDF using Chrome
    /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome \
      --headless \
      --disable-gpu \
      --print-to-pdf=PROJECT_REPORT_FINAL.pdf \
      PROJECT_REPORT_FINAL_temp.html

    rm PROJECT_REPORT_FINAL_temp.html
    echo "✓ Created: PROJECT_REPORT_FINAL.pdf"
    ;;

  html)
    echo "Creating HTML format..."
    pandoc PROJECT_REPORT_FINAL.md -o PROJECT_REPORT_FINAL.html \
      --standalone \
      --toc \
      --toc-depth=3 \
      --css=https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.2.0/github-markdown.min.css
    echo "✓ Created: PROJECT_REPORT_FINAL.html"
    ;;

  all)
    echo "Creating all formats..."
    $0 docx
    $0 pdf
    $0 html
    ;;

  *)
    echo "Unknown format: $FORMAT"
    echo "Usage: $0 [docx|pdf|html|all]"
    exit 1
    ;;
esac

echo ""
echo "Files in docs directory:"
ls -lh PROJECT_REPORT_FINAL.* 2>/dev/null | awk '{print "  " $9 " (" $5 ")"}'
