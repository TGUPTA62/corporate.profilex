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
        # Custom CSS for modern trendy design
        demo.css = """
        * {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        
        body {
            background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
            min-height: 100vh;
        }
        
        .header-container {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 3rem 2rem;
            border-radius: 20px;
            margin-bottom: 2rem;
            box-shadow: 0 20px 60px rgba(102, 126, 234, 0.4);
            text-align: center;
        }
        
        .header-container h1 {
            color: #ffffff;
            font-size: 3rem;
            font-weight: 700;
            margin: 0;
            text-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }
        
        .header-container p {
            color: #e0e7ff;
            font-size: 1.3rem;
            margin: 0.5rem 0 0 0;
            font-weight: 300;
        }
        
        .search-section {
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(10px);
            padding: 2.5rem;
            border-radius: 20px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            margin: 2rem 0;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        }
        
        .search-section h2 {
            color: #667eea;
            font-size: 1.8rem;
            margin-top: 0;
            font-weight: 600;
        }
        
        .search-input-wrapper {
            margin: 1.5rem 0;
        }
        
        .search-input-wrapper input {
            background: rgba(255, 255, 255, 0.1) !important;
            border: 2px solid rgba(102, 126, 234, 0.5) !important;
            border-radius: 12px !important;
            color: #ffffff !important;
            font-size: 1.1rem !important;
            padding: 15px 20px !important;
            transition: all 0.3s ease !important;
        }
        
        .search-input-wrapper input:focus {
            background: rgba(255, 255, 255, 0.15) !important;
            border-color: #667eea !important;
            box-shadow: 0 0 20px rgba(102, 126, 234, 0.4) !important;
        }
        
        .button-group {
            display: flex;
            gap: 1rem;
            margin-top: 1.5rem;
        }
        
        .button-group button {
            flex: 1;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
            color: white !important;
            border: none !important;
            border-radius: 12px !important;
            padding: 14px 28px !important;
            font-size: 1rem !important;
            font-weight: 600 !important;
            cursor: pointer !important;
            transition: all 0.3s ease !important;
            box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3) !important;
        }
        
        .button-group button:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 15px 40px rgba(102, 126, 234, 0.5) !important;
        }
        
        .button-group button:active {
            transform: translateY(0) !important;
        }
        
        .results-section {
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(10px);
            padding: 2rem;
            border-radius: 20px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            margin-top: 2rem;
            min-height: 200px;
        }
        
        .results-section h2 {
            color: #667eea;
            font-size: 1.8rem;
            margin-top: 0;
            font-weight: 600;
        }
        
        .feature-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 1.5rem;
            margin: 2rem 0;
        }
        
        .feature-card {
            background: rgba(102, 126, 234, 0.1);
            border: 2px solid rgba(102, 126, 234, 0.3);
            border-radius: 16px;
            padding: 1.5rem;
            transition: all 0.3s ease;
            cursor: pointer;
        }
        
        .feature-card:hover {
            background: rgba(102, 126, 234, 0.15);
            border-color: #667eea;
            transform: translateY(-4px);
            box-shadow: 0 12px 30px rgba(102, 126, 234, 0.2);
        }
        
        .feature-card h3 {
            color: #667eea;
            margin-top: 0;
            font-size: 1.3rem;
        }
        
        .feature-card p {
            color: #b4b8d1;
            font-size: 0.95rem;
            line-height: 1.6;
        }
        
        .info-section {
            background: rgba(255, 255, 255, 0.02);
            border-radius: 16px;
            padding: 2rem;
            margin-top: 2rem;
            border: 1px solid rgba(255, 255, 255, 0.05);
        }
        
        .info-section h3 {
            color: #667eea;
            font-size: 1.5rem;
        }
        
        .info-section p, .info-section li {
            color: #b4b8d1;
            line-height: 1.8;
        }
        
        .info-section table {
            width: 100%;
            border-collapse: collapse;
            margin: 1rem 0;
        }
        
        .info-section table th {
            background: rgba(102, 126, 234, 0.2);
            color: #667eea;
            padding: 12px;
            text-align: left;
            border-bottom: 2px solid rgba(102, 126, 234, 0.3);
            font-weight: 600;
        }
        
        .info-section table td {
            padding: 12px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
            color: #b4b8d1;
        }
        
        .info-section table tr:hover {
            background: rgba(102, 126, 234, 0.1);
        }
        
        .markdown h1, .markdown h2, .markdown h3 {
            color: #667eea !important;
        }
        
        .markdown p, .markdown li {
            color: #b4b8d1 !important;
        }
        """

        # Header
        gr.HTML(
            """
        <div class="header-container">
            <h1>🎯 CorporateProfileX</h1>
            <p>Next-Gen AI-Powered Corporate Intelligence Platform</p>
        </div>
        """
        )

        # Description
        gr.Markdown(
            """
            ### 📊 What is CorporateProfileX?
            
            CorporateProfileX is an intelligent platform that leverages **multi-agent AI systems** to:
            - **Scrape** and aggregate company data from multiple sources
            - **Extract** key insights and metrics automatically
            - **Generate** comprehensive corporate profiles in real-time
            - **Provide** actionable intelligence and competitive analysis
            """
        )

        # Search section
        gr.Markdown(
            "### 🔍 Start Your Intelligence Gathering"
        )

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
        gr.Markdown(
            "### 📈 Real-Time Results & Insights"
        )

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
        gr.Markdown("### ✨ Platform Features")

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
        gr.Markdown("### 💡 Tips & Information")
        gr.Markdown(
            """
            **Best Practices:**
            - Use specific company names for targeted results
            - Add industry keywords for focused searches
            - Results include web data, financials, and AI-generated insights
            - Combine multiple queries for comprehensive analysis
            
            **What You Get:**
            - Company Overview & Key Metrics
            - Leadership & Team Information
            - Financial Performance Analysis
            - Industry Trends & Competitive Positioning
            - AI-Generated Insights & Recommendations
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
