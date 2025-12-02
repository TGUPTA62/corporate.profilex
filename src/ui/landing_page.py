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
                body, .gradio-container {
                    background: #f5f7fa;
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                }

                #banner {
                    background: linear-gradient(90deg, #003366 0%, #00509e 100%);
                    padding: 25px 40px 30px 40px;
                    border-radius: 10px;
                    box-shadow: 0 8px 15px rgba(0, 48, 99, 0.3);
                    display: flex;
                    justify-content: space-between;
                    align-items: flex-start;
                    position: relative;
                }

                #heading {
                    color: white;
                    font-size: 36px;
                    font-weight: 800;
                    letter-spacing: 1.3px;
                    margin: 0;
                    user-select: none;
                }

                #tagline {
                    color: #cfd9e8;
                    font-size: 14px;
                    font-weight: 400;
                    font-style: italic;
                    margin: 0;
                    user-select: none;
                }

                .section-heading {
                    margin-top: 40px;
                    margin-bottom: 12px;
                    font-weight: 700;
                    color: #003366;
                }

                /* Textbox styling */
                .gr-textbox {
                    width: 100% !important;
                    font-size: 18px !important;
                    padding: 16px 22px !important;
                    border-radius: 16px !important;
                    border: 2px solid #00509e !important;
                    box-shadow: inset 0 2px 6px rgba(0,0,0,0.1);
                    font-weight: 500;
                    resize: vertical !important;
                    transition: border-color 0.3s ease;
                }
                .gr-textbox::placeholder {
                    color: #a0a9bb !important;
                    font-style: italic;
                }
                .gr-textbox:focus {
                    border-color: #0077ff !important;
                    box-shadow: 0 0 14px #0077ff;
                    outline: none !important;
           
                    }

            /* Button styling */

           .custom-blue-btn {
    background-color: #00509e !important;
    color: white !important;
    border: 2px solid #003366 !important;
    border-radius: 12px !important;
    padding: 10px 26px !important;
    font-weight: 500 !important;
    font-size: 14px !important;
    cursor: pointer !important;
    box-shadow: none !important;
    transition: background-color 0.3s ease, border-color 0.3s ease !important;
    outline: none !important;
}

.custom-blue-btn:hover {
    background-color: #0077ff !important;
    border-color: #00509e !important;
    color: white !important;
}
                
                /* Make progress log full width, dynamic height */
                #progress-log {
                    width: 100% !important;        /* full width */
                    text-align: left !important;   /* left aligned text */
                    white-space: pre-wrap;          /* preserve line breaks & spacing */
                    font-family: monospace, monospace; /* for log-like fixed width font */
                    background-color: #000000;     /* black background */
                    color: #FFFFFF;                /* white text */
                    padding: 16px;                 /* some padding inside */
                    border-radius: 10px;
                    box-sizing: border-box;        /* include padding in width */
                    overflow-x: auto;              /* horizontal scroll if content too wide */
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
