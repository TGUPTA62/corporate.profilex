# Main entrypoint - launches the Gradio UI

import sys
from pathlib import Path

# Add src to path for imports
sys.path.insert(
    0, str(Path(__file__).parent / "src")
)

from ui.landing_page import landing_ui

if __name__ == "__main__":
    demo = landing_ui()
    demo.launch()
