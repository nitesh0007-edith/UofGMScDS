#!/usr/bin/env python3
"""
Convert Markdown Report to PDF
Uses markdown2 and reportlab for PDF generation
"""

import sys
import subprocess

# Method 1: Try using pandoc with HTML intermediate
def convert_via_html():
    """Convert MD -> HTML, then use browser print"""
    print("Converting Markdown to HTML...")
    try:
        # Convert to HTML with pandoc
        subprocess.run([
            'pandoc',
            'PROJECT_REPORT_FINAL.md',
            '-o', 'PROJECT_REPORT_FINAL_temp.html',
            '--standalone',
            '--toc',
            '--toc-depth=3',
            '-c', 'https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.2.0/github-markdown.min.css'
        ], check=True)

        print("\n✓ HTML file created: PROJECT_REPORT_FINAL_temp.html")
        print("\nTo convert to PDF:")
        print("  1. Open PROJECT_REPORT_FINAL_temp.html in Chrome/Firefox/Safari")
        print("  2. Press Cmd+P (or Ctrl+P on Windows/Linux)")
        print("  3. Select 'Save as PDF' as the destination")
        print("  4. Save as 'PROJECT_REPORT_FINAL.pdf'")
        print("\nAlternatively, you can use:")
        print("  - An online converter: https://www.markdowntopdf.com/")
        print("  - Chrome headless: google-chrome --headless --print-to-pdf=output.pdf file.html")

        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

# Method 2: Try using Chrome/Chromium headless
def convert_via_chrome():
    """Use Chrome headless to convert HTML to PDF"""
    print("Attempting Chrome headless conversion...")

    # Common Chrome/Chromium paths
    chrome_paths = [
        '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
        '/Applications/Chromium.app/Contents/MacOS/Chromium',
        'google-chrome',
        'chromium',
        'chrome'
    ]

    for chrome_path in chrome_paths:
        try:
            subprocess.run([
                chrome_path,
                '--headless',
                '--disable-gpu',
                '--print-to-pdf=PROJECT_REPORT_FINAL.pdf',
                'PROJECT_REPORT_FINAL_temp.html'
            ], check=True, timeout=30, capture_output=True)

            print(f"\n✓ PDF created successfully: PROJECT_REPORT_FINAL.pdf")
            print(f"  Used: {chrome_path}")
            return True
        except (FileNotFoundError, subprocess.CalledProcessError, subprocess.TimeoutExpired):
            continue

    return False

if __name__ == '__main__':
    # Step 1: Create HTML version
    if not convert_via_html():
        print("\nFailed to create HTML intermediate file.")
        sys.exit(1)

    # Step 2: Try to convert to PDF using Chrome
    print("\nAttempting automatic PDF conversion...")
    if convert_via_chrome():
        print("\n✓ SUCCESS! PDF file is ready for submission.")
    else:
        print("\n⚠ Automatic PDF conversion failed.")
        print("Please follow the manual steps above to create the PDF.")
