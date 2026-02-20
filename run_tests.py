import subprocess
import sys


def main() -> int:
    completed = subprocess.run([sys.executable, "-m", "pytest", "-q"], check=False)
    return completed.returncode


if __name__ == "__main__":
    sys.exit(main())
