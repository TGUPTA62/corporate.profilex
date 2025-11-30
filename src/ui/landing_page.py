import gradio as gr
from pathlib import Path
from typing import Generator
import os

# Import components
try:
    from components.progress_stream import (
        stream_progress,
    )
except ImportError:
    # Fallback if import fails
    def stream_progress(
        user_input: str,
    ) -> Generator[str, None, None]:
        """Fallback streaming function"""
        yield f"Processing: {user_input}..."
        yield "Scraping web data..."
        yield "Analyzing results..."
        yield "Generating insights..."
        yield f"**Results for:** {user_input}\n\n- Result 1\n- Result 2\n- Result 3"


def landing_ui():
    """Create the main landing page UI for CorporateProfileX"""

    with gr.Blocks() as demo:
        # Direct style injection with maximum specificity
        gr.HTML(
            """
        <style>
        :root {
            --primary-blue: #12284C;
            --accent-yellow: #FDB913;
            --text-grey: #404040;
            --bg-white: #FFFFFF;
        }
        
        body, .gradio-container {
            background: linear-gradient(135deg, #FFFFFF 0%, #F5F5F5 100%) !important;
        }
        
        .gradio-container {
            color: var(--text-grey) !important;
        }
        
        h1, h2, h3, h4, h5, h6 {
            color: var(--primary-blue) !important;
        }
        
        button {
            background: linear-gradient(135deg, #12284C 0%, #1a3a6b 100%) !important;
            color: white !important;
            border: 2px solid #12284C !important;
            border-radius: 8px !important;
        }
        
        button:hover {
            background: linear-gradient(135deg, #FDB913 0%, #ffb700 100%) !important;
            color: #12284C !important;
            border-color: #FDB913 !important;
        }
        
        input, textarea {
            background: white !important;
            color: var(--text-grey) !important;
            border: 2px solid var(--primary-blue) !important;
            border-radius: 8px !important;
        }
        
        input:focus, textarea:focus {
            border-color: var(--accent-yellow) !important;
            box-shadow: 0 0 15px rgba(253, 185, 19, 0.3) !important;
        }
        
        .group-box, .component-box {
            background: white !important;
            border: 2px solid var(--primary-blue) !important;
            border-radius: 12px !important;
            box-shadow: 0 4px 15px rgba(18, 40, 76, 0.1) !important;
        }
        
        .label {
            color: var(--primary-blue) !important;
            font-weight: 600 !important;
        }
        </style>
        """
        )

        # Header
        gr.HTML(
            """
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 3rem; padding: 2rem; background: linear-gradient(135deg, #12284C 0%, #1a3a6b 100%); border-radius: 12px; box-shadow: 0 10px 40px rgba(18, 40, 76, 0.2);">
            <div>
                <h1 style="color: #FDB913; font-size: 2.5rem; font-weight: 700; margin: 0; text-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);">🎯 CorporateProfileX</h1>
                <p style="color: #FFFFFF; font-size: 1rem; margin: 0.5rem 0 0 0; font-weight: 300; letter-spacing: 0.5px;">Professional AI-Powered Corporate Intelligence Platform</p>
            </div>
            <div style="text-align: right;">
                <div style="font-size: 3.5rem; font-weight: 700; color: #FDB913; letter-spacing: 2px;">NBD</div>
                <div style="color: #FFFFFF; font-size: 0.8rem; font-weight: 600; letter-spacing: 1px;">Emirates</div>
            </div>
        </div>
        """
        )

        # Description
        gr.Markdown(
            """
            ### 📊 Platform Overview
            
            CorporateProfileX leverages **multi-agent AI systems** to deliver comprehensive corporate intelligence in real-time.
            """
        )

        gr.Markdown("")  # Spacing

        # Search section
        gr.Markdown("### 🔍 Search Intelligence")
        gr.Markdown("")  # Spacing

        with gr.Group():
            user_input = gr.Textbox(
                placeholder="e.g., Tesla, Elon Musk, AI Startups, Technology Innovation...",
                label="Enter company name, person, or topic",
                lines=2,
                scale=4,
            )

            with gr.Row():
                submit_btn = gr.Button(
                    "🚀 Start Intelligence Search",
                    variant="primary",
                    scale=2,
                )
                clear_btn = gr.Button(
                    "🔄 Clear Results", scale=1
                )

        # Output section
        gr.Markdown("### 📈 Results")
        gr.Markdown("")  # Spacing

        output = gr.Markdown(
            value="Results will appear here...",
            label="Search Results",
        )

        # Event handlers
        submit_btn.click(
            fn=stream_progress,
            inputs=user_input,
            outputs=output,
        )

        clear_btn.click(
            fn=lambda: (
                "",
                "Results cleared. Ready for new search.",
            ),
            outputs=[user_input, output],
        )

        # Features section
        gr.Markdown("### ✨ Key Features")
        gr.Markdown("")  # Spacing

        gr.HTML(
            """
        <div class="feature-grid">
            <div class="feature-card">
                <h3>🤖 Multi-Agent AI</h3>
                <p>Specialized AI agents work in parallel for different analysis tasks</p>
            </div>
            <div class="feature-card">
                <h3>⚡ Real-time Updates</h3>
                <p>Live streaming of search progress with instant notifications</p>
            </div>
            <div class="feature-card">
                <h3>🌐 Data Integration</h3>
                <p>Multiple data sources for comprehensive and accurate insights</p>
            </div>
            <div class="feature-card">
                <h3>📊 Advanced Analytics</h3>
                <p>Deep insights, trend analysis, and predictive intelligence</p>
            </div>
        </div>
        """
        )

        # Info section
        gr.Markdown("### 💡 Quick Tips")
        gr.Markdown("")  # Spacing
        gr.Markdown(
            """
            **Best Practices:**
            - Use specific company names for accurate results
            - Add industry keywords for focused searches
            """
        )

    return demo


def create_app():
    """Create and launch the Gradio app"""
    demo = landing_ui()
    return demo


if __name__ == "__main__":
    app = create_app()
    app.launch(
        server_name="127.0.0.1",
        server_port=7860,
        share=False,
        debug=True,
    )
