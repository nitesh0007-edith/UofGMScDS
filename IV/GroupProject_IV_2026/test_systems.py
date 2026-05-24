"""
Quick test script to verify all systems can load data correctly
"""
import subprocess
import sys
import time

systems = [
    ("System A", "SystemA/system_a.py"),
    ("System B", "SystemB/system_b.py"),
    ("System C", "SystemC/system_c.py"),
    ("Generalized Selection", "SystemA/system_a_with_generalization.py")
]

print("Testing all systems...\n")
print("=" * 60)

for name, path in systems:
    print(f"\nTesting {name}...")
    print(f"Path: {path}")

    # Try to import and check data loading
    try:
        result = subprocess.run(
            [sys.executable, "-c", f"""
import sys
sys.path.insert(0, '.')
exec(open('{path}').read().split('if __name__')[0])
print('✓ Data loaded successfully: {{}} records'.format(len(df)))
"""],
            capture_output=True,
            text=True,
            timeout=10
        )

        if result.returncode == 0:
            print(f"✓ {name}: SUCCESS")
            print(f"  Output: {result.stdout.strip()}")
        else:
            print(f"✗ {name}: FAILED")
            print(f"  Error: {result.stderr[:200]}")
    except Exception as e:
        print(f"✗ {name}: EXCEPTION")
        print(f"  Error: {e}")

print("\n" + "=" * 60)
print("Testing complete!")
