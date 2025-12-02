import gradio as gr
from typing import Generator
import time


def stream_progress(
    user_input: str,
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


def landing_page():
    with gr.Blocks() as demo:

        gr.HTML(
            """
         <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;700;800&display=swap');

    body, .gradio-container {
        background: #f5f7fa;
        font-family: 'Poppins', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        color: #1a1a1a;
        line-height: 1.5;
        letter-spacing: 0.02em;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
    }

    #banner {
        background: linear-gradient(90deg, #003366 0%, #00509e 100%);
        padding: 25px 40px 30px 40px;
        border-radius: 12px;
        box-shadow: 0 10px 20px rgba(0, 48, 99, 0.35);
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        position: relative;
        user-select: none;
    }

    #heading {
        color: white;
        font-size: 36px;
        font-weight: 600;
        letter-spacing: 0.08em;
        margin: 0;
        # text-transform: uppercase;
        text-shadow: 0 2px 6px rgba(0,0,0,0.3);
    }

    #tagline {
        color: #cfd9e8;
        font-size: 14px;
        font-weight: 400;
        font-style: italic;
        margin-top: 6px;
        user-select: none;
        text-shadow: 0 1px 4px rgba(0,0,0,0.15);
    }

    .section-heading {
        margin-top: 48px;
        margin-bottom: 16px;
        font-weight: 700;
        color: #003366;
        letter-spacing: 0.05em;
        font-size: 22px;
        user-select: none;
    }

    /* Textbox styling */
    .gr-textbox {
    width: 100% !important;
    font-size: 18px !important;
    padding: 18px 24px !important;
    border-radius: 24px !important;
    border: 2px solid #2a60b8 !important;
    background: linear-gradient(145deg, #e6ecf9, #cbd8f7) !important;
    box-shadow: 
        inset 2px 2px 6px rgba(255, 255, 255, 0.9),
        inset -3px -3px 7px rgba(140, 160, 190, 0.7);
    font-weight: 500;
    font-family: 'Poppins', sans-serif !important;
    resize: vertical !important;
    transition: border-color 0.3s ease, box-shadow 0.3s ease;
}

.gr-textbox::placeholder {
    color: #6a7aab !important;
    font-style: italic;
    letter-spacing: 0.03em;
}

.gr-textbox:focus {
    border-color: #0057ff !important;
    background: linear-gradient(145deg, #d7e2ff, #a4b8ff) !important;
    box-shadow:
        0 0 8px 3px rgba(0, 87, 255, 0.6),
        inset 2px 2px 6px rgba(255, 255, 255, 0.9),
        inset -3px -3px 7px rgba(100, 130, 255, 0.8);
    outline: none !important;
}

    /* Button styling */
    .custom-blue-btn {
        background-color: #00509e !important;
        color: white !important;
        border: 2.5px solid #003366 !important;
        border-radius: 16px !important;
        padding: 8px 20px !important;
        font-weight: 600 !important;
        font-size: 14px !important;
        cursor: pointer !important;
        box-shadow: 0 6px 12px rgba(0,80,158,0.45);
        transition: background-color 0.35s ease, border-color 0.35s ease, box-shadow 0.35s ease !important;
        font-family: 'Poppins', sans-serif !important;
        user-select: none;
    }

    .custom-blue-btn:hover {
        background-color: #0077ff !important;
        border-color: #004a90 !important;
        box-shadow: 0 8px 18px rgba(0,119,255,0.6);
        color: white !important;
    }

    /* Make progress log full width, dynamic height */
    #progress-log {
        width: 100% !important;
        text-align: left !important;
        white-space: pre-wrap;
        font-family: 'Courier New', Courier, monospace;
        background-color: #000000;
        color: #FFFFFF;
        padding: 18px 24px;
        border-radius: 12px;
        box-sizing: border-box;
        overflow-x: auto;
        font-size: 15px;
        line-height: 1.4;
        user-select: text;
        box-shadow: 0 0 14px rgba(0,0,0,0.8);
    }


    .feature-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
        gap: 20px;
        margin-top: 50px;
        margin-bottom: 40px;
    }

    .feature-card {
        background: white;
        border-radius: 16px;
        box-shadow: 0 8px 20px rgba(0, 80, 158, 0.12);
        padding: 24px 28px;
        text-align: center;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        cursor: default;
    }

    .feature-card:hover {
        transform: translateY(-6px);
        box-shadow: 0 16px 40px rgba(0, 80, 158, 0.22);
    }

    .feature-card h3 {
        font-family: 'Poppins', sans-serif;
        font-weight: 700;
        font-size: 20px;
        color: #003366;
        margin-bottom: 10px;
    }

    .feature-card p {
        font-family: 'Poppins', sans-serif;
        font-weight: 500;
        font-size: 14px;
        color: #4a5a7a;
        line-height: 1.4;
    }


</style>

            """
        )

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
                placeholder="e.g., Tesla, Elon Musk, AI Startups, Technology Innovation...",
                label="Enter company name, person, or topic",
                lines=2,
                scale=4,
                interactive=True,
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
            outputs=progress_log,
        )

        clear_btn.click(
            fn=lambda: ("", ""),
            inputs=None,
            outputs=[user_input, progress_log],
        )

    return demo


if __name__ == "__main__":
    demo = landing_page()
    demo.launch()
