import gradio as gr
from pathlib import Path
from typing import Generator


def stream_progress(
    user_input: str,
) -> Generator[str, None, None]:
    yield f"Processing: {user_input}..."
    yield "Scraping web data..."
    yield "Analyzing results..."
    yield "Generating insights..."
    yield f"**Results for:** {user_input}\n\n- Result 1\n- Result 2\n- Result 3"


LOGO_PATH = "src/ui/assets/emiratesNBD_logo.png"


def landing_page():
    with gr.Blocks() as demo:
        gr.HTML(
            """
            <style>
                body, .gradio-container {
                    background: #f5f7fa;
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                }

                /* Banner container with flex for vertical layout */
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

                /* Left content (heading + tagline) stacked vertically */
                #banner-text {
                    display: flex;
                    flex-direction: column;
                    gap: 8px;
                }

                /* Heading: large, bold, white */
                #heading {
                    color: white;
                    font-size: 36px;
                    font-weight: 800;
                    letter-spacing: 1.3px;
                    margin: 0;
                    user-select: none;
                }

                /* Tagline below heading, smaller and lighter */
                #tagline {
                    color: #cfd9e8;
                    font-size: 14px;
                    font-weight: 400;
                    font-style: italic;
                    margin: 0;
                    user-select: none;
                }

              

                /* Input + button row styling */
                .input-row {
                    display: flex;
                    gap: 15px;
                    justify-content: center;
                    margin-top: 45px;
                    margin-bottom: 25px;
                    max-width: 600px;
                    width: 100%;
                }

                .gr-textbox {
                    flex-grow: 1 !important;
                    font-size: 18px !important;
                    padding: 14px 20px !important;
                    border-radius: 12px !important;
                    border: 1.8px solid #00509e !important;
                    box-shadow: inset 0 1px 3px rgba(0,0,0,0.1);
                    transition: border-color 0.3s ease;
                }

                .gr-textbox:focus {
                    border-color: #0077ff !important;
                    box-shadow: 0 0 8px #0077ff;
                    outline: none !important;
                }

                .gr-button {
                    background: #00509e;
                    color: white;
                    font-weight: 700;
                    font-size: 18px;
                    padding: 14px 36px;
                    border-radius: 12px;
                    border: none;
                    box-shadow: 0 4px 12px rgba(0,80,158,0.4);
                    cursor: pointer;
                    transition: background 0.3s ease, box-shadow 0.3s ease;
                    user-select: none;
                }

                .gr-button:hover {
                    background: #0077ff;
                    box-shadow: 0 6px 18px rgba(0,119,255,0.6);
                }

                .gr-markdown {
                    max-width: 700px;
                    margin: 0 auto;
                    margin-top: 30px;
                    font-size: 18px;
                    color: #222;
                    line-height: 1.6;
                    background: white;
                    padding: 20px 28px;
                    border-radius: 12px;
                    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
                    user-select: text;
                }

                .gr-block {
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    padding: 40px 20px 60px 20px;
                }

            </style>
            """
        )

        # Banner content with separate div for heading+tagline (left) and logo (right)
        with gr.Row(elem_id="banner"):
            gr.HTML(
                """
                <div id="banner-text">
                    <h1 id="heading">CorporateProfileX</h1>
                    <p id="tagline">A smart GenAI-powered corporate information profiler.</p>
                </div>
                """
            )

        # Input and button in a styled row
        with gr.Row(elem_classes="input-row"):
            user_input = gr.Textbox(
                label="Enter Company Name",
                placeholder="Start typing...",
                # interactive=True,
            )
            submit = gr.Button("Search")

        output = gr.Markdown()

        submit.click(
            lambda x: f"Searching for **{x}** ...",
            user_input,
            output,
        )

    return demo


if __name__ == "__main__":
    demo = landing_page()
    demo.launch()
