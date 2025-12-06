# Deploying to Render

This guide explains how to deploy the web app to a production server using Render.

## Prerequisites

Make sure your repository includes:
- `requirements.txt` with all dependencies (including `gunicorn`)
- `web_app/__init__.py` with the `create_app()` function

## Deployment Steps

### 1. Create a Render Account

Sign up at [render.com](https://render.com) if you don't have an account.

### 2. Create a New Web Service

1. In the Render Dashboard, click **New > Web Service**
2. Connect your GitHub repository
3. Select the branch to deploy (e.g., `main`)

### 3. Configure the Service

Use these settings:

| Setting | Value |
|---------|-------|
| **Name** | `my-first-repo` (or your preferred name) |
| **Environment** | `Python 3` |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `gunicorn "web_app:create_app()"` |

### 4. Set Environment Variables

In the Render Dashboard, add these environment variables:

- `ALPHAVANTAGE_API_KEY` - Your AlphaVantage API key
- `SECRET_KEY` - A secret key for Flask sessions (f2c72e17563079f0edcc6bae7db54d67)

### 5. Deploy

Click **Create Web Service** and wait for the build to complete.

Your app will be live at `https://your-app-name.onrender.com`

## Automatic Deployments

Each push to your connected branch will automatically trigger a new deployment.

## Troubleshooting

- If the build fails, check the logs in the Render Dashboard
- Make sure all dependencies are listed in `requirements.txt`
- Verify environment variables are set correctly
