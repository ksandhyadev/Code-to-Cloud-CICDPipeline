import os
from flask import Flask, render_template_string, jsonify

app = Flask(__name__)

# Modern, responsive landing page with dark-mode aesthetic
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DevOps CI/CD Pipeline</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Inter', sans-serif;
            background: radial-gradient(circle at 20% 20%, #1a1e2e 0%, #0c0e17 100%);
            color: #f1f5f9;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 24px;
            overflow-x: hidden;
        }

        .container {
            width: 100%;
            max-width: 820px;
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border-radius: 20px;
            padding: 48px 40px;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.6);
            position: relative;
        }

        .container::before {
            content: '';
            position: absolute;
            top: -1px;
            left: 20%;
            right: 20%;
            height: 2px;
            background: linear-gradient(90deg, transparent, #38bdf8, #818cf8, transparent);
        }

        .badge-container {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            margin-bottom: 24px;
        }

        .badge {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: rgba(16, 185, 129, 0.15);
            color: #34d399;
            border: 1px solid rgba(52, 211, 153, 0.3);
            padding: 6px 14px;
            border-radius: 9999px;
            font-size: 0.85rem;
            font-weight: 600;
            letter-spacing: 0.02em;
        }

        .pulse-dot {
            width: 8px;
            height: 8px;
            background-color: #34d399;
            border-radius: 50%;
            box-shadow: 0 0 0 0 rgba(52, 211, 153, 0.7);
            animation: pulse 2s infinite;
        }

        @keyframes pulse {
            0% {
                box-shadow: 0 0 0 0 rgba(52, 211, 153, 0.7);
            }
            70% {
                box-shadow: 0 0 0 10px rgba(52, 211, 153, 0);
            }
            100% {
                box-shadow: 0 0 0 0 rgba(52, 211, 153, 0);
            }
        }

        h1 {
            font-size: 2.5rem;
            font-weight: 800;
            text-align: center;
            line-height: 1.25;
            margin-bottom: 16px;
            background: linear-gradient(135deg, #ffffff 0%, #cbd5e1 50%, #94a3b8 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .highlight-text {
            color: #38bdf8;
            -webkit-text-fill-color: #38bdf8;
        }

        p.subtitle {
            text-align: center;
            color: #94a3b8;
            font-size: 1.1rem;
            line-height: 1.6;
            margin-bottom: 36px;
        }

        .pipeline-flow {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 12px;
            margin-bottom: 36px;
        }

        .stage-card {
            background: rgba(255, 255, 255, 0.02);
            border: 1px solid rgba(255, 255, 255, 0.06);
            border-radius: 12px;
            padding: 16px 12px;
            text-align: center;
            transition: transform 0.2s, border-color 0.2s;
        }

        .stage-card:hover {
            transform: translateY(-2px);
            border-color: rgba(56, 189, 248, 0.4);
        }

        .stage-icon {
            font-size: 1.5rem;
            margin-bottom: 8px;
        }

        .stage-title {
            font-size: 0.85rem;
            font-weight: 700;
            color: #e2e8f0;
            margin-bottom: 4px;
        }

        .stage-desc {
            font-size: 0.72rem;
            color: #64748b;
        }

        .info-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 16px;
            border-top: 1px solid rgba(255, 255, 255, 0.08);
            padding-top: 24px;
        }

        .info-item {
            text-align: center;
        }

        .info-label {
            font-size: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: #64748b;
            margin-bottom: 4px;
        }

        .info-value {
            font-size: 0.95rem;
            font-weight: 600;
            color: #f1f5f9;
        }

        footer {
            margin-top: 24px;
            text-align: center;
            font-size: 0.8rem;
            color: #475569;
        }

        @media (max-width: 680px) {
            .container {
                padding: 32px 20px;
            }
            h1 {
                font-size: 1.8rem;
            }
            .pipeline-flow {
                grid-template-columns: repeat(2, 1fr);
            }
            .info-grid {
                grid-template-columns: 1fr;
                gap: 12px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="badge-container">
            <span class="badge">
                <span class="pulse-dot"></span>
                Production Live
            </span>
        </div>

        <h1>DevOps CI/CD Pipeline <br><span class="highlight-text">Working Successfully!</span></h1>
        
        <p class="subtitle">
            Fully automated Code-to-Cloud deployment pipeline using GitHub Actions, Docker Hub container registry, and AWS EC2.
        </p>

        <div class="pipeline-flow">
            <div class="stage-card">
                <div class="stage-icon">🐙</div>
                <div class="stage-title">GitHub</div>
                <div class="stage-desc">Trigger on Push to main</div>
            </div>
            <div class="stage-card">
                <div class="stage-icon">⚙️</div>
                <div class="stage-title">Actions</div>
                <div class="stage-desc">Automated CI Workflow</div>
            </div>
            <div class="stage-card">
                <div class="stage-icon">🐳</div>
                <div class="stage-title">Docker Hub</div>
                <div class="stage-desc">Container Registry</div>
            </div>
            <div class="stage-card">
                <div class="stage-icon">☁️</div>
                <div class="stage-title">AWS EC2</div>
                <div class="stage-desc">CD via Secure SSH</div>
            </div>
        </div>

        <div class="info-grid">
            <div class="info-item">
                <div class="info-label">Application Port</div>
                <div class="info-value">5000</div>
            </div>
            <div class="info-item">
                <div class="info-label">Environment</div>
                <div class="info-value">Production (EC2)</div>
            </div>
            <div class="info-item">
                <div class="info-label">Status Check</div>
                <div class="info-value" style="color: #34d399;">200 OK / Healthy</div>
            </div>
        </div>
    </div>

    <footer>
        Production-Grade DevOps Portfolio Project &bull; Built with Flask &amp; Docker
    </footer>
</body>
</html>
"""

@app.route('/')
def home():
    """Renders the main application landing page."""
    return render_template_string(HTML_TEMPLATE)

@app.route('/health')
def health_check():
    """Healthcheck endpoint for Docker and monitoring services."""
    return jsonify({
        "status": "healthy",
        "service": "flask-cicd-app",
        "port": 5000
    }), 200

if __name__ == '__main__':
    # Local development server execution
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
