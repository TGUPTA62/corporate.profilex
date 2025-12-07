import gradio as gr
from typing import Generator
import time
import os
from ui.services.autocomplete_engine import (
    get_suggestions,
)


def stream_progress(
    user_input: str = "",
) -> Generator[str, None, None]:
    steps = [
        f"Processing: {user_input}...",
        "Scraping web data...",
        "Analyzing results...",
        "Generating insights...",
        f"**Results for:** {user_input}\n\n- Result 1\n- Result 2\n- Result 3",
    ]
    for step in steps:
        yield step
        time.sleep(1)


def load_css():
    current_dir = os.path.dirname(
        os.path.abspath(__file__)
    )  # → src/ui
    css_path = os.path.join(
        current_dir, "assets", "style.css"
    )  # → src/ui/assets/style.css

    with open(css_path, "r") as f:
        return f"<style>{f.read()}</style>"


def landing_page():

    STAGES = [
        "User Input Received",
        "Entity Normalization",
        "Market & Knowledge Scraping",
        "Raw Data Landed",
        "Document Parsing",
        "Vectorization & RAG Prep",
        "LLM Reasoning & Insights",
        "Frontend Output Rendered",
    ]

    def update_metro(current_stage):
        svg_content = f"""
        <svg width="900" height="120" viewBox="0 0 900 120">
            <!-- Main line -->
            <line x1="50" y1="60" x2="850" y2="60" stroke="#333" stroke-width="8" stroke-linecap="round"/>
            
            <!-- Stations -->
            {''.join([
                f'''
                <circle cx="{80 + i*105}" cy="60" r="22" fill="{"#ff6b6b" if i == current_stage else "#4ecdc4"}" stroke="#333" stroke-width="3"/>
                <text x="{80 + i*105}" y="{{"78" if i == current_stage else "85"}}" text-anchor="middle" font-size="{"13" if i == current_stage else "11"}" 
                    font-weight="{"bold" if i == current_stage else "normal"}" fill="{"white" if i == current_stage else "#333"}">{STAGES[i]}</text>
                '''
                for i in range(len(STAGES))
            ])}
        </svg>
        """
        return gr.update(value=svg_content)

    with gr.Blocks() as demo:

        gr.HTML(load_css())

        with gr.Row(elem_id="banner"):
            gr.HTML(
                """
                <h1 id="heading">CorporateProfileX</h1>
                <p id="tagline">A smart GenAI-powered corporate information profiler.</p>
                """
            )

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

        gr.Markdown(
            "### 🔍 Search Intelligence",
            elem_classes="section-heading",
        )

        with gr.Group():
            user_input = gr.Textbox(
                label=None,
                show_label=False,
                elem_id="my_textbox",
                placeholder="Enter company name e.g., Tesla, Elon Musk, AI Startups, Technology Innovation...",
                lines=2,
                scale=4,
                interactive=True,
            )

            suggestions_dropdown = gr.Dropdown(
                choices=[],
                visible=False,
                label="Suggestions",
                interactive=True,
                elem_id="suggestions_dropdown",
            )

            with gr.Row():
                submit_btn = gr.Button(
                    "🚀 Start Intelligence Search",
                    elem_classes="custom-blue-btn",
                )
                clear_btn = gr.Button(
                    "🔄 Clear Results",
                    elem_classes="custom-blue-btn",
                )

        # Callback to update dropdown suggestions
        def on_user_input(text):
            suggestions = get_suggestions(text)
            visible = len(suggestions) > 0
            return gr.update(
                choices=suggestions,
                value=None,
                visible=visible,
            )

        # When suggestion selected, update textbox value
        def on_suggestion_select(selected):
            return selected

        # Wire events
        user_input.change(
            fn=on_user_input,
            inputs=user_input,
            outputs=suggestions_dropdown,
        )
        suggestions_dropdown.change(
            fn=on_suggestion_select,
            inputs=suggestions_dropdown,
            outputs=user_input,
        )

        gr.Markdown(
            "### ⏳ Metro Line Progress",
            elem_classes="section-heading",
        )

        gr.HTML(
            value="""
    <svg width="100%" height="280" viewBox="0 0 1200 280">
        <!-- Main line -->
        <line x1="60" y1="60" x2="1140" y2="60" stroke="#4a5568" stroke-width="6" stroke-linecap="round"/>
        
        <!-- Stage 0 - CURRENT (#0077ff) -->
        <circle cx="100" cy="60" r="28" fill="#0077ff" stroke="#2c3e50" stroke-width="4"/>
        <text x="100" y="115" text-anchor="middle" font-size="13" font-weight="bold" fill="#2c3e50">User Input</text>
        <text x="100" y="132" text-anchor="middle" font-size="12" font-weight="600" fill="#2c3e50">Received</text>
        <text x="100" y="150" text-anchor="middle" font-size="10" fill="#7f8c8d">1/8</text>
        
        <!-- Stage 1 -->
        <circle cx="240" cy="60" r="28" fill="#95a5a6" stroke="#2c3e50" stroke-width="3"/>
        <text x="240" y="115" text-anchor="middle" font-size="12" font-weight="500" fill="#2c3e50">Entity</text>
        <text x="240" y="132" text-anchor="middle" font-size="12" fill="#2c3e50">Normalization</text>
        <text x="240" y="150" text-anchor="middle" font-size="10" fill="#7f8c8d">2/8</text>
        
        <!-- Stage 2 -->
        <circle cx="380" cy="60" r="28" fill="#95a5a6" stroke="#2c3e50" stroke-width="3"/>
        <text x="380" y="115" text-anchor="middle" font-size="12" font-weight="500" fill="#2c3e50">Market &</text>
        <text x="380" y="132" text-anchor="middle" font-size="12" fill="#2c3e50">Knowledge Scraping</text>
        <text x="380" y="150" text-anchor="middle" font-size="10" fill="#7f8c8d">3/8</text>
        
        <!-- Stage 3 -->
        <circle cx="520" cy="60" r="28" fill="#95a5a6" stroke="#2c3e50" stroke-width="3"/>
        <text x="520" y="115" text-anchor="middle" font-size="12" font-weight="500" fill="#2c3e50">Raw Data</text>
        <text x="520" y="132" text-anchor="middle" font-size="12" fill="#2c3e50">Landed</text>
        <text x="520" y="150" text-anchor="middle" font-size="10" fill="#7f8c8d">4/8</text>
        
        <!-- Stage 4 -->
        <circle cx="660" cy="60" r="28" fill="#95a5a6" stroke="#2c3e50" stroke-width="3"/>
        <text x="660" y="115" text-anchor="middle" font-size="12" font-weight="500" fill="#2c3e50">Document</text>
        <text x="660" y="132" text-anchor="middle" font-size="12" fill="#2c3e50">Parsing</text>
        <text x="660" y="150" text-anchor="middle" font-size="10" fill="#7f8c8d">5/8</text>
        
        <!-- Stage 5 -->
        <circle cx="800" cy="60" r="28" fill="#95a5a6" stroke="#2c3e50" stroke-width="3"/>
        <text x="800" y="115" text-anchor="middle" font-size="12" font-weight="500" fill="#2c3e50">Vectorization</text>
        <text x="800" y="132" text-anchor="middle" font-size="12" fill="#2c3e50">& RAG Prep</text>
        <text x="800" y="150" text-anchor="middle" font-size="10" fill="#7f8c8d">6/8</text>
        
        <!-- Stage 6 -->
        <circle cx="940" cy="60" r="28" fill="#95a5a6" stroke="#2c3e50" stroke-width="3"/>
        <text x="940" y="115" text-anchor="middle" font-size="12" font-weight="500" fill="#2c3e50">LLM Reasoning</text>
        <text x="940" y="132" text-anchor="middle" font-size="12" fill="#2c3e50">& Insights</text>
        <text x="940" y="150" text-anchor="middle" font-size="10" fill="#7f8c8d">7/8</text>
        
        <!-- Stage 7 -->
        <circle cx="1080" cy="60" r="28" fill="#95a5a6" stroke="#2c3e50" stroke-width="3"/>
        <text x="1080" y="115" text-anchor="middle" font-size="12" font-weight="500" fill="#2c3e50">Frontend</text>
        <text x="1080" y="132" text-anchor="middle" font-size="12" fill="#2c3e50">Output Rendered</text>
        <text x="1080" y="150" text-anchor="middle" font-size="10" fill="#7f8c8d">8/8</text>
    </svg>
    """,
            elem_classes="compact-metro",
        )

        gr.Markdown(
            "### 📈 Results",
            elem_classes="section-heading",
        )

        progress_log = gr.Markdown(
            value="",
            elem_id="progress-log",
        )

        submit_btn.click(
            fn=stream_progress,
            inputs=user_input,
            outputs=[progress_log],
        )

        clear_btn.click(
            fn=lambda: ("", ""),
            inputs=None,
            outputs=[
                user_input,
                progress_log,
            ],
        )

    return demo


if __name__ == "__main__":
    demo = landing_page()
    demo.launch()
