"""Zip up each system (A, B, C) with shared files for Moodle submission."""

import os
import shutil
import zipfile

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

SYSTEMS = {
    "A": "system_a.py",
    "B": "system_b.py",
    "C": "system_c.py",
}

SHARED_FILES = [
    ("src/data_prep.py", "data_prep.py"),
    ("data/clean_weather_data.csv", "data/clean_weather_data.csv"),
    ("requirements.txt", "requirements.txt"),
    ("output/uofg_logo_boxed.png", "uofg_logo_boxed.png"),
]


def package_all():
    """Create A.zip, B.zip, C.zip in the output/ folder."""
    out_dir = os.path.join(PROJECT_ROOT, "output")
    os.makedirs(out_dir, exist_ok=True)

    for label, system_file in SYSTEMS.items():
        zip_path = os.path.join(out_dir, f"{label}.zip")
        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
            # System-specific source file
            src_path = os.path.join(PROJECT_ROOT, "src", system_file)
            zf.write(src_path, f"{label}/{system_file}")

            # Shared files
            for rel_src, rel_dst in SHARED_FILES:
                abs_src = os.path.join(PROJECT_ROOT, rel_src)
                zf.write(abs_src, f"{label}/{rel_dst}")

            # Generated HTML
            html_name = f"System_{label}.html"
            html_path = os.path.join(out_dir, html_name)
            if os.path.exists(html_path):
                zf.write(html_path, f"{label}/{html_name}")

        print(f"Created {zip_path}")


if __name__ == "__main__":
    package_all()
