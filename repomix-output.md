This file is a merged representation of the entire codebase, combined into a single document by Repomix.

# File Summary

## Purpose
This file contains a packed representation of the entire repository's contents.
It is designed to be easily consumable by AI systems for analysis, code review,
or other automated processes.

## File Format
The content is organized as follows:
1. This summary section
2. Repository information
3. Directory structure
4. Repository files (if enabled)
5. Multiple file entries, each consisting of:
  a. A header with the file path (## File: path/to/file)
  b. The full contents of the file in a code block

## Usage Guidelines
- This file should be treated as read-only. Any changes should be made to the
  original repository files, not this packed version.
- When processing this file, use the file path to distinguish
  between different files in the repository.
- Be aware that this file may contain sensitive information. Handle it with
  the same level of security as you would the original repository.

## Notes
- Some files may have been excluded based on .gitignore rules and Repomix's configuration
- Binary files are not included in this packed representation. Please refer to the Repository Structure section for a complete list of file paths, including binary files
- Files matching patterns in .gitignore are excluded
- Files matching default ignore patterns are excluded
- Files are sorted by Git change count (files with more changes are at the bottom)

# Directory Structure
```
.github/
  workflows/
    build_documentation.yml
    build_pr_documentation.yml
    upload_pr_documentation.yml
projects/
  unit3/
    build-mcp-server/
      solution/
        manual_test.md
        pyproject.toml
        README.md
        server.py
        test_server.py
      starter/
        pyproject.toml
        README.md
        server.py
        test_server.py
        validate_starter.py
    github-actions-integration/
      solution/
        manual_test.md
        pyproject.toml
        README.md
        server.py
        test_server.py
        webhook_server.py
      starter/
        pyproject.toml
        README.md
        server.py
        test_server.py
        validate_starter.py
        webhook_server.py
      .gitignore
    slack-notification/
      solution/
        github_events.json
        manual_test.md
        pyproject.toml
        README.md
        server.py
        test_server.py
        webhook_server.py
      starter/
        manual_test.md
        pyproject.toml
        README.md
        server.py
        test_server.py
        validate_starter.py
        webhook_server.py
    team-guidelines/
      coding-standards.md
      pr-guidelines.md
    templates/
      bug.md
      docs.md
      feature.md
      performance.md
      refactor.md
      security.md
      test.md
quiz/
  data/
    unit_1.json
  push_questions.py
  pyproject.toml
  README.md
scripts/
  translation.py
  vi.py
units/
  en/
    unit0/
      introduction.mdx
    unit1/
      architectural-components.mdx
      capabilities.mdx
      certificate.mdx
      communication-protocol.mdx
      gradio-mcp.mdx
      introduction.mdx
      key-concepts.mdx
      mcp-clients.mdx
      quiz1.mdx
      quiz2.mdx
      sdk.mdx
      unit1-recap.mdx
    unit2/
      clients.mdx
      continue-client.mdx
      gradio-client.mdx
      gradio-server.mdx
      introduction.mdx
      tiny-agents.mdx
    unit3/
      build-mcp-server-solution-walkthrough.mdx
      build-mcp-server.mdx
      certificate.mdx
      conclusion.mdx
      github-actions-integration.mdx
      introduction.mdx
      slack-notification.mdx
    unit3_1/
      conclusion.mdx
      creating-the-mcp-server.mdx
      introduction.mdx
      mcp-client.mdx
      quiz1.mdx
      quiz2.mdx
      setting-up-the-project.mdx
      webhook-listener.mdx
    _toctree.yml
  vi/
    unit0/
      introduction.mdx
    unit1/
      architectural-components.mdx
      capabilities.mdx
      communication-protocol.mdx
      gradio-mcp.mdx
      introduction.mdx
      key-concepts.mdx
      mcp-clients.mdx
      sdk.mdx
    unit2/
      clients.mdx
      gradio-client.mdx
      gradio-server.mdx
      introduction.mdx
      tiny-agents.mdx
    unit3/
      introduction.mdx
    unit4/
      introduction.mdx
    _toctree.yml
.gitignore
.python-version
hello.py
LICENSE
pyproject.toml
README_vi.md
README.md
requirements.txt
```

# Files

## File: .github/workflows/build_documentation.yml
````yaml
name: Build documentation

on:
  push:
    branches:
      - main

jobs:
  build:
    uses: huggingface/doc-builder/.github/workflows/build_main_documentation.yml@main
    with:
      commit_sha: ${{ github.sha }}
      package: mcp-course
      package_name: mcp-course
      path_to_docs: mcp-course/units/
      additional_args: --not_python_module
      languages: en
    secrets:
      hf_token: ${{ secrets.HF_DOC_BUILD_PUSH }}
````

## File: .github/workflows/build_pr_documentation.yml
````yaml
name: Build PR Documentation

on:
  pull_request:

concurrency:
  group: ${{ github.workflow }}-${{ github.head_ref || github.run_id }}
  cancel-in-progress: true

jobs:
  build:
    uses: huggingface/doc-builder/.github/workflows/build_pr_documentation.yml@main
    with:
      commit_sha: ${{ github.event.pull_request.head.sha }}
      pr_number: ${{ github.event.number }}
      package: mcp-course
      package_name: mcp-course
      path_to_docs: mcp-course/units/
      additional_args: --not_python_module
      languages: en
````

## File: .github/workflows/upload_pr_documentation.yml
````yaml
name: Upload PR Documentation

on:
  workflow_run:
    workflows: ["Build PR Documentation"]
    types:
      - completed

permissions:
  actions: write
  contents: write
  deployments: write
  pull-requests: write


jobs:
  build:
    uses: huggingface/doc-builder/.github/workflows/upload_pr_documentation.yml@main
    with:
      package_name: mcp-course
      hub_base_path: https://moon-ci-docs.huggingface.co/learn
    secrets:
      hf_token: ${{ secrets.HF_DOC_BUILD_PUSH }}
      comment_bot_token: ${{ secrets.COMMENT_BOT_TOKEN }}
````

## File: projects/unit3/build-mcp-server/solution/manual_test.md
````markdown
# Manual Testing Guide for Module 1 Solution

## Prerequisites

1. Ensure you're in a git repository with some changes
2. Install uv following instructions at: https://docs.astral.sh/uv/getting-started/installation/
3. Install dependencies:
   ```bash
   uv sync --all-extras
   ```

## Test 1: Validate the Solution

Run the automated validation script:
```bash
uv run python validate_solution.py
```

This will check:
- Git environment
- Python imports
- Server creation
- Tool registration
- Tool execution
- Template creation

## Test 2: Run Unit Tests

```bash
uv run pytest test_server.py -v
```

## Test 3: Test with Claude Code

1. **Configure MCP Server**
   
   Add the server to Claude Code:
   ```bash
   # Add the MCP server
   claude mcp add pr-agent -- uv --directory /absolute/path/to/module1/solution run server.py
   
   # Verify it's configured
   claude mcp list
   ```

2. **Restart Claude Code** to pick up the new server

3. **Make Some Git Changes**
   
   In any git repository:
   ```bash
   echo "test change" >> README.md
   git add README.md
   ```

4. **Test with Claude**
   
   Ask Claude:
   - "Can you analyze my git changes?"
   - "What PR templates are available?"
   - "Based on my changes, which PR template should I use?"

## Test 4: Direct Server Testing

You can also test the server directly:

```python
import asyncio
from server import analyze_file_changes, get_pr_templates, suggest_template

async def test():
    # Test analyze_file_changes
    changes = await analyze_file_changes("main", True)
    print("Changes:", changes[:200] + "...")
    
    # Test get_pr_templates
    templates = await get_pr_templates()
    print("Templates available:", len(json.loads(templates)))
    
    # Test suggest_template
    suggestion = await suggest_template(
        "Fixed authentication bug", 
        "bug"
    )
    print("Suggestion:", json.loads(suggestion)["recommended_template"]["type"])

asyncio.run(test())
```

## Expected Behavior

1. **analyze_file_changes** should return JSON with:
   - base_branch
   - files_changed
   - statistics
   - commits
   - diff (if include_diff=True)

2. **get_pr_templates** should return JSON array of templates with:
   - filename
   - type
   - content

3. **suggest_template** should return JSON with:
   - recommended_template
   - reasoning
   - template_content
   - usage_hint

## Troubleshooting

- **"Git not found"**: Ensure you're in a git repository
- **Import errors**: Check virtual environment is activated
- **MCP connection failed**: Verify the path in the claude mcp add command is absolute
- **No tools showing**: Restart Claude Code after adding the server
````

## File: projects/unit3/build-mcp-server/solution/pyproject.toml
````toml
[project]
name = "pr-agent"
version = "1.0.0"
description = "MCP server for PR template suggestions"
readme = "README.md"
requires-python = ">=3.10"
dependencies = [
    "mcp[cli]>=1.0.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=8.3.0",
    "pytest-asyncio>=0.21.0",
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["."]

[tool.uv]
dev-dependencies = [
    "pytest>=8.3.0",
    "pytest-asyncio>=0.21.0",
]
````

## File: projects/unit3/build-mcp-server/solution/README.md
````markdown
# Module 1: Basic MCP Server with PR Template Tools

This module implements a basic MCP server that provides tools for analyzing git changes and suggesting appropriate PR templates.

## Setup

### 1. Install uv

Follow the official installation instructions at: https://docs.astral.sh/uv/getting-started/installation/

### 2. Install dependencies

```bash
# Install all dependencies
uv sync

# Or install with dev dependencies for testing
uv sync --all-extras
```

### 3. Configure the MCP Server

Add the server to Claude Code:

```bash
# Add the MCP server
claude mcp add pr-agent -- uv --directory /absolute/path/to/module1/solution run server.py

# Verify it's configured
claude mcp list
```

## Tools Available

1. **analyze_file_changes** - Get the full diff and list of changed files
2. **get_pr_templates** - List available PR templates with their content
3. **suggest_template** - Let Claude analyze changes and suggest a template

## Usage Example

1. Make some changes in a git repository
2. Ask Claude: "Can you analyze my changes and suggest a PR template?"
3. Claude will:
   - Use `analyze_file_changes` to see what changed
   - Analyze the diff to understand the nature of changes
   - Use `suggest_template` to recommend the most appropriate template
   - Help you fill out the template based on the specific changes

## How It Works

Unlike traditional template systems that rely on file extensions or simple patterns, this MCP server provides Claude with raw git data and lets Claude's intelligence determine:
- What type of change is being made (bug fix, feature, refactor, etc.)
- Which template is most appropriate
- How to fill out the template based on the actual code changes

This approach leverages Claude's understanding of code and context rather than rigid rules.

## Running Tests

```bash
# Run the validation script
uv run python validate_solution.py

# Run unit tests
uv run pytest test_server.py -v
```

## Running the Server Directly

```bash
# Start the MCP server
uv run server.py
```
````

## File: projects/unit3/build-mcp-server/starter/pyproject.toml
````toml
[project]
name = "pr-agent"
version = "1.0.0"
description = "MCP server for PR template suggestions - Starter Code"
readme = "README.md"
requires-python = ">=3.10"
dependencies = [
    "mcp[cli]>=1.0.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=8.3.0",
    "pytest-asyncio>=0.21.0",
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["."]

[tool.uv]
dev-dependencies = [
    "pytest>=8.3.0",
    "pytest-asyncio>=0.21.0",
]
````

## File: projects/unit3/build-mcp-server/starter/README.md
````markdown
# Module 1: Basic MCP Server - Starter Code

Welcome to Module 1! In this module, you'll build a basic MCP server that helps developers create better pull requests by analyzing code changes and suggesting appropriate templates.

## Your Task

Implement an MCP server with three tools:

1. **analyze_file_changes** - Retrieve git diff information and changed files
2. **get_pr_templates** - List available PR templates 
3. **suggest_template** - Allow Claude to suggest the most appropriate template

## Setup

### 1. Install uv

Follow the official installation instructions at: https://docs.astral.sh/uv/getting-started/installation/

### 2. Install dependencies

```bash
# Install all dependencies
uv sync

# Or install with dev dependencies for testing
uv sync --all-extras
```

### 3. Start implementing!

Open `server.py` and follow the TODO comments to implement each tool.

**Note**: The starter code includes stub implementations that return "Not implemented" errors. This allows you to:
- Run the server immediately
- Test your setup with Claude
- Replace each stub with your actual implementation
- See helpful hints about what each tool should do

## Design Philosophy

Instead of using rigid rules based on file extensions or patterns, your tools should provide Claude with raw git data and let Claude's intelligence determine:
- What type of change is being made
- Which template is most appropriate
- How to customize the template for the specific changes

## Testing Your Implementation

1. Run the unit tests:
   ```bash
   uv run pytest test_server.py -v
   ```

2. Configure the MCP server in Claude Code:
   ```bash
   # Add the MCP server
   claude mcp add pr-agent -- uv --directory /absolute/path/to/module1/starter run server.py
   
   # Verify it's configured
   claude mcp list
   ```

3. Make some changes in a git repository and ask Claude to analyze your changes and suggest a PR template

## Need Help?

- Check the solution in `../solution/` if you get stuck
- Remember: The goal is to give Claude the data it needs, not to implement complex logic yourself
````

## File: projects/unit3/github-actions-integration/solution/manual_test.md
````markdown
# Manual Testing Guide - Module 2: GitHub Actions Integration

This guide walks through comprehensive testing of the GitHub Actions integration module.

## Prerequisites

- Python environment with `uv` installed
- Claude Code configured
- Port 8080 available
- (Optional) Cloudflare Tunnel installed for real GitHub testing

## Test Sequence

### 1. Environment Setup

```bash
cd projects/unit3/github-actions-integration/solution
uv sync
```

### 2. Start Services

**Terminal 1 - Webhook Server:**
```bash
python webhook_server.py
```

Expected output:
```
🚀 Starting webhook server on http://localhost:8080
📝 Events will be saved to: /path/to/github_events.json
🔗 Webhook URL: http://localhost:8080/webhook/github
```

**Terminal 2 - MCP Server:**
```bash
uv run server.py
```

Expected output:
```
Starting PR Agent MCP server...
To receive GitHub webhooks, run the webhook server separately:
  python webhook_server.py
```

### 3. Claude Code Configuration

Add to Claude Code settings and restart:
```json
{
  "mcpServers": {
    "pr-agent-actions": {
      "command": "uv",
      "args": ["run", "server.py"],
      "cwd": "/path/to/github-actions-integration/solution"
    }
  }
}
```

### 4. Test Module 1 Functionality

Verify existing tools still work:

```
User: "Analyze my file changes"
Expected: Claude uses analyze_file_changes() tool

User: "Show me available PR templates"
Expected: Claude lists all templates

User: "Suggest a template for a bug fix"
Expected: Claude recommends bug.md template
```

### 5. Send Test Webhook Events

**Success Event:**
```bash
curl -X POST http://localhost:8080/webhook/github \
  -H "Content-Type: application/json" \
  -H "X-GitHub-Event: workflow_run" \
  -d '{
    "action": "completed",
    "workflow_run": {
      "id": 123456789,
      "name": "CI Tests",
      "head_branch": "main",
      "head_sha": "abc123",
      "path": ".github/workflows/ci.yml",
      "display_title": "CI Tests for PR #42",
      "run_number": 42,
      "event": "push",
      "status": "completed",
      "conclusion": "success",
      "workflow_id": 12345,
      "url": "https://api.github.com/repos/user/repo/actions/runs/123456789",
      "html_url": "https://github.com/user/repo/actions/runs/123456789",
      "created_at": "2024-01-01T10:00:00Z",
      "updated_at": "2024-01-01T10:05:00Z",
      "run_started_at": "2024-01-01T10:00:00Z"
    },
    "repository": {
      "id": 987654321,
      "name": "repo",
      "full_name": "user/repo",
      "owner": {
        "login": "user",
        "type": "User"
      }
    },
    "sender": {
      "login": "test-user",
      "type": "User"
    }
  }'
```

**Failure Event:**
```bash
curl -X POST http://localhost:8080/webhook/github \
  -H "Content-Type: application/json" \
  -H "X-GitHub-Event: workflow_run" \
  -d '{
    "action": "completed",
    "workflow_run": {
      "id": 123456790,
      "name": "Deploy to Production",
      "head_branch": "release/v1.0",
      "status": "completed",
      "conclusion": "failure",
      "run_number": 15,
      "html_url": "https://github.com/user/repo/actions/runs/123456790",
      "updated_at": "2024-01-01T10:10:00Z"
    },
    "repository": {"full_name": "user/repo"},
    "sender": {"login": "test-user"}
  }'
```

**In-Progress Event:**
```bash
curl -X POST http://localhost:8080/webhook/github \
  -H "Content-Type: application/json" \
  -H "X-GitHub-Event: workflow_run" \
  -d '{
    "action": "in_progress",
    "workflow_run": {
      "id": 123456791,
      "name": "Build and Test",
      "status": "in_progress",
      "conclusion": null,
      "run_number": 100,
      "html_url": "https://github.com/user/repo/actions/runs/123456791",
      "updated_at": "2024-01-01T10:15:00Z"
    },
    "repository": {"full_name": "user/repo"},
    "sender": {"login": "test-user"}
  }'
```

### 6. Test New Tools

```
User: "What GitHub Actions events have we received?"
Expected: Claude shows all 3 events with details

User: "Show me the workflow status"
Expected: Claude shows:
- CI Tests: success
- Deploy to Production: failure  
- Build and Test: in_progress
```

### 7. Test MCP Prompts

Test each prompt by name:

**Prompt 1:**
```
User: "analyze ci results"
Expected: Claude provides formatted analysis showing:
- Overall health: Warning (due to failure)
- Failed workflows: Deploy to Production
- Successful workflows: CI Tests
- In-progress: Build and Test
- Recommendations based on failures
```

**Prompt 2:**
```
User: "create deployment summary"
Expected: Claude creates Slack-style message about the deployment failure
```

**Prompt 3:**
```
User: "generate pr status report"
Expected: Claude combines file changes analysis with CI/CD status
```

**Prompt 4:**
```
User: "troubleshoot workflow failure"
Expected: Claude provides structured troubleshooting for Deploy to Production failure
```

### 8. Verify File Storage

Check that events are persisted:
```bash
cat github_events.json
```

Should contain all 3 events in JSON array format.

### 9. Test Event Limit

Send 5 more events to verify only last 100 are kept (manual verification).

### 10. Test with Real GitHub (Optional)

**Terminal 3 - Cloudflare Tunnel:**
```bash
cloudflared tunnel --url http://localhost:8080
```

1. Note the tunnel URL (e.g., https://random-name.trycloudflare.com)
2. Configure GitHub webhook:
   - Go to repo Settings → Webhooks
   - Add webhook with URL: `https://your-tunnel.trycloudflare.com/webhook/github`
   - Select "Workflow runs" events
3. Push a commit or manually trigger a workflow
4. Verify real events appear in Claude

## Troubleshooting

### No events showing up
- Check webhook server is running
- Verify `github_events.json` exists
- Ensure correct curl commands

### Port 8080 already in use
```bash
lsof -i :8080  # Find process
kill -9 <PID>  # Kill it
```

### Prompts not working
- Use exact lowercase names with spaces
- Don't use quotes around prompt names

### Claude not finding server
- Restart Claude Code after config changes
- Check the cwd path is absolute

## Success Criteria

- [ ] All Module 1 tools work
- [ ] Webhook server receives and stores events
- [ ] Both new tools return correct data
- [ ] All 4 prompts execute successfully
- [ ] Events persist in JSON file
- [ ] Multiple event types handled correctly
- [ ] Real GitHub integration works (if tested)
````

## File: projects/unit3/github-actions-integration/solution/pyproject.toml
````toml
[project]
name = "pr-agent-actions"
version = "2.0.0"
description = "MCP server with GitHub Actions integration and Prompts"
readme = "README.md"
requires-python = ">=3.10"
dependencies = [
    "mcp[cli]>=1.0.0",
    "aiohttp>=3.10.0,<4.0.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=8.3.0",
    "pytest-asyncio>=0.21.0",
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["."]

[tool.uv]
dev-dependencies = [
    "pytest>=8.3.0",
    "pytest-asyncio>=0.21.0",
]
````

## File: projects/unit3/github-actions-integration/solution/README.md
````markdown
# Module 2: GitHub Actions Integration

This module extends the PR Agent with GitHub Actions webhook integration and MCP Prompts for standardized CI/CD workflows.

## Features Added in Module 2

1. **GitHub Actions Tools**:
   - `get_recent_actions_events()` - View recent webhook events
   - `get_workflow_status()` - Check workflow statuses

2. **MCP Prompts for CI/CD**:
   - `analyze_ci_results` - Comprehensive CI/CD analysis
   - `create_deployment_summary` - Team-friendly deployment updates
   - `generate_pr_status_report` - Combined code and CI/CD report
   - `troubleshoot_workflow_failure` - Systematic debugging guide

3. **Webhook Server**:
   - Separate script that runs on port 8080
   - Receives GitHub Actions events
   - Stores events in `github_events.json` for the MCP server to read

## Installation

```bash
# From the solution directory
uv sync
```

## Setting Up Cloudflare Tunnel

To receive GitHub webhooks locally, you'll need to set up Cloudflare Tunnel (cloudflared):

### Step 1: Install cloudflared

**macOS:**
```bash
brew install cloudflared
```

**Windows:**
Download the Windows installer from:
https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-windows-amd64.msi

**Linux:**
```bash
# For Debian/Ubuntu (amd64)
curl -L https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb -o cloudflared.deb
sudo dpkg -i cloudflared.deb

# For other Linux distros, download the appropriate binary:
# https://github.com/cloudflare/cloudflared/releases/latest
```

### Step 2: Start the Tunnel

```bash
# This creates a public URL that forwards to your local webhook server
cloudflared tunnel --url http://localhost:8080
```

You'll see output like:
```
Your quick tunnel has been created! Visit it at:
https://random-name-here.trycloudflare.com
```

### Step 3: Configure GitHub Webhook

1. Go to your GitHub repository → Settings → Webhooks
2. Click "Add webhook"
3. Set **Payload URL** to: `https://your-tunnel-url.trycloudflare.com/webhook/github`
4. Set **Content type** to: `application/json`
5. Select events:
   - Workflow runs
   - Check runs
   - Or choose "Send me everything"
6. Click "Add webhook"

## Running the Server

### For Development

```bash
# Terminal 1: Start the webhook server
python webhook_server.py

# Terminal 2: Start Cloudflare Tunnel (if testing with real GitHub)
cloudflared tunnel --url http://localhost:8080

# Terminal 3: Start the MCP server
uv run server.py
```

### With Claude Code

1. Add to Claude Code settings:
```json
{
  "pr-agent-actions": {
    "command": "uv",
    "args": ["run", "server.py"],
    "cwd": "/path/to/github-actions-integration/solution"
  }
}
```

2. Restart Claude Code
3. In a separate terminal, start the webhook server: `python webhook_server.py`
4. (Optional) Start Cloudflare Tunnel if testing with real GitHub webhooks

## Testing Webhooks

### Manual Test
```bash
# Send a test webhook
curl -X POST http://localhost:8080/webhook/github \
  -H "Content-Type: application/json" \
  -H "X-GitHub-Event: workflow_run" \
  -d '{
    "action": "completed",
    "workflow_run": {
      "id": 123456789,
      "name": "CI Tests",
      "head_branch": "main",
      "run_number": 42,
      "status": "completed",
      "conclusion": "success",
      "html_url": "https://github.com/user/repo/actions/runs/123456789",
      "updated_at": "2024-01-01T10:00:00Z"
    },
    "repository": {
      "full_name": "user/repo"
    },
    "sender": {
      "login": "test-user"
    }
  }'
```

### With Claude Code

After setting up webhooks and pushing a commit:

1. **Check recent events**: 
   - Ask: "What GitHub Actions events have we received?"
   - Claude will use `get_recent_actions_events()`

2. **Analyze CI status**:
   - Use the prompt: "Analyze CI Results"
   - Claude will check workflows and provide insights

3. **Create deployment summary**:
   - Use the prompt: "Create Deployment Summary"
   - Claude will format a team-friendly update

## Module Structure

- `server.py` - Main MCP server with Tools and Prompts
- `webhook_server.py` - Separate webhook server that stores events
- `github_events.json` - File where webhook events are stored (created automatically)
- `pyproject.toml` - Dependencies for both servers
- `README.md` - This file

## Next Steps

- Complete the exercises in the module
- Experiment with different prompt workflows
- Move on to Module 3 for Hugging Face Hub integration
````

## File: projects/unit3/github-actions-integration/solution/webhook_server.py
````python
#!/usr/bin/env python3
"""
Simple webhook server for GitHub Actions events.
Stores events in a JSON file that the MCP server can read.
"""

import json
from datetime import datetime
from pathlib import Path
from aiohttp import web

# File to store events
EVENTS_FILE = Path(__file__).parent / "github_events.json"

async def handle_webhook(request):
    """Handle incoming GitHub webhook"""
    try:
        data = await request.json()
        
        # Create event record
        event = {
            "timestamp": datetime.utcnow().isoformat(),
            "event_type": request.headers.get("X-GitHub-Event", "unknown"),
            "action": data.get("action"),
            "workflow_run": data.get("workflow_run"),
            "check_run": data.get("check_run"),
            "repository": data.get("repository", {}).get("full_name"),
            "sender": data.get("sender", {}).get("login")
        }
        
        # Load existing events
        events = []
        if EVENTS_FILE.exists():
            with open(EVENTS_FILE, 'r') as f:
                events = json.load(f)
        
        # Add new event and keep last 100
        events.append(event)
        events = events[-100:]
        
        # Save events
        with open(EVENTS_FILE, 'w') as f:
            json.dump(events, f, indent=2)
        
        return web.json_response({"status": "received"})
    except Exception as e:
        return web.json_response({"error": str(e)}, status=400)

# Create app and add route
app = web.Application()
app.router.add_post('/webhook/github', handle_webhook)

if __name__ == '__main__':
    print("🚀 Starting webhook server on http://localhost:8080")
    print("📝 Events will be saved to:", EVENTS_FILE)
    print("🔗 Webhook URL: http://localhost:8080/webhook/github")
    web.run_app(app, host='localhost', port=8080)
````

## File: projects/unit3/github-actions-integration/starter/pyproject.toml
````toml
[project]
name = "pr-agent"
version = "1.0.0"
description = "MCP server for PR template suggestions"
readme = "README.md"
requires-python = ">=3.10"
dependencies = [
    "mcp[cli]>=1.0.0",
    "aiohttp>=3.10.0,<4.0.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=8.3.0",
    "pytest-asyncio>=0.21.0",
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["."]

[tool.uv]
dev-dependencies = [
    "pytest>=8.3.0",
    "pytest-asyncio>=0.21.0",
]
````

## File: projects/unit3/github-actions-integration/starter/README.md
````markdown
# Module 2: GitHub Actions Integration - Starter Code

This is your starting point for Module 2. You'll extend the PR Agent from Module 1 with webhook handling and MCP Prompts.

## Your Task

1. **Import Required Types**: Add the necessary imports for MCP Prompts
2. **Connect to Events File**: Define the path to read webhook events
3. **Implement GitHub Actions Tools**: Complete the tools to query events
4. **Create MCP Prompts**: Build prompts for standardized CI/CD workflows

Note: The webhook server (`webhook_server.py`) is provided for you!

## Getting Started

1. Install dependencies:
   ```bash
   uv sync
   ```

2. Start the webhook server (in a separate terminal):
   ```bash
   python webhook_server.py
   ```

3. Follow the TODOs in `server.py` to implement Module 2 features

## Testing Your Implementation

1. Start your server:
   ```bash
   uv run server.py
   ```

2. In another terminal, start Cloudflare Tunnel:
   ```bash
   cloudflared tunnel --url http://localhost:8080
   ```

3. Configure GitHub webhooks with your tunnel URL

4. Test with Claude Code using the new prompts

## Implementation Hints

- The webhook server stores events in `github_events.json`
- Read the JSON file in your tools to get event data
- Prompts are simple functions that return strings with instructions
- Decorate prompt functions with `@mcp.prompt()`

## Need Help?

- Review the Module 2 documentation
- Check the solution in the `solution/` directory
- Look at the MCP documentation for Prompts: https://modelcontextprotocol.io/docs/concepts/prompts
````

## File: projects/unit3/github-actions-integration/starter/webhook_server.py
````python
#!/usr/bin/env python3
"""
Simple webhook server for GitHub Actions events.
Stores events in a JSON file that the MCP server can read.
"""

import json
from datetime import datetime
from pathlib import Path
from aiohttp import web

# File to store events
EVENTS_FILE = Path(__file__).parent / "github_events.json"

async def handle_webhook(request):
    """Handle incoming GitHub webhook"""
    try:
        data = await request.json()
        
        # Create event record
        event = {
            "timestamp": datetime.utcnow().isoformat(),
            "event_type": request.headers.get("X-GitHub-Event", "unknown"),
            "action": data.get("action"),
            "workflow_run": data.get("workflow_run"),
            "check_run": data.get("check_run"),
            "repository": data.get("repository", {}).get("full_name"),
            "sender": data.get("sender", {}).get("login")
        }
        
        # Load existing events
        events = []
        if EVENTS_FILE.exists():
            with open(EVENTS_FILE, 'r') as f:
                events = json.load(f)
        
        # Add new event and keep last 100
        events.append(event)
        events = events[-100:]
        
        # Save events
        with open(EVENTS_FILE, 'w') as f:
            json.dump(events, f, indent=2)
        
        return web.json_response({"status": "received"})
    except Exception as e:
        return web.json_response({"error": str(e)}, status=400)

# Create app and add route
app = web.Application()
app.router.add_post('/webhook/github', handle_webhook)

if __name__ == '__main__':
    print("🚀 Starting webhook server on http://localhost:8080")
    print("📝 Events will be saved to:", EVENTS_FILE)
    print("🔗 Webhook URL: http://localhost:8080/webhook/github")
    web.run_app(app, host='localhost', port=8080)
````

## File: projects/unit3/github-actions-integration/.gitignore
````
# Test data
github_events.json
````

## File: projects/unit3/team-guidelines/coding-standards.md
````markdown
# Coding Standards

## Python
- Use type hints for all function arguments and return values
- Follow PEP 8 style guide
- Maximum line length: 100 characters
- Use descriptive variable names
- Prefer f-strings over .format() or % formatting

## Git Commits
- Use conventional commit format: type(scope): description
- Types: feat, fix, docs, style, refactor, test, chore
- Keep commit messages under 72 characters
- Reference issue numbers when applicable (e.g., "Fixes #123")

## Code Organization
- One class per file for major components
- Group related functionality into modules
- Use __init__.py to control public API
- Keep functions under 50 lines when possible

## Testing
- All new features must include tests
- Maintain >80% test coverage
- Use pytest for Python tests
- Test edge cases and error conditions
- Mock external dependencies

## Documentation
- All public functions need docstrings
- Use Google-style docstrings
- Include usage examples for complex functions
- Keep README files up to date
````

## File: projects/unit3/team-guidelines/pr-guidelines.md
````markdown
# PR Guidelines

## PR Size
- Keep PRs under 500 lines of changes
- Split large features into multiple PRs
- One logical change per PR
- Separate refactoring from feature changes

## PR Description
- Clearly explain what and why
- Include screenshots for UI changes
- List any breaking changes
- Add testing instructions
- Reference related issues/tickets

## Review Process
- At least one approval required
- Address all review comments
- Update PR description with changes made
- Resolve conflicts before requesting review
- Tag relevant team members

## Before Merging
- All CI checks must pass
- Update documentation if needed
- Verify no sensitive data is exposed
- Squash commits if necessary
- Delete feature branch after merge

## PR Title Format
- Use conventional commit format
- Be specific and descriptive
- Examples:
  - "feat(auth): Add OAuth2 support"
  - "fix(api): Handle null response in user endpoint"
  - "docs: Update installation guide"
````

## File: projects/unit3/templates/bug.md
````markdown
## Bug Fix

### Description
<!-- Brief description of the bug being fixed -->

### Root Cause
<!-- What caused the bug? -->

### Solution
<!-- How does this PR fix the bug? -->

### Testing
- [ ] Added/updated tests
- [ ] Manually tested the fix
- [ ] Verified no regressions

### Related Issues
Fixes #<!-- issue number -->
````

## File: projects/unit3/templates/docs.md
````markdown
## Documentation Update

### Description
<!-- What documentation is being updated? -->

### Changes
<!-- List of specific changes made -->

### Review Checklist
- [ ] Grammar and spelling checked
- [ ] Technical accuracy verified
- [ ] Examples tested
- [ ] Links verified
````

## File: projects/unit3/templates/feature.md
````markdown
## New Feature

### Description
<!-- Brief description of the new feature -->

### Motivation
<!-- Why is this feature needed? -->

### Implementation
<!-- High-level overview of the implementation -->

### Testing
- [ ] Added unit tests
- [ ] Added integration tests
- [ ] Tested edge cases

### Documentation
- [ ] Updated relevant documentation
- [ ] Added usage examples

### Breaking Changes
<!-- List any breaking changes -->
````

## File: projects/unit3/templates/performance.md
````markdown
## Performance Improvement

### Description
<!-- What performance issue is being addressed? -->

### Metrics
<!-- Before/after performance metrics -->

### Changes
<!-- Specific optimizations made -->

### Testing
- [ ] Benchmarks added/updated
- [ ] No functionality regression
- [ ] Tested under various loads
````

## File: projects/unit3/templates/refactor.md
````markdown
## Code Refactoring

### Description
<!-- What code is being refactored? -->

### Motivation
<!-- Why is this refactoring needed? -->

### Changes
<!-- List of specific refactoring changes -->

### Testing
- [ ] All existing tests pass
- [ ] No functional changes
- [ ] Performance impact assessed

### Risk Assessment
<!-- Any risks with this refactoring? -->
````

## File: projects/unit3/templates/security.md
````markdown
## Security Update

### Description
<!-- Brief description of security issue (be careful not to expose vulnerabilities) -->

### Impact
<!-- Who/what is affected? -->

### Solution
<!-- How does this PR address the security issue? -->

### Testing
- [ ] Security tests added
- [ ] Penetration testing performed
- [ ] No new vulnerabilities introduced

### References
<!-- Link to security advisories if applicable -->
````

## File: projects/unit3/templates/test.md
````markdown
## Test Update

### Description
<!-- What tests are being added or updated? -->

### Coverage
- Previous coverage: <!-- X% -->
- New coverage: <!-- Y% -->

### Test Types
- [ ] Unit tests
- [ ] Integration tests
- [ ] End-to-end tests

### Related Features
<!-- List features/components being tested -->
````

## File: quiz/data/unit_1.json
````json
[
    {
        "question": "Which of the following best describes a Large Language Model (LLM)?",
        "answer_a": "A model specializing in language recognition",
        "answer_b": "A massive neural network that understands and generates human language",
        "answer_c": "A model exclusively used for language data tasks like summarization or classification",
        "answer_d": "A rule-based chatbot used for conversations",
        "correct_answer": "B"
    }
]
````

## File: quiz/push_questions.py
````python
import json
from pathlib import Path
from datasets import Dataset

ORG_NAME = "mcp-course"


def main():
    """Push quiz questions to the Hugging Face Hub"""

    for file in Path("data").glob("*.json"):
        print(f"Processing {file}")

        with open(file, "r") as f:
            quiz_data = json.load(f)

        repo_id = f"{ORG_NAME}/{file.stem}_quiz"

        dataset = Dataset.from_list(quiz_data)

        print(f"Pushing {repo_id} to the Hugging Face Hub")

        dataset.push_to_hub(
            repo_id,
            private=True,
            commit_message=f"Update quiz questions for {file.stem}",
        )


if __name__ == "__main__":
    main()
````

## File: quiz/pyproject.toml
````toml
[project]
name = "agents-course"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.11"
dependencies = [
    "datasets>=3.2.0",
    "huggingface-hub>=0.27.1",
    "ipykernel>=6.29.5",
    "requests>=2.32.3",
]
````

## File: quiz/README.md
````markdown
# MCP Course quiz scripts
````

## File: scripts/translation.py
````python
import os
import sys
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
load_dotenv()


hf_token = os.environ.get("HF_TOKEN")
if not hf_token:
    raise ValueError("HF_TOKEN not found in environment variables. Please set it in a .env file.")


# Get the directory containing the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
default_inp_dir = os.path.join(script_dir, '..', 'units/en')
default_model = "deepseek-ai/DeepSeek-R1"
default_client = InferenceClient(
    provider="together",
    # api_key is read from the environment
)

def auto_translate(
    output_lang: str,
    prompt: callable,
    inp_dir: str = default_inp_dir,
    model: str = default_model,
    client: InferenceClient = default_client
):
    get_output_path = lambda x: x.replace('/en', f'/{output_lang}')
    escape_special_tokens = lambda x: x.replace('<think>', '<%%think%%>').replace('</think>', '<%%/think%%>')
    unescape_special_tokens = lambda x: x.replace('<%%think%%>', '<think>').replace('<%%/think%%>', '</think>')

    # Get the list of all files in the directory, recursively
    inp_files: list[str] = []
    print('Collecting files...')
    for root, dirs, files in os.walk(inp_dir):
        for file in files:
            if file.endswith('.mdx') or file == "_toctree.yml":
                fname = os.path.join(root, file)
                print('  +', fname)
                inp_files.append(fname)

    def write_out_file(fpath: str, content: str):
        base_path = os.path.dirname(fpath)
        os.makedirs(base_path, exist_ok=True)
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)

    # Read the content of the file and process
    for i, inp_file in enumerate(inp_files):
        out_file = get_output_path(inp_file)
        if os.path.exists(out_file):
            print(f'[{i+1}/{len(inp_files)}] Skipping file: {inp_file}')
            continue
        with open(inp_file, 'r', encoding='utf-8') as f:
            content: str = f.read()
            content = escape_special_tokens(content)
            if content.strip() == "":
                print(f'[{i+1}/{len(inp_files)}] Skipping empty file: {inp_file}')
                write_out_file(out_file, "")
                continue

            print(f'[{i+1}/{len(inp_files)}] Processing file: {inp_file}')
            stream = client.chat.completions.create(
                model=model,
                temperature=0.0,
                messages=[
                    {"role": "user", "content": prompt(content)},
                ],
                stream=True,
            )
            final_text = ""
            for chunk in stream:
                content_chunk = chunk.choices[0].delta.content
                print(content_chunk, end="", flush=True)
                final_text += content_chunk
            # Optionally filter <think>...</think> reasoning process
            final_text = final_text.split('</think>').pop().strip()
            # Write the output to the file
            final_text = unescape_special_tokens(final_text)
            write_out_file(out_file, final_text)
            print()
            print(f'  -> Translated to: {out_file}')
            print("--" * 20)
            #break
````

## File: scripts/vi.py
````python
from translation import auto_translate

output_lang = "vi"

# Fix the prompt function to escape curly braces in the content
prompt = lambda content: f'''
You are a translator for the Vietnamese translation team. You are tasked with translating the following texts into Vietnamese. You must follow these instructions:
- Translate the texts into Vietnamese, while keeping the original formatting (either Markdown, MDX or HTML)
- Inside code blocks, translate the comments but leave the code as-is; If the code block contains quite plain texts, you MUST provide the translation in <details> tag
- Do not translate inline code, the URLs and file paths
- If the term is abbreviated, keep the original term and provide the translation in parentheses for the first time it appears in the text
- If there are any slag or funny joke in english, keep it (do not translate) and give an explanation so Vietnamese reader can understand
- Use "ta", "mình, "chúng ta", "chúng mình", "các bạn" as pronouns

KEEP THESE TERMS (DO NOT TRANSLATE, do NOT add translation in parentheses): MCP, API, SDK, CLI, HTML, GGUF, AI, Client, Server, Hugging Face, Space, CodeAgent, LangGraph, LangChain, Llama, Gemma, inference, notebook, python, transformers, token, pretrain, format, certificate.

For these terms, use the pre-defined translation:
- Quick Quiz: Kiểm tra nhanh
- Unit: Chương
- Bonus Unit: Chương bổ trợ
- Module: Mô-đun
- Lesson ...: Bài ...
- Model: Mô hình
- Dataset: Tập dữ liệu
- Course: Khóa học
- state-of-the-art: nổi tiếng
- Q&A: Hỏi và Đáp
- Dummy: ảo (or "giả", or "thử" depending on the context)
- onboarding: làm quen
- Hands-on: Thực hành
- Challenge: Bài tập lớn
- Training: Huấn luyện
- Model Context Protocol: Giao Thức Ngữ Cảnh Mô Hình

Here is an example:
- Original text: [Agents Course](https://huggingface.co/learn/agents-course/) will guide you through building AI agents with LLMs.
- Translation: [Agents Course](https://huggingface.co/learn/agents-course/) sẽ hướng dẫn các bạn cách xây dựng AI Agents với LLMs.

Here is another example:
- Original text: JSON-RPC defines the message format, but MCP also specifies how these messages are transported between Clients and Servers.
- Translation: JSON-RPC định nghĩa định dạng tin nhắn, nhưng MCP cũng chỉ định cách thức các tin nhắn này được truyền tải giữa Máy khách và Máy chủ.

If the code block contains many plain texts, prove translation in collapsible <details> tag. Example:
- Original text:
    ```python
    def get_weather(location: str) -> dict:
        """Get the current weather for a specified location."""
        # Connect to weather API and fetch data
        return {{
            "temperature": 72,
            "conditions": "Sunny",
            "humidity": 45
        }}
    ```
- Translation (add the <details> collapsible ABOVE of the original code block):
    <details>
    <summary>Bấm để xem bản dịch tiếng Việt</summary>
    ```
    def get_weather(location: str) -> dict:
        """Nhận thông tin thời tiết hiện tại ở một địa điểm cụ thể."""
        # Connect to weather API and fetch data
        return {{
            "temperature": 72,
            "conditions": "Sunny",
            "humidity": 45
        }}
    ```
    </details>
    ```
    def get_weather(location: str) -> dict:
        """Get the current weather for a specified location."""
        # Connect to weather API and fetch data
        return {{
            "temperature": 72,
            "conditions": "Sunny",
            "humidity": 45
        }}
    ```

If the code block does not contain any plain texts or comments, leave it as it is. Example:
- Original text:
    ```json
    {{
    "servers": [
        {{
        "name": "File Explorer",
        "transport": {{
            "type": "stdio",
            "command": "python",
            "args": ["/path/to/file_explorer_server.py"]
        }}
        }}
    ]
    }}
    ```

- Translation:
    ```json
    {{
    "servers": [
        {{
        "name": "File Explorer",
        "transport": {{
            "type": "stdio",
            "command": "python",
            "args": ["/path/to/file_explorer_server.py"]
        }}
        }}
    ]
    }}
    ```

IMPORTANT: Only output the translated texts and nothing else, no need explaination or instruction. The input text is between "=== BEGIN OF TEXT ===" and "=== END OF TEXT ===".

Please translate the following texts to Vietnamese:

=== BEGIN OF TEXT ===
{content}
=== END OF TEXT ===
'''.strip()

auto_translate(
    prompt=prompt,
    output_lang=output_lang,
)
````

## File: units/en/unit1/architectural-components.mdx
````
# Architectural Components of MCP

In the previous section, we discussed the key concepts and terminology of MCP. Now, let's dive deeper into the architectural components that make up the MCP ecosystem.

## Host, Client, and Server

The Model Context Protocol (MCP) is built on a client-server architecture that enables structured communication between AI models and external systems. 

![MCP Architecture](https://huggingface.co/datasets/mcp-course/images/resolve/main/unit1/4.png)

The MCP architecture consists of three primary components, each with well-defined roles and responsibilities: Host, Client, and Server. We touched on these in the previous section, but let's dive deeper into each component and their responsibilities.

### Host

The **Host** is the user-facing AI application that end-users interact with directly. 

Examples include:
- AI Chat apps like OpenAI ChatGPT or Anthropic's Claude Desktop
- AI-enhanced IDEs like Cursor, or integrations to tools like Continue.dev
- Custom AI agents and applications built in libraries like LangChain or smolagents

The Host's responsibilities include:
- Managing user interactions and permissions
- Initiating connections to MCP Servers via MCP Clients
- Orchestrating the overall flow between user requests, LLM processing, and external tools
- Rendering results back to users in a coherent format

In most cases, users will select their host application based on their needs and preferences. For example, a developer may choose Cursor for its powerful code editing capabilities, while domain experts may use custom applications built in smolagents.

### Client

The **Client** is a component within the Host application that manages communication with a specific MCP Server. Key characteristics include:

- Each Client maintains a 1:1 connection with a single Server
- Handles the protocol-level details of MCP communication
- Acts as the intermediary between the Host's logic and the external Server

### Server

The **Server** is an external program or service that exposes capabilities to AI models via the MCP protocol. Servers:

- Provide access to specific external tools, data sources, or services
- Act as lightweight wrappers around existing functionality
- Can run locally (on the same machine as the Host) or remotely (over a network)
- Expose their capabilities in a standardized format that Clients can discover and use

## Communication Flow

Let's examine how these components interact in a typical MCP workflow:

<Tip>

In the next section, we'll dive deeper into the communication protocol that enables these components with practical examples.

</Tip>

1. **User Interaction**: The user interacts with the **Host** application, expressing an intent or query.

2. **Host Processing**: The **Host** processes the user's input, potentially using an LLM to understand the request and determine which external capabilities might be needed.

3. **Client Connection**: The **Host** directs its **Client** component to connect to the appropriate Server(s).

4. **Capability Discovery**: The **Client** queries the **Server** to discover what capabilities (Tools, Resources, Prompts) it offers.

5. **Capability Invocation**: Based on the user's needs or the LLM's determination, the Host instructs the **Client** to invoke specific capabilities from the **Server**.

6. **Server Execution**: The **Server** executes the requested functionality and returns results to the **Client**.

7. **Result Integration**: The **Client** relays these results back to the **Host**, which incorporates them into the context for the LLM or presents them directly to the user.

A key advantage of this architecture is its modularity. A single **Host** can connect to multiple **Servers** simultaneously via different **Clients**. New **Servers** can be added to the ecosystem without requiring changes to existing **Hosts**. Capabilities can be easily composed across different **Servers**.

<Tip>

As we discussed in the previous section, this modularity transforms the traditional M×N integration problem (M AI applications connecting to N tools/services) into a more manageable M+N problem, where each Host and Server needs to implement the MCP standard only once.

</Tip>

The architecture might appear simple, but its power lies in the standardization of the communication protocol and the clear separation of responsibilities between components. This design allows for a cohesive ecosystem where AI models can seamlessly connect with an ever-growing array of external tools and data sources.

## Conclusion

These interaction patterns are guided by several key principles that shape the design and evolution of MCP. The protocol emphasizes **standardization** by providing a universal protocol for AI connectivity, while maintaining **simplicity** by keeping the core protocol straightforward yet enabling advanced features. **Safety** is prioritized by requiring explicit user approval for sensitive operations, and discoverability enables dynamic discovery of capabilities. The protocol is built with **extensibility** in mind, supporting evolution through versioning and capability negotiation, and ensures **interoperability** across different implementations and environments.

In the next section, we'll explore the communication protocol that enables these components to work together effectively.
````

## File: units/en/unit1/capabilities.mdx
````
# Understanding MCP Capabilities

MCP Servers expose a variety of capabilities to Clients through the communication protocol. These capabilities fall into four main categories, each with distinct characteristics and use cases. Let's explore these core primitives that form the foundation of MCP's functionality.

<Tip>

In this section, we'll show examples as framework agnostic functions in each language. This is to focus on the concepts and how they work together, rather than the complexities of any framework.

In the coming units, we'll show how these concepts are implemented in MCP specific code.

</Tip>

## Tools

Tools are executable functions or actions that the AI model can invoke through the MCP protocol.

- **Control**: Tools are typically **model-controlled**, meaning that the AI model (LLM) decides when to call them based on the user's request and context.
- **Safety**: Due to their ability to perform actions with side effects, tool execution can be dangerous. Therefore, they typically require explicit user approval.
- **Use Cases**: Sending messages, creating tickets, querying APIs, performing calculations.

**Example**: A weather tool that fetches current weather data for a given location:

<hfoptions id="tool-example">
<hfoption id="python">

```python
def get_weather(location: str) -> dict:
    """Get the current weather for a specified location."""
    # Connect to weather API and fetch data
    return {
        "temperature": 72,
        "conditions": "Sunny",
        "humidity": 45
    }
```

</hfoption>
<hfoption id="javascript">

```javascript
function getWeather(location) {
    // Connect to weather API and fetch data
    return {
        temperature: 72,
        conditions: 'Sunny',
        humidity: 45
    };
}
```

</hfoption>
</hfoptions>

## Resources

Resources provide read-only access to data sources, allowing the AI model to retrieve context without executing complex logic.

- **Control**: Resources are **application-controlled**, meaning the Host application typically decides when to access them.
- **Nature**: They are designed for data retrieval with minimal computation, similar to GET endpoints in REST APIs.
- **Safety**: Since they are read-only, they typically present lower security risks than Tools.
- **Use Cases**: Accessing file contents, retrieving database records, reading configuration information.

**Example**: A resource that provides access to file contents:

<hfoptions id="resource-example">
<hfoption id="python">

```python
def read_file(file_path: str) -> str:
    """Read the contents of a file at the specified path."""
    with open(file_path, 'r') as f:
        return f.read()
```

</hfoption>
<hfoption id="javascript">

```javascript
function readFile(filePath) {
    // Using fs.readFile to read file contents
    const fs = require('fs');
    return new Promise((resolve, reject) => {
        fs.readFile(filePath, 'utf8', (err, data) => {
            if (err) {
                reject(err);
                return;
            }
            resolve(data);
        });
    });
}
```

</hfoption>
</hfoptions>

## Prompts

Prompts are predefined templates or workflows that guide the interaction between the user, the AI model, and the Server's capabilities.

- **Control**: Prompts are **user-controlled**, often presented as options in the Host application's UI.
- **Purpose**: They structure interactions for optimal use of available Tools and Resources.
- **Selection**: Users typically select a prompt before the AI model begins processing, setting context for the interaction.
- **Use Cases**: Common workflows, specialized task templates, guided interactions.

**Example**: A prompt template for generating a code review:

<hfoptions id="prompt-example">
<hfoption id="python">

```python
def code_review(code: str, language: str) -> list:
    """Generate a code review for the provided code snippet."""
    return [
        {
            "role": "system",
            "content": f"You are a code reviewer examining {language} code. Provide a detailed review highlighting best practices, potential issues, and suggestions for improvement."
        },
        {
            "role": "user",
            "content": f"Please review this {language} code:\n\n```{language}\n{code}\n```"
        }
    ]
```

</hfoption>
<hfoption id="javascript">

```javascript
function codeReview(code, language) {
    return [
        {
            role: 'system',
            content: `You are a code reviewer examining ${language} code. Provide a detailed review highlighting best practices, potential issues, and suggestions for improvement.`
        },
        {
            role: 'user',
            content: `Please review this ${language} code:\n\n\`\`\`${language}\n${code}\n\`\`\``
        }
    ];
}
```

</hfoption>
</hfoptions>

## Sampling

Sampling allows Servers to request the Client (specifically, the Host application) to perform LLM interactions.

- **Control**: Sampling is **server-initiated** but requires Client/Host facilitation.
- **Purpose**: It enables server-driven agentic behaviors and potentially recursive or multi-step interactions.
- **Safety**: Like Tools, sampling operations typically require user approval.
- **Use Cases**: Complex multi-step tasks, autonomous agent workflows, interactive processes.

**Example**: A Server might request the Client to analyze data it has processed:

<hfoptions id="sampling-example">
<hfoption id="python">

```python
def request_sampling(messages, system_prompt=None, include_context="none"):
    """Request LLM sampling from the client."""
    # In a real implementation, this would send a request to the client
    return {
        "role": "assistant",
        "content": "Analysis of the provided data..."
    }
```

</hfoption>
<hfoption id="javascript">

```javascript
function requestSampling(messages, systemPrompt = null, includeContext = 'none') {
    // In a real implementation, this would send a request to the client
    return {
        role: 'assistant',
        content: 'Analysis of the provided data...'
    };
}

function handleSamplingRequest(request) {
    const { messages, systemPrompt, includeContext } = request;
    // In a real implementation, this would process the request and return a response
    return {
        role: 'assistant',
        content: 'Response to the sampling request...'
    };
}
```

</hfoption>
</hfoptions>

The sampling flow follows these steps:
1. Server sends a `sampling/createMessage` request to the client
2. Client reviews the request and can modify it
3. Client samples from an LLM
4. Client reviews the completion
5. Client returns the result to the server

<Tip>

This human-in-the-loop design ensures users maintain control over what the LLM sees and generates. When implementing sampling, it's important to provide clear, well-structured prompts and include relevant context.

</Tip>

## How Capabilities Work Together

Let's look at how these capabilities work together to enable complex interactions. In the table below, we've outlined the capabilities, who controls them, the direction of control, and some other details.

| Capability | Controlled By | Direction | Side Effects | Approval Needed | Typical Use Cases |
|------------|---------------|-----------|--------------|-----------------|-------------------|
| Tools      | Model (LLM)   | Client → Server | Yes (potentially) | Yes | Actions, API calls, data manipulation |
| Resources  | Application   | Client → Server | No (read-only) | Typically no | Data retrieval, context gathering |
| Prompts    | User          | Server → Client | No | No (selected by user) | Guided workflows, specialized templates |
| Sampling   | Server        | Server → Client → Server | Indirectly | Yes | Multi-step tasks, agentic behaviors |

These capabilities are designed to work together in complementary ways:

1. A user might select a **Prompt** to start a specialized workflow
2. The Prompt might include context from **Resources**
3. During processing, the AI model might call **Tools** to perform specific actions
4. For complex operations, the Server might use **Sampling** to request additional LLM processing

The distinction between these primitives provides a clear structure for MCP interactions, enabling AI models to access information, perform actions, and engage in complex workflows while maintaining appropriate control boundaries.

## Discovery Process

One of MCP's key features is dynamic capability discovery. When a Client connects to a Server, it can query the available Tools, Resources, and Prompts through specific list methods:

- `tools/list`: Discover available Tools
- `resources/list`: Discover available Resources
- `prompts/list`: Discover available Prompts

This dynamic discovery mechanism allows Clients to adapt to the specific capabilities each Server offers without requiring hardcoded knowledge of the Server's functionality.

## Conclusion

Understanding these core primitives is essential for working with MCP effectively. By providing distinct types of capabilities with clear control boundaries, MCP enables powerful interactions between AI models and external systems while maintaining appropriate safety and control mechanisms.

In the next section, we'll explore how Gradio integrates with MCP to provide easy-to-use interfaces for these capabilities.
````

## File: units/en/unit1/certificate.mdx
````
# Get your certificate!

Well done! You've completed the first unit of the MCP course. Now it's time to take the exam to get your certificate.

Below is a quiz to check your understanding of the unit. 

<iframe
	src="https://mcp-course-unit-1-quiz.hf.space"
	frameborder="0"
	width="850"
	height="450"
></iframe>

<Tip>

If you're struggling to use the quiz above, go to the space directly [on the Hugging Face Hub](https://huggingface.co/spaces/mcp-course/unit_1_quiz). If you find errors, you can report them in the space's [Community tab](https://huggingface.co/spaces/mcp-course/unit_1_quiz/discussions).

</Tip>
````

## File: units/en/unit1/communication-protocol.mdx
````
# The Communication Protocol

MCP defines a standardized communication protocol that enables Clients and Servers to exchange messages in a consistent, predictable way. This standardization is critical for interoperability across the community. In this section, we'll explore the protocol structure and transport mechanisms used in MCP.

<Tip warning={true}>

We're getting down to the nitty-gritty details of the MCP protocol. You won't need to know all of this to build with MCP, but it's good to know that it exists and how it works.

</Tip>

## JSON-RPC: The Foundation

At its core, MCP uses **JSON-RPC 2.0** as the message format for all communication between Clients and Servers. JSON-RPC is a lightweight remote procedure call protocol encoded in JSON, which makes it:

- Human-readable and easy to debug
- Language-agnostic, supporting implementation in any programming environment
- Well-established, with clear specifications and widespread adoption

![message types](https://huggingface.co/datasets/mcp-course/images/resolve/main/unit1/5.png)

The protocol defines three types of messages:

### 1. Requests

Sent from Client to Server to initiate an operation. A Request message includes:
- A unique identifier (`id`)
- The method name to invoke (e.g., `tools/call`)
- Parameters for the method (if any)

Example Request:

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "weather",
    "arguments": {
      "location": "San Francisco"
    }
  }
}
```

### 2. Responses

Sent from Server to Client in reply to a Request. A Response message includes:
- The same `id` as the corresponding Request
- Either a `result` (for success) or an `error` (for failure)

Example Success Response:
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "temperature": 62,
    "conditions": "Partly cloudy"
  }
}
```

Example Error Response:
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "error": {
    "code": -32602,
    "message": "Invalid location parameter"
  }
}
```

### 3. Notifications

One-way messages that don't require a response. Typically sent from Server to Client to provide updates or notifications about events.

Example Notification:
```json
{
  "jsonrpc": "2.0",
  "method": "progress",
  "params": {
    "message": "Processing data...",
    "percent": 50
  }
}
```

## Transport Mechanisms

JSON-RPC defines the message format, but MCP also specifies how these messages are transported between Clients and Servers. Two primary transport mechanisms are supported:

### stdio (Standard Input/Output)

The stdio transport is used for local communication, where the Client and Server run on the same machine:

The Host application launches the Server as a subprocess and communicates with it by writing to its standard input (stdin) and reading from its standard output (stdout).

<Tip>

**Use cases** for this transport are local tools like file system access or running local scripts.

</Tip>

The main **Advantages** of this transport are that it's simple, no network configuration required, and securely sandboxed by the operating system.

### HTTP + SSE (Server-Sent Events) / Streamable HTTP

The HTTP+SSE transport is used for remote communication, where the Client and Server might be on different machines:

Communication happens over HTTP, with the Server using Server-Sent Events (SSE) to push updates to the Client over a persistent connection.

<Tip>

**Use cases** for this transport are connecting to remote APIs, cloud services, or shared resources.

</Tip>

The main **Advantages** of this transport are that it works across networks, enables integration with web services, and is compatible with serverless environments.

Recent updates to the MCP standard have introduced or refined "Streamable HTTP," which offers more flexibility by allowing servers to dynamically upgrade to SSE for streaming when needed, while maintaining compatibility with serverless environments.

## The Interaction Lifecycle

In the previous section, we discussed the lifecycle of a single interaction between a Client (💻) and a Server (🌐). Let's now look at the lifecycle of a complete interaction between a Client and a Server in the context of the MCP protocol.

The MCP protocol defines a structured interaction lifecycle between Clients and Servers:

### Initialization

The Client connects to the Server and they exchange protocol versions and capabilities, and the Server responds with its supported protocol version and capabilities.

<table style="width: 100%;">
  <tr>
    <td style="background-color: lightgreen; text-align: center; padding: 10px; border: 1px solid #ccc; border-radius: 4px;">💻</td>
    <td style="text-align: center;">→<br>initialize</td>
    <td style="background-color: lightblue; text-align: center; padding: 10px; border: 1px solid #ccc; border-radius: 4px;">🌐</td>
  </tr>
  <tr>
    <td style="background-color: lightgreen; text-align: center; padding: 10px; border: 1px solid #ccc; border-radius: 4px;">💻</td>
    <td style="text-align: center;">←<br>response</td>
    <td style="background-color: lightblue; text-align: center; padding: 10px; border: 1px solid #ccc; border-radius: 4px;">🌐</td>
  </tr>
  <tr>
    <td style="background-color: lightgreen; text-align: center; padding: 10px; border: 1px solid #ccc; border-radius: 4px;">💻</td>
    <td style="text-align: center;">→<br>initialized</td>
    <td style="background-color: lightblue; text-align: center; padding: 10px; border: 1px solid #ccc; border-radius: 4px;">🌐</td>
  </tr>
</table>

The Client confirms the initialization is complete via a notification message.

### Discovery

The Client requests information about available capabilities and the Server responds with a list of available tools.

<table style="width: 100%;">
  <tr>
    <td style="background-color: lightgreen; text-align: center; padding: 10px; border: 1px solid #ccc; border-radius: 4px;">💻</td>
    <td style="text-align: center;">→<br>tools/list</td>
    <td style="background-color: lightblue; text-align: center; padding: 10px; border: 1px solid #ccc; border-radius: 4px;">🌐</td>
  </tr>
  <tr>
    <td style="background-color: lightgreen; text-align: center; padding: 10px; border: 1px solid #ccc; border-radius: 4px;">💻</td>
    <td style="text-align: center;">←<br>response</td>
    <td style="background-color: lightblue; text-align: center; padding: 10px; border: 1px solid #ccc; border-radius: 4px;">🌐</td>
  </tr>
</table>

This process could be repeated for each tool, resource, or prompt type.

### Execution

The Client invokes capabilities based on the Host's needs.

<table style="width: 100%;">
  <tr>
    <td style="background-color: lightgreen; text-align: center; padding: 10px; border: 1px solid #ccc; border-radius: 4px;">💻</td>
    <td style="text-align: center;">→<br>tools/call</td>
    <td style="background-color: lightblue; text-align: center; padding: 10px; border: 1px solid #ccc; border-radius: 4px;">🌐</td>
  </tr>
  <tr>
    <td style="background-color: lightgreen; text-align: center; padding: 10px; border: 1px solid #ccc; border-radius: 4px;">💻</td>
    <td style="text-align: center;">←<br>notification (optional progress)</td>
    <td style="background-color: lightblue; text-align: center; padding: 10px; border: 1px solid #ccc; border-radius: 4px;">🌐</td>
  </tr>
  <tr>
    <td style="background-color: lightgreen; text-align: center; padding: 10px; border: 1px solid #ccc; border-radius: 4px;">💻</td>
    <td style="text-align: center;">←<br>response</td>
    <td style="background-color: lightblue; text-align: center; padding: 10px; border: 1px solid #ccc; border-radius: 4px;">🌐</td>
  </tr>
</table>

### Termination

The connection is gracefully closed when no longer needed and the Server acknowledges the shutdown request.

<table style="width: 100%;">
  <tr>
    <td style="background-color: lightgreen; text-align: center; padding: 10px; border: 1px solid #ccc; border-radius: 4px;">💻</td>
    <td style="text-align: center;">→<br>shutdown</td>
    <td style="background-color: lightblue; text-align: center; padding: 10px; border: 1px solid #ccc; border-radius: 4px;">🌐</td>
  </tr>
  <tr>
    <td style="background-color: lightgreen; text-align: center; padding: 10px; border: 1px solid #ccc; border-radius: 4px;">💻</td>
    <td style="text-align: center;">←<br>response</td>
    <td style="background-color: lightblue; text-align: center; padding: 10px; border: 1px solid #ccc; border-radius: 4px;">🌐</td>
  </tr>
  <tr>
    <td style="background-color: lightgreen; text-align: center; padding: 10px; border: 1px solid #ccc; border-radius: 4px;">💻</td>
    <td style="text-align: center;">→<br>exit</td>
    <td style="background-color: lightblue; text-align: center; padding: 10px; border: 1px solid #ccc; border-radius: 4px;">🌐</td>
  </tr>
</table>

The Client sends the final exit message to complete the termination.

## Protocol Evolution

The MCP protocol is designed to be extensible and adaptable. The initialization phase includes version negotiation, allowing for backward compatibility as the protocol evolves. Additionally, capability discovery enables Clients to adapt to the specific features each Server offers, enabling a mix of basic and advanced Servers in the same ecosystem.
````

## File: units/en/unit1/gradio-mcp.mdx
````
# Gradio MCP Integration

We've now explored the core concepts of the MCP protocol and how to implement MCP Servers and Clients. In this section, we're going to make things slightly easier by using Gradio to create an MCP Server!

<Tip>

Gradio is a popular Python library for quickly creating customizable web interfaces for machine learning models. 

</Tip>

## Introduction to Gradio

Gradio allows developers to create UIs for their models with just a few lines of Python code. It's particularly useful for:

- Creating demos and prototypes
- Sharing models with non-technical users
- Testing and debugging model behavior

With the addition of MCP support, Gradio now offers a straightforward way to expose AI model capabilities through the standardized MCP protocol.

Combining Gradio with MCP allows you to create both human-friendly interfaces and AI-accessible tools with minimal code. But best of all, Gradio is already well-used by the AI community, so you can use it to share your MCP Servers with others.

## Prerequisites

To use Gradio with MCP support, you'll need to install Gradio with the MCP extra:

```bash
pip install "gradio[mcp]"
```

You'll also need an LLM application that supports tool calling using the MCP protocol, such as Cursor ( known as "MCP Hosts").

## Creating an MCP Server with Gradio

Let's walk through a basic example of creating an MCP Server using Gradio:

```python
import gradio as gr

def letter_counter(word: str, letter: str) -> int:
    """
    Count the number of occurrences of a letter in a word or text.

    Args:
        word (str): The input text to search through
        letter (str): The letter to search for

    Returns:
        int: The number of times the letter appears in the text
    """
    word = word.lower()
    letter = letter.lower()
    count = word.count(letter)
    return count

# Create a standard Gradio interface
demo = gr.Interface(
    fn=letter_counter,
    inputs=["textbox", "textbox"],
    outputs="number",
    title="Letter Counter",
    description="Enter text and a letter to count how many times the letter appears in the text."
)

# Launch both the Gradio web interface and the MCP server
if __name__ == "__main__":
    demo.launch(mcp_server=True)
```

With this setup, your letter counter function is now accessible through:

1. A traditional Gradio web interface for direct human interaction
2. An MCP Server that can be connected to compatible clients

The MCP server will be accessible at:
```
http://your-server:port/gradio_api/mcp/sse
```

The application itself will still be accessible and it looks like this:

![Gradio MCP Server](https://huggingface.co/datasets/mcp-course/images/resolve/main/unit1/7.png)

## How It Works Behind the Scenes

When you set `mcp_server=True` in `launch()`, several things happen:

1. Gradio functions are automatically converted to MCP Tools
2. Input components map to tool argument schemas
3. Output components determine the response format
4. The Gradio server now also listens for MCP protocol messages
5. JSON-RPC over HTTP+SSE is set up for client-server communication

## Key Features of the Gradio <> MCP Integration

1. **Tool Conversion**: Each API endpoint in your Gradio app is automatically converted into an MCP tool with a corresponding name, description, and input schema. To view the tools and schemas, visit `http://your-server:port/gradio_api/mcp/schema` or go to the "View API" link in the footer of your Gradio app, and then click on "MCP".

2. **Environment Variable Support**: There are two ways to enable the MCP server functionality:
- Using the `mcp_server` parameter in `launch()`:
  ```python
  demo.launch(mcp_server=True)
  ```
- Using environment variables:
  ```bash
  export GRADIO_MCP_SERVER=True
  ```

3. **File Handling**: The server automatically handles file data conversions, including:
   - Converting base64-encoded strings to file data
   - Processing image files and returning them in the correct format
   - Managing temporary file storage

   It is **strongly** recommended that input images and files be passed as full URLs ("http://..." or "https://...") as MCP Clients do not always handle local files correctly.

4. **Hosted MCP Servers on 🤗 Spaces**: You can publish your Gradio application for free on Hugging Face Spaces, which will allow you to have a free hosted MCP server. Here's an example of such a Space: https://huggingface.co/spaces/abidlabs/mcp-tools

## Troubleshooting Tips

1. **Type Hints and Docstrings**: Ensure you provide type hints and valid docstrings for your functions. The docstring should include an "Args:" block with indented parameter names.

2. **String Inputs**: When in doubt, accept input arguments as `str` and convert them to the desired type inside the function.

3. **SSE Support**: Some MCP Hosts don't support SSE-based MCP Servers. In those cases, you can use `mcp-remote`:
   ```json
   {
     "mcpServers": {
       "gradio": {
         "command": "npx",
         "args": [
           "mcp-remote",
           "http://your-server:port/gradio_api/mcp/sse"
         ]
       }
     }
   }
   ```

4. **Restart**: If you encounter connection issues, try restarting both your MCP Client and MCP Server.

## Share your MCP Server

You can share your MCP Server by publishing your Gradio app to Hugging Face Spaces. The video below shows how to create a Hugging Face Space.

<Youtube id="3bSVKNKb_PY" />

Now, you can share your MCP Server with others by sharing your Hugging Face Space.

## Conclusion

Gradio's integration with MCP provides an accessible entry point to the MCP ecosystem. By leveraging Gradio's simplicity and adding MCP's standardization, developers can quickly create both human-friendly interfaces and AI-accessible tools with minimal code.

As we progress through this course, we'll explore more sophisticated MCP implementations, but Gradio offers an excellent starting point for understanding and experimenting with the protocol.

In the next unit, we'll dive deeper into building MCP applications, focusing on setting up development environments, exploring SDKs, and implementing more advanced MCP Servers and Clients.
````

## File: units/en/unit1/introduction.mdx
````
# Introduction to Model Context Protocol (MCP)

Welcome to Unit 1 of the MCP Course! In this unit, we'll explore the fundamentals of Model Context Protocol.

## What You Will Learn

In this unit, you will:

* Understand what Model Context Protocol is and why it's important
* Learn the key concepts and terminology associated with MCP
* Explore the integration challenges that MCP solves
* Walk through the key benefits and goals of MCP
* See a simple example of MCP integration in action

By the end of this unit, you'll have a solid understanding of the foundational concepts of MCP and be ready to dive deeper into its architecture and implementation in the next unit.

## Importance of MCP

The AI ecosystem is evolving rapidly, with Large Language Models (LLMs) and other AI systems becoming increasingly capable. However, these models are often limited by their training data and lack access to real-time information or specialized tools. This limitation hinders the potential of AI systems to provide truly relevant, accurate, and helpful responses in many scenarios.

This is where Model Context Protocol (MCP) comes in. MCP enables AI models to connect with external data sources, tools, and environments, allowing for the seamless transfer of information and capabilities between AI systems and the broader digital world. This interoperability is crucial for the growth and adoption of truly useful AI applications.

## Overview of Unit 1

Here's a brief overview of what we'll cover in this unit:

1. **What is Model Context Protocol?** - We'll start by defining what MCP is and discussing its role in the AI ecosystem.
2. **Key Concepts** - We'll explore the fundamental concepts and terminology associated with MCP.
3. **Integration Challenges** - We'll examine the problems that MCP aims to solve, particularly the "M×N Integration Problem."
4. **Benefits and Goals** - We'll discuss the key benefits and goals of MCP, including standardization, enhanced AI capabilities, and interoperability.
5. **Simple Example** - Finally, we'll walk through a simple example of MCP integration to see how it works in practice.

Let's dive in and explore the exciting world of Model Context Protocol!
````

## File: units/en/unit1/key-concepts.mdx
````
# Key Concepts and Terminology

Before diving deeper into the Model Context Protocol, it's important to understand the key concepts and terminology that form the foundation of MCP. This section will introduce the fundamental ideas that underpin the protocol and provide a common vocabulary for discussing MCP implementations throughout the course.

MCP is often described as the "USB-C for AI applications." Just as USB-C provides a standardized physical and logical interface for connecting various peripherals to computing devices, MCP offers a consistent protocol for linking AI models to external capabilities. This standardization benefits the entire ecosystem:

- **users** enjoy simpler and more consistent experiences across AI applications
- **AI application developers** gain easy integration with a growing ecosystem of tools and data sources
- **tool and data providers** need only create a single implementation that works with multiple AI applications
- the broader ecosystem benefits from increased interoperability, innovation, and reduced fragmentation

## The Integration Problem

The **M×N Integration Problem** refers to the challenge of connecting M different AI applications to N different external tools or data sources without a standardized approach. 

### Without MCP (M×N Problem)

Without a protocol like MCP, developers would need to create M×N custom integrations—one for each possible pairing of an AI application with an external capability. 

![Without MCP](https://huggingface.co/datasets/mcp-course/images/resolve/main/unit1/1.png)

Each AI application would need to integrate with each tool/data source individually. This is a very complex and expensive process which introduces a lot of friction for developers, and high maintenance costs.

Once we have multiple models and multiple tools, the number of integrations becomes too large to manage, each with its own unique interface.

![Multiple Models and Tools](https://huggingface.co/datasets/mcp-course/images/resolve/main/unit1/1a.png)

### With MCP (M+N Solution)

MCP transforms this into an M+N problem by providing a standard interface: each AI application implements the client side of MCP once, and each tool/data source implements the server side once. This dramatically reduces integration complexity and maintenance burden.

![With MCP](https://huggingface.co/datasets/mcp-course/images/resolve/main/unit1/2.png)

Each AI application implements the client side of MCP once, and each tool/data source implements the server side once.

## Core MCP Terminology

Now that we understand the problem that MCP solves, let's dive into the core terminology and concepts that make up the MCP protocol.

<Tip>

MCP is a standard like HTTP or USB-C, and is a protocol for connecting AI applications to external tools and data sources. Therefore, using standard terminology is crucial to making the MCP work effectively. 

When documenting our applications and communicating with the community, we should use the following terminology.

</Tip>

### Components

Just like client server relationships in HTTP, MCP has a client and a server.

![MCP Components](https://huggingface.co/datasets/mcp-course/images/resolve/main/unit1/3.png)

- **Host**: The user-facing AI application that end-users interact with directly. Examples include Anthropic's Claude Desktop, AI-enhanced IDEs like Cursor, inference libraries like Hugging Face Python SDK, or custom applications built in libraries like LangChain or smolagents. Hosts initiate connections to MCP Servers and orchestrate the overall flow between user requests, LLM processing, and external tools.

- **Client**: A component within the host application that manages communication with a specific MCP Server. Each Client maintains a 1:1 connection with a single Server, handling the protocol-level details of MCP communication and acting as an intermediary between the Host's logic and the external Server.

- **Server**: An external program or service that exposes capabilities (Tools, Resources, Prompts) via the MCP protocol.

<Tip warning={true}>

A lot of content uses 'Client' and 'Host' interchangeably. Technically speaking, the host is the user-facing application, and the client is the component within the host application that manages communication with a specific MCP Server.

</Tip>

### Capabilities

Of course, your application's value is the sum of the capabilities it offers. So the capabilities are the most important part of your application. MCP's can connect with any software service, but there are some common capabilities that are used for many AI applications.

| Capability | Description | Example |
| ---------- | ----------- | ------- |
| **Tools** | Executable functions that the AI model can invoke to perform actions or retrieve computed data. Typically relating to the use case of the application. | A tool for a weather application might be a function that returns the weather in a specific location. |
| **Resources** | Read-only data sources that provide context without significant computation. | A researcher assistant might have a resource for scientific papers. |
| **Prompts** | Pre-defined templates or workflows that guide interactions between users, AI models, and the available capabilities. | A summarization prompt. |
| **Sampling** | Server-initiated requests for the Client/Host to perform LLM interactions, enabling recursive actions where the LLM can review generated content and make further decisions. | A writing application reviewing its own output and decides to refine it further. |

In the following diagram, we can see the collective capabilities applied to a use case for a code agent.

![collective diagram](https://huggingface.co/datasets/mcp-course/images/resolve/main/unit1/8.png)

This application might use their MCP entities in the following way:

| Entity | Name | Description |
| --- | --- | --- |
| Tool | Code Interpreter | A tool that can execute code that the LLM writes. |
| Resource | Documentation | A resource that contains the documentation of the application. |
| Prompt | Code Style | A prompt that guides the LLM to generate code. |
| Sampling | Code Review | A sampling that allows the LLM to review the code and make further decisions. |

### Conclusion

Understanding these key concepts and terminology provides the foundation for working with MCP effectively. In the following sections, we'll build on this foundation to explore the architectural components, communication protocol, and capabilities that make up the Model Context Protocol.
````

## File: units/en/unit1/quiz1.mdx
````
# Quiz 1: MCP Fundamentals

Test your knowledge of the core concepts of Model Context Protocol.

### Q1: What is the primary purpose of Model Context Protocol (MCP)?

<Question
  choices={[
    {
      text: "To limit the training data of AI models",
      explain: "MCP aims to expand, not limit, the contexts AI models can access."
    },
    {
      text: "To enable AI models to connect with external data sources, tools, and environments",
      explain: "Correct! MCP's main goal is to facilitate interoperability.",
      correct: true
    },
    {
      text: "To replace prompting when using Large Language Models",
      explain: "MCP is a protocol that enhances prompting, not a replacement for it."
    },
    {
      text: "To create a new programming language for AI",
      explain: "MCP is a protocol, not a programming language."
    }
  ]}
/>

### Q2: What problem does MCP primarily aim to solve?

<Question
  choices={[
    {
      text: "The lack of AI models",
      explain: "MCP addresses integration challenges, not the availability of AI models themselves."
    },
    {
      text: "The high cost of training LLMs",
      explain: "While MCP can improve efficiency, its primary focus is not on reducing training costs directly."
    },
    {
      text: "The M×N Integration Problem",
      explain: "Correct! MCP standardizes connections to avoid M×N custom integrations.",
      correct: true
    },
    {
      text: "The difficulty in creating new AI algorithms",
      explain: "MCP facilitates using existing algorithms and tools, not creating new ones from scratch."
    }
  ]}
/>

### Q3: Which of the following is a key benefit of MCP?

<Question
  choices={[
    {
      text: "Reduced AI model accuracy",
      explain: "MCP aims to enhance AI capabilities, which should ideally lead to improved or maintained accuracy, not reduced."
    },
    {
      text: "Increased complexity in AI development",
      explain: "MCP aims to simplify integration, thereby reducing complexity."
    },
    {
      text: "Standardization and interoperability in the AI ecosystem",
      explain: "Correct! This is a primary goal and benefit of MCP.",
      correct: true
    },
    {
      text: "Isolation of AI models from external systems",
      explain: "MCP promotes connection and interaction, not isolation."
    }
  ]}
/>

### Q4: In MCP terminology, what is a "Host"?

<Question
  choices={[
    {
      text: "The external program exposing capabilities",
      explain: "This describes an MCP Server."
    },
    {
      text: "The user-facing AI application",
      explain: "Correct! The Host is the application users interact with.",
      correct: true
    },
    {
      text: "A read-only data source",
      explain: "This describes a type of MCP Capability (Resource)."
    },
    {
      text: "A pre-defined template for interactions",
      explain: "This describes a type of MCP Capability (Prompt)."
    }
  ]}
/>

### Q5: What does "M×N Integration Problem" refer to in the context of AI applications?

<Question
  choices={[
    {
      text: "The difficulty of training M models with N datasets",
      explain: "This relates to model training, not the integration problem MCP addresses."
    },
    {
      text: "The challenge of connecting M AI applications to N external tools without a standard",
      explain: "Correct! MCP provides the standard to solve this M*N complexity.",
      correct: true
    },
    {
      text: "The problem of managing M users across N applications",
      explain: "This is a user management or identity problem, not the focus of MCP."
    },
    {
      text: "The complexity of developing M features for N different user segments",
      explain: "This relates to product development strategy, not system integration in the way MCP defines."
    }
  ]}
/>

Congrats on finishing this Quiz 🥳! If you need to review any elements, take the time to revisit the chapter to reinforce your knowledge.
````

## File: units/en/unit1/quiz2.mdx
````
# Quiz 2: MCP SDK

Test your knowledge of the MCP SDKs and their functionalities.

### Q1: What is the main purpose of the MCP SDKs?

<Question
  choices={[
    {
      text: "To define the MCP protocol specification",
      explain: "The SDKs implement the protocol, they don't define it. The specification is separate."
    },
    {
      text: "To make it easier to implement MCP clients and servers",
      explain: "Correct! SDKs abstract away low-level protocol details.",
      correct: true
    },
    {
      text: "To provide a visual interface for MCP interactions",
      explain: "While some tools might offer this (like MCP Inspector), it's not the primary purpose of the SDKs themselves."
    },
    {
      text: "To replace the need for programming languages",
      explain: "SDKs are libraries used within programming languages."
    }
  ]}
/>

### Q2: Which of the following functionalities do the MCP SDKs typically handle?

<Question
  choices={[
    {
      text: "Optimizing MCP Servers",
      explain: "This is outside the scope of MCP SDKs, which focus on protocol implementation."
    },
    {
      text: "Defining new AI algorithms",
      explain: "This is outside the scope of MCP SDKs, which focus on protocol implementation."
    },
    {
      text: "Message serialization/deserialization",
      explain: "Correct! This is a core function for handling JSON-RPC messages.",
      correct: true
    },
    {
      text: "Hosting Large Language Models",
      explain: "MCP enables connection to LLMs, but the SDKs themselves don't host them."
    }
  ]}
/>

### Q3: According to the provided text, which company maintains the official Python SDK for MCP?

<Question
  choices={[
    {
      text: "Google",
      explain: "The text lists Anthropic as the maintainer."
    },
    {
      text: "Anthropic",
      explain: "Correct! The course material indicates Anthropic maintains the Python SDK.",
      correct: true
    },
    {
      text: "Microsoft",
      explain: "Microsoft maintains the C# SDK according to the text."
    },
    {
      text: "JetBrains",
      explain: "JetBrains maintains the Kotlin SDK according to the text."
    }
  ]}
/>

### Q4: What command is used to start a development MCP server using a Python file named `server.py`?

<Question
  choices={[
    {
      text: "python server.py run",
      explain: "While you run Python scripts with `python`, MCP has a specific CLI command."
    },
    {
      text: "mcp start server.py",
      explain: "The command is `mcp dev`, not `mcp start`."
    },
    {
      text: "mcp dev server.py",
      explain: "Correct! This command initializes the development server.",
      correct: true
    },
    {
      text: "serve mcp server.py",
      explain: "This is not the standard MCP CLI command shown in the course material."
    }
  ]}
/>

### Q5: What is the role of JSON-RPC 2.0 in MCP?

<Question
  choices={[
    {
      text: "As a primary transport mechanism for remote communication",
      explain: "HTTP+SSE or Streamable HTTP are transport mechanisms; JSON-RPC is the message format."
    },
    {
      text: "As the message format for all communication between Clients and Servers",
      explain: "Correct! MCP uses JSON-RPC 2.0 for structuring messages.",
      correct: true
    },
    {
      text: "As a tool for debugging AI models",
      explain: "While its human-readable nature helps in debugging communications, it's not a debugging tool for AI models themselves."
    },
    {
      text: "As a method for defining AI capabilities like Tools and Resources",
      explain: "Capabilities are defined by their own schemas; JSON-RPC is used to invoke them and exchange data."
    }
  ]}
/>

Congrats on finishing this Quiz 🥳! If you need to review any elements, take the time to revisit the chapter to reinforce your knowledge.
````

## File: units/en/unit1/unit1-recap.mdx
````
# Unit1 recap

## Model Context Protocol (MCP)

The MCP is a standardized protocol designed to connect AI models with external tools, data sources, and environments. It addresses the limitations of existing AI systems by enabling interoperability and access to real-time information.

## Key Concepts

### Client-Server Architecture
MCP follows a client-server model where clients manage communication between users and servers. This architecture promotes modularity, allowing for easy addition of new servers without requiring changes to existing hosts.

### Components
#### Host
The user-facing AI application that serves as the interface for end-users.

##### Client
A component within the host application responsible for managing communication with a specific MCP server. Clients maintain 1:1 connections with servers and handle protocol-level details.

#### Server
An external program or service that provides access to tools, data sources, or services via the MCP protocol. Servers act as lightweight wrappers around existing functionalities.

### Capabilities
#### Tools
Executable functions that can perform actions (e.g., sending messages, querying APIs). Tools are typically model-controlled and require user approval due to their ability to perform actions with side effects.

#### Resources
Read-only data sources for context retrieval without significant computation. Resources are application-controlled and designed for data retrieval similar to GET endpoints in REST APIs.

#### Prompts
Pre-defined templates or workflows that guide interactions between users, AI models, and available capabilities. Prompts are user-controlled and set the context for interactions.

#### Sampling
Server-initiated requests for LLM processing, enabling server-driven agentic behaviors and potentially recursive or multi-step interactions. Sampling operations typically require user approval.

### Communication Protocol
The MCP protocol uses JSON-RPC 2.0 as the message format for communication between clients and servers. Two primary transport mechanisms are supported: stdio (for local communication) and HTTP+SSE (for remote communication). Messages include requests, responses, and notifications.

### Discovery Process
MCP allows clients to dynamically discover available tools, resources, and prompts through list methods (e.g., `tools/list`). This dynamic discovery mechanism enables clients to adapt to the specific capabilities each server offers without requiring hardcoded knowledge of server functionality.

### MCP SDKs
Official SDKs are available in various programming languages for implementing MCP clients and servers. These SDKs handle protocol-level communication, capability registration, and error handling, simplifying the development process.

### Gradio Integration
Gradio allows easy creation of web interfaces that expose capabilities to the MCP protocol, making it accessible for both humans and AI models. This integration provides a human-friendly interface alongside AI-accessible tools with minimal code.
````

## File: units/en/unit2/introduction.mdx
````
# Building an End-to-End MCP Application

Welcome to Unit 2 of the MCP Course! 

In this unit, we'll build a complete MCP application from scratch, focusing on creating a server with Gradio and connecting it with multiple clients. This hands-on approach will give you practical experience with the entire MCP ecosystem.

<Tip>

In this unit, we're going to build a simple MCP server and client using Gradio and the HuggingFace hub. In the next unit, we'll build a more complex server that tackles a real-world use case.

</Tip>

## What You'll Learn

In this unit, you will:

- Create an MCP Server using Gradio's built-in MCP support
- Build a sentiment analysis tool that can be used by AI models
- Connect to the server using different client implementations:
  - A HuggingFace.js-based client
  - A SmolAgents-based client for Python
- Deploy your MCP Server to Hugging Face Spaces
- Test and debug the complete system

By the end of this unit, you'll have a working MCP application that demonstrates the power and flexibility of the protocol.

## Prerequisites

Before proceeding with this unit, make sure you:

- Have completed Unit 1 or have a basic understanding of MCP concepts
- Are comfortable with both Python and JavaScript/TypeScript
- Have a basic understanding of APIs and client-server architecture
- Have a development environment with:
  - Python 3.10+
  - Node.js 18+
  - A Hugging Face account (for deployment)

## Our End-to-End Project

We'll build a sentiment analysis application that consists of three main parts: the server, the client, and the deployment.

![sentiment analysis application](https://huggingface.co/datasets/mcp-course/images/resolve/main/unit2/1.png)

### Server Side

- Uses Gradio to create a web interface and MCP server via `gr.Interface`
- Implements a sentiment analysis tool using TextBlob
- Exposes the tool through both HTTP and MCP protocols

### Client Side

- Implements a HuggingFace.js client
- Or, creates a smolagents Python client
- Demonstrates how to use the same server with different client implementations

### Deployment

- Deploys the server to Hugging Face Spaces
- Configures the clients to work with the deployed server

## Let's Get Started!

Are you ready to build your first end-to-end MCP application? Let's begin by setting up the development environment and creating our Gradio MCP server.
````

## File: units/en/unit3/build-mcp-server-solution-walkthrough.mdx
````
# Unit 3 Solution Walkthrough: Building a Pull Request Agent with MCP

## Overview

This walkthrough guides you through the complete solution for Unit 3's Pull Request Agent - an MCP server that helps developers create better pull requests by analyzing code changes, monitoring CI/CD pipelines, and automating team communications. The solution demonstrates all three MCP primitives (Tools, Resources, and Prompts) working together in a real-world workflow.

## Architecture Overview

The PR Agent consists of interconnected modules that progressively build a complete automation system:

1. **Build MCP Server** - Basic server with Tools for PR template suggestions
2. **Smart File Analysis** - Enhanced analysis using Resources for project context
3. **GitHub Actions Integration** - CI/CD monitoring with standardized Prompts
4. **Hugging Face Hub Integration** - Model deployment and dataset PR workflows
5. **Slack Notification** - Team communication integrating all MCP primitives

## Module 1: Build MCP Server

### What We're Building
A minimal MCP server that analyzes file changes and suggests appropriate PR templates using MCP Tools.

### Key Components

#### 1. Server Initialization (`server.py`)
```python
# The server registers three essential tools:
# - analyze_file_changes: Returns structured data about changed files
# - get_pr_templates: Lists available templates with metadata
# - suggest_template: Provides intelligent template recommendations
```

The server uses the MCP SDK to expose these tools to Claude Code, allowing it to gather information and make intelligent decisions about which PR template to use.

#### 2. File Analysis Tool
The `analyze_file_changes` tool examines the git diff to identify:
- File types and extensions
- Number of files changed
- Lines added/removed
- Common patterns (tests, configs, docs)

This structured data enables Claude to understand the nature of the changes without hard-coding decision logic.

#### 3. Template Management
Templates are stored as markdown files in the `templates/` directory:
- `bug.md` - For bug fixes
- `feature.md` - For new features
- `docs.md` - For documentation updates
- `refactor.md` - For code refactoring

Each template includes placeholders that Claude can fill based on the analysis.

### How Claude Uses These Tools

1. Claude calls `analyze_file_changes` to understand what changed
2. Uses `get_pr_templates` to see available options
3. Calls `suggest_template` with the analysis data
4. Receives a recommendation with reasoning
5. Can customize the template based on specific changes

### Learning Outcomes
- Understanding tool registration and schemas
- Letting Claude make decisions with structured data
- Separation of data gathering from decision logic

## Module 2: Smart File Analysis

### What We're Building
Enhanced file analysis using MCP Resources to provide project context and team guidelines.

### Key Components

#### 1. Resource Registration
The server exposes four types of resources:
```python
# Resources provide read-only access to:
# - file://templates/ - PR template files
# - file://project-context/ - Coding standards, conventions
# - git://recent-changes/ - Commit history and patterns
# - team://guidelines/ - Review processes and standards
```

#### 2. Project Context Resources
The `project-context/` directory contains:
- `coding-standards.md` - Language-specific conventions
- `review-guidelines.md` - What reviewers look for
- `architecture.md` - System design patterns
- `dependencies.md` - Third-party library policies

Claude can read these to understand project-specific requirements.

#### 3. Git History Analysis
The `git://recent-changes/` resource provides:
- Recent commit messages and patterns
- Common PR titles and descriptions
- Team member contribution patterns
- Historical template usage

This helps Claude suggest templates consistent with team practices.

### How Claude Uses Resources

1. Reads `team://guidelines/review-process.md` to understand PR requirements
2. Accesses `file://project-context/coding-standards.md` for style guides
3. Analyzes `git://recent-changes/` to match team patterns
4. Combines this context with file analysis for better suggestions

### Enhanced Decision Making
With resources, Claude can now:
- Suggest templates matching team conventions
- Include project-specific requirements in PRs
- Reference coding standards in descriptions
- Align with historical team practices

### Learning Outcomes
- Resource URI design and schemas
- Making project knowledge accessible to AI
- Context-aware decision making
- Balancing automation with team standards

## Module 3: GitHub Actions Integration

### What We're Building
Real-time CI/CD monitoring using webhooks and standardized prompts for consistent team communication.

### Key Components

#### 1. Webhook Server
Uses Cloudflare Tunnel to receive GitHub Actions events:
```python
# Webhook endpoint handles:
# - workflow_run events
# - check_run events  
# - pull_request status updates
# - deployment notifications
```

#### 2. Prompt Templates
Four standardized prompts ensure consistency:
- **"Analyze CI Results"** - Process test failures and build errors
- **"Generate Status Summary"** - Create human-readable status updates
- **"Create Follow-up Tasks"** - Suggest next steps based on results
- **"Draft Team Notification"** - Format updates for different audiences

#### 3. Event Processing Pipeline
1. Receive webhook from GitHub
2. Parse event data and extract relevant information
3. Use appropriate prompt based on event type
4. Generate standardized response
5. Store for team notification

### How Claude Uses Prompts

Example prompt usage:
```python
# When tests fail, Claude uses the "Analyze CI Results" prompt:
prompt_data = {
    "event_type": "workflow_run",
    "status": "failure",
    "failed_jobs": ["unit-tests", "lint"],
    "error_logs": "...",
    "pr_context": {...}
}

# Claude generates:
# - Root cause analysis
# - Suggested fixes
# - Impact assessment
# - Next steps
```

### Standardized Workflows
Prompts ensure that regardless of who's working:
- CI failures are analyzed consistently
- Status updates follow team formats
- Follow-up actions align with processes
- Notifications contain required information

### Learning Outcomes
- Webhook integration patterns
- Prompt engineering for consistency
- Event-driven architectures
- Standardizing team workflows

## Module 4: Hugging Face Hub Integration

### What We're Building
Integration with Hugging Face Hub for LLM and dataset PRs, adding specialized workflows for teams working with language models.

### Key Components

#### 1. Hub-Specific Tools
```python
# Tools for Hugging Face workflows:
# - analyze_model_changes: Detect LLM file modifications
# - validate_dataset_format: Check training data compliance
# - generate_model_card: Create/update model documentation
# - suggest_hub_template: PR templates for LLMs/datasets
```

#### 2. Hub Resources
```python
# Resources for Hub context:
# - hub://model-cards/ - LLM card templates and examples
# - hub://dataset-formats/ - Training data specifications
# - hub://community-standards/ - Hub community guidelines
# - hub://license-info/ - License compatibility checks
```

#### 3. LLM-Specific Prompts
```python
# Prompts for LLM workflows:
# - "Analyze Model Changes" - Understand LLM updates
# - "Generate Benchmark Summary" - Create evaluation metrics
# - "Check Dataset Quality" - Validate training data
# - "Draft Model Card Update" - Update documentation
```

### Hub-Specific Workflows

When a PR modifies LLM files:
1. **Tool**: `analyze_model_changes` detects model architecture changes
2. **Resource**: Reads `hub://model-cards/llm-template.md`
3. **Prompt**: "Generate Benchmark Summary" creates evaluation section
4. **Tool**: `generate_model_card` updates documentation
5. **Resource**: Checks `hub://license-info/` for compatibility

### Dataset PR Handling
For training data updates:
- Validates format consistency
- Checks data quality metrics
- Updates dataset cards
- Suggests appropriate reviewers

### Learning Outcomes
- Hugging Face Hub API integration
- LLM-specific PR workflows
- Model and dataset documentation
- Community standards compliance

## Module 5: Slack Notification

### What We're Building
Automated team notifications combining Tools, Resources, and Prompts for complete workflow automation.

### Key Components

#### 1. Communication Tools
```python
# Three tools for team updates:
# - send_slack_message: Post to team channels
# - get_team_members: Identify who to notify
# - track_notification_status: Monitor delivery
```

#### 2. Team Resources
```python
# Resources for team data:
# - team://members/ - Developer profiles and preferences
# - slack://channels/ - Channel configurations
# - notification://templates/ - Message formats
```

#### 3. Notification Prompts
```python
# Prompts for communication:
# - "Format Team Update" - Style messages appropriately
# - "Choose Communication Channel" - Select right audience
# - "Escalate if Critical" - Handle urgent issues
```

### Integration Example

When CI fails on a critical PR:
1. **Tool**: `get_team_members` identifies the PR author and reviewers
2. **Resource**: `team://members/{user}/preferences` checks notification settings
3. **Prompt**: "Format Team Update" creates appropriate message
4. **Tool**: `send_slack_message` delivers to right channel
5. **Resource**: `notification://templates/ci-failure` ensures consistent format
6. **Prompt**: "Escalate if Critical" determines if additional alerts needed

### Intelligent Routing
The system considers:
- Team member availability (from calendar resources)
- Notification preferences (email vs Slack)
- Message urgency (based on PR labels)
- Time zones and working hours

### Learning Outcomes
- Primitive integration patterns
- Complex workflow orchestration
- Balancing automation with human needs
- Production-ready error handling

## Complete Workflow Example

Here's how all components work together for a typical PR:

1. **Developer creates PR**
   - GitHub webhook triggers the server
   - Tool: `analyze_file_changes` examines the diff
   - Resource: Reads team guidelines and project context
   - Prompt: Suggests optimal PR template

2. **CI/CD Pipeline Runs**
   - Webhook receives workflow events
   - Prompt: "Analyze CI Results" processes outcomes
   - Resource: Checks team escalation policies
   - Tool: Updates PR status in GitHub

3. **Hugging Face Hub Integration**
   - Tool: Detects LLM/dataset changes
   - Resource: Reads Hub guidelines
   - Prompt: Generates model card updates
   - Tool: Validates against Hub standards

4. **Team Notification**
   - Tool: Identifies relevant team members
   - Resource: Reads notification preferences
   - Prompt: Formats appropriate message
   - Tool: Sends via Slack channels

5. **Follow-up Actions**
   - Prompt: "Create Follow-up Tasks" generates next steps
   - Tool: Creates GitHub issues if needed
   - Resource: Links to documentation
   - All primitives work together seamlessly

## Testing Strategy

### Unit Tests
Each module includes comprehensive unit tests:
- Tool schema validation
- Resource URI parsing
- Prompt template rendering
- Integration scenarios

### Integration Tests
End-to-end tests cover:
- Complete PR workflow
- Error recovery scenarios
- Performance under load
- Security validation

### Test Structure
```
tests/
├── unit/
│   ├── test_tools.py
│   ├── test_resources.py
│   ├── test_prompts.py
│   └── test_integration.py
├── integration/
│   ├── test_workflow.py
│   ├── test_webhooks.py
│   └── test_notifications.py
└── fixtures/
    ├── sample_events.json
    └── mock_responses.json
```

## Running the Solution

### Local Development Setup
1. **Start the MCP server**: `python server.py`
2. **Configure Claude Code**: Add server to MCP settings
3. **Set up Cloudflare Tunnel**: `cloudflared tunnel --url http://localhost:3000`
4. **Configure webhooks**: Add tunnel URL to GitHub repository
5. **Test the workflow**: Create a PR and watch the automation

### Configuration
Simple file-based configuration for easy setup:
- GitHub tokens in `.env` file
- Slack webhooks in config
- Template customization in `templates/`
- All settings in one place

## Common Patterns and Best Practices

### Tool Design
- Keep tools focused and single-purpose
- Return structured data for AI interpretation
- Include comprehensive error messages
- Version your tool schemas

### Resource Organization
- Use clear URI hierarchies
- Implement resource discovery
- Cache frequently accessed resources
- Version control all resources

### Prompt Engineering
- Make prompts specific but flexible
- Include context and examples
- Test with various inputs
- Maintain prompt libraries

### Integration Patterns
- Use events for loose coupling
- Implement circuit breakers
- Add retries with backoff
- Monitor all external calls

## Troubleshooting Guide

### Common Issues

1. **Webhook not receiving events**
   - Check Cloudflare Tunnel is running
   - Verify GitHub webhook configuration
   - Confirm secret matches

2. **Tools not appearing in Claude**
   - Validate tool schemas
   - Check server registration
   - Review MCP connection

3. **Resources not accessible**
   - Verify file permissions
   - Check URI formatting
   - Confirm resource registration

4. **Prompts producing inconsistent results**
   - Review prompt templates
   - Check context provided
   - Validate input formatting

## Next Steps and Extensions

### Potential Enhancements
1. Add more code analysis tools (complexity, security)
2. Integrate with more communication platforms
3. Add custom workflow definitions
4. Implement PR auto-merge capabilities

### Learning Path
- **Next**: Unit 4 - Deploy this server remotely
- **Advanced**: Custom MCP protocol extensions
- **Expert**: Multi-server orchestration

## Conclusion

This PR Agent demonstrates the power of MCP's three primitives working together. Tools provide capabilities, Resources offer context, and Prompts ensure consistency. Combined, they create an intelligent automation system that enhances developer productivity while maintaining team standards.

The modular architecture ensures each component can be understood, tested, and extended independently, while the integration showcases real-world patterns you'll use in production MCP servers.
````

## File: units/en/unit3_1/conclusion.mdx
````
# Conclusion

Congratulations! 🎉 You've successfully built a Pull Request Agent that automatically enhances Hugging Face model repositories through intelligent tagging using MCP (Model Context Protocol).

The patterns you've learned - webhook processing, MCP tool integration, agent orchestration, and production deployment - are foundational skills for agent and MCP building. These techniques are applicable far beyond model tagging and represent a powerful approach to building intelligent systems that augment human capabilities.

## What we've built

Throughout this unit, you created a complete automation system with four key components:

- **MCP Server** (`mcp_server.py`) - FastMCP-based server with Hub API integration
- **MCP Client** (Agent) - Intelligent orchestration with language model reasoning  
- **Webhook Listener** (FastAPI) - Real-time event processing from Hugging Face Hub
- **Testing Interface** (Gradio) - Development and monitoring dashboard

## Next Steps

### Continue Learning
- Explore advanced MCP patterns and tools
- Study other automation frameworks and AI system architecture
- Learn about multi-agent systems and tool composition

### Build More Agents
- Develop domain-specific automation tools for your own projects
- Try out other types of webhooks (e.g. model uploads, model downloads, etc.)
- Experiment with different workflows

### Share Your Work
- Open source your agent for the community
- Write about your learnings and automation patterns
- Contribute to the MCP ecosystem

### Scale Your Impact
- Deploy agents for multiple repositories or organizations
- Build more sophisticated automation workflows
- Explore commercial applications of AI automation

<Tip>

Consider documenting your experience and sharing it with the community! Your journey from learning MCP to building a production agent will help others explore AI automation.

</Tip>
````

## File: units/en/unit3_1/creating-the-mcp-server.mdx
````
# Creating the MCP Server

The MCP server is the heart of our Pull Request Agent. It provides the tools that our agent will use to interact with the Hugging Face Hub, specifically for reading and updating model repository tags. In this section, we'll build the server using FastMCP and the Hugging Face Hub Python SDK.

## Understanding the MCP Server Architecture

Our MCP server provides two essential tools:

| Tool | Description |
| --- | --- |
| `get_current_tags` | Retrieves existing tags from a model repository |
| `add_new_tag` | Adds a new tag to a repository via pull request |

These tools abstract the complexity of Hub API interactions and provide a clean interface for our agent to work with.

![MCP Server Tools](https://huggingface.co/datasets/mcp-course/images/resolve/main/unit3/architecture.png)

## Complete MCP Server Implementation

Let's create our `mcp_server.py` file step by step. We'll build this incrementally so you understand each component and how they work together.

### 1. Imports and Configuration

First, let's set up all the necessary imports and configuration. 

```python
#!/usr/bin/env python3
"""
Simplified MCP Server for HuggingFace Hub Tagging Operations using FastMCP
"""

import os
import json
from fastmcp import FastMCP
from huggingface_hub import HfApi, model_info, ModelCard, ModelCardData
from huggingface_hub.utils import HfHubHTTPError
from dotenv import load_dotenv

load_dotenv()
```

The imports above give us everything we need to build our MCP server. `FastMCP` provides the server framework, while the `huggingface_hub` imports give us the tools to interact with model repositories.

The `load_dotenv()` call automatically loads environment variables from a `.env` file, making it easy to manage secrets like API tokens during development.

<Tip>

If you're using uv, you can create a `.env` file in the root of the project and you won't need to use `load_dotenv()` if you use `uv run` to run the server.

</Tip>

Next, we'll configure our server with the necessary credentials and create the FastMCP instance:

```python
# Configuration
HF_TOKEN = os.getenv("HF_TOKEN")

# Initialize HF API client
hf_api = HfApi(token=HF_TOKEN) if HF_TOKEN else None

# Create the FastMCP server
mcp = FastMCP("hf-tagging-bot")
```

This configuration block does three important things:
1. Retrieves the Hugging Face token from environment variables
2. Creates an authenticated API client (only if a token is available)
3. Initializes our FastMCP server with a descriptive name

The conditional creation of `hf_api` ensures our server can start even without a token, which is useful for testing the basic structure.

### 2. Get Current Tags Tool

Now let's implement our first tool - `get_current_tags`. This tool retrieves the existing tags from a model repository:

```python
@mcp.tool()
def get_current_tags(repo_id: str) -> str:
    """Get current tags from a HuggingFace model repository"""
    print(f"🔧 get_current_tags called with repo_id: {repo_id}")

    if not hf_api:
        error_result = {"error": "HF token not configured"}
        json_str = json.dumps(error_result)
        print(f"❌ No HF API token - returning: {json_str}")
        return json_str
```

The function starts with validation - checking if we have an authenticated API client. Notice how we return JSON strings instead of Python objects. This is crucial for MCP communication.

<Tip>

All MCP tools must return strings, not Python objects. That's why we use `json.dumps()` to convert our results to JSON strings. This ensures reliable data exchange between the MCP server and client.

</Tip>

Let's continue with the main logic of the `get_current_tags` function:

```python
    try:
        print(f"📡 Fetching model info for: {repo_id}")
        info = model_info(repo_id=repo_id, token=HF_TOKEN)
        current_tags = info.tags if info.tags else []
        print(f"🏷️ Found {len(current_tags)} tags: {current_tags}")

        result = {
            "status": "success",
            "repo_id": repo_id,
            "current_tags": current_tags,
            "count": len(current_tags),
        }
        json_str = json.dumps(result)
        print(f"✅ get_current_tags returning: {json_str}")
        return json_str

    except Exception as e:
        print(f"❌ Error in get_current_tags: {str(e)}")
        error_result = {"status": "error", "repo_id": repo_id, "error": str(e)}
        json_str = json.dumps(error_result)
        print(f"❌ get_current_tags error returning: {json_str}")
        return json_str
```

This implementation follows a clear pattern:
1. **Fetch data** using the Hugging Face Hub API
2. **Process the response** to extract tag information
3. **Structure the result** in a consistent JSON format
4. **Handle errors gracefully** with detailed error messages

<Tip>

The extensive logging might seem overkill, but it helps with debugging and monitoring when the server is running. Remember, your application will autonomously reacting to events from the Hub, so you won't be able to see the logs in real time.

</Tip>

### 3. Add New Tag Tool

Now for the more complex tool - `add_new_tag`. This tool adds a new tag to a repository by creating a pull request. Let's start with the initial setup and validation:

```python
@mcp.tool()
def add_new_tag(repo_id: str, new_tag: str) -> str:
    """Add a new tag to a HuggingFace model repository via PR"""
    print(f"🔧 add_new_tag called with repo_id: {repo_id}, new_tag: {new_tag}")

    if not hf_api:
        error_result = {"error": "HF token not configured"}
        json_str = json.dumps(error_result)
        print(f"❌ No HF API token - returning: {json_str}")
        return json_str
```

Similar to our first tool, we start with validation. Now let's fetch the current repository state to check if the tag already exists:

```python
    try:
        # Get current model info and tags
        print(f"📡 Fetching current model info for: {repo_id}")
        info = model_info(repo_id=repo_id, token=HF_TOKEN)
        current_tags = info.tags if info.tags else []
        print(f"🏷️ Current tags: {current_tags}")

        # Check if tag already exists
        if new_tag in current_tags:
            print(f"⚠️ Tag '{new_tag}' already exists in {current_tags}")
            result = {
                "status": "already_exists",
                "repo_id": repo_id,
                "tag": new_tag,
                "message": f"Tag '{new_tag}' already exists",
            }
            json_str = json.dumps(result)
            print(f"🏷️ add_new_tag (already exists) returning: {json_str}")
            return json_str
```

This section demonstrates an important principle: **validate before acting**. We check if the tag already exists to avoid creating unnecessary pull requests.

<Tip>

Always check the current state before making changes. This prevents duplicate work and provides better user feedback. It's especially important when creating pull requests, as duplicate PRs can clutter the repository.

</Tip>

Next, we'll prepare the updated tag list and handle the model card:

```python
        # Add the new tag to existing tags
        updated_tags = current_tags + [new_tag]
        print(f"🆕 Will update tags from {current_tags} to {updated_tags}")

        # Create model card content with updated tags
        try:
            # Load existing model card
            print(f"📄 Loading existing model card...")
            card = ModelCard.load(repo_id, token=HF_TOKEN)
            if not hasattr(card, "data") or card.data is None:
                card.data = ModelCardData()
        except HfHubHTTPError:
            # Create new model card if none exists
            print(f"📄 Creating new model card (none exists)")
            card = ModelCard("")
            card.data = ModelCardData()

        # Update tags - create new ModelCardData with updated tags
        card_dict = card.data.to_dict()
        card_dict["tags"] = updated_tags
        card.data = ModelCardData(**card_dict)
```

This section handles model card management. We try to load an existing model card first, but create a new one if none exists. This ensures our tool works with any repository, even if it's empty.

The model card (`README.md`) contains the repository metadata, including tags. By updating the model card data and creating a pull request, we're following the standard Hugging Face workflow for metadata changes.

Now for the pull request creation - the main part of our tool:

```python
        # Create a pull request with the updated model card
        pr_title = f"Add '{new_tag}' tag"
        pr_description = f"""
## Add tag: {new_tag}

This PR adds the `{new_tag}` tag to the model repository.

**Changes:**
- Added `{new_tag}` to model tags
- Updated from {len(current_tags)} to {len(updated_tags)} tags

**Current tags:** {", ".join(current_tags) if current_tags else "None"}
**New tags:** {", ".join(updated_tags)}

🤖 This is a pull request created by the Hugging Face Hub Tagging Bot.
"""

        print(f"🚀 Creating PR with title: {pr_title}")
```

We create a detailed pull request description that explains what's changing and why. This transparency is crucial for repository maintainers who will review the PR.

<Tip>

Clear, detailed PR descriptions are essential for automated pull requests. They help repository maintainers understand what's happening and make informed decisions about whether to merge the changes.

Also, it's good practice to clearly state that the PR is created by an automated tool. This helps repository maintainers understand how to deal with the PR.

</Tip>

Finally, we create the commit and pull request:

```python
        # Create commit with updated model card using CommitOperationAdd
        from huggingface_hub import CommitOperationAdd

        commit_info = hf_api.create_commit(
            repo_id=repo_id,
            operations=[
                CommitOperationAdd(
                    path_in_repo="README.md", path_or_fileobj=str(card).encode("utf-8")
                )
            ],
            commit_message=pr_title,
            commit_description=pr_description,
            token=HF_TOKEN,
            create_pr=True,
        )

        # Extract PR URL from commit info
        pr_url_attr = commit_info.pr_url
        pr_url = pr_url_attr if hasattr(commit_info, "pr_url") else str(commit_info)

        print(f"✅ PR created successfully! URL: {pr_url}")

        result = {
            "status": "success",
            "repo_id": repo_id,
            "tag": new_tag,
            "pr_url": pr_url,
            "previous_tags": current_tags,
            "new_tags": updated_tags,
            "message": f"Created PR to add tag '{new_tag}'",
        }
        json_str = json.dumps(result)
        print(f"✅ add_new_tag success returning: {json_str}")
        return json_str
```

The `create_commit` function with `create_pr=True` is the key to our automation. It creates a commit with the updated `README.md` file and automatically opens a pull request for review.

Don't forget the error handling for this complex operation:

```python
    except Exception as e:
        print(f"❌ Error in add_new_tag: {str(e)}")
        print(f"❌ Error type: {type(e)}")
        import traceback
        print(f"❌ Traceback: {traceback.format_exc()}")

        error_result = {
            "status": "error",
            "repo_id": repo_id,
            "tag": new_tag,
            "error": str(e),
        }
        json_str = json.dumps(error_result)
        print(f"❌ add_new_tag error returning: {json_str}")
        return json_str
```

The comprehensive error handling includes the full traceback, which is invaluable for debugging when things go wrong.

Emojis in log messages might seem silly, but they make scanning logs much faster. 🔧 for function calls, 📡 for API requests, ✅ for success, and ❌ for errors create visual patterns that help you quickly find what you're looking for.

<Tip>

Whilst building this application, it's easy to accidentally create an infinite loop of PRs. This is because the `create_commit` function with `create_pr=True` will create a PR for every commit. If the PR is not merged, the `create_commit` function will be called again, and again, and again...

We've added checks to prevent this, but it's something to be aware of.

</Tip>

## Next Steps

Now that we have our MCP server implemented with robust tagging tools, we need to:

1. **Create the MCP Client** - Build the interface between our agent and MCP server
2. **Implement Webhook Handling** - Listen for Hub discussion events
3. **Integrate Agent Logic** - Connect webhooks with MCP tool calls
4. **Test the Complete System** - Validate end-to-end functionality

In the next section, we'll create the MCP client that will allow our webhook handler to interact with these tools intelligently.

<Tip>

The MCP server runs as a separate process from your main application. This isolation provides better error handling and allows the server to be reused by multiple clients or applications.

</Tip>
````

## File: units/vi/unit0/introduction.mdx
````
# Chào mừng bạn đến với 🤗 Khóa học Giao Thức Ngữ Cảnh Mô Hình (MCP)

![MCP Course thumbnail](https://huggingface.co/datasets/mcp-course/images/resolve/main/unit0/1.png)

Chào mừng các bạn đến với chủ đề thú vị nhất trong AI hiện nay: **Giao Thức Ngữ Cảnh Mô Hình (MCP)**!

Khóa học miễn phí này sẽ dẫn dắt các bạn **từ người mới bắt đầu trở thành người am hiểu** về cách sử dụng và xây dựng ứng dụng với MCP.

Chương đầu tiên sẽ giúp bạn làm quen:
* Khám phá **giáo trình khóa học**
* **Nhận thêm thông tin về quy trình cấp chứng chỉ và lịch trình**
* Làm quen với đội ngũ xây dựng khóa học
* Tạo **tài khoản** của bạn
* **Tham gia Discord** để gặp gỡ bạn học và chúng mình

Cùng bắt đầu thôi!

## Bạn sẽ học được gì từ khóa học này?

Trong khóa học này, các bạn sẽ:
* 📖 Nghiên cứu MCP về **lý thuyết, thiết kế và thực hành**
* 🧑‍💻 Học cách **sử dụng các SDK và framework MCP phổ biến**
* 💾 **Chia sẻ dự án** và khám phá ứng dụng từ cộng đồng
* 🏆 Tham gia các bài tập lớn để **đánh giá cách triển khai MCP của bạn so với các học viên khác**
* 🎓 **Nhận chứng chỉ hoàn thành** bằng cách hoàn thành các bài tập

Và còn nhiều hơn thế!

Kết thúc khóa học, bạn sẽ hiểu **cách MCP hoạt động và cách xây dựng ứng dụng AI sử dụng dữ liệu/công cụ bên ngoài theo chuẩn MCP mới nhất**.

Đừng quên [**đăng ký khóa học!**](https://huggingface.co/mcp-course)

## Cấu trúc khóa học như thế nào?

Khóa học bao gồm:
* _Chương nền tảng_: nơi bạn học **khái niệm lý thuyết** về MCP
* _Thực hành_: nơi bạn học **cách sử dụng SDK MCP** để xây dựng ứng dụng. Các phần thực hành sẽ có môi trường được cấu hình sẵn
* _Bài tập tình huống_: nơi bạn áp dụng kiến thức đã học để giải quyết vấn đề thực tế do bạn lựa chọn
* _Hợp tác_: Chúng tôi hợp tác với các đối tác của Hugging Face để mang đến cho bạn những triển khai MCP mới nhất

**Khóa học này là dự án sống, phát triển cùng phản hồi và đóng góp của bạn!** Hãy thoải mái tạo issue/PR trên GitHub và thảo luận tại Discord server của chúng ta.

Sau khi hoàn thành khóa học, bạn có thể gửi phản hồi 👉 qua [biểu mẫu này]

## Giáo trình chi tiết

Dưới đây là **giáo trình tổng quan**. Danh sách chi tiết sẽ được cập nhật theo từng chương.

| Chương | Chủ đề                                       | Mô tả                                                                                                            |
| ------- | ------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| 0       | Làm quen                                  | Thiết lập công cụ và nền tảng cần dùng                                                             |
| 1       | Nguyên lý, kiến trúc và khái niệm cốt lõi của MCP | Giải thích khái niệm cơ bản, kiến trúc và thành phần của MCP. Minh họa trường hợp sử dụng đơn giản với MCP       |
| 2       | Ứng dụng end-to-end: MCP trong thực tế              | Xây dựng ứng dụng MCP end-to-end đơn giản để chia sẻ với cộng đồng |
| 3       | Triển khai ứng dụng: MCP trong thực tế               | Xây dựng ứng dụng MCP triển khai thực tế sử dụng hệ sinh thái Hugging Face và dịch vụ đối tác                                        |
| 4       | Chương bổ trợ                                  | Các chương nâng cao giúp bạn tận dụng tối đa khóa học, làm việc với thư viện và dịch vụ đối tác                                        |

## Yêu cầu đầu vào

Để theo học hiệu quả, bạn cần:
* Hiểu biết cơ bản về AI và các khái niệm LLM
* Quen thuộc với nguyên tắc phát triển phần mềm và khái niệm API
* Có kinh nghiệm với ít nhất một ngôn ngữ lập trình (ví dụ Python hoặc TypeScript sẽ được sử dụng minh họa)

Nếu bạn chưa có những kiến thức này, đừng lo! Dưới đây là một số tài nguyên hữu ích:

* [LLM Course](https://huggingface.co/learn/llm-course/) sẽ hướng dẫn bạn những kiến thức cơ bản về sử dụng và xây dựng với LLMs.
* [Agents Course](https://huggingface.co/learn/agents-course/) sẽ hướng dẫn bạn cách xây dựng AI Agents với LLMs.

<Tip>

Các khóa học trên không phải là điều kiện bắt buộc, vì vậy nếu bạn đã hiểu các khái niệm về LLM và Agents, các bạn có thể bắt đầu khóa học ngay bây giờ!

</Tip>

## Tôi cần những công cụ gì?

Bạn chỉ cần 2 thứ:

* _Một máy tính_ có kết nối internet.
* _Tài khoản_: để truy cập tài nguyên khóa học và tạo dự án. Nếu chưa có tài khoản, bạn có thể tạo [tại đây](https://huggingface.co/join) (miễn phí).

## Quy trình cấp chứng chỉ

Bạn có thể chọn học khóa học này ở _chế độ audit_, hoặc hoàn thành các hoạt động và _nhận một trong hai chứng chỉ mà chúng tôi cấp_. Nếu chọn audit, bạn vẫn có thể tham gia tất cả bài tập lớn và làm bài tập nếu muốn, **bạn không cần thông báo với chúng tôi**.

Quy trình cấp chứng chỉ **hoàn toàn miễn phí**:

* _Để nhận chứng chỉ kiến thức cơ bản_: bạn cần hoàn thành Chương 1. Dành cho học viên muốn cập nhật xu hướng mới nhất về MCP mà không cần xây dựng ứng dụng đầy đủ.
* _Để nhận chứng chỉ hoàn thành_: bạn cần hoàn thành các chương ứng dụng (2 và 3). Dành cho học viên muốn xây dựng ứng dụng hoàn chỉnh và chia sẻ với cộng đồng.

## Tốc độ học được khuyến nghị?

Mỗi chương trong khóa học được thiết kế **để hoàn thành trong 1 tuần, với khoảng 3-4 giờ học mỗi tuần**.

Vì có thời hạn cụ thể, chúng tôi đưa ra lộ trình khuyến nghị:

![Recommended Pace](https://huggingface.co/datasets/mcp-course/images/resolve/main/unit0/2.png)

## Làm thế nào để học hiệu quả nhất?

Để học hiệu quả nhất, chúng tôi có vài lời khuyên:

1. Tham gia nhóm học tập trên Discord: học cùng nhau luôn dễ dàng hơn. Hãy tham gia Discord của chúng tôi và xác thực tài khoản.
2. **Làm bài kiểm tra và bài tập**: cách học tốt nhất là qua thực hành và tự đánh giá.
3. **Lập lịch học để theo kịp tiến độ**: bạn có thể dùng lộ trình khuyến nghị bên dưới hoặc tự tạo lịch riêng.

![Course advice](https://huggingface.co/datasets/mcp-course/images/resolve/main/unit0/3.png)

## Về chúng tôi

Thông tin tác giả:

### Ben Burtenshaw

Ben là Kỹ sư Máy học tại Hugging Face, tập trung vào xây dựng các ứng dụng LLM với phương pháp hậu huấn luyện và agentic.

<!-- ## Acknowledgments -->

<!-- We would like to extend our gratitude to the following individuals and partners for their invaluable contributions and support: -->

<!-- TODO: @burtenshaw add contributors and partners -->

## Tôi phát hiện lỗi hoặc muốn cải thiện khóa học

Mọi đóng góp đều **được chào đón** 🤗

* Nếu bạn _phát hiện lỗi 🐛 trong notebook_, hãy mở một issue và **mô tả vấn đề**.
* Nếu bạn _muốn cải thiện khóa học_, bạn có thể mở một Pull Request.
* Nếu bạn _muốn thêm một mục đầy đủ hoặc một Chương mới_, cách tốt nhất là mở một issue và **mô tả nội dung bạn muốn thêm trước khi bắt đầu viết để chúng tôi có thể hướng dẫn bạn**.

## Tôi vẫn còn thắc mắc

Hãy đặt câu hỏi của bạn trên máy chủ Discord của chúng tôi tại kênh #mcp-course-questions.

Giờ bạn đã có đầy đủ thông tin, hãy cùng nhau lên đường ⛵
````

## File: units/vi/unit1/architectural-components.mdx
````
# Các thành phần kiến trúc của MCP

Ở chương trước, chúng ta đã thảo luận về các khái niệm và thuật ngữ chính của MCP. Giờ hãy cùng đi sâu hơn vào các thành phần kiến trúc tạo nên hệ sinh thái MCP.

## Host, Client và Server

Giao Thức Ngữ Cảnh Mô Hình (MCP) được xây dựng trên kiến trúc client-server để kích hoạt giao tiếp có cấu trúc giữa các mô hình AI và hệ thống bên ngoài.

![MCP Architecture](https://huggingface.co/datasets/mcp-course/images/resolve/main/unit1/4.png)

Kiến trúc MCP bao gồm ba thành phần chính với vai trò và trách nhiệm được xác định rõ ràng: Host, Client và Server. Chúng ta đã đề cập sơ qua ở phần trước, giờ hãy phân tích kỹ hơn từng thành phần.

### Host

**Host** là ứng dụng AI tiếp xúc trực tiếp với người dùng cuối. 

Ví dụ bao gồm:
- Ứng dụng chat AI như OpenAI ChatGPT hay Claude Desktop của Anthropic
- IDE tích hợp AI như Cursor, hoặc các công cụ như Continue.dev
- Các agent AI tùy chỉnh và ứng dụng xây dựng bằng thư viện như LangChain hay smolagents

Trách nhiệm của Host:
- Quản lý tương tác và quyền hạn người dùng
- Thiết lập kết nối tới MCP Server thông qua MCP Client
- Điều phối luồng xử lý giữa yêu cầu người dùng, xử lý LLM và công cụ bên ngoài
- Hiển thị kết quả cho người dùng dưới định dạng mạch lạc

Thông thường, người dùng sẽ chọn ứng dụng Host dựa trên nhu cầu cá nhân. Ví dụ, nhà phát triển có thể chọn Cursor cho khả năng chỉnh sửa mã mạnh mẽ, trong khi chuyên gia nghiệp vụ có thể dùng ứng dụng tùy chỉnh xây bằng smolagents.

### Client

**Client** là thành phần trong ứng dụng Host quản lý giao tiếp với một MCP Server cụ thể. Đặc điểm chính:

- Mỗi Client duy trì kết nối 1:1 với một Server
- Xử lý các chi tiết giao thức của MCP
- Đóng vai trò trung gian giữa logic của Host và Server bên ngoài

### Server

**Server** là chương trình/dịch vụ bên ngoài cung cấp khả năng truy cập vào các công cụ, nguồn dữ liệu hoặc dịch vụ thông qua giao thức MCP. Server:

- Cung cấp quyền truy cập vào các công cụ/dịch vụ bên ngoài
- Đóng vai trò lớp bao bọc nhẹ cho chức năng có sẵn
- Có thể chạy cục bộ (cùng máy với Host) hoặc từ xa (qua mạng)
- Cung cấp khả năng dưới định dạng chuẩn để Client khám phá và sử dụng

## Luồng giao tiếp

Cùng xem cách các thành phần tương tác trong quy trình MCP điển hình:

<Tip>

Trong phần tiếp theo, chúng ta sẽ khám phá sâu hơn về giao thức giao tiếp với các ví dụ thực tế.

</Tip>

1. **Tương tác người dùng**: Người dùng tương tác với ứng dụng **Host**, thể hiện nhu cầu hoặc truy vấn.

2. **Xử lý Host**: **Host** xử lý đầu vào, có thể dùng LLM để hiểu yêu cầu và xác định cần dùng công cụ nào.

3. **Kết nối Client**: **Host** hướng dẫn **Client** kết nối tới Server phù hợp.

4. **Khám phá khả năng**: **Client** truy vấn **Server** để biết các khả năng (Công cụ, Tài nguyên, Prompt) mà nó cung cấp.

5. **Kích hoạt khả năng**: Dựa trên nhu cầu người dùng hoặc quyết định của LLM, Host yêu cầu **Client** kích hoạt khả năng cụ thể từ **Server**.

6. **Thực thi Server**: **Server** thực thi chức năng được yêu cầu và trả kết quả về **Client**.

7. **Tích hợp kết quả**: **Client** chuyển kết quả về **Host**, nơi tích hợp chúng vào ngữ cảnh LLM hoặc hiển thị trực tiếp cho người dùng.

Ưu điểm chính của kiến trúc này là tính mô-đun. Một Host duy nhất có thể kết nối với nhiều Server cùng lúc thông qua các Client khác nhau. Có thể thêm Server mới vào hệ sinh thái mà không cần thay đổi Host hiện có. Có thể dễ dàng kết hợp các khả năng trên nhiều Server khác nhau.

<Tip>

Như đã thảo luận ở phần trước, tính mô-đun này biến bài toán tích hợp M×N truyền thống (khi M ứng dụng AI kết nối với N công cụ/dịch vụ) thành một bài toán M+N dễ quản lý hơn - nơi mỗi Host và Server chỉ cần triển khai chuẩn MCP một lần.

</Tip>

Kiến trúc này trông có vẻ đơn giản, nhưng sức mạnh thực sự nằm ở việc chuẩn hóa giao thức truyền thông và sự phân tách rõ ràng trách nhiệm giữa các thành phần. Thiết kế này cho phép tạo ra một hệ sinh thái gắn kết nơi các mô hình AI có thể kết nối liền mạch với một mảng các công cụ và nguồn dữ liệu bên ngoài ngày càng phát triển.

## Kết luận

Những mẫu tương tác này được định hướng bởi các nguyên tắc chính định hình thiết kế và sự phát triển của MCP. Giao thức nhấn mạnh **tính chuẩn hóa** thông qua việc cung cấp một giao thức kết nối phổ quát cho AI, đồng thời duy trì **sự đơn giản** bằng cách giữ phần lõi giao thức dễ hiểu nhưng vẫn hỗ trợ các tính năng nâng cao. **An toàn** được ưu tiên thông qua yêu cầu phê duyệt rõ ràng từ người dùng cho các thao tác nhạy cảm, trong khi khả năng khám phá cho phép phát hiện động các chức năng. Giao thức được xây dựng với tư duy **mở rộng**, hỗ trợ phát triển thông qua phiên bản hóa và đàm phán chức năng, đồng thời đảm bảo **khả năng tương tác** giữa các triển khai và môi trường khác nhau.

Trong phần tiếp theo, chúng ta sẽ khám phá giao thức truyền thông giúp các thành phần này phối hợp hiệu quả với nhau.
````

## File: units/vi/unit1/capabilities.mdx
````
# Hiểu về Khả năng của MCP

Các MCP Server cung cấp nhiều khả năng khác nhau cho Client thông qua giao thức truyền thông. Những khả năng này được chia thành bốn loại chính, mỗi loại có đặc điểm và trường hợp sử dụng riêng. Hãy cùng khám phá các nguyên thủy cốt lõi tạo nền tảng cho chức năng của MCP.

<Tip>

Trong phần này, chúng ta sẽ xem các ví dụ dưới dạng hàm độc lập với framework trong mỗi ngôn ngữ. Mục đích là tập trung vào khái niệm và cách chúng phối hợp với nhau, thay vì sự phức tạp của bất kỳ framework cụ thể nào.

Trong các chương tiếp theo, chúng ta sẽ xem cách triển khai các khái niệm này trong mã cụ thể của MCP.

</Tip>

## Công cụ (Tools)

Công cụ là các hàm hoặc hành động có thể thực thi mà mô hình AI có thể gọi thông qua giao thức MCP.

- **Kiểm soát**: Công cụ thường **được kiểm soát bởi mô hình** (model-controlled), nghĩa là mô hình AI (LLM) quyết định khi nào gọi chúng dựa trên yêu cầu và ngữ cảnh của người dùng.
- **An toàn**: Do khả năng thực hiện các hành động có tác dụng phụ, việc thực thi công cụ có thể nguy hiểm. Vì vậy chúng thường yêu cầu sự chấp thuận rõ ràng từ người dùng.
- **Trường hợp sử dụng**: Gửi tin nhắn, tạo ticket, truy vấn API, thực hiện tính toán.

**Ví dụ**: Một công cụ thời tiết lấy dữ liệu thời tiết hiện tại cho một địa điểm:

<hfoptions id="tool-example">
<hfoption id="python">

<details>
<summary>Bấm để xem bản dịch tiếng Việt</summary>

```python
def get_weather(location: str) -> dict:
    """Nhận thông tin thời tiết hiện tại ở một địa điểm cụ thể."""
    # Connect to weather API and fetch data
    return {
        "temperature": 72,
        "conditions": "Sunny",
        "humidity": 45
    }
```
</details>

```python
def get_weather(location: str) -> dict:
    """Get the current weather for a specified location."""
    # Connect to weather API and fetch data
    return {
        "temperature": 72,
        "conditions": "Sunny",
        "humidity": 45
    }
```

</hfoption>
<hfoption id="javascript">

<details>
<summary>Bấm để xem bản dịch tiếng Việt</summary>

```javascript
function getWeather(location) {
    // Kết nối đến API thời tiết và lấy dữ liệu
    return {
        temperature: 72,
        conditions: 'Sunny',
        humidity: 45
    };
}
```
</details>

```javascript
function getWeather(location) {
    // Connect to weather API and fetch data
    return {
        temperature: 72,
        conditions: 'Sunny',
        humidity: 45
    };
}
```

</hfoption>
</hfoptions>

## Tài nguyên (Resources)

Tài nguyên cung cấp quyền truy cập chỉ đọc (read-only) vào các nguồn dữ liệu, cho phép mô hình AI truy xuất ngữ cảnh mà không cần thực thi logic phức tạp.

- **Kiểm soát**: Tài nguyên **được kiểm soát bởi ứng dụng** (application-controlled), nghĩa là ứng dụng Host thường quyết định khi nào truy cập chúng.
- **Bản chất**: Được thiết kế để truy xuất dữ liệu với tính toán tối thiểu, tương tự các endpoint GET trong REST API.
- **An toàn**: Vì chỉ đọc nên chúng thường ít rủi ro bảo mật hơn so với Công cụ.
- **Trường hợp sử dụng**: Truy cập nội dung file, lấy bản ghi cơ sở dữ liệu, đọc thông tin cấu hình.

**Ví dụ**: Một tài nguyên cung cấp quyền truy cập vào nội dung file:

<hfoptions id="resource-example">
<hfoption id="python">

<details>
<summary>Bấm để xem bản dịch tiếng Việt</summary>

```python
def read_file(file_path: str) -> str:
    """Đọc nội dung của file tại đường dẫn được chỉ định."""
    with open(file_path, 'r') as f:
        return f.read()
```
</details>

```python
def read_file(file_path: str) -> str:
    """Read the contents of a file at the specified path."""
    with open(file_path, 'r') as f:
        return f.read()
```

</hfoption>
<hfoption id="javascript">

<details>
<summary>Bấm để xem bản dịch tiếng Việt</summary>

```javascript
function readFile(filePath) {
    // Sử dụng fs.readFile để đọc nội dung file
    const fs = require('fs');
    return new Promise((resolve, reject) => {
        fs.readFile(filePath, 'utf8', (err, data) => {
            if (err) {
                reject(err);
                return;
            }
            resolve(data);
        });
    });
}
```
</details>

```javascript
function readFile(filePath) {
    // Using fs.readFile to read file contents
    const fs = require('fs');
    return new Promise((resolve, reject) => {
        fs.readFile(filePath, 'utf8', (err, data) => {
            if (err) {
                reject(err);
                return;
            }
            resolve(data);
        });
    });
}
```

</hfoption>
</hfoptions>

## Lời nhắc

Lời nhắc (Prompts) là các mẫu hoặc quy trình làm việc được định nghĩa trước nhằm hướng dẫn tương tác giữa người dùng, Mô hình AI và khả năng của Server.

- **Kiểm soát**: Lời nhắc **do người dùng kiểm soát**, thường được hiển thị dưới dạng các tùy chọn trong giao diện ứng dụng Host.
- **Mục đích**: Chúng cấu trúc các tương tác để tối ưu hóa việc sử dụng Công cụ và Tài nguyên sẵn có.
- **Lựa chọn**: Người dùng thường chọn một lời nhắc trước khi Mô hình AI bắt đầu xử lý, thiết lập ngữ cảnh cho tương tác.
- **Trường hợp sử dụng**: Quy trình làm việc phổ biến, mẫu tác vụ chuyên biệt, tương tác có hướng dẫn.

**Ví dụ**: Mẫu lời nhắc để tạo đánh giá mã nguồn:

<hfoptions id="prompt-example">
<hfoption id="python">

<details>
<summary>Bấm để xem bản dịch tiếng Việt</summary>

```python
def code_review(code: str, language: str) -> list:
    """Tạo đánh giá mã nguồn cho đoạn code được cung cấp."""
    return [
        {
            "role": "system",
            "content": f"You are a code reviewer examining {language} code. Provide a detailed review highlighting best practices, potential issues, and suggestions for improvement."
        },
        {
            "role": "user",
            "content": f"Please review this {language} code:\n\n```{language}\n{code}\n```"
        }
    ]
```
</details>

```python
def code_review(code: str, language: str) -> list:
    """Generate a code review for the provided code snippet."""
    return [
        {
            "role": "system",
            "content": f"You are a code reviewer examining {language} code. Provide a detailed review highlighting best practices, potential issues, and suggestions for improvement."
        },
        {
            "role": "user",
            "content": f"Please review this {language} code:\n\n```{language}\n{code}\n```"
        }
    ]
```

</hfoption>
<hfoption id="javascript">

<details>
<summary>Bấm để xem bản dịch tiếng Việt</summary>

```javascript
function codeReview(code, language) {
    return [
        {
            role: 'system',
            content: `You are a code reviewer examining ${language} code. Provide a detailed review highlighting best practices, potential issues, and suggestions for improvement.`
        },
        {
            role: 'user',
            content: `Please review this ${language} code:\n\n\`\`\`${language}\n${code}\n\`\`\``
        }
    ];
}
```
</details>

```javascript
function codeReview(code, language) {
    return [
        {
            role: 'system',
            content: `You are a code reviewer examining ${language} code. Provide a detailed review highlighting best practices, potential issues, and suggestions for improvement.`
        },
        {
            role: 'user',
            content: `Please review this ${language} code:\n\n\`\`\`${language}\n${code}\n\`\`\``
        }
    ];
}
```

</hfoption>
</hfoptions>

## Lấy mẫu (Sampling)

Lấy mẫu cho phép Server yêu cầu Client (cụ thể là ứng dụng Host) thực hiện các tương tác LLM.

- **Kiểm soát**: Lấy mẫu **do Server khởi xướng** nhưng cần sự hỗ trợ từ Client/Host.
- **Mục đích**: Kích hoạt các hành vi tự chủ từ Server và các tương tác đệ quy/đa bước tiềm năng.
- **An toàn**: Giống như Công cụ, các thao tác lấy mẫu thường yêu cầu sự chấp thuận của người dùng.
- **Trường hợp sử dụng**: Các tác vụ đa bước phức tạp, quy trình làm việc của agent tự động, quá trình tương tác.

**Ví dụ**: Server có thể yêu cầu Client phân tích dữ liệu đã xử lý:

<hfoptions id="sampling-example">
<hfoption id="python">

<details>
<summary>Bấm để xem bản dịch tiếng Việt</summary>
```python
def request_sampling(messages, system_prompt=None, include_context="none"):
    """Yêu cầu lấy mẫu LLM từ máy khách."""
    # Trong triển khai thực tế, phần này sẽ gửi yêu cầu đến máy khách
    return {
        "role": "assistant",
        "content": "Analysis of the provided data..."
    }
```
</details>

```python
def request_sampling(messages, system_prompt=None, include_context="none"):
    """Request LLM sampling from the client."""
    # In a real implementation, this would send a request to the client
    return {
        "role": "assistant",
        "content": "Analysis of the provided data..."
    }
```

</hfoption>
<hfoption id="javascript">

<details>
<summary>Bấm để xem bản dịch tiếng Việt</summary>
```javascript
function requestSampling(messages, systemPrompt = null, includeContext = 'none') {
    // Trong triển khai thực tế, phần này sẽ gửi yêu cầu đến máy khách
    return {
        role: 'assistant',
        content: 'Analysis of the provided data...'
    };
}

function handleSamplingRequest(request) {
    const { messages, systemPrompt, includeContext } = request;
    // Trong triển khai thực tế, phần này sẽ xử lý yêu cầu và trả về phản hồi
    return {
        role: 'assistant',
        content: 'Response to the sampling request...'
    };
}
```
</details>

```javascript
function requestSampling(messages, systemPrompt = null, includeContext = 'none') {
    // In a real implementation, this would send a request to the client
    return {
        role: 'assistant',
        content: 'Analysis of the provided data...'
    };
}

function handleSamplingRequest(request) {
    const { messages, systemPrompt, includeContext } = request;
    // In a real implementation, this would process the request and return a response
    return {
        role: 'assistant',
        content: 'Response to the sampling request...'
    };
}
```

</hfoption>
</hfoptions>

Quy trình lấy mẫu (sampling) diễn ra theo các bước sau:
1. Server gửi yêu cầu `sampling/createMessage` đến client
2. Client xem xét và có thể chỉnh sửa yêu cầu này
3. Client lấy mẫu từ một LLM
4. Client kiểm tra kết quả hoàn thiện
5. Client trả kết quả về cho server

<Tip>

Thiết kế human-in-the-loop (có sự tham gia của con người trong vòng lặp) này đảm bảo người dùng duy trì quyền kiểm soát những gì LLM nhìn thấy và tạo ra. Khi triển khai sampling, điều quan trọng là phải cung cấp các lời nhắc rõ ràng, được cấu trúc tốt và bao gồm ngữ cảnh liên quan.

</Tip>

## Cách Các Khả Năng Phối Hợp

Hãy cùng xem cách các khả năng này phối hợp với nhau để tạo ra các tương tác phức tạp. Trong bảng dưới đây, chúng ta đã liệt kê các khả năng, đối tượng kiểm soát, hướng kiểm soát và một số chi tiết khác.

| Khả năng    | Được kiểm soát bởi | Hướng     | Tác dụng phụ       | Cần phê duyệt | Trường hợp sử dụng điển hình       |
|------------|-------------------|-----------|--------------------|---------------|-----------------------------------|
| Tools      | Mô hình (LLM)     | Client → Server | Có (có thể)       | Có            | Hành động, gọi API, thao tác dữ liệu |
| Resources  | Ứng dụng          | Client → Server | Không (chỉ đọc)   | Thường không  | Truy xuất dữ liệu, thu thập ngữ cảnh |
| Prompts    | Người dùng        | Server → Client | Không              | Không (do người dùng chọn) | Quy trình làm việc có hướng dẫn, mẫu chuyên biệt |
| Sampling   | Server            | Server → Client → Server | Gián tiếp | Có            | Tác vụ nhiều bước, hành vi agentic |

Các khả năng này được thiết kế để bổ trợ cho nhau theo những cách sau:

1. Người dùng có thể chọn **Prompt** để bắt đầu quy trình làm việc chuyên biệt
2. Prompt có thể bao gồm ngữ cảnh từ **Tài nguyên**
3. Trong quá trình xử lý, mô hình AI có thể gọi **Công cụ** để thực hiện hành động cụ thể
4. Với các thao tác phức tạp, Server có thể sử dụng **Sampling** để yêu cầu xử lý LLM bổ sung

Sự phân biệt giữa chúng tạo ra cấu trúc rõ ràng cho các tương tác MCP, cho phép các mô hình AI truy cập thông tin, thực hiện hành động và tham gia vào các quy trình làm việc phức tạp trong khi vẫn duy trì các ranh giới kiểm soát phù hợp.

## Quá Trình Khám Phá

Một tính năng chính của MCP là khả năng khám phá động. Khi Client kết nối với Server, nó có thể truy vấn các Tools, Resources và Prompts khả dụng thông qua các phương thức danh sách cụ thể:

- `tools/list`: Khám phá Tools khả dụng
- `resources/list`: Khám phá Resources khả dụng
- `prompts/list`: Khám phá Prompts khả dụng

Cơ chế khám phá động này cho phép Client thích ứng với các khả năng cụ thể mà mỗi Server cung cấp mà không cần biết trước về chức năng của Server.

## Kết Luận

Hiểu rõ các yếu tố cốt lõi này là điều cần thiết để làm việc hiệu quả với MCP. Bằng cách cung cấp các loại khả năng riêng biệt với ranh giới kiểm soát rõ ràng, MCP cho phép các tương tác mạnh mẽ giữa mô hình AI và hệ thống bên ngoài trong khi vẫn duy trì các cơ chế an toàn và kiểm soát phù hợp.

Trong phần tiếp theo, chúng ta sẽ khám phá cách Gradio tích hợp với MCP để cung cấp các giao diện dễ sử dụng cho các khả năng này.
````

## File: units/vi/unit1/communication-protocol.mdx
````
# Giao Thức Truyền Thông

MCP định nghĩa một giao thức truyền thông chuẩn hóa cho phép Client và Server trao đổi thông điệp một cách nhất quán, dễ dự đoán. Sự chuẩn hóa này rất quan trọng để đảm bảo khả năng tương tác trong cộng đồng. Trong phần này, chúng ta sẽ khám phá cấu trúc giao thức và cơ chế vận chuyển được sử dụng trong MCP.

<Tip warning={true}>

Chúng ta đang đi sâu vào những chi tiết phức tạp của giao thức MCP (nguyên văn: "nitty-gritty" - chỉ những chi tiết quan trọng và phức tạp). Bạn không cần biết tất cả những điều này để xây dựng với MCP, nhưng nên biết về sự tồn tại và cách hoạt động của nó.

</Tip>

## JSON-RPC: Nền Tảng

Cốt lõi của MCP sử dụng **JSON-RPC 2.0** làm định dạng thông điệp cho mọi giao tiếp giữa Client và Server. JSON-RPC là giao thức gọi thủ tục từ xa nhẹ được mã hóa bằng JSON, mang lại các ưu điểm:

- Dễ đọc và dễ gỡ lỗi
- Không phụ thuộc ngôn ngữ, hỗ trợ triển khai trên mọi môi trường lập trình
- Được thiết lập tốt với đặc tả rõ ràng và được áp dụng rộng rãi

![message types](https://huggingface.co/datasets/mcp-course/images/resolve/main/unit1/5.png)

Giao thức định nghĩa ba loại thông điệp:

### 1. Yêu Cầu (Requests)

Được gửi từ Client đến Server để khởi tạo một thao tác. Thông điệp Yêu cầu bao gồm:
- Định danh duy nhất (`id`)
- Tên phương thức cần gọi (ví dụ: `tools/call`)
- Tham số cho phương thức (nếu có)

Ví dụ Yêu cầu:

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "weather",
    "arguments": {
      "location": "San Francisco"
    }
  }
}
```

### 2. Phản Hồi (Responses)

Được gửi từ Server đến Client để trả lời Yêu cầu. Thông điệp Phản hồi bao gồm:
- `id` giống với Yêu cầu tương ứng
- Hoặc `result` (thành công) hoặc `error` (thất bại)

Ví dụ Phản hồi Thành công:
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "temperature": 62,
    "conditions": "Partly cloudy"
  }
}
```

Ví dụ Phản hồi Lỗi:
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "error": {
    "code": -32602,
    "message": "Invalid location parameter"
  }
}
```

### 3. Thông Báo

Thông điệp một chiều không yêu cầu phản hồi. Thường được gửi từ Server đến Client để cập nhật tiến trình hoặc thông báo sự kiện.

Ví dụ Thông Báo:
```json
{
  "jsonrpc": "2.0",
  "method": "progress",
  "params": {
    "message": "Processing data...",
    "percent": 50
  }
}
```

## Cơ Chế Vận Chuyển

JSON-RPC định nghĩa định dạng thông điệp, nhưng MCP cũng chỉ định cách thức các thông điệp này được truyền tải giữa Server đến Client. Hai cơ chế vận chuyển chính được hỗ trợ:

### stdio (Đầu vào/Đầu ra chuẩn)

Cơ chế stdio được dùng cho giao tiếp cục bộ, khi Client và Server chạy trên cùng máy:

Ứng dụng chủ khởi chạy Server như một tiến trình con và giao tiếp bằng cách ghi vào đầu vào chuẩn (stdin) và đọc từ đầu ra chuẩn (stdout).

<Tip>

**Trường hợp sử dụng** cho phương thức truyền tải này là các công cụ local như truy cập hệ thống file hoặc chạy script local.

</Tip>

**Ưu điểm** chính của phương thức này là đơn giản, không yêu cầu cấu hình mạng và được hệ điều hành cách ly an toàn.

### HTTP + SSE (Server-Sent Events) / HTTP có thể streaming

Phương thức HTTP + SSE được dùng cho giao tiếp từ xa khi Client và Server có thể ở các máy khác nhau:

Giao tiếp diễn ra qua HTTP, với Server sử dụng Server-Sent Events (SSE) để đẩy các cập nhật tới Client qua kết nối liên tục.

<Tip>

**Trường hợp sử dụng** cho phương thức này là kết nối tới API từ xa, dịch vụ đám mây hoặc tài nguyên dùng chung.

</Tip>

**Ưu điểm** chính là hoạt động được qua mạng, tích hợp được với dịch vụ web và tương thích với môi trường serverless.

Các bản cập nhật gần đây của chuẩn MCP đã giới thiệu hoặc cải tiến "Streamable HTTP", mang lại tính linh hoạt cao hơn bằng cách cho phép Server nâng cấp động lên SSE để streaming khi cần, đồng thời vẫn giữ được tính tương thích với môi trường serverless.

## Vòng đời tương tác

Ở phần trước, chúng ta đã thảo luận về vòng đời của một lượt tương tác đơn lẻ giữa Client (💻) và Server (🌐). Giờ hãy xem xét vòng đời của một lượt tương tác hoàn chỉnh trong ngữ cảnh giao thức MCP.

Giao thức MCP định nghĩa vòng đời tương tác có cấu trúc giữa Client và Server:

### Khởi tạo

Client kết nối tới Server và hai bên trao đổi phiên bản giao thức cùng các tính năng hỗ trợ, Server phản hồi với phiên bản giao thức và tính năng mà nó hỗ trợ.

<table style="width: 100%;">
  <tr>
    <td style="background-color: lightgreen; text-align: center; padding: 10px; border: 1px solid #ccc; border-radius: 4px;">💻</td>
    <td style="text-align: center;">→<br>initialize</td>
    <td style="background-color: lightblue; text-align: center; padding: 10px; border: 1px solid #ccc; border-radius: 4px;">🌐</td>
  </tr>
  <tr>
    <td style="background-color: lightgreen; text-align: center; padding: 10px; border: 1px solid #ccc; border-radius: 4px;">💻</td>
    <td style="text-align: center;">←<br>response</td>
    <td style="background-color: lightblue; text-align: center; padding: 10px; border: 1px solid #ccc; border-radius: 4px;">🌐</td>
  </tr>
  <tr>
    <td style="background-color: lightgreen; text-align: center; padding: 10px; border: 1px solid #ccc; border-radius: 4px;">💻</td>
    <td style="text-align: center;">→<br>initialized</td>
    <td style="background-color: lightblue; text-align: center; padding: 10px; border: 1px solid #ccc; border-radius: 4px;">🌐</td>
  </tr>
</table>

Client xác nhận hoàn tất khởi tạo qua thông báo.

### Khám phá

Client yêu cầu thông tin về các tính năng khả dụng và Server phản hồi với danh sách công cụ có sẵn.

<table style="width: 100%;">
  <tr>
    <td style="background-color: lightgreen; text-align: center; padding: 10px; border: 1px solid #ccc; border-radius: 4px;">💻</td>
    <td style="text-align: center;">→<br>tools/list</td>
    <td style="background-color: lightblue; text-align: center; padding: 10px; border: 1px solid #ccc; border-radius: 4px;">🌐</td>
  </tr>
  <tr>
    <td style="background-color: lightgreen; text-align: center; padding: 10px; border: 1px solid #ccc; border-radius: 4px;">💻</td>
    <td style="text-align: center;">←<br>response</td>
    <td style="background-color: lightblue; text-align: center; padding: 10px; border: 1px solid #ccc; border-radius: 4px;">🌐</td>
  </tr>
</table>

Quá trình này có thể được lặp lại cho từng công cụ, tài nguyên hoặc loại prompt.

### Thực thi

Client kích hoạt các khả năng dựa trên nhu cầu của Host.

<table style="width: 100%;">
  <tr>
    <td style="background-color: lightgreen; text-align: center; padding: 10px; border: 1px solid #ccc; border-radius: 4px;">💻</td>
    <td style="text-align: center;">→<br>tools/call</td>
    <td style="background-color: lightblue; text-align: center; padding: 10px; border: 1px solid #ccc; border-radius: 4px;">🌐</td>
  </tr>
  <tr>
    <td style="background-color: lightgreen; text-align: center; padding: 10px; border: 1px solid #ccc; border-radius: 4px;">💻</td>
    <td style="text-align: center;">←<br>thông báo (tiến trình tùy chọn)</td>
    <td style="background-color: lightblue; text-align: center; padding: 10px; border: 1px solid #ccc; border-radius: 4px;">🌐</td>
  </tr>
  <tr>
    <td style="background-color: lightgreen; text-align: center; padding: 10px; border: 1px solid #ccc; border-radius: 4px;">💻</td>
    <td style="text-align: center;">←<br>phản hồi</td>
    <td style="background-color: lightblue; text-align: center; padding: 10px; border: 1px solid #ccc; border-radius: 4px;">🌐</td>
  </tr>
</table>

### Kết thúc

Kết nối được đóng một cách hợp lệ khi không còn cần thiết và Server xác nhận yêu cầu tắt.

<table style="width: 100%;">
  <tr>
    <td style="background-color: lightgreen; text-align: center; padding: 10px; border: 1px solid #ccc; border-radius: 4px;">💻</td>
    <td style="text-align: center;">→<br>tắt máy</td>
    <td style="background-color: lightblue; text-align: center; padding: 10px; border: 1px solid #ccc; border-radius: 4px;">🌐</td>
  </tr>
  <tr>
    <td style="background-color: lightgreen; text-align: center; padding: 10px; border: 1px solid #ccc; border-radius: 4px;">💻</td>
    <td style="text-align: center;">←<br>phản hồi</td>
    <td style="background-color: lightblue; text-align: center; padding: 10px; border: 1px solid #ccc; border-radius: 4px;">🌐</td>
  </tr>
  <tr>
    <td style="background-color: lightgreen; text-align: center; padding: 10px; border: 1px solid #ccc; border-radius: 4px;">💻</td>
    <td style="text-align: center;">→<br>thoát</td>
    <td style="background-color: lightblue; text-align: center; padding: 10px; border: 1px solid #ccc; border-radius: 4px;">🌐</td>
  </tr>
</table>

Client gửi thông điệp thoát cuối cùng để hoàn tất việc kết thúc.

## Tiến hóa của Giao thức

Giao thức MCP được thiết kế để có thể mở rộng và thích ứng. Giai đoạn khởi tạo bao gồm thương lượng phiên bản, cho phép tương thích ngược khi giao thức phát triển. Bên cạnh đó, việc khám phá khả năng cho phép Client thích ứng với các tính năng cụ thể mà mỗi Server cung cấp, cho phép kết hợp cả Máy chủ cơ bản và nâng cao trong cùng một hệ sinh thái.
````

## File: units/vi/unit1/gradio-mcp.mdx
````
# Tích hợp Gradio với MCP

Giờ chúng ta đã tìm hiểu các khái niệm cốt lõi của Giao Thức Ngữ Cảnh Mô Hình (MCP) và cách triển khai MCP Servers và Clients. Trong phần này, chúng ta sẽ làm mọi thứ dễ dàng hơn bằng cách sử dụng Gradio để tạo một MCP Server!

<Tip>

Gradio là thư viện Python nổi tiếng giúp tạo giao diện web tùy chỉnh nhanh chóng cho các mô hình học máy.

</Tip>

## Giới thiệu về Gradio

Gradio cho phép các nhà phát triển tạo giao diện người dùng (UI) cho mô hình của họ chỉ với vài dòng mã Python. Thư viện này đặc biệt hữu ích cho:

- Tạo demo và nguyên mẫu
- Chia sẻ mô hình với người dùng không chuyên về kỹ thuật
- Kiểm tra và gỡ lỗi hành vi của mô hình

Với việc hỗ trợ thêm MCP, Gradio giờ đây cung cấp cách đơn giản để hiển thị các khả năng của mô hình AI thông qua giao thức MCP chuẩn hóa.

Kết hợp Gradio với MCP cho phép bạn tạo cả giao diện thân thiện với con người và công cụ truy cập được bằng AI với mã tối thiểu. Điều tuyệt nhất là Gradio đã được cộng đồng AI sử dụng rộng rãi, vì vậy bạn có thể dùng nó để chia sẻ MCP Servers của mình với người khác.

## Điều kiện tiên quyết

Để sử dụng Gradio với hỗ trợ MCP, bạn cần cài đặt Gradio với phần mở rộng MCP:

```bash
pip install "gradio[mcp]"
```

Bạn cũng cần một ứng dụng LLM hỗ trợ gọi công cụ sử dụng giao thức MCP, như Cursor (được gọi là "MCP Hosts").

## Tạo MCP Server với Gradio

Hãy cùng xem qua ví dụ cơ bản về cách tạo MCP Server bằng Gradio:

<details>
<summary>Bấm để xem bản dịch tiếng Việt</summary>
```python
import gradio as gr

def letter_counter(word: str, letter: str) -> int:
    """
    Đếm số lần xuất hiện của một ký tự trong từ hoặc văn bản.

    Args:
        word (str): Văn bản đầu vào để tìm kiếm
        letter (str): Ký tự cần tìm

    Returns:
        int: Số lần ký tự xuất hiện trong văn bản
    """
    word = word.lower()
    letter = letter.lower()
    count = word.count(letter)
    return count

# Tạo giao diện Gradio tiêu chuẩn
demo = gr.Interface(
    fn=letter_counter,
    inputs=["textbox", "textbox"],
    outputs="number",
    title="Bộ đếm ký tự",
    description="Nhập văn bản và một ký tự để đếm số lần ký tự đó xuất hiện trong văn bản."
)

# Khởi chạy cả giao diện web Gradio và MCP Server
if __name__ == "__main__":
    demo.launch(mcp_server=True)
```
</details>

```python
import gradio as gr

def letter_counter(word: str, letter: str) -> int:
    """
    Count the number of occurrences of a letter in a word or text.

    Args:
        word (str): The input text to search through
        letter (str): The letter to search for

    Returns:
        int: The number of times the letter appears in the text
    """
    word = word.lower()
    letter = letter.lower()
    count = word.count(letter)
    return count

# Create a standard Gradio interface
demo = gr.Interface(
    fn=letter_counter,
    inputs=["textbox", "textbox"],
    outputs="number",
    title="Letter Counter",
    description="Enter text and a letter to count how many times the letter appears in the text."
)

# Launch both the Gradio web interface and the MCP server
if __name__ == "__main__":
    demo.launch(mcp_server=True)
```

Với thiết lập này, hàm đếm ký tự của bạn giờ có thể truy cập qua:

1. Giao diện web Gradio truyền thống cho tương tác trực tiếp của con người
2. MCP Server có thể kết nối với các clients tương thích

MCP server sẽ truy cập được tại:
```
http://your-server:port/gradio_api/mcp/sse
```

Ứng dụng trông như thế này:

![Gradio MCP Server](https://huggingface.co/datasets/mcp-course/images/resolve/main/unit1/7.png)

## Cách thức hoạt động đằng sau hậu trường

Khi bạn thiết lập `mcp_server=True` trong `launch()`, những điều sau sẽ xảy ra:

1. Các hàm Gradio được tự động chuyển đổi thành MCP Tools
2. Các thành phần đầu vào ánh xạ thành lược đồ tham số công cụ
3. Các thành phần đầu xác định định dạng phản hồi
4. Server Gradio giờ cũng lắng nghe các tin nhắn theo giao thức MCP
5. JSON-RPC qua HTTP+SSE được thiết lập cho giao tiếp client-server

## Tính năng chính của tích hợp Gradio <> MCP

1. **Chuyển đổi công cụ**: Mỗi API endpoint trong ứng dụng Gradio của bạn sẽ tự động chuyển thành MCP tool với tên, mô tả và lược đồ đầu vào tương ứng. Để xem các công cụ và lược đồ, truy cập `http://your-server:port/gradio_api/mcp/schema` hoặc vào link "View API" ở footer ứng dụng Gradio, sau đó click vào "MCP".

2. **Hỗ trợ biến môi trường**: Có hai cách để kích hoạt chức năng MCP server:
- Dùng tham số `mcp_server` trong `launch()`:
  ```python
  demo.launch(mcp_server=True)
  ```
- Dùng biến môi trường:
  ```bash
  export GRADIO_MCP_SERVER=True
  ```

3. **Xử lý file**: Server tự động xử lý chuyển đổi dữ liệu file bao gồm:
   - Chuyển đổi chuỗi mã hóa base64 thành dữ liệu file
   - Xử lý file ảnh và trả về đúng định dạng
   - Quản lý bộ nhớ file tạm

   Chúng ta **nên** truyền ảnh/file đầu vào dưới dạng URL đầy đủ ("http://..." hoặc "https://...") vì MCP Client không phải lúc nào cũng xử lý đúng file local.

4. **Server MCP được host trên 🤗 Spaces**: Bạn có thể publish ứng dụng Gradio miễn phí trên Hugging Face Spaces để có MCP server được host miễn phí. Đây là ví dụ một Space như vậy: https://huggingface.co/spaces/abidlabs/mcp-tools

## Mẹo xử lý sự cố

1. **Gợi ý kiểu và chuỗi tài liệu**: Đảm bảo bạn cung cấp gợi ý kiểu và chuỗi tài liệu hợp lệ cho hàm. Chuỗi tài liệu cần có khối "Args:" với các tham số được thụt lề.

2. **Đầu vào dạng chuỗi**: Khi không chắc chắn, hãy chấp nhận đối số đầu vào dạng `str` và chuyển đổi sang kiểu mong muốn bên trong hàm.

3. **Hỗ trợ SSE**: Một số MCP Host không hỗ trợ MCP Server dùng SSE. Trong trường hợp đó, bạn có thể dùng `mcp-remote`:
   ```json
   {
     "mcpServers": {
       "gradio": {
         "command": "npx",
         "args": [
           "mcp-remote",
           "http://your-server:port/gradio_api/mcp/sse"
         ]
       }
     }
   }
   ```

4. **Khởi động lại**: Nếu gặp vấn đề kết nối, hãy thử khởi động lại cả MCP Client và MCP Server.

## Chia sẻ MCP Server của bạn

Bạn có thể chia sẻ MCP Server bằng cách publish ứng dụng Gradio lên Hugging Face Spaces. Video dưới đây hướng dẫn cách tạo Hugging Face Space.

<Youtube id="3bSVKNKb_PY" />

Giờ bạn có thể chia sẻ MCP Server với người khác bằng cách chia sẻ Hugging Face Space của mình.

## Kết luận

Việc tích hợp Gradio với MCP mang đến điểm khởi đầu dễ tiếp cận vào hệ sinh thái MCP. Bằng cách tận dụng sự đơn giản của Gradio và thêm chuẩn hóa từ MCP, các bạn có thể nhanh chóng tạo cả giao diện thân thiện với người dùng lẫn công cụ truy cập được bằng AI với ít code nhất.

Trong suốt khóa học này, chúng ta sẽ khám phá thêm nhiều cách triển khai MCP phức tạp hơn, nhưng Gradio vẫn là điểm khởi đầu tuyệt vời để hiểu và thử nghiệm với giao thức
````

## File: units/vi/unit1/introduction.mdx
````
# Giới thiệu về Giao Thức Ngữ Cảnh Mô Hình (MCP)

Chào mừng các bạn đến với Chương 1 của Khóa học MCP! Trong chương này, chúng ta sẽ cùng khám phá những nguyên tắc cơ bản của Giao Thức Ngữ Cảnh Mô Hình.

## Những gì bạn sẽ học

Trong chương này, các bạn sẽ:

* Hiểu MCP là gì và tại sao nó quan trọng
* Nắm được các khái niệm chính và thuật ngữ liên quan đến MCP
* Khám phá những thách thức tích hợp mà MCP giải quyết
* Tìm hiểu các lợi ích và mục tiêu chính của MCP
* Xem ví dụ đơn giản về tích hợp MCP trong thực tế

Khi kết thúc chương này, các bạn sẽ nắm vững những khái niệm nền tảng về MCP và sẵn sàng đi sâu vào kiến trúc và cách triển khai ở chương tiếp theo.

## Tầm quan trọng của MCP

Hệ sinh thái AI đang phát triển nhanh chóng với các Mô hình Ngôn ngữ Lớn (LLMs) và hệ thống AI khác ngày càng mạnh mẽ. Tuy nhiên, các mô hình này thường bị giới hạn bởi dữ liệu huấn luyện và thiếu khả năng truy cập thông tin thời gian thực hay các công cụ chuyên biệt. Hạn chế này cản trở tiềm năng của hệ thống AI trong việc đưa ra phản hồi thực sự phù hợp, chính xác và hữu ích.

Đây chính là lúc Giao Thức Ngữ Cảnh Mô Hình (MCP) phát huy tác dụng. MCP cho phép các mô hình AI kết nối với nguồn dữ liệu bên ngoài, công cụ và môi trường, tạo điều kiện trao đổi thông tin liền mạch giữa hệ thống AI và thế giới số. Khả năng tương tác này rất quan trọng cho sự phát triển và ứng dụng rộng rãi của các ứng dụng AI thực sự hữu ích.

## Tổng quan Chương 1

Dưới đây là những nội dung chính chúng ta sẽ đề cập:

1. **MCP là gì?** - Bắt đầu với định nghĩa về MCP và vai trò của nó trong hệ sinh thái AI
2. **Khái niệm chính** - Khám phá những khái niệm nền tảng và thuật ngữ liên quan
3. **Thách thức tích hợp** - Phân tích các vấn đề MCP hướng tới giải quyết, đặc biệt là "Bài toán tích hợp M×N"
4. **Lợi ích và mục tiêu** - Thảo luận về các ưu điểm và mục đích chính của MCP như chuẩn hóa, nâng cao khả năng AI và khả năng tương tác
5. **Ví dụ đơn giản** - Cùng xem qua ví dụ thực tế về tích hợp MCP

Hãy cùng bắt đầu hành trình khám phá thế giới thú vị của Giao Thức Ngữ Cảnh Mô Hình!
````

## File: units/vi/unit1/key-concepts.mdx
````
# Các Khái Niệm và Thuật Ngữ Chính

Trước khi đi sâu vào Giao Thức Ngữ Cảnh Mô Hình (MCP), chúng ta cần hiểu các khái niệm và thuật ngữ then chốt tạo nền tảng cho MCP. Chương này sẽ giới thiệu những ý tưởng cốt lõi cùng bộ từ vựng chung để thảo luận về các triển khai MCP xuyên suốt khóa học.

MCP thường được ví như "USB-C cho các ứng dụng AI". Giống như USB-C cung cấp giao diện vật lý và logic chuẩn hóa để kết nối các thiết bị ngoại vi với máy tính, MCP đưa ra giao thức đồng nhất để liên kết các mô hình AI với khả năng mở rộng. Sự chuẩn hóa này mang lợi ích cho toàn bộ hệ sinh thái:

- **Người dùng** được trải nghiệm đơn giản và nhất quán hơn trên mọi ứng dụng AI
- **Nhà phát triển ứng dụng AI** dễ dàng tích hợp với hệ sinh thái công cụ và nguồn dữ liệu ngày càng phong phú
- **Nhà cung cấp công cụ/dữ liệu** chỉ cần xây dựng một triển khai duy nhất tương thích với nhiều ứng dụng AI
- **Toàn hệ sinh thái** hưởng lợi từ khả năng tương tác cao hơn, đổi mới mạnh mẽ hơn và giảm phân mảnh

## Bài Toán Tích Hợp

**Bài Toán Tích Hợp M×N** ám chỉ thách thức khi kết nối M ứng dụng AI khác nhau với N công cụ/nguồn dữ liệu ngoài mà không có phương pháp chuẩn hóa.

### Không có MCP (Bài Toán M×N)

Không có giao thức như MCP, nhà phát triển phải tạo M×N tích hợp tùy biến - mỗi tích hợp cho một cặp ứng dụng AI với khả năng mở rộng.

![Without MCP](https://huggingface.co/datasets/mcp-course/images/resolve/main/unit1/1.png)

Mỗi ứng dụng AI cần tích hợp riêng lẻ với từng công cụ/nguồn dữ liệu. Quá trình này rất phức tạp, tốn kém và gây nhiều khó khăn cho nhà phát triển, đồng thời làm tăng chi phí bảo trì.

### Với MCP (Giải Pháp M+N)

MCP biến bài toán này thành M+N bằng cách cung cấp giao diện chuẩn: mỗi ứng dụng AI triển khai phía Máy khách MCP một lần, mỗi công cụ/nguồn dữ liệu triển khai phía Máy chủ một lần. Cách này giảm đáng kể độ phức tạp tích hợp và gánh nặng bảo trì.

![With MCP](https://huggingface.co/datasets/mcp-course/images/resolve/main/unit1/2.png)

Mỗi ứng dụng AI triển khai phía Máy khách MCP một lần, mỗi công cụ/nguồn dữ liệu triển khai phía Máy chủ một lần.

## Thuật ngữ cốt lõi trong MCP

Giờ chúng ta đã hiểu vấn đề mà MCP giải quyết, hãy cùng khám phá các thuật ngữ và khái niệm cốt lõi tạo nên giao thức MCP.

<Tip>

MCP là một chuẩn như HTTP hay USB-C, và là giao thức để kết nối các ứng dụng AI với công cụ và nguồn dữ liệu bên ngoài. Vì vậy, việc sử dụng thuật ngữ chuẩn là cực kỳ quan trọng để MCP hoạt động hiệu quả.

Khi viết tài liệu ứng dụng và trao đổi với cộng đồng, chúng ta nên sử dụng các thuật ngữ sau đây.

</Tip>

### Thành phần

Tương tự như mối quan hệ client-server trong HTTP, MCP có client (máy khách) và server (máy chủ).

![MCP Components](https://huggingface.co/datasets/mcp-course/images/resolve/main/unit1/3.png)

- **Host**: Ứng dụng AI mà người dùng cuối tương tác trực tiếp. Ví dụ: Claude Desktop của Anthropic, các IDE tích hợp AI như Cursor, thư viện inference như Hugging Face Python SDK, hoặc ứng dụng tùy chỉnh xây dựng bằng thư viện như LangChain hay smolagents. Host khởi tạo kết nối đến Máy chủ MCP và điều phối luồng làm việc giữa yêu cầu người dùng, xử lý LLM và công cụ bên ngoài.

- **Client**: Thành phần trong ứng dụng Host quản lý giao tiếp với một MCP Server cụ thể. Mỗi Client duy trì kết nối 1:1 với một Server, xử lý các chi tiết giao thức của MCP và đóng vai trò trung gian giữa logic của Host và Server bên ngoài.

- **Server**: Chương trình hoặc dịch vụ bên ngoài cung cấp các khả năng (Tools, Resources, Prompts) thông qua giao thức MCP.

<Tip warning={true}>

Nhiều tài liệu sử dụng 'Client' và 'Host' thay thế cho nhau. Về mặt kỹ thuật, Host là ứng dụng hướng đến người dùng, còn Client là thành phần bên trong ứng dụng Host quản lý giao tiếp với MCP Server.

</Tip>

### Khả năng

Tất nhiên, giá trị ứng dụng của bạn được quyết định bởi tổng các khả năng mà nó cung cấp. Các khả năng là phần quan trọng nhất trong ứng dụng. MCP có thể kết nối với mọi dịch vụ phần mềm, nhưng có một số khả năng phổ biến được dùng cho nhiều ứng dụng AI.

| Khả năng     | Mô tả         | Ví dụ         |
| ------------ | ------------- | ------------- |
| **Tools**    | Các hàm có thể thực thi mà mô hình AI có thể gọi để thực hiện hành động hoặc truy xuất dữ liệu đã tính toán. Thường liên quan đến use case của ứng dụng. | Một tool cho ứng dụng thời tiết có thể là hàm trả về thời tiết ở địa điểm cụ thể. |
| **Resources** | Nguồn dữ liệu chỉ đọc cung cấp ngữ cảnh mà không cần tính toán phức tạp. | Trợ lý nghiên cứu có thể có nguồn về các bài báo khoa học. |
| **Prompts**   | Các mẫu hoặc quy trình làm việc được định nghĩa sẵn để hướng dẫn tương tác giữa người dùng, mô hình AI và các khả năng có sẵn. | Prompt tóm tắt văn bản. |
| **Sampling**  | Các yêu cầu do Máy chủ khởi tạo để Client/Host thực hiện tương tác LLM, cho phép hành động đệ quy nơi LLM có thể xem xét nội dung đã tạo và đưa ra quyết định tiếp theo. | Ứng dụng viết lách tự đánh giá output và quyết định cải thiện thêm. |

Trong sơ đồ sau, chúng ta có thể thấy các khả năng được áp dụng cho use case của một CodeAgent.

![collective diagram](https://huggingface.co/datasets/mcp-course/images/resolve/main/unit1/8.png)

Ứng dụng này có thể sử dụng các thực thể MCP theo cách sau:

| Thực thể | Tên            | Mô tả                     |
| -------- | -------------- | ------------------------- |
| Tool     | Code Interpreter | Công cụ có thể thực thi mã mà LLM viết. |
| Resource | Documentation  | Tài nguyên chứa tài liệu hướng dẫn của ứng dụng. |
| Prompt   | Code Style     | Prompt hướng dẫn LLM tạo mã. |
| Sampling | Code Review    | Sampling cho phép LLM review mã và đưa ra quyết định tiếp theo.|

### Kết luận

Hiểu rõ những khái niệm và thuật ngữ chính này sẽ tạo nền tảng để làm việc hiệu quả với MCP (Giao Thức Ngữ Cảnh Mô Hình). Trong các phần tiếp theo, chúng ta sẽ xây dựng dựa trên nền tảng này để khám phá các thành phần kiến trúc, giao thức truyền thông và tính năng tạo nên Giao Thức Ngữ Cảnh Mô Hình.
````

## File: units/vi/unit2/clients.mdx
````
# Xây dựng MCP Clients

Trong phần này, chúng ta sẽ tạo các client có thể tương tác với MCP server bằng các ngôn ngữ lập trình khác nhau. Chúng ta sẽ triển khai cả client JavaScript sử dụng HuggingFace.js và client Python sử dụng smolagents.

## Cấu hình MCP Clients

Việc triển khai hiệu quả MCP servers và clients yêu cầu cấu hình phù hợp. Đặc tả MCP vẫn đang phát triển, vì vậy các phương pháp cấu hình có thể thay đổi. Chúng ta sẽ tập trung vào các best practice hiện tại về cấu hình.

### Cấu hình Files của MCP

Các MCP hosts sử dụng configuration files để quản lý kết nối server. Những files này xác định các servers nào có sẵn và cách kết nối đến chúng.

Các configuration files rất đơn giản, dễ hiểu và thống nhất giữa các MCP hosts chính.

#### Cấu trúc `mcp.json`

File cấu hình chuẩn cho MCP có tên `mcp.json`. Đây là cấu trúc cơ bản:

```json
{
  "servers": [
    {
      "name": "MCP Server",
      "transport": {
        "type": "sse",
        "url": "http://localhost:7860/gradio_api/mcp/sse"
      }
    }
  ]
}
```

Trong ví dụ này, chúng ta có một server được cấu hình sử dụng SSE transport, kết nối đến Gradio server local chạy trên cổng 7860.

<Tip>

Chúng ta đã kết nối đến ứng dụng Gradio qua giao thức SSE vì giả định rằng ứng dụng gradio đang chạy trên một Server từ xa. Tuy nhiên nếu bạn muốn kết nối đến script local, `stdio` transport thay vì `sse` transport là lựa chọn tốt hơn.

</Tip>

#### Cấu hình cho HTTP+SSE Transport

Với các servers từ xa sử dụng HTTP+SSE transport, cấu hình bao gồm URL của server:

```json
{
  "servers": [
    {
      "name": "Remote MCP Server",
      "transport": {
        "type": "sse",
        "url": "https://example.com/gradio_api/mcp/sse"
      }
    }
  ]
}
```

Cấu hình này cho phép UI client của bạn giao tiếp với Gradio MCP server sử dụng MCP protocol, giúp tích hợp liền mạch giữa frontend và dịch vụ MCP.

## Cấu hình UI MCP Client

Khi làm việc với Gradio MCP servers, bạn có thể cấu hình UI client để kết nối đến server sử dụng MCP protocol. Cách thiết lập như sau:

### Cấu hình cơ bản

Tạo file mới tên `config.json` với cấu hình sau:

```json
{
  "mcpServers": {
    "mcp": {
      "url": "http://localhost:7860/gradio_api/mcp/sse"
    }
  }
}
```

Cấu hình này cho phép UI client của bạn giao tiếp với Gradio MCP server sử dụng MCP protocol, giúp tích hợp liền mạch giữa frontend và dịch vụ MCP.
````

## File: units/vi/unit2/gradio-server.mdx
````
# Xây dựng Gradio MCP Server

Trong phần này, chúng ta sẽ tạo một MCP server phân tích cảm xúc bằng Gradio. Server này sẽ cung cấp công cụ phân tích cảm xúc cho cả người dùng qua giao diện web và các mô hình AI thông qua giao thức MCP.

## Giới thiệu tích hợp Gradio MCP

Gradio cung cấp cách đơn giản để tạo MCP server bằng việc tự động chuyển đổi các hàm Python thành MCP Tools. Khi bạn đặt `mcp_server=True` trong `launch()`, Gradio sẽ:

1. Tự động chuyển đổi các hàm thành MCP Tools
2. Ánh xạ các thành phần đầu vào sang schema tham số công cụ
3. Xác định định dạng phản hồi từ các thành phần đầu ra
4. Thiết lập JSON-RPC qua HTTP+SSE cho giao tiếp client-server
5. Tạo cả giao diện web và endpoint MCP server

## Thiết lập dự án

Đầu tiên, hãy tạo thư mục mới cho dự án và cài đặt các phụ thuộc cần thiết:

```bash
mkdir mcp-sentiment
cd mcp-sentiment
python -m venv venv
source venv/bin/activate  # Trên Windows: venv\Scripts\activate
pip install "gradio[mcp]" textblob
```

## Tạo Server

Tạo một tệp mới có tên `server.py` với mã sau:

<details>
<summary>Bấm để xem bản dịch tiếng Việt</summary>
```python
import gradio as gr
from textblob import TextBlob

def sentiment_analysis(text: str) -> dict:
    """
    Phân tích cảm xúc của văn bản được cung cấp.

    Args:
        text (str): Văn bản cần phân tích

    Returns:
        dict: Từ điển chứa thông tin về độ phân cực, tính chủ quan và đánh giá
    """
    blob = TextBlob(text)
    sentiment = blob.sentiment
    
    return {
        "polarity": round(sentiment.polarity, 2),  # -1 (tiêu cực) đến 1 (tích cực)
        "subjectivity": round(sentiment.subjectivity, 2),  # 0 (khách quan) đến 1 (chủ quan)
        "assessment": "positive" if sentiment.polarity > 0 else "negative" if sentiment.polarity < 0 else "neutral"
    }

# Tạo giao diện Gradio
demo = gr.Interface(
    fn=sentiment_analysis,
    inputs=gr.Textbox(placeholder="Nhập văn bản để phân tích..."),
    outputs=gr.JSON(),
    title="Phân Tích Cảm Xúc Văn Bản",
    description="Phân tích cảm xúc văn bản sử dụng TextBlob"
)

# Khởi chạy giao diện và Server MCP
if __name__ == "__main__":
    demo.launch(mcp_server=True)
```
</details>

```python
import gradio as gr
from textblob import TextBlob

def sentiment_analysis(text: str) -> dict:
    """
    Analyze the sentiment of the given text.

    Args:
        text (str): The text to analyze

    Returns:
        dict: A dictionary containing polarity, subjectivity, and assessment
    """
    blob = TextBlob(text)
    sentiment = blob.sentiment
    
    return {
        "polarity": round(sentiment.polarity, 2),  # -1 (negative) to 1 (positive)
        "subjectivity": round(sentiment.subjectivity, 2),  # 0 (objective) to 1 (subjective)
        "assessment": "positive" if sentiment.polarity > 0 else "negative" if sentiment.polarity < 0 else "neutral"
    }

# Create the Gradio interface
demo = gr.Interface(
    fn=sentiment_analysis,
    inputs=gr.Textbox(placeholder="Enter text to analyze..."),
    outputs=gr.JSON(),
    title="Text Sentiment Analysis",
    description="Analyze the sentiment of text using TextBlob"
)

# Launch the interface and MCP server
if __name__ == "__main__":
    demo.launch(mcp_server=True)
```

## Hiểu về Mã

Hãy cùng phân tích các thành phần chính:

1. **Định nghĩa Hàm**:
   - Hàm `sentiment_analysis` nhận đầu vào là văn bản và trả về một từ điển
   - Sử dụng TextBlob để phân tích cảm xúc
   - Docstring rất quan trọng vì giúp Gradio tạo lược đồ công cụ MCP
   - Gợi ý kiểu dữ liệu (`str` và `dict`) giúp xác định lược đồ đầu vào/đầu ra

2. **Giao diện Gradio**:
   - `gr.Interface` tạo cả giao diện web và Server MCP
   - Hàm được hiển thị như một công cụ MCP tự động
   - Các thành phần đầu vào và đầu ra xác định lược đồ công cụ
   - Thành phần đầu ra JSON đảm bảo tuần tự hóa đúng cách

3. **Server MCP**:
   - Thiết lập `mcp_server=True` kích hoạt Server MCP
   - Server sẽ có sẵn tại `http://localhost:7860/gradio_api/mcp/sse`
   - Bạn cũng có thể kích hoạt bằng biến môi trường:
     ```bash
     export GRADIO_MCP_SERVER=True
     ```

## Chạy Server

Khởi động Server bằng cách chạy:

```bash
python server.py
```

Bạn sẽ thấy đầu ra cho biết cả giao diện web và Server MCP đang chạy. Giao diện web sẽ có sẵn tại `http://localhost:7860`, và Server MCP tại `http://localhost:7860/gradio_api/mcp/sse`.

## Kiểm tra Server

Bạn có thể kiểm tra Server bằng hai cách:

1. **Giao diện Web**:
   - Mở `http://localhost:7860` trong trình duyệt
   - Nhập văn bản và nhấp "Submit"
   - Bạn sẽ thấy kết quả phân tích cảm xúc

2. **Lược đồ MCP**:
   - Truy cập `http://localhost:7860/gradio_api/mcp/schema`
   - Hiển thị lược đồ công cụ MCP mà các Client sẽ sử dụng
   - Bạn cũng có thể tìm thấy liên kết này trong phần "View API" ở chân trang ứng dụng Gradio

## Mẹo Xử lý Sự cố

1. **Gợi ý Kiểu dữ liệu và Docstring**:
   - Luôn cung cấp gợi ý kiểu dữ liệu cho tham số hàm và giá trị trả về
   - Bao gồm docstring với khối "Args:" cho mỗi tham số
   - Điều này giúp Gradio tạo lược đồ công cụ MCP chính xác

2. **Đầu vào Chuỗi**:
   - Khi không chắc chắn, hãy chấp nhận đối số đầu vào dưới dạng `str`
   - Chuyển đổi chúng sang kiểu mong muốn bên trong hàm
   - Cung cấp khả năng tương thích tốt hơn với các Client MCP

3. **Hỗ trợ SSE**:
   - Một số Client MCP không hỗ trợ Server MCP dựa trên SSE
   - Trong trường hợp đó, sử dụng `mcp-remote`:
     ```json
     {
       "mcpServers": {
         "gradio": {
           "command": "npx",
           "args": [
             "mcp-remote",
             "http://localhost:7860/gradio_api/mcp/sse"
           ]
         }
       }
     }
     ```

4. **Sự cố Kết nối**:
   - Nếu gặp vấn đề kết nối, thử khởi động lại cả Client và Server
   - Kiểm tra xem Server đang chạy và có thể truy cập được không
   - Xác nhận rằng lược đồ MCP có sẵn tại URL mong đợi

## Triển khai lên Hugging Face Spaces

Để làm cho Server của bạn có sẵn cho người khác, bạn có thể triển khai lên Hugging Face Spaces:

1. Tạo một Space mới trên Hugging Face:
   - Truy cập huggingface.co/spaces
   - Nhấp "Create new Space"
   - Chọn "Gradio" làm SDK
   - Đặt tên cho Space của bạn (ví dụ: "mcp-sentiment")

2. Tạo tệp `requirements.txt`:
```txt
gradio[mcp]
textblob
```

3. Đẩy mã của bạn lên Space:
```bash
git init
git add server.py requirements.txt
git commit -m "Initial commit"
git remote add origin https://huggingface.co/spaces/YOUR_USERNAME/mcp-sentiment
git push -u origin main
```

Server MCP của các bạn giờ đã có thể truy cập tại:
```
https://YOUR_USERNAME-mcp-sentiment.hf.space/gradio_api/mcp/sse
```

## Bước tiếp theo

Giờ khi đã có Server MCP đang chạy, chúng ta sẽ tạo các Client để tương tác với nó. Trong các phần tiếp theo, chúng ta sẽ:

1. Tạo một Client dựa trên HuggingFace.js lấy cảm hứng từ Tiny Agents
2. Triển khai một Client Python dựa trên SmolAgents
3. Kiểm tra cả hai Client với Server đã triển khai

Hãy cùng chuyển sang phần xây dựng Client đầu tiên nào!
````

## File: units/vi/unit2/introduction.mdx
````
# Xây Dựng Ứng Dụng MCP Đầu Cuối

Chào mừng các bạn đến với Chương 2 của Khóa học MCP!

Trong chương này, chúng ta sẽ xây dựng một ứng dụng MCP hoàn chỉnh từ đầu, tập trung vào việc tạo Server với Gradio và kết nối nó với nhiều Client. Cách tiếp cận thực hành này sẽ giúp bạn có được kinh nghiệm thực tế với toàn bộ hệ sinh thái MCP.

<Tip>

Trong chương này, chúng ta sẽ xây dựng một Server và Client MCP đơn giản bằng Gradio và HuggingFace Hub. Ở chương tiếp theo, chúng ta sẽ phát triển một Server phức tạp hơn để giải quyết các bài toán thực tế.

</Tip>

## Những Nội Dung Bạn Sẽ Học

Trong chương này, các bạn sẽ:

- Tạo Server MCP sử dụng tính năng hỗ trợ MCP tích hợp của Gradio
- Xây dựng công cụ phân tích cảm xúc có thể được sử dụng bởi các Mô hình AI
- Kết nối với Server bằng các cách triển khai Client khác nhau:
  - Client dựa trên HuggingFace.js
  - Client SmolAgents dành cho Python
- Triển khai Server MCP lên Hugging Face Spaces
- Kiểm tra và gỡ lỗi toàn bộ hệ thống

Kết thúc chương này, bạn sẽ có một ứng dụng MCP hoạt động thể hiện được sức mạnh và tính linh hoạt của giao thức này.

## Điều Kiện Tiên Quyết

Trước khi bắt đầu chương này, hãy đảm bảo bạn:

- Đã hoàn thành Chương 1 hoặc hiểu cơ bản về các khái niệm MCP
- Thành thạo cả Python và JavaScript/TypeScript
- Hiểu cơ bản về API và kiến trúc Client-Server
- Có môi trường phát triển với:
  - Python 3.10+
  - Node.js 18+
  - Tài khoản Hugging Face (để triển khai)

## Dự Án End-to-End Của Chúng Ta

Chúng ta sẽ xây dựng ứng dụng phân tích cảm xúc bao gồm 3 phần chính: Server, Client và phần triển khai.

![sentiment analysis application](https://huggingface.co/datasets/mcp-course/images/resolve/main/unit2/1.png)

### Phía Server

- Sử dụng Gradio để tạo giao diện web và Server MCP qua `gr.Interface`
- Triển khai công cụ phân tích cảm xúc bằng TextBlob
- Cung cấp công cụ qua cả giao thức HTTP và MCP

### Phía Client

- Triển khai Client HuggingFace.js
- Hoặc tạo Client Python smolagents
- Minh họa cách sử dụng cùng một Server với các cách triển khai Client khác nhau

### Triển Khai

- Đưa Server lên Hugging Face Spaces
- Cấu hình các Client để làm việc với Server đã triển khai

## Hãy Bắt Đầu Nào!

## Hãy Bắt Đầu Nào!

Bạn đã sẵn sàng xây dựng ứng dụng MCP đầu cuối đầu tiên chưa? Hãy bắt đầu bằng cách thiết lập môi trường phát triển và tạo máy chủ MCP Gradio của chúng ta.
````

## File: units/vi/unit2/tiny-agents.mdx
````
# Tiny Agents: Một agent chạy bằng MCP chỉ với 50 dòng mã

Sau khi đã xây dựng các máy chủ MCP bằng Gradio, giờ chúng ta sẽ khám phá sâu hơn về máy khách MCP. Phần này phát triển từ dự án thử nghiệm [Tiny Agents](https://huggingface.co/blog/tiny-agents) - minh họa cách triển khai máy khách MCP siêu đơn giản có thể kết nối với các dịch vụ như máy chủ phân tích cảm xúc Gradio của chúng ta.

Trong bài thực hành ngắn này, chúng mình sẽ hướng dẫn các bạn cách triển khai máy khách MCP bằng TypeScript (JS) có thể giao tiếp với bất kỳ máy chủ MCP nào, bao gồm cả máy chủ phân tích cảm xúc dựa trên Gradio đã xây dựng ở phần trước. Bạn sẽ thấy MCP chuẩn hóa cách các agent tương tác với công cụ như thế nào, giúp phát triển AI Agent trở nên đơn giản hơn đáng kể.

![meme](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/tiny-agents/thumbnail.jpg)
<figcaption>Ảnh được cung cấp bởi https://x.com/adamdotdev</figcaption>

Chúng ta sẽ chỉ cách kết nối tiny agent của bạn với các máy chủ MCP chạy trên Gradio, cho phép nó tận dụng cả công cụ phân tích cảm xúc tùy chỉnh của bạn lẫn các công cụ có sẵn khác.

## Cách chạy bản demo hoàn chỉnh

Nếu đã cài NodeJS (với `pnpm` hoặc `npm`), chỉ cần chạy lệnh sau trong terminal:

```bash
npx @huggingface/mcp-client
```

hoặc nếu dùng `pnpm`:

```bash
pnpx @huggingface/mcp-client
```

Lệnh này sẽ cài đặt gói vào thư mục tạm rồi thực thi lệnh của nó.

Bạn sẽ thấy Agent đơn giản của mình kết nối với nhiều máy chủ MCP (chạy local), tải các công cụ của chúng (tương tự cách nó tải công cụ phân tích cảm xúc Gradio của bạn), sau đó nhắc bạn bắt đầu hội thoại.

<video controls autoplay loop>
  <source src="https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/tiny-agents/use-filesystem.mp4" type="video/mp4">
</video>

Mặc định, ví dụ của chúng ta kết nối với hai máy chủ MCP:

- Máy chủ ["hệ thống file" chuẩn](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem) - có quyền truy cập vào Desktop của bạn
- Máy chủ [Playwright MCP](https://github.com/microsoft/playwright-mcp) - biết cách dùng trình duyệt Chromium trong môi trường sandbox

Bạn có thể dễ dàng thêm máy chủ phân tích cảm xúc Gradio của mình vào danh sách này như chúng ta sẽ minh họa sau.

> [!NOTE]
> Lưu ý: Hiện tại tất cả máy chủ MCP trong tiny agents đều là các tiến trình local (dù các máy chủ từ xa sẽ sớm được hỗ trợ). Điều này không bao gồm máy chủ Gradio của chúng ta chạy trên localhost:7860.

Đầu vào cho video đầu tiên là:

> write a haiku about the Hugging Face community and write it to a file named "hf.txt" on my Desktop

Giờ thử prompt liên quan đến duyệt Web:

> do a Web Search for HF inference providers on Brave Search and open the first 3 results

<video controls autoplay loop>
  <source src="https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/tiny-agents/brave-search.mp4" type="video/mp4">
</video>

Với công cụ phân tích cảm xúc Gradio đã kết nối, chúng ta có thể hỏi tương tự:
> analyze the sentiment of this review: "I absolutely loved the product, it exceeded all my expectations!"

### Mô hình và nhà cung cấp mặc định

Về cặp mô hình/nhà cung cấp, Agent mẫu của chúng ta mặc định dùng:
- ["Qwen/Qwen2.5-72B-Instruct"](https://huggingface.co/Qwen/Qwen2.5-72B-Instruct)
- chạy trên [Nebius](https://huggingface.co/docs/inference-providers/providers/nebius)

Tất cả cài đặt này đều có thể tùy chỉnh qua biến môi trường! Ở đây, chúng ta cũng sẽ hướng dẫn cách thêm máy chủ Gradio MCP của mình:

```ts
const agent = new Agent({
	provider: process.env.PROVIDER ?? "nebius",
	model: process.env.MODEL_ID ?? "Qwen/Qwen2.5-72B-Instruct",
	apiKey: process.env.HF_TOKEN,
	servers: [
		// Các máy chủ mặc định
		{
			command: "npx",
			args: ["@modelcontextprotocol/servers", "filesystem"]
		},
		{
			command: "npx",
			args: ["playwright-mcp"]
		},
		// Máy chủ phân tích cảm xúc Gradio của chúng ta
		{
			command: "npx",
			args: [
				"mcp-remote",
				"http://localhost:7860/gradio_api/mcp/sse"
			]
		}
	],
});
```

<Tip>

Chúng ta kết nối tới máy chủ MCP dựa trên Gradio thông qua gói [`mcp-remote`](https://www.npmjs.com/package/mcp-remote).

</Tip>


## Nền tảng cho điều này: hỗ trợ gọi công cụ native trong LLMs

Điều giúp kết nối các máy chủ MCP Gradio với Tiny Agent của chúng ta là các LLM (cả closed và open) gần đây đã được huấn luyện để gọi hàm (function calling), hay còn gọi là sử dụng công cụ. Chính khả năng này hỗ trợ tích hợp của chúng ta với công cụ phân tích cảm xúc mà chúng ta đã xây dựng bằng Gradio.

Một công cụ được định nghĩa bởi tên, mô tả và biểu diễn JSONSchema của các tham số - giống hệt cách chúng ta định nghĩa hàm phân tích cảm xúc trong máy chủ Gradio. Hãy xem một ví dụ đơn giản:

<details>
<summary>Bấm để xem bản dịch tiếng Việt</summary>
```ts
const weatherTool = {
	type: "function",
	function: {
		name: "get_weather",
		description: "Nhận nhiệt độ hiện tại cho một địa điểm cụ thể.",
		parameters: {
			type: "object",
			properties: {
				location: {
					type: "string",
					description: "Thành phố và quốc gia, ví dụ: Hà Nội, Việt Nam",
				},
			},
		},
	},
};
```
</details>

```ts
const weatherTool = {
	type: "function",
	function: {
		name: "get_weather",
		description: "Get current temperature for a given location.",
		parameters: {
			type: "object",
			properties: {
				location: {
					type: "string",
					description: "City and country e.g. Bogotá, Colombia",
				},
			},
		},
	},
};
```

Công cụ phân tích cảm xúc Gradio của chúng ta sẽ có cấu trúc tương tự, với `text` làm tham số đầu vào thay vì `location`.

Tài liệu chính thức mà mình sẽ liên kết ở đây là [tài liệu function calling của OpenAI](https://platform.openai.com/docs/guides/function-calling?api-mode=chat). (Đúng vậy... OpenAI gần như định nghĩa các tiêu chuẩn LLM cho cả cộng đồng 😅).

Các inference engine cho phép bạn truyền một danh sách công cụ khi gọi LLM, và LLM có thể tự do gọi không, một hoặc nhiều công cụ trong số đó.
Là một developer, bạn chạy các công cụ và đưa kết quả của chúng trở lại LLM để tiếp tục quá trình sinh kết quả.

> Lưu ý rằng ở backend (ở cấp độ inference engine), các công cụ đơn giản được truyền vào mô hình trong một `chat_template` được định dạng đặc biệt, giống như bất kỳ tin nhắn nào khác, sau đó được phân tích từ phản hồi (sử dụng các token đặc biệt của mô hình) để hiển thị dưới dạng các lệnh gọi công cụ.

## Triển khai MCP client trên InferenceClient

Giờ chúng ta đã biết tool là gì trong các LLM hiện đại, hãy cùng triển khai MCP client thực tế để giao tiếp với Gradio server và các MCP server khác.

Tài liệu chính thức tại https://modelcontextprotocol.io/quickstart/client khá chi tiết. Bạn chỉ cần thay thế mọi đề cập đến SDK client Anthropic bằng bất kỳ SDK client tương thích OpenAI nào khác. (Có một file [llms.txt](https://modelcontextprotocol.io/llms-full.txt) bạn có thể dùng để huấn luyện LLM của mình hỗ trợ viết code).

Nhắc lại, chúng ta dùng `InferenceClient` của HF cho inference client.

> [!TIP]
> File code hoàn chỉnh `McpClient.ts` có tại [đây](https://github.com/huggingface/huggingface.js/blob/main/packages/mcp-client/src/McpClient.ts) nếu bạn muốn xem code thực tế 🤓

Lớp `McpClient` của chúng ta có:
- Một Inference Client (hoạt động với mọi Nhà cung cấp Inference, và `huggingface/inference` hỗ trợ cả endpoint từ xa lẫn local)
- Một tập hợp các phiên MCP client, mỗi phiên cho một MCP server được kết nối (cho phép kết nối đến nhiều server, bao gồm cả Gradio server của chúng ta)
- Danh sách các tool khả dụng sẽ được điền từ các server đã kết nối và định dạng lại một chút.

```ts
export class McpClient {
	protected client: InferenceClient;
	protected provider: string;
	protected model: string;
	private clients: Map<ToolName, Client> = new Map();
	public readonly availableTools: ChatCompletionInputTool[] = [];

	constructor({ provider, model, apiKey }: { provider: InferenceProvider; model: string; apiKey: string }) {
		this.client = new InferenceClient(apiKey);
		this.provider = provider;
		this.model = model;
	}
	
	// [...]
}
```

Để kết nối đến MCP server (như Gradio server phân tích cảm xúc của chúng ta), SDK TypeScript chính thức `@modelcontextprotocol/sdk/client` cung cấp lớp `Client` với phương thức `listTools()`:

```ts
async addMcpServer(server: StdioServerParameters): Promise<void> {
	const transport = new StdioClientTransport({
		...server,
		env: { ...server.env, PATH: process.env.PATH ?? "" },
	});
	const mcp = new Client({ name: "@huggingface/mcp-client", version: packageVersion });
	await mcp.connect(transport);

	const toolsResult = await mcp.listTools();
	debug(
		"Connected to server with tools:",
		toolsResult.tools.map(({ name }) => name)
	);

	for (const tool of toolsResult.tools) {
		this.clients.set(tool.name, mcp);
	}

	this.availableTools.push(
		...toolsResult.tools.map((tool) => {
			return {
				type: "function",
				function: {
					name: tool.name,
					description: tool.description,
					parameters: tool.inputSchema,
				},
			} satisfies ChatCompletionInputTool;
		})
	);
}
```

`StdioServerParameters` là một interface từ MCP SDK giúp bạn dễ dàng tạo một process local: như đã đề cập, hiện tại tất cả MCP server đều là các process local, bao gồm cả Gradio server của chúng ta (dù chúng ta truy cập qua HTTP).

Với mỗi MCP server được kết nối (bao gồm Gradio server phân tích cảm xúc), chúng ta định dạng lại danh sách tool của nó và thêm vào `this.availableTools`.

### Cách sử dụng các công cụ

Sử dụng công cụ phân tích cảm xúc của chúng ta (hoặc bất kỳ công cụ MCP nào khác) rất đơn giản. Bạn chỉ cần truyền `this.availableTools` vào LLM chat-completion, cùng với mảng messages thông thường:

```ts
const stream = this.client.chatCompletionStream({
	provider: this.provider,
	model: this.model,
	messages,
	tools: this.availableTools,
	tool_choice: "auto",
});
```

`tool_choice: "auto"` là tham số bạn truyền để LLM có thể tạo ra không, một hoặc nhiều lệnh gọi công cụ.

Khi phân tích hoặc stream kết quả, LLM sẽ tạo ra các lệnh gọi công cụ (ví dụ: tên hàm và các đối số được mã hóa JSON) mà bạn (với tư cách là nhà phát triển) cần xử lý. SDK MCP Client một lần nữa giúp việc này trở nên dễ dàng; nó có phương thức `client.callTool()`:

```ts
const toolName = toolCall.function.name;
const toolArgs = JSON.parse(toolCall.function.arguments);

const toolMessage: ChatCompletionInputMessageTool = {
	role: "tool",
	tool_call_id: toolCall.id,
	content: "",
	name: toolName,
};

/// Lấy session phù hợp cho công cụ này
const client = this.clients.get(toolName);
if (client) {
	const result = await client.callTool({ name: toolName, arguments: toolArgs });
	toolMessage.content = result.content[0].text;
} else {
	toolMessage.content = `Error: No session found for tool: ${toolName}`;
}
```

Nếu LLM chọn sử dụng công cụ phân tích cảm xúc của chúng ta, đoạn code này sẽ tự động định tuyến lệnh gọi đến Gradio server của chúng ta, thực thi phân tích và trả về kết quả cho LLM.

Cuối cùng, bạn sẽ thêm message công cụ kết quả vào mảng `messages` và đưa ngược lại vào LLM.

## Agent 50-dòng-code của chúng ta 🤯

Giờ đây khi đã có MCP client có khả năng kết nối đến các MCP server tùy ý (bao gồm cả Gradio sentiment analysis server) để lấy danh sách công cụ và chèn chúng vào LLM inference, vậy... Agent là gì?

> Khi bạn đã có một inference client với một bộ công cụ, thì Agent chỉ đơn giản là một vòng lặp while bao quanh nó.

Cụ thể hơn, Agent là sự kết hợp của:
- một system prompt
- một LLM Inference client
- một MCP client để kết nối các công cụ từ nhiều MCP server (bao gồm Gradio server của chúng ta)
- một số luồng điều khiển cơ bản (xem vòng lặp while bên dưới)

> [!TIP]
> File code hoàn chỉnh `Agent.ts` có tại [đây](https://github.com/huggingface/huggingface.js/blob/main/packages/mcp-client/src/Agent.ts).

Lớp Agent của chúng ta đơn giản kế thừa từ McpClient:

```ts
export class Agent extends McpClient {
	private readonly servers: StdioServerParameters[];
	protected messages: ChatCompletionInputMessage[];

	constructor({
		provider,
		model,
		apiKey,
		servers,
		prompt,
	}: {
		provider: InferenceProvider;
		model: string;
		apiKey: string;
		servers: StdioServerParameters[];
		prompt?: string;
	}) {
		super({ provider, model, apiKey });
		this.servers = servers;
		this.messages = [
			{
				role: "system",
				content: prompt ?? DEFAULT_SYSTEM_PROMPT,
			},
		];
	}
}
```

Mặc định, chúng ta sử dụng system prompt đơn giản lấy cảm hứng từ [hướng dẫn prompt GPT-4.1](https://cookbook.openai.com/examples/gpt4-1_prompting_guide).

Mặc dù điều này đến từ OpenAI 😈, nhưng câu này đặc biệt áp dụng cho ngày càng nhiều mô hình, cả đóng và mở:

> Chúng tôi khuyến khích nhà phát triển chỉ sử dụng trường tools để truyền công cụ, thay vì thủ công chèn mô tả công cụ vào prompt và viết parser riêng cho lệnh gọi công cụ như một số đã làm trước đây.

Nghĩa là chúng ta không cần cung cấp danh sách ví dụ về cách sử dụng công cụ được định dạng kỹ lưỡng trong prompt. Tham số `tools: this.availableTools` là đủ, và LLM sẽ biết cách sử dụng cả công cụ hệ thống file và công cụ phân tích cảm xúc Gradio của chúng ta.

Việc tải công cụ lên Agent đơn giản chỉ là kết nối đến các MCP server mong muốn (song song vì rất dễ thực hiện trong JS):

```ts
async loadTools(): Promise<void> {
	await Promise.all(this.servers.map((s) => this.addMcpServer(s)));
}
```

Chúng ta thêm hai công cụ bổ sung (ngoài MCP) mà LLM có thể sử dụng cho luồng điều khiển của Agent:

```ts
const taskCompletionTool: ChatCompletionInputTool = {
	type: "function",
	function: {
		name: "task_complete",
		description: "Call this tool when the task given by the user is complete",
		parameters: {
			type: "object",
			properties: {},
		},
	},
};
const askQuestionTool: ChatCompletionInputTool = {
	type: "function",
	function: {
		name: "ask_question",
		description: "Ask a question to the user to get more info required to solve or clarify their problem.",
		parameters: {
			type: "object",
			properties: {},
		},
	},
};
const exitLoopTools = [taskCompletionTool, askQuestionTool];
```

Khi gọi bất kỳ công cụ nào trong số này, Agent sẽ ngắt vòng lặp và trả lại quyền kiểm soát cho người dùng để có dữ liệu đầu vào mới.

### Vòng lặp while hoàn chỉnh

Hãy xem vòng lặp while hoàn chỉnh của chúng tôi.🎉

Điểm mấu chốt của vòng lặp while chính của Agent là chúng tôi chỉ lặp lại với LLM luân phiên giữa việc gọi công cụ và cung cấp cho nó kết quả công cụ, và chúng tôi làm như vậy **cho đến khi LLM bắt đầu phản hồi bằng hai thông báo không phải công cụ liên tiếp**.

Đây là vòng lặp while hoàn chỉnh:

```ts
let numOfTurns = 0;
let nextTurnShouldCallTools = true;
while (true) {
	try {
		yield* this.processSingleTurnWithTools(this.messages, {
			exitLoopTools,
			exitIfFirstChunkNoTool: numOfTurns > 0 && nextTurnShouldCallTools,
			abortSignal: opts.abortSignal,
		});
	} catch (err) {
		if (err instanceof Error && err.message === "AbortError") {
			return;
		}
		throw err;
	}
	numOfTurns++;
	const currentLast = this.messages.at(-1)!;
	if (
		currentLast.role === "tool" &&
		currentLast.name &&
		exitLoopTools.map((t) => t.function.name).includes(currentLast.name)
	) {
		return;
	}
	if (currentLast.role !== "tool" && numOfTurns > MAX_NUM_TURNS) {
		return;
	}
	if (currentLast.role !== "tool" && nextTurnShouldCallTools) {
		return;
	}
	if (currentLast.role === "tool") {
		nextTurnShouldCallTools = false;
	} else {
		nextTurnShouldCallTools = true;
	}
}
```

## Kết nối Tiny Agents với Gradio MCP Servers

Giờ thì chúng ta đã hiểu về cả Tiny Agents và Gradio MCP servers, hãy xem cách chúng hoạt động cùng nhau nhé! Điểm tuyệt vời của MCP là nó cung cấp cách chuẩn hóa để các agent tương tác với bất kỳ server nào tương thích MCP, bao gồm cả máy chủ phân tích cảm xúc (sentiment analysis) dựa trên Gradio của chúng ta.

### Sử dụng Gradio Server với Tiny Agents

Để kết nối Tiny Agent của chúng ta với máy chủ phân tích cảm xúc Gradio đã xây dựng trước đó, chúng ta chỉ cần thêm nó vào danh sách servers. Dưới đây là cách chúng ta có thể điều chỉnh cấu hình agent:

```ts
const agent = new Agent({
    provider: process.env.PROVIDER ?? "nebius",
    model: process.env.MODEL_ID ?? "Qwen/Qwen2.5-72B-Instruct",
    apiKey: process.env.HF_TOKEN,
    servers: [
        // ... existing servers ...
        {
            command: "npx",
            args: [
                "mcp-remote",
                "http://localhost:7860/gradio_api/mcp/sse"  // Your Gradio MCP server
            ]
        }
    ],
});
```

Giờ đây agent của chúng ta đã có thể sử dụng công cụ phân tích cảm xúc cùng với các công cụ khác! Ví dụ, nó có thể:
1. Đọc văn bản từ file bằng filesystem server
2. Phân tích cảm xúc bằng Gradio server của chúng ta
3. Ghi kết quả trở lại file

### Ví dụ tương tác

Đây là ví dụ về cuộc hội thoại với agent:

```
User: Read the file "feedback.txt" from my Desktop and analyze its sentiment

Agent: I'll help you analyze the sentiment of the feedback file. Let me break this down into steps:

1. First, I'll read the file using the filesystem tool
2. Then, I'll analyze its sentiment using the sentiment analysis tool
3. Finally, I'll write the results to a new file

[Agent tiến hành sử dụng các công cụ và cung cấp phân tích]
```

### Lưu ý khi triển khai

Khi triển khai Gradio MCP server của bạn lên Hugging Face Spaces, bạn cần cập nhật URL server trong cấu hình agent để trỏ tới space đã triển khai:

```ts
{
    command: "npx",
    args: [
        "mcp-remote",
        "https://YOUR_USERNAME-mcp-sentiment.hf.space/gradio_api/mcp/sse"
    ]
}
```

Cách này cho phép agent của bạn sử dụng công cụ phân tích cảm xúc từ bất kỳ đâu, không chỉ trên local!
````

## File: units/vi/unit3/introduction.mdx
````
# Sắp ra mắt

Đây sẽ là một trường hợp sử dụng khác đi sâu hơn vào giao thức MCP và cách sử dụng nó theo những phương pháp phức tạp hơn.
````

## File: units/vi/unit4/introduction.mdx
````
# Sắp ra mắt

Chương này sẽ là sự hợp tác với các đối tác từ cộng đồng AI.

Nếu các bạn đang xây dựng công cụ MCP, hãy liên hệ với chúng mình để được thêm vào chương. Mở [thảo luận](https://huggingface.co/spaces/mcp-course/README/discussions) trên hub.
````

## File: units/vi/_toctree.yml
````yaml
- title: "0. Chào mừng đến với Khóa học MCP"
  sections:
  - local: unit0/introduction
    title: Chào mừng đến với Khóa học MCP
    
- title: "1. Giới thiệu về Giao Thức Ngữ Cảnh Mô Hình (MCP)"
  sections:
  - local: unit1/introduction
    title: Giới thiệu về Giao Thức Ngữ Cảnh Mô Hình (MCP)
  - local: unit1/key-concepts
    title: Khái niệm và Thuật ngữ chính
  - local: unit1/architectural-components
    title: Các thành phần kiến trúc
  - local: unit1/communication-protocol
    title: Giao thức truyền thông
  - local: unit1/capabilities
    title: Hiểu về khả năng của MCP
  - local: unit1/sdk
    title: MCP SDK
  - local: unit1/mcp-clients
    title: MCP Clients
  - local: unit1/gradio-mcp
    title: Tích hợp Gradio với MCP

- title: "2. Trường hợp sử dụng: Ứng dụng MCP đầu cuối"
  sections:
  - local: unit2/introduction
    title: Giới thiệu về Xây dựng Ứng dụng MCP
  - local: unit2/gradio-server
    title: Xây dựng Máy chủ Gradio MCP
  - local: unit2/clients
    title: Sử dụng MCP Clients với ứng dụng của bạn
  - local: unit2/gradio-client
    title: Xây dựng MCP Clients bằng Gradio
  - local: unit2/tiny-agents
    title: Xây dựng Tiny Agent với TypeScript

- title: "3. Trường hợp sử dụng: Phát triển MCP Nâng cao"
  sections:
  - local: unit3/introduction
    title: Sắp ra mắt

- title: "Các chương bổ trợ"
  sections:
  - local: unit4/introduction
    title: Sắp ra mắt
````

## File: .python-version
````
3.12
````

## File: hello.py
````python
def main():
    print("Hello from mcp-course!")


if __name__ == "__main__":
    main()
````

## File: LICENSE
````
Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright [yyyy] [name of copyright owner]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
````

## File: pyproject.toml
````toml
[project]
name = "mcp-course"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.12"
dependencies = []
````

## File: README_vi.md
````markdown
# Khóa Học Về Model Context Protocol (MCP)

<div align="center"> <a href="README.md">🇺🇸 English</a> | <a href="README_vi.md">🇻🇳 Tiếng Việt</a> </div>

![1](https://github.com/user-attachments/assets/d26dcc5e-46cb-449e-aecb-49ece10d342a)

Nếu bạn thích khóa học này, **đừng ngần ngại đánh dấu ⭐ cho repo này**. Điều này giúp chúng ta **làm cho khóa học trở nên phổ biến hơn 🤗**.

<img src="https://huggingface.co/datasets/agents-course/course-images/resolve/main/en/communication/please_star.gif" alt="Đánh dấu sao cho kho lưu trữ" />

## Nội dung

Khóa học được chia thành 4 phần. Những phần này sẽ đưa bạn từ **những kiến thức cơ bản về Model Context Protocol đến một dự án cuối cùng triển khai MCP trong ứng dụng AI**.

Đăng ký tại đây (miễn phí) 👉 [Sắp ra mắt]

Bạn có thể truy cập khóa học tại đây 👉 [Sắp ra mắt]

| Phần    | Chủ đề                                              | Mô tả                                                                                                 |
| ------- | --------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| 0       | Chào mừng đến với Khóa học                          | Lời chào mừng, hướng dẫn, công cụ cần thiết và tổng quan về khóa học.                                |
| 1       | Giới thiệu về Model Context Protocol                | Định nghĩa của MCP, các khái niệm chính và vai trò của nó trong việc kết nối mô hình AI với dữ liệu  |
| 2       | Xây dựng với MCP: Phát triển thực tế                | Học cách triển khai MCP client và server sử dụng SDK và framework có sẵn.                            |

## Điều kiện tiên quyết

* Hiểu biết cơ bản về AI và các khái niệm LLM
* Quen thuộc với nguyên tắc phát triển phần mềm và khái niệm API
* Có kinh nghiệm với ít nhất một ngôn ngữ lập trình (các ví dụ sẽ tập trung vào Python hoặc TypeScript)

## Hướng dẫn đóng góp

Nếu bạn muốn đóng góp cho khóa học này, hoan nghênh các bạn. Vui lòng mở issue hoặc gửi pull request. Đối với những đóng góp cụ thể, dưới đây là một số hướng dẫn:

### Sửa lỗi chính tả và ngữ pháp nhỏ

Nếu bạn tìm thấy lỗi chính tả hoặc lỗi ngữ pháp nhỏ, vui lòng tự sửa và gửi pull request. Điều này rất hữu ích cho học viên.

### Phần mới

Nếu bạn muốn thêm một phần mới, **vui lòng tạo một issue trong kho lưu trữ, mô tả phần đó và lý do tại sao nên thêm vào**. Chúng tôi sẽ thảo luận và nếu đó là một bổ sung tốt, chúng ta có thể cộng tác để thực hiện.

## Trích dẫn dự án

Để trích dẫn kho lưu trữ này trong các ấn phẩm:

```
@misc{mcp-course,
  author = {Your Name},
  title = {The Model Context Protocol Course},
  year = {2025},
  howpublished = {\url{https://github.com/yourusername/mcp-course}},
  note = {GitHub repository},
}
```
````

## File: requirements.txt
````
certifi==2025.6.15
cffi==1.17.1
numpy==2.3.0
pillow==11.2.1
pycparser==2.22
scipy==1.15.3
wheel==0.45.1
attrs==25.3.0
black==25.1.0
certifi==2025.6.15
charset-normalizer==3.4.2
click==8.2.1
fastjsonschema==2.21.1
filelock==3.18.0
fsspec==2025.5.1
gitdb==4.0.12
gitpython==3.1.44
hf-doc-builder==0.5.0
hf-xet==1.1.5
huggingface-hub==0.33.0
idna==3.10
jsonschema==4.24.0
jsonschema-specifications==2025.4.1
jupyter-core==5.8.1
markdown==3.8.2
mdx-truly-sane-lists==1.3
mypy-extensions==1.1.0
nbformat==5.10.4
packaging==25.0
pathspec==0.12.1
platformdirs==4.3.8
pyyaml==6.0.2
referencing==0.36.2
requests==2.32.4
rpds-py==0.25.1
smmap==5.0.2
tqdm==4.67.1
traitlets==5.14.3
typing-extensions==4.14.0
urllib3==2.5.0
````

## File: projects/unit3/build-mcp-server/starter/test_server.py
````python
#!/usr/bin/env python3
"""
Unit tests for Module 1: Basic MCP Server
Run these tests to validate your implementation
"""

import json
import pytest
import asyncio
from pathlib import Path
from unittest.mock import patch, MagicMock

# Import your implemented functions
try:
    from server import (
        mcp,
        analyze_file_changes,
        get_pr_templates,
        suggest_template
    )
    IMPORTS_SUCCESSFUL = True
except ImportError as e:
    IMPORTS_SUCCESSFUL = False
    IMPORT_ERROR = str(e)


class TestImplementation:
    """Test that the required functions are implemented."""
    
    def test_imports(self):
        """Test that all required functions can be imported."""
        assert IMPORTS_SUCCESSFUL, f"Failed to import required functions: {IMPORT_ERROR if not IMPORTS_SUCCESSFUL else ''}"
        assert mcp is not None, "FastMCP server instance not found"
        assert callable(analyze_file_changes), "analyze_file_changes should be a callable function"
        assert callable(get_pr_templates), "get_pr_templates should be a callable function"
        assert callable(suggest_template), "suggest_template should be a callable function"


@pytest.mark.skipif(not IMPORTS_SUCCESSFUL, reason="Imports failed")
class TestAnalyzeFileChanges:
    """Test the analyze_file_changes tool."""
    
    @pytest.mark.asyncio
    async def test_returns_json_string(self):
        """Test that analyze_file_changes returns a JSON string."""
        with patch('subprocess.run') as mock_run:
            mock_run.return_value = MagicMock(stdout="", stderr="")
            
            result = await analyze_file_changes()
            
            assert isinstance(result, str), "Should return a string"
            # Should be valid JSON
            data = json.loads(result)
            assert isinstance(data, dict), "Should return a JSON object"
    
    @pytest.mark.asyncio
    async def test_includes_required_fields(self):
        """Test that the result includes expected fields."""
        with patch('subprocess.run') as mock_run:
            mock_run.return_value = MagicMock(stdout="M\tfile1.py\n", stderr="")
            
            result = await analyze_file_changes()
            data = json.loads(result)
            
            # For starter code, accept error messages; for full implementation, expect data
            is_implemented = not ("error" in data and "Not implemented" in str(data.get("error", "")))
            if is_implemented:
                # Check for some expected fields (flexible to allow different implementations)
                assert any(key in data for key in ["files_changed", "files", "changes", "diff"]), \
                    "Result should include file change information"
            else:
                # Starter code - just verify it returns something structured
                assert isinstance(data, dict), "Should return a JSON object even if not implemented"


@pytest.mark.skipif(not IMPORTS_SUCCESSFUL, reason="Imports failed")
class TestGetPRTemplates:
    """Test the get_pr_templates tool."""
    
    @pytest.mark.asyncio
    async def test_returns_json_string(self):
        """Test that get_pr_templates returns a JSON string."""
        result = await get_pr_templates()
        
        assert isinstance(result, str), "Should return a string"
        # Should be valid JSON
        data = json.loads(result)
        
        # For starter code, accept error messages; for full implementation, expect list
        is_implemented = not ("error" in data and isinstance(data, dict))
        if is_implemented:
            assert isinstance(data, list), "Should return a JSON array of templates"
        else:
            # Starter code - just verify it returns something structured
            assert isinstance(data, dict), "Should return a JSON object even if not implemented"
    
    @pytest.mark.asyncio
    async def test_returns_templates(self):
        """Test that templates are returned."""
        result = await get_pr_templates()
        templates = json.loads(result)
        
        # For starter code, accept error messages; for full implementation, expect templates
        is_implemented = not ("error" in templates and isinstance(templates, dict))
        if is_implemented:
            assert len(templates) > 0, "Should return at least one template"
            
            # Check that templates have expected structure
            for template in templates:
                assert isinstance(template, dict), "Each template should be a dictionary"
                # Should have some identifying information
                assert any(key in template for key in ["filename", "name", "type", "id"]), \
                    "Templates should have an identifier"
        else:
            # Starter code - just verify it's structured correctly
            assert isinstance(templates, dict), "Should return structured error for starter code"


@pytest.mark.skipif(not IMPORTS_SUCCESSFUL, reason="Imports failed")
class TestSuggestTemplate:
    """Test the suggest_template tool."""
    
    @pytest.mark.asyncio
    async def test_returns_json_string(self):
        """Test that suggest_template returns a JSON string."""
        result = await suggest_template(
            "Fixed a bug in the authentication system",
            "bug"
        )
        
        assert isinstance(result, str), "Should return a string"
        # Should be valid JSON
        data = json.loads(result)
        assert isinstance(data, dict), "Should return a JSON object"
    
    @pytest.mark.asyncio
    async def test_suggestion_structure(self):
        """Test that the suggestion has expected structure."""
        result = await suggest_template(
            "Added new feature for user management",
            "feature"
        )
        suggestion = json.loads(result)
        
        # For starter code, accept error messages; for full implementation, expect suggestion
        is_implemented = not ("error" in suggestion and "Not implemented" in str(suggestion.get("error", "")))
        if is_implemented:
            # Check for some expected fields (flexible to allow different implementations)
            assert any(key in suggestion for key in ["template", "recommended_template", "suggestion"]), \
                "Should include a template recommendation"
        else:
            # Starter code - just verify it's structured correctly
            assert isinstance(suggestion, dict), "Should return structured error for starter code"


@pytest.mark.skipif(not IMPORTS_SUCCESSFUL, reason="Imports failed")
class TestToolRegistration:
    """Test that tools are properly registered with FastMCP."""
    
    def test_tools_have_decorators(self):
        """Test that tool functions are decorated with @mcp.tool()."""
        # In FastMCP, decorated functions should have certain attributes
        # This is a basic check that functions exist and are callable
        assert hasattr(analyze_file_changes, '__name__'), \
            "analyze_file_changes should be a proper function"
        assert hasattr(get_pr_templates, '__name__'), \
            "get_pr_templates should be a proper function"
        assert hasattr(suggest_template, '__name__'), \
            "suggest_template should be a proper function"


if __name__ == "__main__":
    if not IMPORTS_SUCCESSFUL:
        print(f"❌ Cannot run tests - imports failed: {IMPORT_ERROR}")
        print("\nMake sure you've:")
        print("1. Implemented all three tool functions")
        print("2. Decorated them with @mcp.tool()")
        print("3. Installed dependencies with: uv sync")
        exit(1)
    
    # Run tests
    pytest.main([__file__, "-v"])
````

## File: projects/unit3/build-mcp-server/starter/validate_starter.py
````python
#!/usr/bin/env python3
"""
Validation script for Module 1 starter code
Ensures the starter template is ready for learners to implement
"""

import subprocess
import sys
import os
from pathlib import Path

def test_project_structure():
    """Check that all required files exist."""
    print("Project Structure:")
    required_files = [
        "server.py",
        "pyproject.toml",
        "README.md"
    ]
    
    all_exist = True
    for file in required_files:
        if Path(file).exists():
            print(f"  ✓ {file} exists")
        else:
            print(f"  ✗ {file} missing")
            all_exist = False
    
    return all_exist

def test_imports():
    """Test that the starter code imports work."""
    try:
        # Test importing the server module
        import server
        print("✓ server.py imports successfully")
        
        # Check that FastMCP is imported
        if hasattr(server, 'mcp'):
            print("✓ FastMCP server instance found")
        else:
            print("✗ FastMCP server instance not found")
            return False
            
        return True
    except ImportError as e:
        print(f"✗ Import error: {e}")
        print("  Please ensure you've installed dependencies: uv sync")
        return False

def test_todos():
    """Check that TODO comments exist for learners."""
    print("\nTODO Comments:")
    
    with open("server.py", "r") as f:
        content = f.read()
    
    todos = []
    for i, line in enumerate(content.split('\n'), 1):
        if 'TODO' in line:
            todos.append((i, line.strip()))
    
    if todos:
        print(f"✓ Found {len(todos)} TODO comments for learners:")
        for line_no, todo in todos[:5]:  # Show first 5
            print(f"  Line {line_no}: {todo[:60]}...")
        if len(todos) > 5:
            print(f"  ... and {len(todos) - 5} more")
        return True
    else:
        print("✗ No TODO comments found - learners need guidance!")
        return False

def test_starter_runs():
    """Test that the starter code can at least be executed."""
    print("\nExecution Test:")
    
    try:
        # Try to import and check if server can be initialized
        import server
        # If we can import it and it has the right attributes, it should run
        if hasattr(server, 'mcp') and hasattr(server, 'analyze_file_changes'):
            print("✓ Server imports and initializes correctly")
            return True
        else:
            print("✗ Server missing required components")
            return False
        
    except Exception as e:
        print(f"✗ Failed to initialize server: {e}")
        return False

def test_dependencies():
    """Check that pyproject.toml is properly configured."""
    print("\nDependencies:")
    
    try:
        import tomllib
    except ImportError:
        import tomli as tomllib
    
    try:
        with open("pyproject.toml", "rb") as f:
            config = tomllib.load(f)
        
        # Check for required sections
        if "project" in config and "dependencies" in config["project"]:
            deps = config["project"]["dependencies"]
            print(f"✓ Found {len(deps)} dependencies")
            for dep in deps:
                print(f"  - {dep}")
        else:
            print("✗ No dependencies section found")
            return False
            
        return True
    except Exception as e:
        print(f"✗ Error reading pyproject.toml: {e}")
        return False

def test_no_implementation():
    """Ensure starter code doesn't contain the solution."""
    print("\nImplementation Check:")
    
    with open("server.py", "r") as f:
        content = f.read()
    
    # Check that tool functions are not implemented
    solution_indicators = [
        "subprocess.run",  # Git commands
        "json.dumps",      # Returning JSON
        "git diff",        # Git operations
        "template",        # Template logic
    ]
    
    found_implementations = []
    for indicator in solution_indicators:
        if indicator in content.lower():
            found_implementations.append(indicator)
    
    if found_implementations:
        print(f"⚠️  Found possible solution code: {', '.join(found_implementations)}")
        print("   Make sure these are only in comments/examples")
        return True  # Warning, not failure
    else:
        print("✓ No solution implementation found (good!)")
        return True

def main():
    """Run all validation checks."""
    print("Module 1 Starter Code Validation")
    print("=" * 50)
    
    # Change to starter directory if needed
    if Path("validate_starter.py").exists():
        os.chdir(Path("validate_starter.py").parent)
    
    tests = [
        ("Project Structure", test_project_structure),
        ("Python Imports", test_imports),
        ("TODO Comments", test_todos),
        ("Starter Execution", test_starter_runs),
        ("Dependencies", test_dependencies),
        ("Clean Starter", test_no_implementation)
    ]
    
    results = []
    for test_name, test_func in tests:
        print(f"\n{test_name}:")
        try:
            results.append(test_func())
        except Exception as e:
            print(f"✗ Test failed with error: {e}")
            results.append(False)
    
    print("\n" + "=" * 50)
    passed = sum(results)
    total = len(results)
    print(f"Checks passed: {passed}/{total}")
    
    if passed == total:
        print("\n✓ Starter code is ready for learners!")
        print("\nLearners should:")
        print("1. Run: uv sync")
        print("2. Follow the TODO comments in server.py")
        print("3. Test with: uv run pytest test_server.py")
        print("4. Configure Claude Desktop when ready")
    else:
        print("\n✗ Some checks failed. Please review the starter code.")
        sys.exit(1)

if __name__ == "__main__":
    main()
````

## File: projects/unit3/github-actions-integration/solution/test_server.py
````python
#!/usr/bin/env python3
"""
Unit tests for Module 1: Basic MCP Server
"""

import json
import pytest
import asyncio
from pathlib import Path
from unittest.mock import patch, MagicMock, AsyncMock
from server import (
    mcp,
    analyze_file_changes,
    get_pr_templates,
    suggest_template,
    create_default_template,
    TEMPLATES_DIR
)


class TestAnalyzeFileChanges:
    """Test the analyze_file_changes tool."""
    
    @pytest.mark.asyncio
    async def test_analyze_with_diff(self):
        """Test analyzing changes with full diff included."""
        mock_result = MagicMock()
        mock_result.stdout = "M\tfile1.py\nA\tfile2.py\n"
        mock_result.stderr = ""
        
        with patch('subprocess.run') as mock_run:
            mock_run.return_value = mock_result
            
            result = await analyze_file_changes("main", include_diff=True)
            
            assert isinstance(result, str)
            data = json.loads(result)
            assert data["base_branch"] == "main"
            assert "files_changed" in data
            assert "statistics" in data
            assert "commits" in data
            assert "diff" in data
    
    @pytest.mark.asyncio
    async def test_analyze_without_diff(self):
        """Test analyzing changes without diff content."""
        mock_result = MagicMock()
        mock_result.stdout = "M\tfile1.py\n"
        
        with patch('subprocess.run') as mock_run:
            mock_run.return_value = mock_result
            
            result = await analyze_file_changes("main", include_diff=False)
            
            data = json.loads(result)
            assert "Diff not included" in data["diff"]
    
    @pytest.mark.asyncio
    async def test_analyze_git_error(self):
        """Test handling git command errors."""
        with patch('subprocess.run') as mock_run:
            mock_run.side_effect = Exception("Git not found")
            
            result = await analyze_file_changes("main", True)
            
            assert "Error:" in result


class TestPRTemplates:
    """Test PR template management."""
    
    @pytest.mark.asyncio
    async def test_get_templates(self, tmp_path, monkeypatch):
        """Test getting available templates."""
        # Use temporary directory for templates
        monkeypatch.setattr('server.TEMPLATES_DIR', tmp_path)
        
        result = await get_pr_templates()
        
        templates = json.loads(result)
        assert len(templates) > 0
        assert any(t["type"] == "Bug Fix" for t in templates)
        assert any(t["type"] == "Feature" for t in templates)
        assert all("content" in t for t in templates)
    
    def test_create_default_template(self, tmp_path):
        """Test creating default template files."""
        template_path = tmp_path / "test.md"
        
        create_default_template(template_path, "Bug Fix")
        
        assert template_path.exists()
        content = template_path.read_text()
        assert "## Bug Fix" in content
        assert "Description" in content
        assert "Root Cause" in content


class TestSuggestTemplate:
    """Test template suggestion based on analysis."""
    
    @pytest.mark.asyncio
    async def test_suggest_bug_fix(self, tmp_path, monkeypatch):
        """Test suggesting bug fix template."""
        monkeypatch.setattr('server.TEMPLATES_DIR', tmp_path)
        
        # Create templates first
        await get_pr_templates()
        
        result = await suggest_template(
            "Fixed null pointer exception in user service",
            "bug"
        )
        
        suggestion = json.loads(result)
        assert suggestion["recommended_template"]["filename"] == "bug.md"
        assert "Bug Fix" in suggestion["recommended_template"]["type"]
        assert "reasoning" in suggestion
    
    @pytest.mark.asyncio
    async def test_suggest_feature(self, tmp_path, monkeypatch):
        """Test suggesting feature template."""
        monkeypatch.setattr('server.TEMPLATES_DIR', tmp_path)
        
        await get_pr_templates()
        
        result = await suggest_template(
            "Added new authentication method for API",
            "feature"
        )
        
        suggestion = json.loads(result)
        assert suggestion["recommended_template"]["filename"] == "feature.md"
    
    @pytest.mark.asyncio
    async def test_suggest_with_type_variations(self, tmp_path, monkeypatch):
        """Test template suggestion with various type names."""
        monkeypatch.setattr('server.TEMPLATES_DIR', tmp_path)
        
        await get_pr_templates()
        
        # Test variations
        for change_type, expected_file in [
            ("fix", "bug.md"),
            ("enhancement", "feature.md"),
            ("documentation", "docs.md"),
            ("cleanup", "refactor.md"),
            ("testing", "test.md"),
            ("optimization", "performance.md")
        ]:
            result = await suggest_template(f"Some {change_type} work", change_type)
            suggestion = json.loads(result)
            assert suggestion["recommended_template"]["filename"] == expected_file


class TestIntegration:
    """Integration tests for the complete workflow."""
    
    @pytest.mark.asyncio
    async def test_full_workflow(self, tmp_path, monkeypatch):
        """Test the complete workflow from analysis to suggestion."""
        monkeypatch.setattr('server.TEMPLATES_DIR', tmp_path)
        
        # Mock git commands
        with patch('subprocess.run') as mock_run:
            mock_run.return_value = MagicMock(
                stdout="M\tsrc/main.py\nM\ttests/test_main.py\n",
                stderr=""
            )
            
            # 1. Analyze changes
            analysis_result = await analyze_file_changes("main", True)
            
            # 2. Get templates
            templates_result = await get_pr_templates()
            
            # 3. Suggest template based on analysis
            suggestion_result = await suggest_template(
                "Updated main functionality and added tests",
                "feature"
            )
            
            # Verify results
            assert all(isinstance(r, str) for r in [analysis_result, templates_result, suggestion_result])
            
            suggestion = json.loads(suggestion_result)
            assert "recommended_template" in suggestion
            assert "template_content" in suggestion
            assert suggestion["recommended_template"]["type"] == "Feature"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
````

## File: projects/unit3/github-actions-integration/starter/test_server.py
````python
#!/usr/bin/env python3
"""
Unit tests for Module 1: Basic MCP Server
Run these tests to validate your implementation
"""

import json
import pytest
import asyncio
from pathlib import Path
from unittest.mock import patch, MagicMock

# Import your implemented functions
try:
    from server import (
        mcp,
        analyze_file_changes,
        get_pr_templates,
        suggest_template
    )
    IMPORTS_SUCCESSFUL = True
except ImportError as e:
    IMPORTS_SUCCESSFUL = False
    IMPORT_ERROR = str(e)


class TestImplementation:
    """Test that the required functions are implemented."""
    
    def test_imports(self):
        """Test that all required functions can be imported."""
        assert IMPORTS_SUCCESSFUL, f"Failed to import required functions: {IMPORT_ERROR if not IMPORTS_SUCCESSFUL else ''}"
        assert mcp is not None, "FastMCP server instance not found"
        assert callable(analyze_file_changes), "analyze_file_changes should be a callable function"
        assert callable(get_pr_templates), "get_pr_templates should be a callable function"
        assert callable(suggest_template), "suggest_template should be a callable function"


@pytest.mark.skipif(not IMPORTS_SUCCESSFUL, reason="Imports failed")
class TestAnalyzeFileChanges:
    """Test the analyze_file_changes tool."""
    
    @pytest.mark.asyncio
    async def test_returns_json_string(self):
        """Test that analyze_file_changes returns a JSON string."""
        with patch('subprocess.run') as mock_run:
            mock_run.return_value = MagicMock(stdout="", stderr="")
            
            result = await analyze_file_changes()
            
            assert isinstance(result, str), "Should return a string"
            # Should be valid JSON
            data = json.loads(result)
            assert isinstance(data, dict), "Should return a JSON object"
    
    @pytest.mark.asyncio
    async def test_includes_required_fields(self):
        """Test that the result includes expected fields."""
        with patch('subprocess.run') as mock_run:
            mock_run.return_value = MagicMock(stdout="M\tfile1.py\n", stderr="")
            
            result = await analyze_file_changes()
            data = json.loads(result)
            
            # Check for some expected fields (flexible to allow different implementations)
            assert any(key in data for key in ["files_changed", "files", "changes", "diff"]), \
                "Result should include file change information"


@pytest.mark.skipif(not IMPORTS_SUCCESSFUL, reason="Imports failed")
class TestGetPRTemplates:
    """Test the get_pr_templates tool."""
    
    @pytest.mark.asyncio
    async def test_returns_json_string(self):
        """Test that get_pr_templates returns a JSON string."""
        result = await get_pr_templates()
        
        assert isinstance(result, str), "Should return a string"
        # Should be valid JSON
        data = json.loads(result)
        assert isinstance(data, list), "Should return a JSON array of templates"
    
    @pytest.mark.asyncio
    async def test_returns_templates(self):
        """Test that templates are returned."""
        result = await get_pr_templates()
        templates = json.loads(result)
        
        assert len(templates) > 0, "Should return at least one template"
        
        # Check that templates have expected structure
        for template in templates:
            assert isinstance(template, dict), "Each template should be a dictionary"
            # Should have some identifying information
            assert any(key in template for key in ["filename", "name", "type", "id"]), \
                "Templates should have an identifier"


@pytest.mark.skipif(not IMPORTS_SUCCESSFUL, reason="Imports failed")
class TestSuggestTemplate:
    """Test the suggest_template tool."""
    
    @pytest.mark.asyncio
    async def test_returns_json_string(self):
        """Test that suggest_template returns a JSON string."""
        result = await suggest_template(
            "Fixed a bug in the authentication system",
            "bug"
        )
        
        assert isinstance(result, str), "Should return a string"
        # Should be valid JSON
        data = json.loads(result)
        assert isinstance(data, dict), "Should return a JSON object"
    
    @pytest.mark.asyncio
    async def test_suggestion_structure(self):
        """Test that the suggestion has expected structure."""
        result = await suggest_template(
            "Added new feature for user management",
            "feature"
        )
        suggestion = json.loads(result)
        
        # Check for some expected fields (flexible to allow different implementations)
        assert any(key in suggestion for key in ["template", "recommended_template", "suggestion"]), \
            "Should include a template recommendation"


@pytest.mark.skipif(not IMPORTS_SUCCESSFUL, reason="Imports failed")
class TestToolRegistration:
    """Test that tools are properly registered with FastMCP."""
    
    def test_tools_have_decorators(self):
        """Test that tool functions are decorated with @mcp.tool()."""
        # In FastMCP, decorated functions should have certain attributes
        # This is a basic check that functions exist and are callable
        assert hasattr(analyze_file_changes, '__name__'), \
            "analyze_file_changes should be a proper function"
        assert hasattr(get_pr_templates, '__name__'), \
            "get_pr_templates should be a proper function"
        assert hasattr(suggest_template, '__name__'), \
            "suggest_template should be a proper function"


if __name__ == "__main__":
    if not IMPORTS_SUCCESSFUL:
        print(f"❌ Cannot run tests - imports failed: {IMPORT_ERROR}")
        print("\nMake sure you've:")
        print("1. Implemented all three tool functions")
        print("2. Decorated them with @mcp.tool()")
        print("3. Installed dependencies with: uv sync")
        exit(1)
    
    # Run tests
    pytest.main([__file__, "-v"])
````

## File: projects/unit3/github-actions-integration/starter/validate_starter.py
````python
#!/usr/bin/env python3
"""
Validation script for Module 1 starter code
Ensures the starter template is ready for learners to implement
"""

import subprocess
import sys
import os
from pathlib import Path

def test_project_structure():
    """Check that all required files exist."""
    print("Project Structure:")
    required_files = [
        "server.py",
        "pyproject.toml",
        "README.md"
    ]
    
    all_exist = True
    for file in required_files:
        if Path(file).exists():
            print(f"  ✓ {file} exists")
        else:
            print(f"  ✗ {file} missing")
            all_exist = False
    
    return all_exist

def test_imports():
    """Test that the starter code imports work."""
    try:
        # Test importing the server module
        import server
        print("✓ server.py imports successfully")
        
        # Check that FastMCP is imported
        if hasattr(server, 'mcp'):
            print("✓ FastMCP server instance found")
        else:
            print("✗ FastMCP server instance not found")
            return False
            
        return True
    except ImportError as e:
        print(f"✗ Import error: {e}")
        print("  Please ensure you've installed dependencies: uv sync")
        return False

def test_todos():
    """Check that TODO comments exist for learners."""
    print("\nTODO Comments:")
    
    with open("server.py", "r") as f:
        content = f.read()
    
    todos = []
    for i, line in enumerate(content.split('\n'), 1):
        if 'TODO' in line:
            todos.append((i, line.strip()))
    
    if todos:
        print(f"✓ Found {len(todos)} TODO comments for learners:")
        for line_no, todo in todos[:5]:  # Show first 5
            print(f"  Line {line_no}: {todo[:60]}...")
        if len(todos) > 5:
            print(f"  ... and {len(todos) - 5} more")
        return True
    else:
        print("✗ No TODO comments found - learners need guidance!")
        return False

def test_starter_runs():
    """Test that the starter code can at least be executed."""
    print("\nExecution Test:")
    
    try:
        # Try to import and check if server can be initialized
        import server
        # If we can import it and it has the right attributes, it should run
        if hasattr(server, 'mcp') and hasattr(server, 'get_recent_actions_events'):
            print("✓ Server imports and initializes correctly")
            return True
        else:
            print("✗ Server missing required components")
            return False
        
    except Exception as e:
        print(f"✗ Failed to initialize server: {e}")
        return False

def test_dependencies():
    """Check that pyproject.toml is properly configured."""
    print("\nDependencies:")
    
    try:
        import tomllib
    except ImportError:
        import tomli as tomllib
    
    try:
        with open("pyproject.toml", "rb") as f:
            config = tomllib.load(f)
        
        # Check for required sections
        if "project" in config and "dependencies" in config["project"]:
            deps = config["project"]["dependencies"]
            print(f"✓ Found {len(deps)} dependencies")
            for dep in deps:
                print(f"  - {dep}")
        else:
            print("✗ No dependencies section found")
            return False
            
        return True
    except Exception as e:
        print(f"✗ Error reading pyproject.toml: {e}")
        return False

def test_no_implementation():
    """Ensure starter code doesn't contain the solution."""
    print("\nImplementation Check:")
    
    with open("server.py", "r") as f:
        content = f.read()
    
    # Check that tool functions are not implemented
    solution_indicators = [
        "subprocess.run",  # Git commands
        "json.dumps",      # Returning JSON
        "git diff",        # Git operations
        "template",        # Template logic
    ]
    
    found_implementations = []
    for indicator in solution_indicators:
        if indicator in content.lower():
            found_implementations.append(indicator)
    
    if found_implementations:
        print(f"⚠️  Found possible solution code: {', '.join(found_implementations)}")
        print("   Make sure these are only in comments/examples")
        return True  # Warning, not failure
    else:
        print("✓ No solution implementation found (good!)")
        return True

def main():
    """Run all validation checks."""
    print("Module 1 Starter Code Validation")
    print("=" * 50)
    
    # Change to starter directory if needed
    if Path("validate_starter.py").exists():
        os.chdir(Path("validate_starter.py").parent)
    
    tests = [
        ("Project Structure", test_project_structure),
        ("Python Imports", test_imports),
        ("TODO Comments", test_todos),
        ("Starter Execution", test_starter_runs),
        ("Dependencies", test_dependencies),
        ("Clean Starter", test_no_implementation)
    ]
    
    results = []
    for test_name, test_func in tests:
        print(f"\n{test_name}:")
        try:
            results.append(test_func())
        except Exception as e:
            print(f"✗ Test failed with error: {e}")
            results.append(False)
    
    print("\n" + "=" * 50)
    passed = sum(results)
    total = len(results)
    print(f"Checks passed: {passed}/{total}")
    
    if passed == total:
        print("\n✓ Starter code is ready for learners!")
        print("\nLearners should:")
        print("1. Run: uv sync")
        print("2. Follow the TODO comments in server.py")
        print("3. Test with: uv run pytest test_server.py")
        print("4. Configure Claude Desktop when ready")
    else:
        print("\n✗ Some checks failed. Please review the starter code.")
        sys.exit(1)

if __name__ == "__main__":
    main()
````

## File: projects/unit3/slack-notification/solution/github_events.json
````json
[
  {
    "timestamp": "2025-05-30T22:42:00.904997",
    "event_type": "workflow_run",
    "action": "completed",
    "workflow_run": {
      "name": "CI",
      "status": "completed",
      "conclusion": "failure",
      "run_number": 42,
      "html_url": "https://github.com/test/repo/actions/runs/123",
      "head_branch": "test",
      "head_sha": "abc123"
    },
    "check_run": null,
    "repository": null,
    "sender": null
  }
]
````

## File: projects/unit3/slack-notification/solution/manual_test.md
````markdown
# Manual Testing Guide - Slack Notification Module

This guide provides curl-based tests so you can verify your implementation without setting up a full GitHub repository and Actions workflow.

## Prerequisites

1. MCP server running: `uv run server.py`
2. Webhook server running: `python webhook_server.py` 
3. Slack webhook URL set: `export SLACK_WEBHOOK_URL="https://hooks.slack.com/services/..."`

## Test 1: Direct Slack Tool Test

Test your `send_slack_notification` tool directly via Claude Code:

```bash
# Start your MCP server and connect with Claude Code, then ask:
# "Send a test message to Slack: 'Hello from MCP Course Module 3!'"
```

Expected result: Message appears in your Slack channel.

## Test 2: Simulate GitHub Webhook Events

### 2a. Simulate CI Failure Event

Send a fake GitHub Actions failure event to your webhook server:

```bash
curl -X POST http://localhost:8080/webhook/github \
  -H "Content-Type: application/json" \
  -H "X-GitHub-Event: workflow_run" \
  -d '{
    "action": "completed",
    "workflow_run": {
      "id": 123456789,
      "name": "CI",
      "status": "completed",
      "conclusion": "failure",
      "run_number": 42,
      "created_at": "2024-01-15T10:30:00Z",
      "updated_at": "2024-01-15T10:35:00Z",
      "html_url": "https://github.com/user/repo/actions/runs/123456789",
      "head_branch": "feature/slack-integration",
      "head_sha": "abc123f456789",
      "repository": {
        "name": "mcp-course",
        "full_name": "user/mcp-course",
        "html_url": "https://github.com/user/mcp-course"
      },
      "pull_requests": [{
        "number": 42,
        "url": "https://api.github.com/repos/user/mcp-course/pulls/42",
        "html_url": "https://github.com/user/mcp-course/pull/42"
      }]
    }
  }'
```

### 2b. Simulate CI Success Event

```bash
curl -X POST http://localhost:8080/webhook/github \
  -H "Content-Type: application/json" \
  -H "X-GitHub-Event: workflow_run" \
  -d '{
    "action": "completed",
    "workflow_run": {
      "id": 123456790,
      "name": "Deploy",
      "status": "completed",
      "conclusion": "success",
      "run_number": 43,
      "created_at": "2024-01-15T11:30:00Z",
      "updated_at": "2024-01-15T11:35:00Z",
      "html_url": "https://github.com/user/repo/actions/runs/123456790",
      "head_branch": "main",
      "head_sha": "def456g789012",
      "repository": {
        "name": "mcp-course",
        "full_name": "user/mcp-course",
        "html_url": "https://github.com/user/mcp-course"
      },
      "pull_requests": [{
        "number": 43,
        "url": "https://api.github.com/repos/user/mcp-course/pulls/43",
        "html_url": "https://github.com/user/mcp-course/pull/43"
      }]
    }
  }'
```

## Test 3: End-to-End Workflow Tests

After sending the webhook events above, test the complete workflow via Claude Code:

### 3a. Test Failure Alert Workflow

Ask Claude Code:
```
"Check recent CI events, find any failures, format them as a Slack alert, and send to the team"
```

Expected workflow:
1. Claude calls `get_recent_actions_events()` → finds failure event
2. Claude calls `format_ci_failure_alert()` → generates formatted message
3. Claude calls `send_slack_notification()` → sends to Slack

Expected Slack message:
```
❌ *CI Failed* - mcp-course

> CI workflow failed on feature/slack-integration

*Details:*
• Workflow: `CI`
• Branch: `feature/slack-integration`
• Commit: `abc123f`

*Next Steps:*
• <https://github.com/user/mcp-course/pull/42|View Pull Request>
• <https://github.com/user/repo/actions/runs/123456789|Check Action Logs>
```

### 3b. Test Success Summary Workflow

Ask Claude Code:
```
"Check recent CI events, find any successful deployments, format them as a celebration message, and send to the team"
```

Expected workflow:
1. Claude calls `get_recent_actions_events()` → finds success event
2. Claude calls `format_ci_success_summary()` → generates formatted message  
3. Claude calls `send_slack_notification()` → sends to Slack

Expected Slack message:
```
✅ *Deployment Successful* - mcp-course

> Deploy workflow completed successfully on main

*Changes:*
• Module 3 Slack integration added
• Team notification system implemented

*Links:*
• <https://github.com/user/mcp-course/pull/43|View Changes>
• <https://github.com/user/mcp-course|Visit Repository>
```

## Test 4: Error Handling Tests

### 4a. Test Missing Webhook URL

```bash
# Temporarily unset the environment variable
unset SLACK_WEBHOOK_URL

# Ask Claude Code to send a message
# Expected: Error message about missing environment variable
```

### 4b. Test Invalid Webhook URL

```bash
# Set invalid webhook URL
export SLACK_WEBHOOK_URL="https://invalid-webhook-url.com/test"

# Ask Claude Code to send a message  
# Expected: Error message about connection failure
```

### 4c. Restore Valid Webhook URL

```bash
export SLACK_WEBHOOK_URL="https://hooks.slack.com/services/YOUR/ACTUAL/URL"
```

## Test 5: Prompt-Only Tests

Test the formatting prompts without sending to Slack:

### 5a. Test Failure Alert Prompt

Ask Claude Code:
```
"Use the format_ci_failure_alert prompt to create a failure message for the recent CI failure, but don't send it to Slack yet"
```

### 5b. Test Success Summary Prompt

Ask Claude Code:
```
"Use the format_ci_success_summary prompt to create a success message for the recent deployment, but don't send it to Slack yet"
```

## Test 6: Integration with Previous Modules

Test that all previous module functionality still works:

### 6a. Module 1 Integration

Ask Claude Code:
```
"Analyze current file changes, suggest a PR template, then create a Slack message about the PR status"
```

### 6b. Module 2 Integration

Ask Claude Code:
```
"Check workflow status, analyze the CI results, and create a comprehensive team update for Slack"
```

## Verification Checklist

After running these tests, verify:

- [ ] Direct Slack tool works (Test 1)
- [ ] Webhook server receives and stores events (Test 2)
- [ ] Failure alert workflow works end-to-end (Test 3a)
- [ ] Success summary workflow works end-to-end (Test 3b)
- [ ] Error handling works properly (Test 4)
- [ ] Prompts work independently (Test 5)
- [ ] Integration with previous modules works (Test 6)
- [ ] Slack messages display with proper formatting
- [ ] All tools and prompts are accessible to Claude Code

## Troubleshooting

### Webhook Server Issues
```bash
# Check if webhook server is running
curl http://localhost:8080/health

# Check stored events
cat github_events.json
```

### MCP Server Issues
```bash
# Check if MCP server is responding
# Should see server startup messages when running uv run server.py
```

### Slack Issues
```bash
# Test webhook URL directly
curl -X POST -H 'Content-type: application/json' \
  --data '{"text":"Direct webhook test"}' \
  $SLACK_WEBHOOK_URL
```

This testing approach lets you validate your implementation without needing to set up a real GitHub repository with Actions workflows!
````

## File: projects/unit3/slack-notification/solution/pyproject.toml
````toml
[project]
name = "pr-agent-slack"
version = "3.0.0"
description = "MCP server with Slack notifications integrating Tools and Prompts"
readme = "README.md"
requires-python = ">=3.10"
dependencies = [
    "mcp[cli]>=1.0.0",
    "aiohttp>=3.10.0,<4.0.0",
    "requests>=2.32.0,<3.0.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=8.3.0",
    "pytest-asyncio>=0.21.0",
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["."]

[tool.uv]
dev-dependencies = [
    "pytest>=8.3.0",
    "pytest-asyncio>=0.21.0",
]
````

## File: projects/unit3/slack-notification/solution/README.md
````markdown
# Module 3: Slack Notification - Complete Solution

This is the complete implementation of Module 3, demonstrating how to integrate MCP Tools and Prompts for team communication via Slack.

## What This Implements

This solution extends Modules 1 and 2 with:

1. **`send_slack_notification` tool** - Sends formatted messages to Slack via webhook with proper error handling
2. **`format_ci_failure_alert` prompt** - Creates rich failure alerts with Slack markdown
3. **`format_ci_success_summary` prompt** - Creates celebration messages for successful deployments

## Setup and Usage

1. Install dependencies:
   ```bash
   uv sync
   ```

2. Set up Slack webhook:
   ```bash
   export SLACK_WEBHOOK_URL="https://hooks.slack.com/services/YOUR/WEBHOOK/URL"
   ```

3. Start services:
   ```bash
   # Terminal 1: Webhook server
   python webhook_server.py
   
   # Terminal 2: MCP server
   uv run server.py
   
   # Terminal 3: Cloudflare tunnel (optional)
   cloudflared tunnel --url http://localhost:8080
   ```

## Testing

See `manual_test.md` for comprehensive testing instructions using curl commands to simulate GitHub webhook events.

## Key Learning Outcomes

This solution demonstrates all MCP primitives working together for real-world team automation.
````

## File: projects/unit3/slack-notification/solution/test_server.py
````python
#!/usr/bin/env python3
"""
Unit tests for Module 1: Basic MCP Server
"""

import json
import pytest
import asyncio
from pathlib import Path
from unittest.mock import patch, MagicMock, AsyncMock
from server import (
    mcp,
    analyze_file_changes,
    get_pr_templates,
    suggest_template,
    create_default_template,
    TEMPLATES_DIR
)


class TestAnalyzeFileChanges:
    """Test the analyze_file_changes tool."""
    
    @pytest.mark.asyncio
    async def test_analyze_with_diff(self):
        """Test analyzing changes with full diff included."""
        mock_result = MagicMock()
        mock_result.stdout = "M\tfile1.py\nA\tfile2.py\n"
        mock_result.stderr = ""
        
        with patch('subprocess.run') as mock_run:
            mock_run.return_value = mock_result
            
            result = await analyze_file_changes("main", include_diff=True)
            
            assert isinstance(result, str)
            data = json.loads(result)
            assert data["base_branch"] == "main"
            assert "files_changed" in data
            assert "statistics" in data
            assert "commits" in data
            assert "diff" in data
    
    @pytest.mark.asyncio
    async def test_analyze_without_diff(self):
        """Test analyzing changes without diff content."""
        mock_result = MagicMock()
        mock_result.stdout = "M\tfile1.py\n"
        
        with patch('subprocess.run') as mock_run:
            mock_run.return_value = mock_result
            
            result = await analyze_file_changes("main", include_diff=False)
            
            data = json.loads(result)
            assert "Diff not included" in data["diff"]
    
    @pytest.mark.asyncio
    async def test_analyze_git_error(self):
        """Test handling git command errors."""
        with patch('subprocess.run') as mock_run:
            mock_run.side_effect = Exception("Git not found")
            
            result = await analyze_file_changes("main", True)
            
            assert "Error:" in result


class TestPRTemplates:
    """Test PR template management."""
    
    @pytest.mark.asyncio
    async def test_get_templates(self, tmp_path, monkeypatch):
        """Test getting available templates."""
        # Use temporary directory for templates
        monkeypatch.setattr('server.TEMPLATES_DIR', tmp_path)
        
        result = await get_pr_templates()
        
        templates = json.loads(result)
        assert len(templates) > 0
        assert any(t["type"] == "Bug Fix" for t in templates)
        assert any(t["type"] == "Feature" for t in templates)
        assert all("content" in t for t in templates)
    
    def test_create_default_template(self, tmp_path):
        """Test creating default template files."""
        template_path = tmp_path / "test.md"
        
        create_default_template(template_path, "Bug Fix")
        
        assert template_path.exists()
        content = template_path.read_text()
        assert "## Bug Fix" in content
        assert "Description" in content
        assert "Root Cause" in content


class TestSuggestTemplate:
    """Test template suggestion based on analysis."""
    
    @pytest.mark.asyncio
    async def test_suggest_bug_fix(self, tmp_path, monkeypatch):
        """Test suggesting bug fix template."""
        monkeypatch.setattr('server.TEMPLATES_DIR', tmp_path)
        
        # Create templates first
        await get_pr_templates()
        
        result = await suggest_template(
            "Fixed null pointer exception in user service",
            "bug"
        )
        
        suggestion = json.loads(result)
        assert suggestion["recommended_template"]["filename"] == "bug.md"
        assert "Bug Fix" in suggestion["recommended_template"]["type"]
        assert "reasoning" in suggestion
    
    @pytest.mark.asyncio
    async def test_suggest_feature(self, tmp_path, monkeypatch):
        """Test suggesting feature template."""
        monkeypatch.setattr('server.TEMPLATES_DIR', tmp_path)
        
        await get_pr_templates()
        
        result = await suggest_template(
            "Added new authentication method for API",
            "feature"
        )
        
        suggestion = json.loads(result)
        assert suggestion["recommended_template"]["filename"] == "feature.md"
    
    @pytest.mark.asyncio
    async def test_suggest_with_type_variations(self, tmp_path, monkeypatch):
        """Test template suggestion with various type names."""
        monkeypatch.setattr('server.TEMPLATES_DIR', tmp_path)
        
        await get_pr_templates()
        
        # Test variations
        for change_type, expected_file in [
            ("fix", "bug.md"),
            ("enhancement", "feature.md"),
            ("documentation", "docs.md"),
            ("cleanup", "refactor.md"),
            ("testing", "test.md"),
            ("optimization", "performance.md")
        ]:
            result = await suggest_template(f"Some {change_type} work", change_type)
            suggestion = json.loads(result)
            assert suggestion["recommended_template"]["filename"] == expected_file


class TestIntegration:
    """Integration tests for the complete workflow."""
    
    @pytest.mark.asyncio
    async def test_full_workflow(self, tmp_path, monkeypatch):
        """Test the complete workflow from analysis to suggestion."""
        monkeypatch.setattr('server.TEMPLATES_DIR', tmp_path)
        
        # Mock git commands
        with patch('subprocess.run') as mock_run:
            mock_run.return_value = MagicMock(
                stdout="M\tsrc/main.py\nM\ttests/test_main.py\n",
                stderr=""
            )
            
            # 1. Analyze changes
            analysis_result = await analyze_file_changes("main", True)
            
            # 2. Get templates
            templates_result = await get_pr_templates()
            
            # 3. Suggest template based on analysis
            suggestion_result = await suggest_template(
                "Updated main functionality and added tests",
                "feature"
            )
            
            # Verify results
            assert all(isinstance(r, str) for r in [analysis_result, templates_result, suggestion_result])
            
            suggestion = json.loads(suggestion_result)
            assert "recommended_template" in suggestion
            assert "template_content" in suggestion
            assert suggestion["recommended_template"]["type"] == "Feature"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
````

## File: projects/unit3/slack-notification/solution/webhook_server.py
````python
#!/usr/bin/env python3
"""
Simple webhook server for GitHub Actions events.
Stores events in a JSON file that the MCP server can read.
"""

import json
from datetime import datetime
from pathlib import Path
from aiohttp import web

# File to store events
EVENTS_FILE = Path(__file__).parent / "github_events.json"

async def handle_webhook(request):
    """Handle incoming GitHub webhook"""
    try:
        data = await request.json()
        
        # Create event record
        event = {
            "timestamp": datetime.utcnow().isoformat(),
            "event_type": request.headers.get("X-GitHub-Event", "unknown"),
            "action": data.get("action"),
            "workflow_run": data.get("workflow_run"),
            "check_run": data.get("check_run"),
            "repository": data.get("repository", {}).get("full_name"),
            "sender": data.get("sender", {}).get("login")
        }
        
        # Load existing events
        events = []
        if EVENTS_FILE.exists():
            with open(EVENTS_FILE, 'r') as f:
                events = json.load(f)
        
        # Add new event and keep last 100
        events.append(event)
        events = events[-100:]
        
        # Save events
        with open(EVENTS_FILE, 'w') as f:
            json.dump(events, f, indent=2)
        
        return web.json_response({"status": "received"})
    except Exception as e:
        return web.json_response({"error": str(e)}, status=400)

# Create app and add route
app = web.Application()
app.router.add_post('/webhook/github', handle_webhook)

if __name__ == '__main__':
    print("🚀 Starting webhook server on http://localhost:8080")
    print("📝 Events will be saved to:", EVENTS_FILE)
    print("🔗 Webhook URL: http://localhost:8080/webhook/github")
    web.run_app(app, host='localhost', port=8080)
````

## File: projects/unit3/slack-notification/starter/manual_test.md
````markdown
# Manual Testing Guide - Slack Notification Module

This guide provides curl-based tests so you can verify your implementation without setting up a full GitHub repository and Actions workflow.

## Prerequisites

1. MCP server running: `uv run server.py`
2. Webhook server running: `python webhook_server.py` 
3. Slack webhook URL set: `export SLACK_WEBHOOK_URL="https://hooks.slack.com/services/..."`

## Test 1: Direct Slack Tool Test

Test your `send_slack_notification` tool directly via Claude Code:

```bash
# Start your MCP server and connect with Claude Code, then ask:
# "Send a test message to Slack: 'Hello from MCP Course Module 3!'"
```

Expected result: Message appears in your Slack channel.

## Test 2: Simulate GitHub Webhook Events

### 2a. Simulate CI Failure Event

Send a fake GitHub Actions failure event to your webhook server:

```bash
curl -X POST http://localhost:8080/webhook/github \
  -H "Content-Type: application/json" \
  -H "X-GitHub-Event: workflow_run" \
  -d '{
    "action": "completed",
    "workflow_run": {
      "id": 123456789,
      "name": "CI",
      "status": "completed",
      "conclusion": "failure",
      "run_number": 42,
      "created_at": "2024-01-15T10:30:00Z",
      "updated_at": "2024-01-15T10:35:00Z",
      "html_url": "https://github.com/user/repo/actions/runs/123456789",
      "head_branch": "feature/slack-integration",
      "head_sha": "abc123f456789",
      "repository": {
        "name": "mcp-course",
        "full_name": "user/mcp-course",
        "html_url": "https://github.com/user/mcp-course"
      },
      "pull_requests": [{
        "number": 42,
        "url": "https://api.github.com/repos/user/mcp-course/pulls/42",
        "html_url": "https://github.com/user/mcp-course/pull/42"
      }]
    }
  }'
```

### 2b. Simulate CI Success Event

```bash
curl -X POST http://localhost:8080/webhook/github \
  -H "Content-Type: application/json" \
  -H "X-GitHub-Event: workflow_run" \
  -d '{
    "action": "completed",
    "workflow_run": {
      "id": 123456790,
      "name": "Deploy",
      "status": "completed",
      "conclusion": "success",
      "run_number": 43,
      "created_at": "2024-01-15T11:30:00Z",
      "updated_at": "2024-01-15T11:35:00Z",
      "html_url": "https://github.com/user/repo/actions/runs/123456790",
      "head_branch": "main",
      "head_sha": "def456g789012",
      "repository": {
        "name": "mcp-course",
        "full_name": "user/mcp-course",
        "html_url": "https://github.com/user/mcp-course"
      },
      "pull_requests": [{
        "number": 43,
        "url": "https://api.github.com/repos/user/mcp-course/pulls/43",
        "html_url": "https://github.com/user/mcp-course/pull/43"
      }]
    }
  }'
```

## Test 3: End-to-End Workflow Tests

After sending the webhook events above, test the complete workflow via Claude Code:

### 3a. Test Failure Alert Workflow

Ask Claude Code:
```
"Check recent CI events, find any failures, format them as a Slack alert, and send to the team"
```

Expected workflow:
1. Claude calls `get_recent_actions_events()` → finds failure event
2. Claude calls `format_ci_failure_alert()` → generates formatted message
3. Claude calls `send_slack_notification()` → sends to Slack

Expected Slack message:
```
❌ *CI Failed* - mcp-course

> CI workflow failed on feature/slack-integration

*Details:*
• Workflow: `CI`
• Branch: `feature/slack-integration`
• Commit: `abc123f`

*Next Steps:*
• <https://github.com/user/mcp-course/pull/42|View Pull Request>
• <https://github.com/user/repo/actions/runs/123456789|Check Action Logs>
```

### 3b. Test Success Summary Workflow

Ask Claude Code:
```
"Check recent CI events, find any successful deployments, format them as a celebration message, and send to the team"
```

Expected workflow:
1. Claude calls `get_recent_actions_events()` → finds success event
2. Claude calls `format_ci_success_summary()` → generates formatted message  
3. Claude calls `send_slack_notification()` → sends to Slack

Expected Slack message:
```
✅ *Deployment Successful* - mcp-course

> Deploy workflow completed successfully on main

*Changes:*
• Module 3 Slack integration added
• Team notification system implemented

*Links:*
• <https://github.com/user/mcp-course/pull/43|View Changes>
• <https://github.com/user/mcp-course|Visit Repository>
```

## Test 4: Error Handling Tests

### 4a. Test Missing Webhook URL

```bash
# Temporarily unset the environment variable
unset SLACK_WEBHOOK_URL

# Ask Claude Code to send a message
# Expected: Error message about missing environment variable
```

### 4b. Test Invalid Webhook URL

```bash
# Set invalid webhook URL
export SLACK_WEBHOOK_URL="https://invalid-webhook-url.com/test"

# Ask Claude Code to send a message  
# Expected: Error message about connection failure
```

### 4c. Restore Valid Webhook URL

```bash
export SLACK_WEBHOOK_URL="https://hooks.slack.com/services/YOUR/ACTUAL/URL"
```

## Test 5: Prompt-Only Tests

Test the formatting prompts without sending to Slack:

### 5a. Test Failure Alert Prompt

Ask Claude Code:
```
"Use the format_ci_failure_alert prompt to create a failure message for the recent CI failure, but don't send it to Slack yet"
```

### 5b. Test Success Summary Prompt

Ask Claude Code:
```
"Use the format_ci_success_summary prompt to create a success message for the recent deployment, but don't send it to Slack yet"
```

## Test 6: Integration with Previous Modules

Test that all previous module functionality still works:

### 6a. Module 1 Integration

Ask Claude Code:
```
"Analyze current file changes, suggest a PR template, then create a Slack message about the PR status"
```

### 6b. Module 2 Integration

Ask Claude Code:
```
"Check workflow status, analyze the CI results, and create a comprehensive team update for Slack"
```

## Verification Checklist

After running these tests, verify:

- [ ] Direct Slack tool works (Test 1)
- [ ] Webhook server receives and stores events (Test 2)
- [ ] Failure alert workflow works end-to-end (Test 3a)
- [ ] Success summary workflow works end-to-end (Test 3b)
- [ ] Error handling works properly (Test 4)
- [ ] Prompts work independently (Test 5)
- [ ] Integration with previous modules works (Test 6)
- [ ] Slack messages display with proper formatting
- [ ] All tools and prompts are accessible to Claude Code

## Troubleshooting

### Webhook Server Issues
```bash
# Check if webhook server is running
curl http://localhost:8080/health

# Check stored events
cat github_events.json
```

### MCP Server Issues
```bash
# Check if MCP server is responding
# Should see server startup messages when running uv run server.py
```

### Slack Issues
```bash
# Test webhook URL directly
curl -X POST -H 'Content-type: application/json' \
  --data '{"text":"Direct webhook test"}' \
  $SLACK_WEBHOOK_URL
```

This testing approach lets you validate your implementation without needing to set up a real GitHub repository with Actions workflows!
````

## File: projects/unit3/slack-notification/starter/pyproject.toml
````toml
[project]
name = "pr-agent-slack"
version = "3.0.0"
description = "MCP server with Slack notifications integrating Tools and Prompts"
readme = "README.md"
requires-python = ">=3.10"
dependencies = [
    "mcp[cli]>=1.0.0",
    "aiohttp>=3.10.0,<4.0.0",
    "requests>=2.32.0,<3.0.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=8.3.0",
    "pytest-asyncio>=0.21.0",
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["."]

[tool.uv]
dev-dependencies = [
    "pytest>=8.3.0",
    "pytest-asyncio>=0.21.0",
]
````

## File: projects/unit3/slack-notification/starter/README.md
````markdown
# Module 3: Slack Notification - Starter

This starter code extends Modules 1 and 2 with Slack integration, demonstrating how to combine MCP Tools and Prompts for complete team communication workflows.

## What You'll Implement

In this module, you'll complete:

1. **`send_slack_notification` tool** - Send messages to Slack via webhook
2. **`format_ci_failure_alert` prompt** - Format CI failures for Slack
3. **`format_ci_success_summary` prompt** - Format successful deployments for Slack

## Prerequisites

- Completed Modules 1 and 2
- A Slack workspace with webhook permissions
- Environment variable: `SLACK_WEBHOOK_URL`

## Setup

1. Install dependencies:
   ```bash
   uv sync
   ```

2. Set up Slack webhook:
   - Create Slack app at https://api.slack.com/apps
   - App name: "MCP Course Notifications"
   - Enable incoming webhooks
   - Add webhook to workspace
   - Export URL: `export SLACK_WEBHOOK_URL="https://hooks.slack.com/services/..."`

3. Test webhook:
   ```bash
   curl -X POST -H 'Content-type: application/json' \
     --data '{"text":"Hello from MCP Course!"}' \
     $SLACK_WEBHOOK_URL
   ```

## Implementation Tasks

### 1. Complete `send_slack_notification` Tool

In `server.py`, implement the TODO sections:

```python
@mcp.tool()
async def send_slack_notification(message: str) -> str:
    # TODO: Import requests library at top of file
    # TODO: Send POST request to webhook_url
    # TODO: Include message in JSON payload: {"text": message}
    # TODO: Handle response and return status
```

### 2. Test the Prompts

The formatting prompts are complete - test them with Claude Code:
- Use `format_ci_failure_alert` to create failure messages
- Use `format_ci_success_summary` to create success messages
- Send formatted messages using your `send_slack_notification` tool

### 3. End-to-End Workflow

Test the complete integration:

1. Start webhook server: `python webhook_server.py`
2. Start MCP server: `uv run server.py`
3. Start Cloudflare tunnel: `cloudflared tunnel --url http://localhost:8080`
4. Trigger GitHub Actions
5. Use prompts to format messages
6. Send to Slack and verify formatting

## Expected Slack Output

**Failure Alert:**
```
❌ *CI Failed* - mcp-course

> Tests failed in Module 3 implementation

*Details:*
• Workflow: `CI`
• Branch: `feature/slack-integration`
• Commit: `abc123f`

*Next Steps:*
• <https://github.com/user/mcp-course/pull/42|View Pull Request>
• <https://github.com/user/mcp-course/actions/runs/123|Check Action Logs>
```

## Security Note

⚠️ **Important**: The `SLACK_WEBHOOK_URL` is a sensitive secret that grants permission to post messages to your Slack channel. Always:
- Store it as an environment variable, never in code
- Never commit webhook URLs to version control
- Treat it like a password

## Available Tools & Prompts

This module includes all tools and prompts from Modules 1 & 2, plus:

**New Tools:**
- `send_slack_notification` - Send messages to Slack

**New Prompts:**  
- `format_ci_failure_alert` - Create failure alerts
- `format_ci_success_summary` - Create success summaries

**From Previous Modules:**
- All file analysis tools (Module 1)
- All GitHub Actions tools (Module 2)  
- All CI/CD analysis prompts (Module 2)

## Testing Your Implementation

1. **Tool Test**: Call `send_slack_notification` directly with a test message
2. **Prompt Test**: Use formatting prompts to generate messages, then send them
3. **Integration Test**: Full workflow from GitHub webhook to Slack notification
4. **Format Test**: Verify Slack markdown renders correctly in your channel

## Next Steps

Once complete, you'll have built a production-ready MCP server that demonstrates all core MCP primitives working together for real-world team automation!
````

## File: projects/unit3/slack-notification/starter/test_server.py
````python
#!/usr/bin/env python3
"""
Unit tests for Module 1: Basic MCP Server
Run these tests to validate your implementation
"""

import json
import pytest
import asyncio
from pathlib import Path
from unittest.mock import patch, MagicMock

# Import your implemented functions
try:
    from server import (
        mcp,
        analyze_file_changes,
        get_pr_templates,
        suggest_template
    )
    IMPORTS_SUCCESSFUL = True
except ImportError as e:
    IMPORTS_SUCCESSFUL = False
    IMPORT_ERROR = str(e)


class TestImplementation:
    """Test that the required functions are implemented."""
    
    def test_imports(self):
        """Test that all required functions can be imported."""
        assert IMPORTS_SUCCESSFUL, f"Failed to import required functions: {IMPORT_ERROR if not IMPORTS_SUCCESSFUL else ''}"
        assert mcp is not None, "FastMCP server instance not found"
        assert callable(analyze_file_changes), "analyze_file_changes should be a callable function"
        assert callable(get_pr_templates), "get_pr_templates should be a callable function"
        assert callable(suggest_template), "suggest_template should be a callable function"


@pytest.mark.skipif(not IMPORTS_SUCCESSFUL, reason="Imports failed")
class TestAnalyzeFileChanges:
    """Test the analyze_file_changes tool."""
    
    @pytest.mark.asyncio
    async def test_returns_json_string(self):
        """Test that analyze_file_changes returns a JSON string."""
        with patch('subprocess.run') as mock_run:
            mock_run.return_value = MagicMock(stdout="", stderr="")
            
            result = await analyze_file_changes()
            
            assert isinstance(result, str), "Should return a string"
            # Should be valid JSON
            data = json.loads(result)
            assert isinstance(data, dict), "Should return a JSON object"
    
    @pytest.mark.asyncio
    async def test_includes_required_fields(self):
        """Test that the result includes expected fields."""
        with patch('subprocess.run') as mock_run:
            mock_run.return_value = MagicMock(stdout="M\tfile1.py\n", stderr="")
            
            result = await analyze_file_changes()
            data = json.loads(result)
            
            # Check for some expected fields (flexible to allow different implementations)
            assert any(key in data for key in ["files_changed", "files", "changes", "diff"]), \
                "Result should include file change information"


@pytest.mark.skipif(not IMPORTS_SUCCESSFUL, reason="Imports failed")
class TestGetPRTemplates:
    """Test the get_pr_templates tool."""
    
    @pytest.mark.asyncio
    async def test_returns_json_string(self):
        """Test that get_pr_templates returns a JSON string."""
        result = await get_pr_templates()
        
        assert isinstance(result, str), "Should return a string"
        # Should be valid JSON
        data = json.loads(result)
        assert isinstance(data, list), "Should return a JSON array of templates"
    
    @pytest.mark.asyncio
    async def test_returns_templates(self):
        """Test that templates are returned."""
        result = await get_pr_templates()
        templates = json.loads(result)
        
        assert len(templates) > 0, "Should return at least one template"
        
        # Check that templates have expected structure
        for template in templates:
            assert isinstance(template, dict), "Each template should be a dictionary"
            # Should have some identifying information
            assert any(key in template for key in ["filename", "name", "type", "id"]), \
                "Templates should have an identifier"


@pytest.mark.skipif(not IMPORTS_SUCCESSFUL, reason="Imports failed")
class TestSuggestTemplate:
    """Test the suggest_template tool."""
    
    @pytest.mark.asyncio
    async def test_returns_json_string(self):
        """Test that suggest_template returns a JSON string."""
        result = await suggest_template(
            "Fixed a bug in the authentication system",
            "bug"
        )
        
        assert isinstance(result, str), "Should return a string"
        # Should be valid JSON
        data = json.loads(result)
        assert isinstance(data, dict), "Should return a JSON object"
    
    @pytest.mark.asyncio
    async def test_suggestion_structure(self):
        """Test that the suggestion has expected structure."""
        result = await suggest_template(
            "Added new feature for user management",
            "feature"
        )
        suggestion = json.loads(result)
        
        # Check for some expected fields (flexible to allow different implementations)
        assert any(key in suggestion for key in ["template", "recommended_template", "suggestion"]), \
            "Should include a template recommendation"


@pytest.mark.skipif(not IMPORTS_SUCCESSFUL, reason="Imports failed")
class TestToolRegistration:
    """Test that tools are properly registered with FastMCP."""
    
    def test_tools_have_decorators(self):
        """Test that tool functions are decorated with @mcp.tool()."""
        # In FastMCP, decorated functions should have certain attributes
        # This is a basic check that functions exist and are callable
        assert hasattr(analyze_file_changes, '__name__'), \
            "analyze_file_changes should be a proper function"
        assert hasattr(get_pr_templates, '__name__'), \
            "get_pr_templates should be a proper function"
        assert hasattr(suggest_template, '__name__'), \
            "suggest_template should be a proper function"


if __name__ == "__main__":
    if not IMPORTS_SUCCESSFUL:
        print(f"❌ Cannot run tests - imports failed: {IMPORT_ERROR}")
        print("\nMake sure you've:")
        print("1. Implemented all three tool functions")
        print("2. Decorated them with @mcp.tool()")
        print("3. Installed dependencies with: uv sync")
        exit(1)
    
    # Run tests
    pytest.main([__file__, "-v"])
````

## File: projects/unit3/slack-notification/starter/validate_starter.py
````python
#!/usr/bin/env python3
"""
Validation script for Module 1 starter code
Ensures the starter template is ready for learners to implement
"""

import subprocess
import sys
import os
from pathlib import Path

def test_project_structure():
    """Check that all required files exist."""
    print("Project Structure:")
    required_files = [
        "server.py",
        "pyproject.toml",
        "README.md"
    ]
    
    all_exist = True
    for file in required_files:
        if Path(file).exists():
            print(f"  ✓ {file} exists")
        else:
            print(f"  ✗ {file} missing")
            all_exist = False
    
    return all_exist

def test_imports():
    """Test that the starter code imports work."""
    try:
        # Test importing the server module
        import server
        print("✓ server.py imports successfully")
        
        # Check that FastMCP is imported
        if hasattr(server, 'mcp'):
            print("✓ FastMCP server instance found")
        else:
            print("✗ FastMCP server instance not found")
            return False
            
        return True
    except ImportError as e:
        print(f"✗ Import error: {e}")
        print("  Please ensure you've installed dependencies: uv sync")
        return False

def test_todos():
    """Check that TODO comments exist for learners."""
    print("\nTODO Comments:")
    
    with open("server.py", "r") as f:
        content = f.read()
    
    todos = []
    for i, line in enumerate(content.split('\n'), 1):
        if 'TODO' in line:
            todos.append((i, line.strip()))
    
    if todos:
        print(f"✓ Found {len(todos)} TODO comments for learners:")
        for line_no, todo in todos[:5]:  # Show first 5
            print(f"  Line {line_no}: {todo[:60]}...")
        if len(todos) > 5:
            print(f"  ... and {len(todos) - 5} more")
        return True
    else:
        print("✗ No TODO comments found - learners need guidance!")
        return False

def test_starter_runs():
    """Test that the starter code can at least be executed."""
    print("\nExecution Test:")
    
    try:
        # Try to import and check if server can be initialized
        import server
        # If we can import it and it has the right attributes, it should run
        if hasattr(server, 'mcp') and hasattr(server, 'send_slack_notification'):
            print("✓ Server imports and initializes correctly")
            return True
        else:
            print("✗ Server missing required components")
            return False
        
    except Exception as e:
        print(f"✗ Failed to initialize server: {e}")
        return False

def test_dependencies():
    """Check that pyproject.toml is properly configured."""
    print("\nDependencies:")
    
    try:
        import tomllib
    except ImportError:
        import tomli as tomllib
    
    try:
        with open("pyproject.toml", "rb") as f:
            config = tomllib.load(f)
        
        # Check for required sections
        if "project" in config and "dependencies" in config["project"]:
            deps = config["project"]["dependencies"]
            print(f"✓ Found {len(deps)} dependencies")
            for dep in deps:
                print(f"  - {dep}")
        else:
            print("✗ No dependencies section found")
            return False
            
        return True
    except Exception as e:
        print(f"✗ Error reading pyproject.toml: {e}")
        return False

def test_no_implementation():
    """Ensure starter code doesn't contain the solution."""
    print("\nImplementation Check:")
    
    with open("server.py", "r") as f:
        content = f.read()
    
    # Check that tool functions are not implemented
    solution_indicators = [
        "subprocess.run",  # Git commands
        "json.dumps",      # Returning JSON
        "git diff",        # Git operations
        "template",        # Template logic
    ]
    
    found_implementations = []
    for indicator in solution_indicators:
        if indicator in content.lower():
            found_implementations.append(indicator)
    
    if found_implementations:
        print(f"⚠️  Found possible solution code: {', '.join(found_implementations)}")
        print("   Make sure these are only in comments/examples")
        return True  # Warning, not failure
    else:
        print("✓ No solution implementation found (good!)")
        return True

def main():
    """Run all validation checks."""
    print("Module 1 Starter Code Validation")
    print("=" * 50)
    
    # Change to starter directory if needed
    if Path("validate_starter.py").exists():
        os.chdir(Path("validate_starter.py").parent)
    
    tests = [
        ("Project Structure", test_project_structure),
        ("Python Imports", test_imports),
        ("TODO Comments", test_todos),
        ("Starter Execution", test_starter_runs),
        ("Dependencies", test_dependencies),
        ("Clean Starter", test_no_implementation)
    ]
    
    results = []
    for test_name, test_func in tests:
        print(f"\n{test_name}:")
        try:
            results.append(test_func())
        except Exception as e:
            print(f"✗ Test failed with error: {e}")
            results.append(False)
    
    print("\n" + "=" * 50)
    passed = sum(results)
    total = len(results)
    print(f"Checks passed: {passed}/{total}")
    
    if passed == total:
        print("\n✓ Starter code is ready for learners!")
        print("\nLearners should:")
        print("1. Run: uv sync")
        print("2. Follow the TODO comments in server.py")
        print("3. Test with: uv run pytest test_server.py")
        print("4. Configure Claude Desktop when ready")
    else:
        print("\n✗ Some checks failed. Please review the starter code.")
        sys.exit(1)

if __name__ == "__main__":
    main()
````

## File: projects/unit3/slack-notification/starter/webhook_server.py
````python
#!/usr/bin/env python3
"""
Simple webhook server for GitHub Actions events.
Stores events in a JSON file that the MCP server can read.
"""

import json
from datetime import datetime
from pathlib import Path
from aiohttp import web

# File to store events
EVENTS_FILE = Path(__file__).parent / "github_events.json"

async def handle_webhook(request):
    """Handle incoming GitHub webhook"""
    try:
        data = await request.json()
        
        # Create event record
        event = {
            "timestamp": datetime.utcnow().isoformat(),
            "event_type": request.headers.get("X-GitHub-Event", "unknown"),
            "action": data.get("action"),
            "workflow_run": data.get("workflow_run"),
            "check_run": data.get("check_run"),
            "repository": data.get("repository", {}).get("full_name"),
            "sender": data.get("sender", {}).get("login")
        }
        
        # Load existing events
        events = []
        if EVENTS_FILE.exists():
            with open(EVENTS_FILE, 'r') as f:
                events = json.load(f)
        
        # Add new event and keep last 100
        events.append(event)
        events = events[-100:]
        
        # Save events
        with open(EVENTS_FILE, 'w') as f:
            json.dump(events, f, indent=2)
        
        return web.json_response({"status": "received"})
    except Exception as e:
        return web.json_response({"error": str(e)}, status=400)

# Create app and add route
app = web.Application()
app.router.add_post('/webhook/github', handle_webhook)

if __name__ == '__main__':
    print("🚀 Starting webhook server on http://localhost:8080")
    print("📝 Events will be saved to:", EVENTS_FILE)
    print("🔗 Webhook URL: http://localhost:8080/webhook/github")
    web.run_app(app, host='localhost', port=8080)
````

## File: units/en/unit2/gradio-server.mdx
````
# Building the Gradio MCP Server

In this section, we'll create our sentiment analysis MCP server using Gradio. This server will expose a sentiment analysis tool that can be used by both human users through a web interface and AI models through the MCP protocol.

## Introduction to Gradio MCP Integration

Gradio provides a straightforward way to create MCP servers by automatically converting your Python functions into MCP tools. When you set `mcp_server=True` in `launch()`, Gradio:

1. Automatically converts your functions into MCP Tools
2. Maps input components to tool argument schemas
3. Determines response formats from output components
4. Sets up JSON-RPC over HTTP+SSE for client-server communication
5. Creates both a web interface and an MCP server endpoint

## Setting Up the Project

First, let's create a new directory for our project and set up the required dependencies:

```bash
mkdir mcp-sentiment
cd mcp-sentiment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install "gradio[mcp]" textblob
```

## Creating the Server

> Hugging face spaces needs an app.py file to build the space. So the name of the python file has to be app.py 

Create a new file called `app.py` with the following code:

```python
import json
import gradio as gr
from textblob import TextBlob

def sentiment_analysis(text: str) -> str:
    """
    Analyze the sentiment of the given text.

    Args:
        text (str): The text to analyze

    Returns:
        str: A JSON string containing polarity, subjectivity, and assessment
    """
    blob = TextBlob(text)
    sentiment = blob.sentiment
    
    result = {
        "polarity": round(sentiment.polarity, 2),  # -1 (negative) to 1 (positive)
        "subjectivity": round(sentiment.subjectivity, 2),  # 0 (objective) to 1 (subjective)
        "assessment": "positive" if sentiment.polarity > 0 else "negative" if sentiment.polarity < 0 else "neutral"
    }

    return json.dumps(result)

# Create the Gradio interface
demo = gr.Interface(
    fn=sentiment_analysis,
    inputs=gr.Textbox(placeholder="Enter text to analyze..."),
    outputs=gr.Textbox(),  # Changed from gr.JSON() to gr.Textbox()
    title="Text Sentiment Analysis",
    description="Analyze the sentiment of text using TextBlob"
)

# Launch the interface and MCP server
if __name__ == "__main__":
    demo.launch(mcp_server=True)
```

## Understanding the Code

Let's break down the key components:

1. **Function Definition**:
   - The `sentiment_analysis` function takes a text input and returns a dictionary
   - It uses TextBlob to analyze the sentiment
   - The docstring is crucial as it helps Gradio generate the MCP tool schema
   - Type hints (`str` and `dict`) help define the input/output schema

2. **Gradio Interface**:
   - `gr.Interface` creates both the web UI and MCP server
   - The function is exposed as an MCP tool automatically
   - Input and output components define the tool's schema
   - The JSON output component ensures proper serialization

3. **MCP Server**:
   - Setting `mcp_server=True` enables the MCP server
   - The server will be available at `http://localhost:7860/gradio_api/mcp/sse`
   - You can also enable it using the environment variable:
     ```bash
     export GRADIO_MCP_SERVER=True
     ```

## Running the Server

Start the server by running:

```bash
python app.py
```

You should see output indicating that both the web interface and MCP server are running. The web interface will be available at `http://localhost:7860`, and the MCP server at `http://localhost:7860/gradio_api/mcp/sse`.

## Testing the Server

You can test the server in two ways:

1. **Web Interface**:
   - Open `http://localhost:7860` in your browser
   - Enter some text and click "Submit"
   - You should see the sentiment analysis results

2. **MCP Schema**:
   - Visit `http://localhost:7860/gradio_api/mcp/schema`
   - This shows the MCP tool schema that clients will use
   - You can also find this in the "View API" link in the footer of your Gradio app

## Troubleshooting Tips

1. **Type Hints and Docstrings**:
   - Always provide type hints for your function parameters and return values
   - Include a docstring with an "Args:" block for each parameter
   - This helps Gradio generate accurate MCP tool schemas

2. **String Inputs**:
   - When in doubt, accept input arguments as `str`
   - Convert them to the desired type inside the function
   - This provides better compatibility with MCP clients

3. **SSE Support**:
   - Some MCP clients don't support SSE-based MCP Servers
   - In those cases, use `mcp-remote`:
     ```json
     {
       "mcpServers": {
         "gradio": {
           "command": "npx",
           "args": [
             "mcp-remote",
             "http://localhost:7860/gradio_api/mcp/sse"
           ]
         }
       }
     }
     ```

4. **Connection Issues**:
   - If you encounter connection problems, try restarting both the client and server
   - Check that the server is running and accessible
   - Verify that the MCP schema is available at the expected URL

## Deploying to Hugging Face Spaces

To make your server available to others, you can deploy it to Hugging Face Spaces:

1. Create a new Space on Hugging Face:
   - Go to huggingface.co/spaces
   - Click "Create new Space"
   - Choose "Gradio" as the SDK
   - Name your space (e.g., "mcp-sentiment")

2. Create a `requirements.txt` file:
```txt
gradio[mcp]
textblob
```

3. Push your code to the Space:
```bash
git init
git add app.py requirements.txt
git commit -m "Initial commit"
git remote add origin https://huggingface.co/spaces/YOUR_USERNAME/mcp-sentiment
git push -u origin main
```

Your MCP server will now be available at:
```
https://YOUR_USERNAME-mcp-sentiment.hf.space/gradio_api/mcp/sse
```

## Next Steps

Now that we have our MCP server running, we'll create clients to interact with it. In the next sections, we'll:

1. Create a HuggingFace.js-based client inspired by Tiny Agents
2. Implement a SmolAgents-based Python client
3. Test both clients with our deployed server

Let's move on to building our first client!
````

## File: units/en/unit3/certificate.mdx
````
# Get your certificate!

Well done! You've completed Unit 3 of the MCP course. Now it's time to take the exam to get your certificate.

Below is a quiz to check your understanding of the unit. 

<iframe
	src="https://mcp-course-unit-3-quiz.hf.space"
	frameborder="0"
	width="850"
	height="450"
></iframe>

<Tip>

If you're struggling to use the quiz above, go to the space directly [on the Hugging Face Hub](https://huggingface.co/spaces/mcp-course/unit_3_quiz). If you find errors, you can report them in the space's [Community tab](https://huggingface.co/spaces/mcp-course/unit_3_quiz/discussions).

</Tip>
````

## File: units/en/unit3_1/introduction.mdx
````
# Build a Pull Request Agent on the Hugging Face Hub

Welcome to Unit 3 of the MCP Course! 

In this unit, we'll build a pull request agent that automatically tags Hugging Face model repositories based on discussions and comments. This real-world application demonstrates how to integrate MCP with webhook listeners and automated workflows.

<Tip>

This unit showcases a real world use case where MCP servers can respond to real-time events from the Hugging Face Hub, automatically creating pull requests to improve repository metadata.

</Tip>

## What You'll Learn

In this unit, you will:

- Create an MCP Server that interacts with the Hugging Face Hub API
- Implement webhook listeners to respond to discussion events
- Set up automated tagging workflows for model repositories
- Deploy a complete webhook-driven application to Hugging Face Spaces

By the end of this unit, you'll have a working PR agent that can monitor discussions and automatically improve repository metadata through pull requests.

## Prerequisites

Before proceeding with this unit, make sure you:

- Have completed Units 1 and 2, or have experience with MCP concepts
- Are comfortable with Python, FastAPI, and webhook concepts
- Have a basic understanding of Hugging Face Hub workflows and pull requests
- Have a development environment with:
  - Python 3.11+
  - A Hugging Face account with API access

## Our Pull Request Agent Project

We'll build a tagging agent that consists of four main components: the MCP server, webhook listener, agent logic, and deployment infrastructure. The agent will be able to tag model repositories based on discussions and comments. This should save model authors time by receiving ready to use PRs, instead of having to manually tag their repositories.

![PR Agent Architecture](https://huggingface.co/datasets/mcp-course/images/resolve/main/unit3/architecture.png)

In the diagram above, we have a MCP server that can read and update model tags. We have a webhook listener that can receive webhooks from the Hugging Face Hub. We have an agent that can analyze discussions and comments and create PRs to update model tags. We have a deployment infrastructure that can deploy the MCP server to Hugging Face Spaces.

### Project Overview

  To build this application we will need the following files:

| File | Purpose | Description |
|------|---------|-------------|
| `mcp_server.py` | **Core MCP Server** | FastMCP-based server with tools for reading and updating model tags |
| `app.py` | **Webhook Listener & Agent** | FastAPI app that receives webhooks, processes discussions, and creates PRs |
| `requirements.txt` | **Dependencies** | Python packages including FastMCP, FastAPI, and huggingface-hub |
| `pyproject.toml` | **Project Configuration** | Modern Python packaging with uv dependency management |
| `Dockerfile` | **Deployment** | Container configuration for Hugging Face Spaces |
| `env.example` | **Configuration Template** | Required environment variables and secrets |
| `cleanup.py` | **Utility** | Helper script for development and testing cleanup |

Let's go through each of these files and understand their purpose.

### MCP Server (`mcp_server.py`)

The heart of our application - a FastMCP server that provides tools for:
- Reading current tags from model repositories
- Adding new tags via pull requests to the Hub
- Error handling and validation

This is where you will implement the MCP server and do most of the work for this project. The Gradio app and FastAPI app will be used to test the MCP server and the webhook listener, and they are ready to use.

### Webhook Integration

Following the [Hugging Face Webhooks Guide](https://huggingface.co/docs/hub/webhooks-guide-discussion-bot), our agent:
- Listens for discussion comment events
- Validates webhook signatures for security
- Processes mentions and tag suggestions
- Creates pull requests automatically

### Agent Functionality

The agent analyzes discussion content to:
- Extract explicit tag mentions (`tag: pytorch`, `#transformers`)
- Recognize implicit tags from natural language
- Validate tags against known ML/AI categories
- Generate appropriate pull request descriptions

### Deployment & Production

- Containerized deployment to Hugging Face Spaces
- Environment variable management for secrets
- Background task processing for webhook responses
- Gradio interface for testing and monitoring

## Webhook Integration Overview

Our PR agent leverages the same webhook infrastructure used by Hugging Face's discussion bots. Here's how webhooks enable real-time responses:

![Webhook Flow](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/hub/webhooks-guides/001-discussion-bot/webhook-creation.png)

The webhook flow works as follows:
1. **Event Trigger**: A user creates a comment in a model repository discussion
2. **Webhook Delivery**: Hugging Face sends a POST request to our endpoint
3. **Authentication**: We validate the webhook secret for security
4. **Processing**: Our agent analyzes the comment for tag suggestions
5. **Action**: If relevant tags are found, we create a pull request
6. **Response**: The webhook returns immediately while PR creation happens in the background

## Let's Get Started!

Ready to build a production-ready PR agent that can automatically improve Hugging Face repositories? Let's begin by setting up the project structure and understanding the MCP server implementation.
````

## File: units/en/unit3_1/mcp-client.mdx
````
# MCP Client

Now that we have our MCP server with tagging tools, we need to create a client that can interact with these tools. The MCP client serves as the bridge between our webhook handler and the MCP server, enabling our agent to use the Hub tagging functionality.

For the sake of this project, we'll build both an API and a Gradio app. The API will be used to test the MCP server and the webhook listener, and the Gradio app will be used to test the MCP client with simulated webhook events.

<Tip>

For educational purposes, we will build the MCP Server and MCP Client in the same repo. In a real-world application, you would likely have a separate repo for the MCP Server and MCP Client. In fact, you might only build one of these components.

</Tip>

## Understanding the MCP Client Architecture

In our application, the MCP client is integrated into the main FastAPI application (`app.py`). It creates and manages connections to our MCP server, providing a seamless interface for tool execution.

![MCP Client Integration](https://huggingface.co/datasets/mcp-course/images/resolve/main/unit3/app.png)

## Agent-Based MCP Client

We use the `huggingface_hub` Agent class that has built-in MCP support. This provides both language model capabilities and MCP tool integration in a single component.

### 1. Agent Configuration

Let's start by setting up the agent configuration and understanding each component:

```python
from huggingface_hub.inference._mcp.agent import Agent
from typing import Optional, Literal

# Configuration
HF_TOKEN = os.getenv("HF_TOKEN")
HF_MODEL = os.getenv("HF_MODEL", "microsoft/DialoGPT-medium")
DEFAULT_PROVIDER: Literal["hf-inference"] = "hf-inference"

# Global agent instance
agent_instance: Optional[Agent] = None
```

We start with the necessary imports and configuration. The global `agent_instance` variable ensures we create the agent only once and reuse it across multiple requests. This is important for performance since agent initialization can be expensive.

Now let's implement the function that creates and manages our agent:

```python
async def get_agent():
    """Get or create Agent instance"""
    print("🤖 get_agent() called...")
    global agent_instance
    if agent_instance is None and HF_TOKEN:
        print("🔧 Creating new Agent instance...")
        print(f"🔑 HF_TOKEN present: {bool(HF_TOKEN)}")
        print(f"🤖 Model: {HF_MODEL}")
        print(f"🔗 Provider: {DEFAULT_PROVIDER}")
```

The function starts by checking if we already have an agent instance. This singleton pattern prevents unnecessary recreations and ensures consistent state.

Let's continue with the agent creation:

```python
        try:
            agent_instance = Agent(
                model=HF_MODEL,
                provider=DEFAULT_PROVIDER,
                api_key=HF_TOKEN,
                servers=[
                    {
                        "type": "stdio",
                        "config": {
                            "command": "python",
                            "args": ["mcp_server.py"],
                            "cwd": ".",
                            "env": {"HF_TOKEN": HF_TOKEN} if HF_TOKEN else {},
                        },
                    }
                ],
            )
            print("✅ Agent instance created successfully")
            print("🔧 Loading tools...")
            await agent_instance.load_tools()
            print("✅ Tools loaded successfully")
        except Exception as e:
            print(f"❌ Error creating/loading agent: {str(e)}")
            agent_instance = None
```

This is where the important part happens! Let's break down the Agent configuration:

**Agent Parameters:**
- `model`: The language model that will reason about tool usage
- `provider`: How to access the model (Hugging Face Inference Providers)
- `api_key`: Hugging Face API key

**MCP Server Connection:**
- `type: "stdio"`: Connect to the MCP server via standard input/output
- `command: "python"`: Run our MCP server as a Python subprocess
- `args: ["mcp_server.py"]`: The script file to execute
- `env`: Pass the HF_TOKEN to the server process

<Tip>

The `stdio` connection type means the agent starts your MCP server as a subprocess and communicates with it through standard input/output. This is perfect for development and single-machine deployments.

</Tip>

The `load_tools()` call is crucial - it discovers what tools are available from the MCP server and makes them accessible to the agent's reasoning engine.

This completes our agent management function with proper error handling and logging.

## Tool Discovery and Usage

Once the agent is created and tools are loaded, it can automatically discover and use the MCP tools. This is where the real power of the Agent approach shines.

### Available Tools

The agent discovers our MCP tools automatically:
- `get_current_tags(repo_id: str)` - Retrieve existing repository tags
- `add_new_tag(repo_id: str, new_tag: str)` - Add new tag via pull request

The agent doesn't just call these tools blindly - it reasons about when and how to use them based on the prompt you give it.

### Tool Execution Example

Here's how the agent intelligently uses tools:

```python
# Example of how the agent would use tools
async def example_tool_usage():
    agent = await get_agent()
    
    if agent:
        # The agent can reason about which tools to use
        response = await agent.run(
            "Check the current tags for microsoft/DialoGPT-medium and add the tag 'conversational-ai' if it's not already present"
        )
        print(response)
```

Notice how we give the agent a natural language instruction, and it figures out:
1. First call `get_current_tags` to see what tags exist
2. Check if `conversational-ai` is already there
3. If not, call `add_new_tag` to add it
4. Provide a summary of what it did

This is much more intelligent than calling tools directly!

## Integration with Webhook Processing

Now let's see how the MCP client integrates into our webhook processing pipeline. This is where everything comes together.

### 1. Tag Extraction and Processing

Here's the main function that processes webhook events and uses our MCP agent:

```python
async def process_webhook_comment(webhook_data: Dict[str, Any]):
    """Process webhook to detect and add tags"""
    print("🏷️ Starting process_webhook_comment...")

    try:
        comment_content = webhook_data["comment"]["content"]
        discussion_title = webhook_data["discussion"]["title"]
        repo_name = webhook_data["repo"]["name"]
        
        # Extract potential tags from the comment and discussion title
        comment_tags = extract_tags_from_text(comment_content)
        title_tags = extract_tags_from_text(discussion_title)
        all_tags = list(set(comment_tags + title_tags))

        print(f"🔍 All unique tags: {all_tags}")

        if not all_tags:
            return ["No recognizable tags found in the discussion."]
```

This first part extracts and combines tags from both the comment content and discussion title. We use a set to deduplicate any tags that appear in both places.

<Tip>

Processing both the comment and discussion title increases our chances of catching relevant tags. Users might mention tags in the title like "Missing pytorch tag" or in comments like "This needs #transformers".

</Tip>

Next, we get our agent and process each tag:

```python
        # Get agent instance
        agent = await get_agent()
        if not agent:
            return ["Error: Agent not configured (missing HF_TOKEN)"]

        # Process each tag
        result_messages = []
        for tag in all_tags:
            try:
                # Use agent to process the tag
                prompt = f"""
                For the repository '{repo_name}', check if the tag '{tag}' already exists.
                If it doesn't exist, add it via a pull request.
                
                Repository: {repo_name}
                Tag to check/add: {tag}
                """
                
                print(f"🤖 Processing tag '{tag}' for repo '{repo_name}'")
                response = await agent.run(prompt)
                
                # Parse agent response for success/failure
                if "success" in response.lower():
                    result_messages.append(f"✅ Tag '{tag}' processed successfully")
                else:
                    result_messages.append(f"⚠️ Issue with tag '{tag}': {response}")
                    
            except Exception as e:
                error_msg = f"❌ Error processing tag '{tag}': {str(e)}"
                print(error_msg)
                result_messages.append(error_msg)

        return result_messages
```

The key insight here is that we give the agent a clear, structured prompt for each tag. The agent then:
1. Understands it needs to check the current tags first
2. Compares with the new tag we want to add
3. Creates a pull request if needed
4. Returns a summary of its actions

This approach handles the complexity of tool orchestration automatically.

### 2. Tag Extraction Logic

Let's examine the tag extraction logic that feeds into our MCP processing:

```python
import re
from typing import List

# Recognized ML/AI tags for validation
RECOGNIZED_TAGS = {
    "pytorch", "tensorflow", "jax", "transformers", "diffusers",
    "text-generation", "text-classification", "question-answering",
    "text-to-image", "image-classification", "object-detection",
    "fill-mask", "token-classification", "translation", "summarization",
    "feature-extraction", "sentence-similarity", "zero-shot-classification",
    "image-to-text", "automatic-speech-recognition", "audio-classification",
    "voice-activity-detection", "depth-estimation", "image-segmentation",
    "video-classification", "reinforcement-learning", "tabular-classification",
    "tabular-regression", "time-series-forecasting", "graph-ml", "robotics",
    "computer-vision", "nlp", "cv", "multimodal",
}
```

This curated list of recognized tags helps us focus on relevant ML/AI tags and avoid adding inappropriate tags to repositories.

Now the extraction function itself:

```python
def extract_tags_from_text(text: str) -> List[str]:
    """Extract potential tags from discussion text"""
    text_lower = text.lower()
    explicit_tags = []

    # Pattern 1: "tag: something" or "tags: something"
    tag_pattern = r"tags?:\s*([a-zA-Z0-9-_,\s]+)"
    matches = re.findall(tag_pattern, text_lower)
    for match in matches:
        tags = [tag.strip() for tag in match.split(",")]
        explicit_tags.extend(tags)

    # Pattern 2: "#hashtag" style
    hashtag_pattern = r"#([a-zA-Z0-9-_]+)"
    hashtag_matches = re.findall(hashtag_pattern, text_lower)
    explicit_tags.extend(hashtag_matches)

    # Pattern 3: Look for recognized tags mentioned in natural text
    mentioned_tags = []
    for tag in RECOGNIZED_TAGS:
        if tag in text_lower:
            mentioned_tags.append(tag)

    # Combine and deduplicate
    all_tags = list(set(explicit_tags + mentioned_tags))

    # Filter to only include recognized tags or explicitly mentioned ones
    valid_tags = []
    for tag in all_tags:
        if tag in RECOGNIZED_TAGS or tag in explicit_tags:
            valid_tags.append(tag)

    return valid_tags
```

This function uses multiple strategies to extract tags:

1. **Explicit patterns**: "tags: pytorch, transformers" or "tag: nlp"
2. **Hashtags**: "#pytorch #nlp"
3. **Natural mentions**: "This transformers model does text-generation"

The validation step ensures we only suggest appropriate tags, preventing spam or irrelevant tags from being added.


## Performance Considerations

When building production MCP clients, performance is critical for maintaining responsive webhook processing. Let's look at some of the considerations we've made.

### 1. Agent Singleton Pattern

The agent is created once and reused to avoid:
- Repeated MCP server startup overhead
- Tool loading delays
- Connection establishment costs

This pattern is essential for webhook handlers that need to respond quickly.

### 2. Async Processing

All MCP operations are async to:
- Handle multiple webhook requests concurrently
- Avoid blocking the main FastAPI thread
- Provide responsive webhook responses

The async nature allows your webhook handler to accept new requests while processing tags in the background.

### 3. Background Task Processing

FastAPI has a built in `BackgroundTasks` class that can be used to run tasks in the background. This is useful for running long running tasks without blocking the main thread.

```python
from fastapi import BackgroundTasks

@app.post("/webhook")
async def webhook_handler(request: Request, background_tasks: BackgroundTasks):
    """Handle webhook and process in background"""
    
    # Validate webhook quickly
    if request.headers.get("X-Webhook-Secret") != WEBHOOK_SECRET:
        return {"error": "Invalid secret"}
    
    webhook_data = await request.json()
    
    # Process in background to return quickly
    background_tasks.add_task(process_webhook_comment, webhook_data)
    
    return {"status": "accepted"}
```

This pattern ensures webhook responses are fast (under 1 second) while allowing complex tag processing to happen in the background.

<Tip>

Webhook endpoints should respond within 10 seconds or the platform may consider them timed out. Using background tasks ensures you can always respond quickly while handling complex processing asynchronously.

</Tip>

## Next Steps

With our MCP client implemented, we can now:

1. **Implement the Webhook Listener** - Create the FastAPI endpoint that receives Hub events
2. **Integrate Everything** - Connect webhooks, client, and server into a complete system
3. **Add Testing Interface** - Create a Gradio interface for development and monitoring
4. **Deploy and Test** - Validate the complete system in production

In the next section, we'll implement the webhook listener that will trigger our MCP-powered tagging agent.

<Tip>

The Agent class from `huggingface_hub` provides both MCP tool integration and language model reasoning, making it perfect for building intelligent automation workflows like our PR agent.

</Tip>
````

## File: units/en/unit3_1/quiz1.mdx
````
# Quiz 1: MCP Server Implementation

Test your knowledge of MCP server concepts and implementation for the Pull Request Agent.

### Q1: What is the primary role of an MCP Server in the Pull Request Agent architecture?

<Question
  choices={[
    {
      text: "To host the user interface for the application",
      explain: "The MCP Server provides backend capabilities, not the user interface."
    },
    {
      text: "To expose tools and resources that the AI agent can use to interact with GitHub",
      explain: "Close, but this project focuses on the Hugging Face Hub, not GitHub."
    },
    {
      text: "To expose tools for reading and updating model repository tags on the Hugging Face Hub",
      explain: "Correct! The MCP Server provides get_current_tags and add_new_tag tools for Hub interactions.",
      correct: true
    },
    {
      text: "To train the AI model on pull request data",
      explain: "MCP Servers provide runtime capabilities, not model training functionality."
    }
  ]}
/>

### Q2: In the FastMCP implementation, why must all MCP tool functions return strings instead of Python objects?

<Question
  choices={[
    {
      text: "To improve performance by reducing memory usage",
      explain: "While strings might be more memory efficient, this is not the primary reason."
    },
    {
      text: "To ensure reliable data exchange between the MCP server and client",
      explain: "Correct! MCP protocol requires string responses, so we use json.dumps() to serialize data.",
      correct: true
    },
    {
      text: "To make the code easier to debug",
      explain: "While JSON strings are readable, this is not the primary technical requirement."
    },
    {
      text: "To comply with Hugging Face Hub API requirements",
      explain: "This is an MCP protocol requirement, not specific to the Hub API."
    }
  ]}
/>

### Q3: When implementing the `add_new_tag` tool, what is the purpose of checking if a tag already exists before creating a pull request?

<Question
  choices={[
    {
      text: "To reduce API calls and improve performance",
      explain: "While this helps performance, it's not the primary reason for the check."
    },
    {
      text: "To prevent creating duplicate pull requests and provide better user feedback",
      explain: "Correct! This validation prevents unnecessary PRs and returns meaningful status messages.",
      correct: true
    },
    {
      text: "To comply with Hugging Face Hub rate limits",
      explain: "While avoiding unnecessary calls helps with rate limits, this is not the primary purpose."
    },
    {
      text: "To ensure the tag format is valid",
      explain: "Tag validation is separate from checking if it already exists."
    }
  ]}
/>

### Q4: In the MCP server implementation, what happens when a model repository doesn't have an existing README.md file?

<Question
  choices={[
    {
      text: "The add_new_tag tool will fail with an error",
      explain: "The implementation handles this case gracefully."
    },
    {
      text: "The tool creates a new ModelCard with ModelCardData and proceeds with the tag addition",
      explain: "Correct! The code handles HfHubHTTPError and creates a new model card when none exists.",
      correct: true
    },
    {
      text: "The tool skips adding the tag and returns a warning",
      explain: "The tool doesn't skip the operation - it creates what's needed."
    },
    {
      text: "The tool automatically creates a default README with placeholder content",
      explain: "It creates a minimal model card structure, not placeholder content."
    }
  ]}
/>

### Q5: What is the significance of using `create_pr=True` in the `hf_api.create_commit()` function call?

<Question
  choices={[
    {
      text: "It makes the commit directly to the main branch",
      explain: "Setting create_pr=True creates a pull request, not a direct commit to main."
    },
    {
      text: "It automatically creates a pull request instead of committing directly to the main branch",
      explain: "Correct! This enables the review workflow and follows repository governance practices.",
      correct: true
    },
    {
      text: "It creates a private branch that only the repository owner can see",
      explain: "Pull requests are visible to repository collaborators and can be public."
    },
    {
      text: "It validates the commit before creating it",
      explain: "Validation happens regardless of the create_pr parameter."
    }
  ]}
/>

### Q6: Why does the MCP server implementation use extensive logging with emojis throughout the code?

<Question
  choices={[
    {
      text: "To make the code more fun and engaging for developers",
      explain: "While emojis are visually appealing, there's a more practical reason."
    },
    {
      text: "To help with debugging and monitoring when the server runs autonomously in response to Hub events",
      explain: "Correct! Since the agent responds to webhooks automatically, detailed logs are crucial for troubleshooting.",
      correct: true
    },
    {
      text: "To comply with FastMCP logging requirements",
      explain: "FastMCP doesn't require specific logging formats or emojis."
    },
    {
      text: "To reduce the amount of text in log files",
      explain: "Emojis don't significantly reduce log file size and this isn't the primary goal."
    }
  ]}
/>

Congrats on finishing this Quiz 🥳! If you need to review any elements, take the time to revisit the chapter to reinforce your knowledge.
````

## File: units/en/unit3_1/quiz2.mdx
````
# Quiz 2: Pull Request Agent Integration

Test your knowledge of the complete Pull Request Agent system including MCP client integration and webhook handling.

### Q1: What is the primary purpose of the webhook listener in the Pull Request Agent architecture?

<Question
  choices={[
    {
      text: "To provide a user interface for managing pull requests",
      explain: "The webhook listener handles GitHub events, not user interfaces."
    },
    {
      text: "To receive and process Hugging Face Hub discussion comment events in real-time",
      explain: "Correct! The webhook listener responds to Hub discussion events to trigger agent actions.",
      correct: true
    },
    {
      text: "To store pull request data permanently in a database",
      explain: "While it may process PR data, its primary role is event handling, not storage."
    },
    {
      text: "To authenticate users with the Hugging Face Hub",
      explain: "Webhook listeners handle events, not user authentication."
    }
  ]}
/>

### Q2: In the Agent-based MCP client implementation, how does the client connect to the MCP server?

<Question
  choices={[
    {
      text: "Through direct function calls in the same process",
      explain: "The Agent uses subprocess communication, not direct function calls."
    },
    {
      text: "Using stdio connection type to communicate with the MCP server as a subprocess",
      explain: "Correct! The Agent starts the MCP server with 'python mcp_server.py' and communicates via stdin/stdout.",
      correct: true
    },
    {
      text: "By writing files to a shared directory",
      explain: "MCP uses real-time communication, not file-based communication."
    },
    {
      text: "Through HTTP REST API calls",
      explain: "The stdio connection type doesn't use HTTP - it uses standard input/output streams."
    }
  ]}
/>

### Q3: Why does the webhook handler use FastAPI's `background_tasks.add_task()` instead of processing requests synchronously?

<Question
  choices={[
    {
      text: "To reduce server memory usage",
      explain: "Background tasks don't necessarily reduce memory usage."
    },
    {
      text: "To comply with Hugging Face Hub requirements",
      explain: "While Hub expects timely responses, this isn't a specific Hub requirement."
    },
    {
      text: "To return responses quickly (within 10 seconds) while allowing complex tag processing in the background",
      explain: "Correct! Webhook endpoints must respond quickly or be considered failed by the sending platform.",
      correct: true
    },
    {
      text: "To enable multiple webhook requests to be processed in parallel",
      explain: "While this enables parallelism, the primary reason is response time requirements."
    }
  ]}
/>

### Q4: What is the purpose of validating the `X-Webhook-Secret` header in the webhook handler?

<Question
  choices={[
    {
      text: "To identify which repository sent the webhook",
      explain: "Repository information comes from the webhook payload, not the secret header."
    },
    {
      text: "To prevent unauthorized requests and ensure the webhook is legitimate from Hugging Face",
      explain: "Correct! The shared secret acts as authentication between Hugging Face and your application.",
      correct: true
    },
    {
      text: "To decode the webhook payload data",
      explain: "The secret is for authentication, not for decoding payload data."
    },
    {
      text: "To determine which MCP tools to use",
      explain: "Tool selection is based on the webhook content, not the secret header."
    }
  ]}
/>

### Q5: In the Agent implementation, what happens when `await agent_instance.load_tools()` is called?

<Question
  choices={[
    {
      text: "It downloads tools from the Hugging Face Hub",
      explain: "The tools are local MCP server tools, not downloaded from the Hub."
    },
    {
      text: "It discovers and makes available the MCP tools from the connected server (get_current_tags and add_new_tag)",
      explain: "Correct! This discovers what tools the MCP server provides and makes them available to the agent's reasoning engine.",
      correct: true
    },
    {
      text: "It starts the FastAPI webhook server",
      explain: "load_tools() is specific to MCP tool discovery, not starting web servers."
    },
    {
      text: "It authenticates with the Hugging Face API",
      explain: "Authentication happens during agent creation, not during tool loading."
    }
  ]}
/>

### Q6: How does the Agent intelligently use MCP tools when processing a natural language instruction?

<Question
  choices={[
    {
      text: "It randomly calls available tools until one works",
      explain: "The Agent uses reasoning to determine which tools to call and in what order."
    },
    {
      text: "It always calls get_current_tags first, then add_new_tag second",
      explain: "While this might be a common pattern, the Agent reasons about which tools to use based on the instruction."
    },
    {
      text: "It reasons about the instruction and determines which tools to call and in what sequence",
      explain: "Correct! The Agent can understand complex instructions and create tool execution plans automatically.",
      correct: true
    },
    {
      text: "It requires explicit function calls to be specified in the instruction",
      explain: "The Agent can work with natural language instructions without explicit function specifications."
    }
  ]}
/>

### Q7: What filtering logic determines whether a webhook event should trigger tag processing?

<Question
  choices={[
    {
      text: "All webhook events are processed regardless of type",
      explain: "The handler filters events to only process relevant ones."
    },
    {
      text: "Only events where action='create' and scope='discussion.comment'",
      explain: "Correct! This ensures we only process new discussion comments, ignoring other Hub events.",
      correct: true
    },
    {
      text: "Only events from verified repository owners",
      explain: "The filtering is based on event type, not user verification status."
    },
    {
      text: "Only events that contain the word 'tag' in the comment",
      explain: "Event filtering happens before content analysis - we filter by event type first."
    }
  ]}
/>

Congrats on finishing this Quiz 🥳! If you need to review any elements, take the time to revisit the chapter to reinforce your knowledge.
````

## File: units/en/unit3_1/setting-up-the-project.mdx
````
# Setting up the Project

In this section, we'll set up the development environment for our Pull Request Agent. 

<Tip>

We'll use modern Python tooling with `uv` for dependency management and create the necessary configuration files. If you're not familiar with `uv`, you can learn more about it [here](https://docs.astral.sh/uv/).

</Tip>


## Project Structure

Let's start by creating the project directory and understanding the file structure:

```bash
git clone https://huggingface.co/spaces/mcp-course/tag-this-repo
```

Our final project structure will look like this:

```
hf-pr-agent/
├── mcp_server.py              # Core MCP server with tagging tools
├── app.py                     # FastAPI webhook listener and agent
├── requirements.txt           # Python dependencies
├── pyproject.toml             # Project configuration
├── env.example                # Environment variables template
├── cleanup.py                 # Development utility
```

## Dependencies and Configuration

Let's walk through the dependencies and configuration for our project. 

### 1. Python Project Configuration

We will use `uv` to create the `pyproject.toml` file to define our project:

<Tip>

If you don't have `uv` installed, you can follow the instructions [here](https://docs.astral.sh/uv/getting-started/installation/).

</Tip>

```toml
[project]
name = "mcp-course-unit3-example"
version = "0.1.0"
description = "FastAPI and Gradio app for Hugging Face Hub discussion webhooks"
readme = "README.md"
requires-python = ">=3.11"
dependencies = [
    "fastapi>=0.104.0",
    "uvicorn[standard]>=0.24.0",
    "gradio>=4.0.0",
    "huggingface-hub[mcp]>=0.32.0",
    "pydantic>=2.0.0",
    "python-multipart>=0.0.6",
    "requests>=2.31.0",
    "python-dotenv>=1.0.0",
    "fastmcp>=2.0.0",
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["src"]
```

For compatibility with various deployment platforms, the same is repeated in `requirements.txt`

To create a virtual environment, run:

```bash
uv venv
source .venv/bin/activate # or .venv/Scripts/activate on Windows
```

To install the dependencies, run:

```bash
uv sync
```

### 2. Environment Configuration

Create `env.example` to document required environment variables:

```bash
# Hugging Face API Token (required)
# Get from: https://huggingface.co/settings/tokens
HF_TOKEN=hf_your_token_here

# Webhook Secret (required for production)
# Use a strong, random string
WEBHOOK_SECRET=your-webhook-secret-here

# Model for the agent (optional)
HF_MODEL=owner/model

# Provider for MCP agent (optional)
HF_PROVIDER=huggingface
```

You will need to get your Hugging Face API token from [here](https://huggingface.co/settings/tokens).

You will also need to generate a webhook secret. You can do this by running the following command:

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

You will then need to add the webhook secret to your `.env` file based on the `env.example` file.

## Next Steps

With our project structure and environment set up, we're ready to:

1. **Create the MCP Server** - Implement the core tagging functionality
2. **Build the Webhook Listener** - Handle incoming discussion events
3. **Integrate the Agent** - Connect MCP tools with webhook processing
4. **Test and Deploy** - Validate functionality and deploy to Spaces

In the next section, we'll dive into creating our MCP server that will handle all the Hugging Face Hub interactions.

<Tip>

Keep your `.env` file secure and never commit it to version control. The `.env` file should be added to your `.gitignore` file to prevent accidental exposure of secrets.

</Tip>
````

## File: units/en/unit3_1/webhook-listener.mdx
````
# Webhook Listener

The webhook listener is the entry point for our Pull Request Agent. It receives real-time events from the Hugging Face Hub when discussions are created or updated, triggering our MCP-powered tagging workflow. In this section, we'll implement a webhook handler using FastAPI.

## Understanding Webhook Integration

Following the [Hugging Face Webhooks Guide](https://raw.githubusercontent.com/huggingface/hub-docs/refs/heads/main/docs/hub/webhooks-guide-discussion-bot.md), our webhook listener validates incoming requests and processes discussion events in real-time.

![Webhook Creation](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/hub/webhooks-guides/001-discussion-bot/webhook-creation.png)

### Webhook Event Flow

Understanding the webhook flow is crucial for building a reliable listener:

1. **User Action**: Someone creates a comment in a model repository discussion
2. **Hub Event**: Hugging Face generates a webhook event
3. **Webhook Delivery**: Hub sends POST request to our endpoint
4. **Authentication**: We validate the webhook secret
5. **Processing**: Extract tags from the comment content
6. **Action**: Use MCP tools to create pull requests for new tags

<Tip>

Webhooks are push notifications - the Hugging Face Hub actively sends events to your application rather than you polling for changes. This enables real-time responses to discussions and comments.

</Tip>

## FastAPI Webhook Application

Let's build our webhook listener step by step, starting with the foundation and building up to the complete processing logic.

### 1. Application Setup

First, let's set up the basic FastAPI application with all necessary imports and configuration:

```python
import os
import json
from datetime import datetime
from typing import List, Dict, Any, Optional

from fastapi import FastAPI, Request, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
```

These imports give us everything we need to build a robust webhook handler. `FastAPI` provides the web framework, `BackgroundTasks` enables async processing, and the typing imports help with data validation.

Now let's configure our application:

```python
# Configuration
WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET")
HF_TOKEN = os.getenv("HF_TOKEN")

# Simple storage for processed operations
tag_operations_store: List[Dict[str, Any]] = []

app = FastAPI(title="HF Tagging Bot")
app.add_middleware(CORSMiddleware, allow_origins=["*"])
```

This configuration sets up:
- **Webhook secret**: For validating incoming webhooks
- **HF token**: For authenticating with the Hub API
- **Operations store**: In-memory storage for monitoring processed operations
- **CORS middleware**: Allows cross-origin requests for the web interface

<Tip>
The `tag_operations_store` list keeps track of recent webhook processing operations. This is useful for debugging and monitoring, but in production you might want to use a database or limit the size of this list.
</Tip>

### 2. Webhook Data Models

Based on the [Hugging Face webhook documentation](https://raw.githubusercontent.com/huggingface/hub-docs/refs/heads/main/docs/hub/webhooks-guide-discussion-bot.md), we need to understand the webhook data structure:

```python
class WebhookEvent(BaseModel):
    event: Dict[str, str]          # Contains action and scope information
    comment: Dict[str, Any]        # Comment content and metadata
    discussion: Dict[str, Any]     # Discussion information
    repo: Dict[str, str]           # Repository details
```

This Pydantic model helps us understand the webhook structure.

The key fields we care about are:
- `event.action`: Usually "create" for new comments
- `event.scope`: Usually "discussion.comment" for comment events
- `comment.content`: The actual comment text
- `repo.name`: The repository where the comment was made

### 3. Core Webhook Handler

Now for the main webhook handler - this is where the important part happens. Let's break it down into digestible pieces:

```python
@app.post("/webhook")
async def webhook_handler(request: Request, background_tasks: BackgroundTasks):
    """
    Handle incoming webhooks from Hugging Face Hub
    Following the pattern from: https://raw.githubusercontent.com/huggingface/hub-docs/refs/heads/main/docs/hub/webhooks-guide-discussion-bot.md
    """
    print("🔔 Webhook received!")
    
    # Step 1: Validate webhook secret (security)
    webhook_secret = request.headers.get("X-Webhook-Secret")
    if webhook_secret != WEBHOOK_SECRET:
        print("❌ Invalid webhook secret")
        return {"error": "incorrect secret"}, 400
```

The first step is security validation. We check the `X-Webhook-Secret` header against our configured secret to ensure the webhook is legitimate.

<Tip>

Always validate webhook secrets! Without this check, anyone could send fake webhook requests to your application. The secret acts as a shared password between Hugging Face and your application.

</Tip>

Next, let's parse and validate the webhook data:

```python
    # Step 2: Parse webhook data
    try:
        webhook_data = await request.json()
        print(f"📥 Webhook data: {json.dumps(webhook_data, indent=2)}")
    except Exception as e:
        print(f"❌ Error parsing webhook data: {str(e)}")
        return {"error": "invalid JSON"}, 400
    
    # Step 3: Validate event structure
    event = webhook_data.get("event", {})
    if not event:
        print("❌ No event data in webhook")
        return {"error": "missing event data"}, 400
```

This parsing step handles potential JSON errors gracefully and validates that we have the expected event structure.

Now for the event filtering logic:

```python
    # Step 4: Check if this is a discussion comment creation
    # Following the webhook guide pattern:
    if (
        event.get("action") == "create" and 
        event.get("scope") == "discussion.comment"
    ):
        print("✅ Valid discussion comment creation event")
        
        # Process in background to return quickly to Hub
        background_tasks.add_task(process_webhook_comment, webhook_data)
        
        return {
            "status": "accepted",
            "message": "Comment processing started",
            "timestamp": datetime.now().isoformat()
        }
    else:
        print(f"ℹ️ Ignoring event: action={event.get('action')}, scope={event.get('scope')}")
        return {
            "status": "ignored",
            "reason": "Not a discussion comment creation"
        }
```

This filtering ensures we only process the events we care about - new discussion comments. We ignore other events like repository creation, model uploads, etc.

We use FastAPI's `background_tasks.add_task()` to process the webhook asynchronously. This allows us to return a response quickly (within seconds) while the actual tag processing happens in the background.

<Tip>

Webhook endpoints should respond within 10 seconds, or the sending platform may consider them failed. Using background tasks ensures fast responses while allowing complex processing to happen asynchronously.

</Tip>

### 4. Comment Processing Logic

Now let's implement the core comment processing function that does the actual tag extraction and MCP tool usage:

```python
async def process_webhook_comment(webhook_data: Dict[str, Any]):
    """
    Process webhook comment to detect and add tags
    Integrates with our MCP client for Hub interactions
    """
    print("🏷️ Starting process_webhook_comment...")
    
    try:
        # Extract comment and repository information
        comment_content = webhook_data["comment"]["content"]
        discussion_title = webhook_data["discussion"]["title"]
        repo_name = webhook_data["repo"]["name"]
        discussion_num = webhook_data["discussion"]["num"]
        comment_author = webhook_data["comment"]["author"].get("id", "unknown")
        
        print(f"📝 Comment from {comment_author}: {comment_content}")
        print(f"📰 Discussion: {discussion_title}")
        print(f"📦 Repository: {repo_name}")
```

This initial section extracts all the relevant information from the webhook data. We get both the comment content and discussion title since tags might be mentioned in either place.

Next, we extract and process the tags:

```python
        # Extract potential tags from comment and title
        comment_tags = extract_tags_from_text(comment_content)
        title_tags = extract_tags_from_text(discussion_title)
        all_tags = list(set(comment_tags + title_tags))
        
        print(f"🔍 Found tags: {all_tags}")
        
        # Store operation for monitoring
        operation = {
            "timestamp": datetime.now().isoformat(),
            "repo_name": repo_name,
            "discussion_num": discussion_num,
            "comment_author": comment_author,
            "extracted_tags": all_tags,
            "comment_preview": comment_content[:100] + "..." if len(comment_content) > 100 else comment_content,
            "status": "processing"
        }
        tag_operations_store.append(operation)
```

We combine tags from both sources and create an operation record for monitoring. This record tracks the progress of each webhook processing operation.

<Tip>

Storing operation records is crucial for debugging and monitoring. When something goes wrong, you can look at recent operations to understand what happened and why.

</Tip>

Now for the MCP agent integration:

```python
        if not all_tags:
            operation["status"] = "no_tags"
            operation["message"] = "No recognizable tags found"
            print("❌ No tags found to process")
            return
        
        # Get MCP agent for tag processing
        agent = await get_agent()
        if not agent:
            operation["status"] = "error"
            operation["message"] = "Agent not configured (missing HF_TOKEN)"
            print("❌ No agent available")
            return
        
        # Process each extracted tag
        operation["results"] = []
        for tag in all_tags:
            try:
                print(f"🤖 Processing tag '{tag}' for repo '{repo_name}'")
                
                # Create prompt for agent to handle tag processing
                prompt = f"""
                Analyze the repository '{repo_name}' and determine if the tag '{tag}' should be added.
                
                First, check the current tags using get_current_tags.
                If '{tag}' is not already present and it's a valid tag, add it using add_new_tag.
                
                Repository: {repo_name}
                Tag to process: {tag}
                
                Provide a clear summary of what was done.
                """
                
                response = await agent.run(prompt)
                print(f"🤖 Agent response for '{tag}': {response}")
                
                # Parse response and store result
                tag_result = {
                    "tag": tag,
                    "response": response,
                    "timestamp": datetime.now().isoformat()
                }
                operation["results"].append(tag_result)
                
            except Exception as e:
                error_msg = f"❌ Error processing tag '{tag}': {str(e)}"
                print(error_msg)
                operation["results"].append({
                    "tag": tag,
                    "error": str(e),
                    "timestamp": datetime.now().isoformat()
                })
        
        operation["status"] = "completed"
        print(f"✅ Completed processing {len(all_tags)} tags")
```

This section handles the core business logic:
1. **Validation**: Ensure we have tags to process and an available agent
2. **Processing**: For each tag, create a natural language prompt for the agent
3. **Recording**: Store all results for monitoring and debugging
4. **Error handling**: Gracefully handle errors for individual tags

The agent prompt is carefully crafted to instruct the AI on exactly what steps to take: check current tags first, then add the new tag if appropriate.


### 5. Health and Monitoring Endpoints

Besides the webhook handler, we need endpoints for monitoring and debugging. Let's add these essential endpoints:

```python
@app.get("/")
async def root():
    """Root endpoint with basic information"""
    return {
        "name": "HF Tagging Bot",
        "status": "running",
        "description": "Webhook listener for automatic model tagging",
        "endpoints": {
            "webhook": "/webhook",
            "health": "/health",
            "operations": "/operations"
        }
    }
```

The root endpoint provides basic information about your service and its available endpoints.

```python
@app.get("/health")
async def health_check():
    """Health check endpoint for monitoring"""
    agent = await get_agent()
    
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "components": {
            "webhook_secret": "configured" if WEBHOOK_SECRET else "missing",
            "hf_token": "configured" if HF_TOKEN else "missing",
            "mcp_agent": "ready" if agent else "not_ready"
        }
    }
```

The health check endpoint validates that all your components are properly configured. This is essential for production monitoring.

```python
@app.get("/operations")
async def get_operations():
    """Get recent tag operations for monitoring"""
    # Return last 50 operations
    recent_ops = tag_operations_store[-50:] if tag_operations_store else []
    return {
        "total_operations": len(tag_operations_store),
        "recent_operations": recent_ops
    }
```

The operations endpoint lets you see recent webhook processing activity, which is invaluable for debugging and monitoring.

<Tip>

Health and monitoring endpoints are crucial for production deployments. They help you quickly identify configuration issues and monitor your application's activity without digging through logs.

</Tip>

## Webhook Configuration on Hugging Face Hub

Now that we have our webhook listener ready, let's configure it on the Hugging Face Hub. This is where we connect our application to real repository events.

### 1. Create Webhook in Settings

Following the [webhook setup guide](https://huggingface.co/docs/hub/webhooks-guide-discussion-bot):

![Webhook Settings](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/hub/webhooks-guides/001-discussion-bot/webhook-creation.png)

Navigate to your [Hugging Face Settings](https://huggingface.co/settings/webhooks) and configure:

1. **Target Repositories**: Specify which repositories to monitor
2. **Webhook URL**: Your deployed application endpoint (e.g., `https://your-space.hf.space/webhook`)
3. **Secret**: Use the same secret from your `WEBHOOK_SECRET` environment variable
4. **Events**: Subscribe to "Community (PR & discussions)" events

<Tip>

Start with one or two test repositories before configuring webhooks for many repositories. This lets you validate your application works correctly before scaling up.

</Tip>

### 2. Space URL Configuration

For Hugging Face Spaces deployment, you'll need to get your direct URL:

![Direct URL](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/hub/webhooks-guides/001-discussion-bot/direct-url.png)

The process is:
1. Click "Embed this Space" in your Space settings
2. Copy the "Direct URL" 
3. Append `/webhook` to create your webhook endpoint
4. Update your webhook configuration with this URL

For example, if your Space URL is `https://username-space-name.hf.space`, your webhook endpoint would be `https://username-space-name.hf.space/webhook`.

![Space URL](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/hub/webhooks-guides/001-discussion-bot/direct-url.png)

## Testing the Webhook Listener

Testing is crucial before deploying to production. Let's walk through different testing approaches:

### 1. Local Testing

You can test your webhook handler locally using a simple script:

```python
# test_webhook_local.py
import requests
import json

# Test data matching webhook format
test_webhook_data = {
    "event": {
        "action": "create",
        "scope": "discussion.comment"
    },
    "comment": {
        "content": "This model needs tags: pytorch, transformers",
        "author": {"id": "test-user"}
    },
    "discussion": {
        "title": "Missing tags",
        "num": 1
    },
    "repo": {
        "name": "test-user/test-model"
    }
}

# Send test webhook
response = requests.post(
    "http://localhost:8000/webhook",
    json=test_webhook_data,
    headers={"X-Webhook-Secret": "your-test-secret"}
)

print(f"Status: {response.status_code}")
print(f"Response: {response.json()}")
```

This script simulates a real webhook request, allowing you to test your handler without waiting for real events.

### 2. Simulation Endpoint for Development

You can also add a simulation endpoint to your FastAPI application for easier testing:

```python
@app.post("/simulate_webhook")
async def simulate_webhook(
    repo_name: str, 
    discussion_title: str, 
    comment_content: str
) -> str:
    """Simulate webhook for testing purposes"""
    
    # Create mock webhook data
    mock_webhook_data = {
        "event": {
            "action": "create",
            "scope": "discussion.comment"
        },
        "comment": {
            "content": comment_content,
            "author": {"id": "test-user"}
        },
        "discussion": {
            "title": discussion_title,
            "num": 999
        },
        "repo": {
            "name": repo_name
        }
    }
    
    # Process the simulated webhook
    await process_webhook_comment(mock_webhook_data)
    
    return f"Simulated webhook processed for {repo_name}"
```

This endpoint makes it easy to test different scenarios through your application's interface.

<Tip>
Simulation endpoints are incredibly useful during development. They let you test different tag combinations and edge cases without creating actual repository discussions.
</Tip>

## Expected Webhook Result

When everything is working correctly, you should see results like the discussion bot example:

![Discussion Result](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/hub/webhooks-guides/001-discussion-bot/discussion-result.png)

<!-- This shows the bot responding to a discussion comment, creating a PR -->

This screenshot shows a successful webhook processing where the bot creates a pull request in response to a discussion comment.

## Next Steps

With our webhook listener implemented, we now have:

1. **Secure webhook validation** following Hugging Face best practices
2. **Real-time event processing** with background task handling
3. **MCP integration** for intelligent tag management
4. **Monitoring and debugging** capabilities

In the next section, we'll integrate everything into a complete Pull Request Agent that demonstrates the full workflow from webhook to PR creation.

<Tip>

Always return webhook responses quickly (within 10 seconds) to avoid timeouts. Use background tasks for longer processing operations like MCP tool execution and pull request creation.

</Tip>
````

## File: units/vi/unit1/mcp-clients.mdx
````
# MCP Clients

Giờ khi đã hiểu cơ bản về Giao Thức Ngữ Cảnh Mô Hình (MCP), chúng ta có thể khám phá vai trò quan trọng của Client MCP trong hệ sinh thái MCP.

Trong phần này của Chương 1, chúng ta sẽ khám phá vai trò thiết yếu của Client MCP trong hệ sinh thái MCP.

Trong phần này, các bạn sẽ:

* Hiểu Client MCP là gì và vai trò của chúng trong kiến trúc MCP
* Tìm hiểu về các trách nhiệm chính của Client MCP
* Khám phá các triển khai Client MCP chính
* Khám phá cách sử dụng triển khai Client MCP của Hugging Face
* Xem các ví dụ thực tế về cách sử dụng Client MCP

## Hiểu về Client MCP

Client MCP là thành phần quan trọng đóng vai trò cầu nối giữa các ứng dụng AI (Server) và các khả năng bên ngoài được cung cấp bởi Server MCP. Hãy hình dung Server như ứng dụng chính của bạn (ví dụ: trợ lý AI hoặc IDE) và Client như một mô-đun chuyên biệt trong Server đó chịu trách nhiệm xử lý các giao tiếp MCP.

## Client giao diện người dùng

Hãy bắt đầu bằng cách khám phá các Client giao diện người dùng có sẵn cho MCP.

### Client giao diện chat

Claude Desktop của Anthropic là một trong những Client MCP nổi bật nhất, cung cấp tích hợp với nhiều Server MCP khác nhau.

### Client phát triển tương tác

Triển khai Client MCP của Cursor cho phép trợ lý lập trình hỗ trợ AI thông qua tích hợp trực tiếp với các tính năng chỉnh sửa code. Nó hỗ trợ nhiều kết nối Server MCP và cung cấp khả năng gọi công cụ thời gian thực khi lập trình, biến nó thành công cụ mạnh mẽ cho các nhà phát triển.

Continue.dev là một ví dụ khác về Client phát triển tương tác hỗ trợ MCP và kết nối với Server MCP từ VS Code.

## Cấu hình Client MCP

Giờ khi đã nắm được phần cốt lõi của giao thức MCP, hãy xem cách cấu hình các Server và Client MCP của bạn.

Triển khai hiệu quả các Server và Client MCP yêu cầu cấu hình đúng cách.

<Tip>

Đặc tả MCP vẫn đang phát triển, vì vậy các phương pháp cấu hình có thể thay đổi. Chúng ta sẽ tập trung vào các phương pháp tốt nhất hiện tại để cấu hình.

</Tip>

### Tệp cấu hình MCP

Các Server MCP sử dụng các tệp cấu hình để quản lý kết nối với Server. Những tệp này xác định các Server nào có sẵn và cách kết nối với chúng.

May mắn là các tệp cấu hình rất đơn giản, dễ hiểu và thống nhất giữa các Server MCP chính.

#### Cấu trúc `mcp.json`

Tệp cấu hình tiêu chuẩn cho MCP có tên `mcp.json`. Đây là cấu trúc cơ bản:

```json
{
  "servers": [
    {
      "name": "Server Name",
      "transport": {
        "type": "stdio|sse",
        // Cấu hình cụ thể cho phương thức truyền tải
      }
    }
  ]
}
```

Trong ví dụ này, chúng ta có một Server duy nhất với tên và loại phương thức truyền tải. Loại phương thức truyền tải có thể là `stdio` hoặc `sse`.

#### Cấu hình cho phương thức truyền tải stdio

Đối với các Server cục bộ sử dụng phương thức truyền tải stdio, cấu hình bao gồm lệnh và các đối số để khởi chạy tiến trình Server:

```json
{
  "servers": [
    {
      "name": "File Explorer",
      "transport": {
        "type": "stdio",
        "command": "python",
        "args": ["/path/to/file_explorer_server.py"]
      }
    }
  ]
}
```

Ở đây, chúng ta có một Server có tên "File Explorer" là một tập lệnh cục bộ.

#### Cấu hình cho phương thức truyền tải HTTP+SSE

Đối với các Server từ xa sử dụng phương thức truyền tải HTTP+SSE, cấu hình bao gồm URL của Server:

```json
{
  "servers": [
    {
      "name": "Remote API Server",
      "transport": {
        "type": "sse",
        "url": "https://example.com/mcp-server"
      }
    }
  ]
}
```

#### Biến môi trường trong cấu hình

Các biến môi trường có thể được truyền vào tiến trình Server bằng cách sử dụng trường `env`. Đây là cách truy cập chúng trong mã Server của bạn:

<hfoptions id="env-variables">
<hfoption id="python">

Trong Python, chúng ta sử dụng module `os` để truy cập các biến môi trường:

<details>
<summary>Bấm để xem bản dịch tiếng Việt</summary>
```
import os

# Truy cập các biến môi trường
github_token = os.environ.get("GITHUB_TOKEN")
if not github_token:
    raise ValueError("GITHUB_TOKEN environment variable is required")

# Sử dụng token trong mã Server
def make_github_request():
    headers = {"Authorization": f"Bearer {github_token}"}
    # ... phần còn lại của mã
```
</details>
```
import os

# Access environment variables
github_token = os.environ.get("GITHUB_TOKEN")
if not github_token:
    raise ValueError("GITHUB_TOKEN environment variable is required")

# Use the token in your server code
def make_github_request():
    headers = {"Authorization": f"Bearer {github_token}"}
    # ... rest of your code
```

</hfoption>
<hfoption id="javascript">

Trong JavaScript, chúng ta sử dụng object `process.env` để truy cập các biến môi trường:

<details>
<summary>Bấm để xem bản dịch tiếng Việt</summary>
```
// Truy cập các biến môi trường
const githubToken = process.env.GITHUB_TOKEN;
if (!githubToken) {
    throw new Error("GITHUB_TOKEN environment variable is required");
}

// Sử dụng token trong mã Server
function makeGithubRequest() {
    const headers = { "Authorization": `Bearer ${githubToken}` };
    // ... phần còn lại của mã
}
```
</details>
```
// Access environment variables
const githubToken = process.env.GITHUB_TOKEN;
if (!githubToken) {
    throw new Error("GITHUB_TOKEN environment variable is required");
}

// Use the token in your server code
function makeGithubRequest() {
    const headers = { "Authorization": `Bearer ${githubToken}` };
    // ... rest of your code
}
```

</hfoption>
</hfoptions>

Cấu hình tương ứng trong `mcp.json` sẽ trông như thế này:

```json
{
  "servers": [
    {
      "name": "GitHub API",
      "transport": {
        "type": "stdio",
        "command": "python",
        "args": ["/path/to/github_server.py"],
        "env": {
          "GITHUB_TOKEN": "your_github_token"
        }
      }
    }
  ]
}
```

### Ví dụ về Cấu hình

Hãy cùng xem qua một số kịch bản cấu hình trong thực tế:

#### Kịch bản 1: Cấu hình Server Cục bộ

Trong kịch bản này, chúng ta có một Server cục bộ là script Python có thể là trình khám phá file hoặc trình chỉnh sửa code.

```json
{
  "servers": [
    {
      "name": "File Explorer",
      "transport": {
        "type": "stdio",
        "command": "python",
        "args": ["/path/to/file_explorer_server.py"]
      }
    }
  ]
}
```

#### Kịch bản 2: Cấu hình Server Từ xa

Trong kịch bản này, chúng ta có một Server từ xa là API thời tiết.

```json
{
  "servers": [
    {
      "name": "Weather API",
      "transport": {
        "type": "sse",
        "url": "https://example.com/mcp-server"
      }
    }
  ]
}
```

Việc cấu hình đúng cách là yếu tố thiết yếu để triển khai thành công các tích hợp MCP. Bằng cách hiểu rõ các khía cạnh này, các bạn có thể tạo ra các kết nối mạnh mẽ và đáng tin cậy giữa các ứng dụng AI và các khả năng bên ngoài.

Trong phần tiếp theo, chúng ta sẽ khám phá hệ sinh thái các Server MCP có sẵn trên Hugging Face Hub và cách xuất bản Server của riêng bạn tại đó.

## Code Clients

Bạn cũng có thể sử dụng MCP Client trong code để các công cụ có sẵn cho LLM. Hãy cùng khám phá một số ví dụ trong `smolagents`.

Đầu tiên, hãy xem qua Server thời tiết từ trang trước. Trong `smolagents`, chúng ta có thể sử dụng lớp `ToolCollection` để tự động phát hiện và đăng ký các công cụ từ Server MCP. Việc này được thực hiện bằng cách truyền `StdioServerParameters` hoặc `SSEServerParameters` vào phương thức `ToolCollection.from_mcp`. Sau đó chúng ta có thể in các công cụ ra console.

<details>
<summary>Bấm để xem bản dịch tiếng Việt</summary>
```python
from smolagents import ToolCollection, CodeAgent
from mcp.client.stdio import StdioServerParameters

server_parameters = StdioServerParameters(command="uv", args=["run", "server.py"])

with ToolCollection.from_mcp(
    server_parameters, trust_remote_code=True
) as tools:
    print("\n".join(f"{t.name}: {t.description}" for t in tools))
```
</details>
```python
from smolagents import ToolCollection, CodeAgent
from mcp.client.stdio import StdioServerParameters

server_parameters = StdioServerParameters(command="uv", args=["run", "server.py"])

with ToolCollection.from_mcp(
    server_parameters, trust_remote_code=True
) as tools:
    print("\n".join(f"{t.name}: {t.description}" for t in tools))

```

<details>
<summary>
Kết quả
</summary>

```sh
Weather API: Get the weather in a specific location

```

</details>

Chúng ta cũng có thể kết nối đến Server MCP được host trên máy từ xa. Trong trường hợp này, chúng ta cần truyền `SSEServerParameters` vào phương thức `ToolCollection.from_mcp`.

<details>
<summary>Bấm để xem bản dịch tiếng Việt</summary>
```python
from smolagents.mcp_client import MCPClient

with MCPClient(
    {"url": "https://abidlabs-mcp-tools2.hf.space/gradio_api/mcp/sse"}
) as tools:
    # Tools from the remote server are available
    print("\n".join(f"{t.name}: {t.description}" for t in tools))
```
</details>
```python
from smolagents.mcp_client import MCPClient

with MCPClient(
    {"url": "https://abidlabs-mcp-tools2.hf.space/gradio_api/mcp/sse"}
) as tools:
    # Tools from the remote server are available
    print("\n".join(f"{t.name}: {t.description}" for t in tools))
```

<details>
<summary>
Kết quả
</summary>

```sh
prime_factors: Compute the prime factorization of a positive integer.
generate_cheetah_image: Generate a cheetah image.
image_orientation: Returns whether image is portrait or landscape.
sepia: Apply a sepia filter to the input image.
```

</details>

Bây giờ hãy xem cách sử dụng MCP Client trong một code agent.

<details>
<summary>Bấm để xem bản dịch tiếng Việt</summary>
```python
from smolagents import ToolCollection, CodeAgent
from mcp.client.stdio import StdioServerParameters
from smolagents import CodeAgent, InferenceClientModel

model = InferenceClientModel()

server_parameters = StdioServerParameters(command="uv", args=["run", "server.py"])

with ToolCollection.from_mcp(
    server_parameters, trust_remote_code=True
) as tool_collection:
    agent = CodeAgent(tools=[*tool_collection.tools], model=model)
    agent.run("What's the weather in Tokyo?")
```
</details>
```python
from smolagents import ToolCollection, CodeAgent
from mcp.client.stdio import StdioServerParameters
from smolagents import CodeAgent, InferenceClientModel

model = InferenceClientModel()

server_parameters = StdioServerParameters(command="uv", args=["run", "server.py"])

with ToolCollection.from_mcp(
    server_parameters, trust_remote_code=True
) as tool_collection:
    agent = CodeAgent(tools=[*tool_collection.tools], model=model)
    agent.run("What's the weather in Tokyo?")

```

<details>
<summary>
Kết quả
</summary>

```sh
The weather in Tokyo is sunny with a temperature of 20 degrees Celsius.
```

</details>

Chúng ta cũng có thể kết nối đến các gói MCP. Đây là ví dụ về cách kết nối đến gói `pubmedmcp`.

```python
from smolagents import ToolCollection, CodeAgent
from mcp import StdioServerParameters

server_parameters = StdioServerParameters(
    command="uv",
    args=["--quiet", "pubmedmcp@0.1.3"],
    env={"UV_PYTHON": "3.12", **os.environ},
)

with ToolCollection.from_mcp(server_parameters, trust_remote_code=True) as tool_collection:
    agent = CodeAgent(tools=[*tool_collection.tools], add_base_tools=True)
    agent.run("Please find a remedy for hangover.")
```

<details>
<summary>Kết quả</summary>

<details>
<summary>Bấm để xem bản dịch tiếng Việt</summary>
```sh
Phương pháp chữa nôn nao là uống nước.
```
</details>
```sh
The remedy for hangover is to drink water.
```

</details>

## Bước tiếp theo

Giờ bạn đã hiểu về MCP Client, hãy sẵn sàng để:
* Khám phá các triển khai MCP Server cụ thể
* Tìm hiểu về cách tạo MCP Client tùy chỉnh
* Đi sâu vào các mẫu tích hợp MCP nâng cao

Hãy tiếp tục hành trình của chúng ta vào thế giới của Giao Thức Ngữ Cảnh Mô Hình!
````

## File: units/vi/unit1/sdk.mdx
````
# MCP SDK

Giao Thức Ngữ Cảnh Mô Hình (MCP) cung cấp SDK chính thức cho cả JavaScript, Python và các ngôn ngữ khác. Điều này giúp việc triển khai Client và Server MCP trong ứng dụng của bạn trở nên dễ dàng. Các SDK này xử lý các chi tiết giao thức cấp thấp, cho phép bạn tập trung vào việc xây dựng chức năng ứng dụng.

## Tổng quan về SDK

Cả hai SDK đều cung cấp chức năng cốt lõi tương tự, tuân theo đặc tả giao thức MCP mà chúng ta đã thảo luận trước đó. Chúng xử lý:

- Giao tiếp ở cấp độ giao thức
- Đăng ký và khám phá tính năng
- Tuần tự hóa/giải tuần tự hóa tin nhắn
- Quản lý kết nối
- Xử lý lỗi

## Triển khai các thành phần cốt lõi

Hãy cùng khám phá cách triển khai từng thành phần cốt lõi (Tools, Resources, và Prompts) bằng cả hai SDK.

<hfoptions id="server-implementation">
<hfoption id="python">

<Youtube id="exzrb5QNUis" />

<details>
<summary>Bấm để xem bản dịch tiếng Việt</summary>
```python
from mcp.server.fastmcp import FastMCP

# Tạo Server MCP
mcp = FastMCP("Dịch vụ Thời tiết")


@mcp.tool()
def get_weather(location: str) -> str:
    """Nhận thông tin thời tiết hiện tại ở một địa điểm cụ thể."""
    return f"Weather in {location}: Sunny, 72°F"


@mcp.resource("weather://{location}")
def weather_resource(location: str) -> str:
    """Cung cấp dữ liệu thời tiết dưới dạng tài nguyên."""
    return f"Weather data for {location}: Sunny, 72°F"


@mcp.prompt()
def weather_report(location: str) -> str:
    """Tạo lời nhắc báo cáo thời tiết."""
    return f"""You are a weather reporter. Weather report for {location}?"""


# Chạy Server
if __name__ == "__main__":
    mcp.run()
```
</details>

```python
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Weather Service")


@mcp.tool()
def get_weather(location: str) -> str:
    """Get the current weather for a specified location."""
    return f"Weather in {location}: Sunny, 72°F"


@mcp.resource("weather://{location}")
def weather_resource(location: str) -> str:
    """Provide weather data as a resource."""
    return f"Weather data for {location}: Sunny, 72°F"


@mcp.prompt()
def weather_report(location: str) -> str:
    """Create a weather report prompt."""
    return f"""You are a weather reporter. Weather report for {location}?"""


# Run the server
if __name__ == "__main__":
    mcp.run()

```

</hfoption>
<hfoption id="javascript">

<details>
<summary>Bấm để xem bản dịch tiếng Việt</summary>
```javascript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Tạo Server MCP
const server = new McpServer({
    name: "Dịch vụ Thời tiết",
    version: "1.0.0"
});

// Triển khai công cụ
server.tool("get_weather",
    { location: z.string() },
    async ({ location }) => ({
        content: [{
            type: "text",
            text: `Weather in ${location}: Sunny, 72°F`
        }]
    })
);

// Triển khai tài nguyên
server.resource(
    "weather",
    new ResourceTemplate("weather://{location}", { list: undefined }),
    async (uri, { location }) => ({
        contents: [{
            uri: uri.href,
            text: `Weather data for ${location}: Sunny, 72°F`
        }]
    })
);

// Triển khai prompt
server.prompt(
    "weather_report",
    { location: z.string() },
    async ({ location }) => ({
        messages: [
            {
                role: "assistant",
                content: {
                    type: "text",
                    text: "You are a weather reporter."
                }
            },
            {
                role: "user",
                content: {
                    type: "text",
                    text: `Weather report for ${location}?`
                }
            }
        ]
    })
);

// Chạy server
const transport = new StdioServerTransport();
await server.connect(transport);
```

Sau khi đã triển khai máy chủ của mình, bạn có thể khởi chạy nó bằng cách chạy script server.

```bash
mcp dev server.py
```

</details>

```javascript
// index.mjs
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Create an MCP server
const server = new McpServer({
    name: "Weather Service",
    version: "1.0.0"
});

// Tool implementation
server.tool("get_weather",
    { location: z.string() },
    async ({ location }) => ({
        content: [{
            type: "text",
            text: `Weather in ${location}: Sunny, 72°F`
        }]
    })
);

// Resource implementation
server.resource(
    "weather",
    new ResourceTemplate("weather://{location}", { list: undefined }),
    async (uri, { location }) => ({
        contents: [{
            uri: uri.href,
            text: `Weather data for ${location}: Sunny, 72°F`
        }]
    })
);

// Prompt implementation
server.prompt(
    "weather_report",
    { location: z.string() },
    async ({ location }) => ({
        messages: [
            {
                role: "assistant",
                content: {
                    type: "text",
                    text: "You are a weather reporter."
                }
            },
            {
                role: "user",
                content: {
                    type: "text",
                    text: `Weather report for ${location}?`
                }
            }
        ]
    })
);

// Run the server
const transport = new StdioServerTransport();
await server.connect(transport);
```

Sau khi đã triển khai máy chủ của mình, bạn có thể khởi chạy nó bằng cách chạy script server.

```bash
npx @modelcontextprotocol/inspector node ./index.mjs
```

</hfoption>
</hfoptions>

Lệnh này sẽ khởi tạo một máy chủ phát triển chạy file `server.py` và ghi lại output sau:

<details>
<summary>Bấm để xem bản dịch tiếng Việt</summary>
```
Starting MCP inspector...
⚙️ Proxy server listening on port 6277
Spawned stdio transport
Connected MCP client to backing server transport
Created web app transport
Set up MCP proxy
🔍 MCP Inspector is up and running at http://127.0.0.1:6274 🚀
```
</details>
```bash
Starting MCP inspector...
⚙️ Proxy server listening on port 6277
Spawned stdio transport
Connected MCP client to backing server transport
Created web app transport
Set up MCP proxy
🔍 MCP Inspector is up and running at http://127.0.0.1:6274 🚀
```

Bạn có thể mở MCP Inspector tại [http://127.0.0.1:6274](http://127.0.0.1:6274) để xem các tính năng của máy chủ và tương tác với chúng.

Bạn sẽ thấy các tính năng của máy chủ và khả năng gọi chúng thông qua giao diện người dùng.

![MCP Inspector](https://huggingface.co/datasets/mcp-course/images/resolve/main/unit1/6.png)

## Bộ SDK MCP

MCP được thiết kế để độc lập với ngôn ngữ lập trình, và hiện có các SDK chính thức cho nhiều ngôn ngữ phổ biến:

| Ngôn ngữ | Kho lưu trữ | Người bảo trì | Trạng thái |
|----------|------------|---------------|--------|
| TypeScript | [github.com/modelcontextprotocol/typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk) | Anthropic | Hoạt động |
| Python | [github.com/modelcontextprotocol/python-sdk](https://github.com/modelcontextprotocol/python-sdk) | Anthropic | Hoạt động |
| Java | [github.com/modelcontextprotocol/java-sdk](https://github.com/modelcontextprotocol/java-sdk) | Spring AI (VMware) | Hoạt động |
| Kotlin | [github.com/modelcontextprotocol/kotlin-sdk](https://github.com/modelcontextprotocol/kotlin-sdk) | JetBrains | Hoạt động |
| C# | [github.com/modelcontextprotocol/csharp-sdk](https://github.com/modelcontextprotocol/csharp-sdk) | Microsoft | Hoạt động (Xem trước) |
| Swift | [github.com/modelcontextprotocol/swift-sdk](https://github.com/modelcontextprotocol/swift-sdk) | loopwork-ai | Hoạt động |
| Rust | [github.com/modelcontextprotocol/rust-sdk](https://github.com/modelcontextprotocol/rust-sdk) | Anthropic/Cộng đồng | Hoạt động |

Các SDK này cung cấp các abstraction đặc thù cho từng ngôn ngữ, giúp đơn giản hóa việc làm việc với giao thức MCP, cho phép bạn tập trung vào việc triển khai logic cốt lõi của máy chủ hoặc máy khách thay vì xử lý các chi tiết giao thức cấp thấp.

## Bước tiếp theo

Chúng ta mới chỉ chạm vào bề mặt của những gì có thể làm với MCP nhưng bạn đã có một máy chủ cơ bản đang chạy. Thực tế, bạn cũng đã kết nối với nó bằng MCP Client trên trình duyệt.

Trong phần tiếp theo, chúng ta sẽ xem cách kết nối với máy chủ từ một LLM.
````

## File: units/vi/unit2/gradio-client.mdx
````
# Gradio với vai trò Máy khách MCP

Ở chương trước, chúng ta đã tìm hiểu cách tạo MCP Server bằng Gradio và kết nối đến nó bằng một MCP Client. Trong chương này, chúng ta sẽ khám phá cách sử dụng Gradio như một MCP Client để kết nối đến MCP Server.

<Tip>

Gradio phù hợp nhất để tạo UI client và MCP server, nhưng cũng có thể dùng nó như MCP Client và hiển thị dưới dạng UI.

</Tip>

Chúng ta sẽ kết nối đến MCP server đã tạo ở chương trước và dùng nó để trả lời câu hỏi.

## MCP Client trong Gradio

Đầu tiên, cần cài đặt các thư viện `smolagents`, gradio và mcp-client nếu chưa có:

```bash
pip install smolagents[mcp] gradio[mcp] mcp
```

Giờ chúng ta có thể import các thư viện cần thiết và tạo giao diện Gradio đơn giản sử dụng MCP Client để kết nối đến MCP Server.

```python
import gradio as gr

from mcp.client.stdio import StdioServerParameters
from smolagents import ToolCollection, CodeAgent
from smolagents import CodeAgent, InferenceClientModel
from smolagents.mcp_client import MCPClient
```

Tiếp theo, kết nối đến MCP Server và lấy các công cụ có thể dùng để trả lời câu hỏi.

```python
mcp_client = MCPClient(
    {"url": "http://localhost:7860/gradio_api/mcp/sse"}
)
tools = mcp_client.get_tools()
```

Sau khi có các công cụ, ta có thể tạo một agent đơn giản sử dụng chúng để trả lời câu hỏi. Hiện tại chúng ta sẽ dùng `InferenceClientModel` và mô hình mặc định từ `smolagents`.

```python
model = InferenceClientModel()
agent = CodeAgent(tools=[*tools], model=model)
```

Giờ tạo giao diện Gradio đơn giản sử dụng agent để trả lời câu hỏi.

```python
demo = gr.ChatInterface(
    fn=lambda message, history: str(agent.run(message)),
    type="messages",
    examples=["Prime factorization of 68"],
    title="Agent with MCP Tools",
    description="Đây là agent đơn giản sử dụng các công cụ MCP để trả lời câu hỏi.",
    messages=[],
)

demo.launch()
```

Vậy là xong! Chúng ta đã tạo một giao diện Gradio đơn giản dùng MCP Client để kết nối đến MCP Server và trả lời câu hỏi.

<iframe
	src="https://mcp-course-unit2-gradio-client.hf.space"
	frameborder="0"
	width="850"
	height="450"
></iframe>


## Ví dụ hoàn chỉnh

Dưới đây là ví dụ hoàn chỉnh của MCP Client trong Gradio:

```python
import gradio as gr

from mcp.client.stdio import StdioServerParameters
from smolagents import ToolCollection, CodeAgent
from smolagents import CodeAgent, InferenceClientModel
from smolagents.mcp_client import MCPClient


try:
    mcp_client = MCPClient(
        # {"url": "https://abidlabs-mcp-tools.hf.space/gradio_api/mcp/sse"}
        {"url": "http://localhost:7860/gradio_api/mcp/sse"}
    )
    tools = mcp_client.get_tools()

    model = InferenceClientModel()
    agent = CodeAgent(tools=[*tools], model=model)

    def call_agent(message, history):
        return str(agent.run(message))


    demo = gr.ChatInterface(
        fn=lambda message, history: str(agent.run(message)),
        type="messages",
        examples=["Prime factorization of 68"],
        title="Agent with MCP Tools",
        description="Đây là agent đơn giản sử dụng các công cụ MCP để trả lời câu hỏi.",
        messages=[],
    )

    demo.launch()
finally:
    mcp_client.close()
```

Bạn sẽ thấy chúng ta đóng MCP Client trong khối `finally`. Điều này quan trọng vì MCP Client là đối tượng tồn tại lâu dài cần được đóng khi chương trình kết thúc.

## Triển khai lên Hugging Face Spaces

Để chia sẻ server của bạn với mọi người, bạn có thể triển khai lên Hugging Face Spaces như đã làm ở chương trước.
Để triển khai Gradio MCP client lên Hugging Face Spaces:

1. Tạo Space mới trên Hugging Face:
   - Truy cập huggingface.co/spaces
   - Click "Create new Space"
   - Chọn "Gradio" làm SDK
   - Đặt tên cho Space (ví dụ: "mcp-client")

2. Tạo một tệp `requirements.txt`:
```txt
gradio[mcp]
smolagents[mcp]
```

3. Đẩy code lên Space:
```bash
git init
git add server.py requirements.txt
git commit -m "Initial commit"
git remote add origin https://huggingface.co/spaces/YOUR_USERNAME/mcp-client
git push -u origin main
```

## Kết luận

Trong phần này, chúng ta đã tìm hiểu cách sử dụng Gradio như một MCP Client để kết nối đến một MCP Server. Chúng ta cũng đã xem qua cách triển khai MCP Client trên Hugging Face Spaces.
````

## File: .gitignore
````
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
cover/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
.pybuilder/
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
#   For a library or package, you might want to ignore these files since the code is
#   intended to run in multiple environments; otherwise, check them in:
# .python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
#Pipfile.lock

# UV
#   Similar to Pipfile.lock, it is generally recommended to include uv.lock in version control.
#   This is especially recommended for binary packages to ensure reproducibility, and is more
#   commonly ignored for libraries.
#uv.lock

# poetry
#   Similar to Pipfile.lock, it is generally recommended to include poetry.lock in version control.
#   This is especially recommended for binary packages to ensure reproducibility, and is more
#   commonly ignored for libraries.
#   https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control
#poetry.lock

# pdm
#   Similar to Pipfile.lock, it is generally recommended to include pdm.lock in version control.
#pdm.lock
#   pdm stores project-wide configurations in .pdm.toml, but it is recommended to not include it
#   in version control.
#   https://pdm.fming.dev/latest/usage/project/#working-with-version-control
.pdm.toml
.pdm-python
.pdm-build/

# PEP 582; used by e.g. github.com/David-OConnor/pyflow and github.com/pdm-project/pdm
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# pytype static type analyzer
.pytype/

# Cython debug symbols
cython_debug/

# PyCharm
#  JetBrains specific template is maintained in a separate JetBrains.gitignore that can
#  be found at https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore
#  and can be added to the global gitignore or merged into this file.  For a more nuclear
#  option (not recommended) you can uncomment the following to ignore the entire idea folder.
#.idea/

# Ruff stuff:
.ruff_cache/

# PyPI configuration file
.pypirc

.DS_Store

videos/
````

## File: README.md
````markdown
# The Model Context Protocol (MCP) Course

<div align="center"> <a href="README.md">🇺🇸 English</a> | <a href="README_vi.md">🇻🇳 Tiếng Việt</a> </div>

![1](https://github.com/user-attachments/assets/d26dcc5e-46cb-449e-aecb-49ece10d342a)

If you like the course, **don't hesitate to ⭐ star this repository**. This helps us to **make the course more visible 🤗**.

<img src="https://huggingface.co/datasets/agents-course/course-images/resolve/main/en/communication/please_star.gif" alt="Star the repo" />

## Content

The course is divided into 4 units. These will take you from **the basics of Model Context Protocol to a final project implementing MCP in an AI application**.

Sign up here (it's free) 👉 [Coming Soon]

You can access the course here 👉 [Coming Soon]

| Unit    | Topic                                               | Description                                                                                             |
| ------- | --------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| 0       | Welcome to the Course                               | Welcome, guidelines, necessary tools, and course overview.                                              |
| 1       | Introduction to Model Context Protocol              | Definition of MCP, key concepts, and its role in connecting AI models with external data and tools.     |
| 2       | Building with MCP: Practical Development            | Learn to implement MCP clients and servers using available SDKs and frameworks.                         |
| 3       | MCP Protocol Deep Dive                            | Explore advanced MCP features, architecture, and real-world integration patterns|
| 4       | Bonus Units & Collaborations                    | Special topics, partner libraries, and community-driven projects.|

## Prerequisites

* Basic understanding of AI and LLM concepts
* Familiarity with software development principles and API concepts
* Experience with at least one programming language (Python or TypeScript examples will be emphasized)

## Contribution Guidelines

If you want to contribute to this course, you're welcome to do so. Feel free to open an issue or submit a pull request. For specific contributions, here are some guidelines:

### Small typo and grammar fixes

If you find a small typo or grammar mistake, please fix it yourself and submit a pull request. This is very helpful for students.

### New unit

If you want to add a new unit, **please create an issue in the repository, describe the unit, and why it should be added**. We will discuss it and if it's a good addition, we can collaborate on it.

## Citing the project

To cite this repository in publications:

```
@misc{mcp-course,
  author = {Burtenshaw, Ben and Notov, Alex},
  title = {The Model Context Protocol Course},
  year = {2025},
  howpublished = {\url{https://github.com/huggingface/mcp-course}},
  note = {GitHub repository},
}
```
````

## File: projects/unit3/build-mcp-server/solution/test_server.py
````python
#!/usr/bin/env python3
"""
Unit tests for Module 1: Basic MCP Server
Run these tests to validate your implementation
"""

import json
import pytest
import asyncio
from pathlib import Path
from unittest.mock import patch, MagicMock

# Import your implemented functions
try:
    from server import (
        mcp,
        analyze_file_changes,
        get_pr_templates,
        suggest_template
    )
    IMPORTS_SUCCESSFUL = True
except ImportError as e:
    IMPORTS_SUCCESSFUL = False
    IMPORT_ERROR = str(e)


class TestImplementation:
    """Test that the required functions are implemented."""
    
    def test_imports(self):
        """Test that all required functions can be imported."""
        assert IMPORTS_SUCCESSFUL, f"Failed to import required functions: {IMPORT_ERROR if not IMPORTS_SUCCESSFUL else ''}"
        assert mcp is not None, "FastMCP server instance not found"
        assert callable(analyze_file_changes), "analyze_file_changes should be a callable function"
        assert callable(get_pr_templates), "get_pr_templates should be a callable function"
        assert callable(suggest_template), "suggest_template should be a callable function"


@pytest.mark.skipif(not IMPORTS_SUCCESSFUL, reason="Imports failed")
class TestAnalyzeFileChanges:
    """Test the analyze_file_changes tool."""
    
    @pytest.mark.asyncio
    async def test_returns_json_string(self):
        """Test that analyze_file_changes returns a JSON string."""
        with patch('subprocess.run') as mock_run:
            mock_run.return_value = MagicMock(stdout="", stderr="")
            
            result = await analyze_file_changes()
            
            assert isinstance(result, str), "Should return a string"
            # Should be valid JSON
            data = json.loads(result)
            assert isinstance(data, dict), "Should return a JSON object"
    
    @pytest.mark.asyncio
    async def test_includes_required_fields(self):
        """Test that the result includes expected fields."""
        with patch('subprocess.run') as mock_run:
            mock_run.return_value = MagicMock(stdout="M\tfile1.py\n", stderr="")
            
            result = await analyze_file_changes()
            data = json.loads(result)
            
            # For starter code, accept error messages; for full implementation, expect data
            is_implemented = not ("error" in data and "Not implemented" in str(data.get("error", "")))
            if is_implemented:
                # Check for some expected fields (flexible to allow different implementations)
                assert any(key in data for key in ["files_changed", "files", "changes", "diff"]), \
                    "Result should include file change information"
            else:
                # Starter code - just verify it returns something structured
                assert isinstance(data, dict), "Should return a JSON object even if not implemented"
    
    @pytest.mark.asyncio
    async def test_output_limiting(self):
        """Test that large diffs are properly truncated."""
        with patch('subprocess.run') as mock_run:
            # Create a mock diff with many lines
            large_diff = "\n".join([f"+ line {i}" for i in range(1000)])
            
            # Set up mock responses
            mock_run.side_effect = [
                MagicMock(stdout="M\tfile1.py\n", stderr=""),  # files changed
                MagicMock(stdout="1 file changed, 1000 insertions(+)", stderr=""),  # stats
                MagicMock(stdout=large_diff, stderr=""),  # diff
                MagicMock(stdout="abc123 Initial commit", stderr="")  # commits
            ]
            
            # Test with default limit (500 lines)
            result = await analyze_file_changes(include_diff=True)
            data = json.loads(result)
            
            # Check if it's implemented
            if "error" not in data or "Not implemented" not in str(data.get("error", "")):
                if "diff" in data and data["diff"] != "Diff not included (set include_diff=true to see full diff)":
                    diff_lines = data["diff"].split('\n')
                    # Should be truncated to around 500 lines plus truncation message
                    assert len(diff_lines) < 600, "Large diffs should be truncated"
                    
                    # Check for truncation indicator
                    if "truncated" in data:
                        assert data["truncated"] == True, "Should indicate truncation"
                    
                    # Should have truncation message
                    assert "truncated" in data["diff"].lower() or "..." in data["diff"], \
                        "Should indicate diff was truncated"


@pytest.mark.skipif(not IMPORTS_SUCCESSFUL, reason="Imports failed")
class TestGetPRTemplates:
    """Test the get_pr_templates tool."""
    
    @pytest.mark.asyncio
    async def test_returns_json_string(self):
        """Test that get_pr_templates returns a JSON string."""
        result = await get_pr_templates()
        
        assert isinstance(result, str), "Should return a string"
        # Should be valid JSON
        data = json.loads(result)
        
        # For starter code, accept error messages; for full implementation, expect list
        is_implemented = not ("error" in data and isinstance(data, dict))
        if is_implemented:
            assert isinstance(data, list), "Should return a JSON array of templates"
        else:
            # Starter code - just verify it returns something structured
            assert isinstance(data, dict), "Should return a JSON object even if not implemented"
    
    @pytest.mark.asyncio
    async def test_returns_templates(self):
        """Test that templates are returned."""
        result = await get_pr_templates()
        templates = json.loads(result)
        
        # For starter code, accept error messages; for full implementation, expect templates
        is_implemented = not ("error" in templates and isinstance(templates, dict))
        if is_implemented:
            assert len(templates) > 0, "Should return at least one template"
            
            # Check that templates have expected structure
            for template in templates:
                assert isinstance(template, dict), "Each template should be a dictionary"
                # Should have some identifying information
                assert any(key in template for key in ["filename", "name", "type", "id"]), \
                    "Templates should have an identifier"
        else:
            # Starter code - just verify it's structured correctly
            assert isinstance(templates, dict), "Should return structured error for starter code"


@pytest.mark.skipif(not IMPORTS_SUCCESSFUL, reason="Imports failed")
class TestSuggestTemplate:
    """Test the suggest_template tool."""
    
    @pytest.mark.asyncio
    async def test_returns_json_string(self):
        """Test that suggest_template returns a JSON string."""
        result = await suggest_template(
            "Fixed a bug in the authentication system",
            "bug"
        )
        
        assert isinstance(result, str), "Should return a string"
        # Should be valid JSON
        data = json.loads(result)
        assert isinstance(data, dict), "Should return a JSON object"
    
    @pytest.mark.asyncio
    async def test_suggestion_structure(self):
        """Test that the suggestion has expected structure."""
        result = await suggest_template(
            "Added new feature for user management",
            "feature"
        )
        suggestion = json.loads(result)
        
        # For starter code, accept error messages; for full implementation, expect suggestion
        is_implemented = not ("error" in suggestion and "Not implemented" in str(suggestion.get("error", "")))
        if is_implemented:
            # Check for some expected fields (flexible to allow different implementations)
            assert any(key in suggestion for key in ["template", "recommended_template", "suggestion"]), \
                "Should include a template recommendation"
        else:
            # Starter code - just verify it's structured correctly
            assert isinstance(suggestion, dict), "Should return structured error for starter code"


@pytest.mark.skipif(not IMPORTS_SUCCESSFUL, reason="Imports failed")
class TestToolRegistration:
    """Test that tools are properly registered with FastMCP."""
    
    def test_tools_have_decorators(self):
        """Test that tool functions are decorated with @mcp.tool()."""
        # In FastMCP, decorated functions should have certain attributes
        # This is a basic check that functions exist and are callable
        assert hasattr(analyze_file_changes, '__name__'), \
            "analyze_file_changes should be a proper function"
        assert hasattr(get_pr_templates, '__name__'), \
            "get_pr_templates should be a proper function"
        assert hasattr(suggest_template, '__name__'), \
            "suggest_template should be a proper function"


if __name__ == "__main__":
    if not IMPORTS_SUCCESSFUL:
        print(f"❌ Cannot run tests - imports failed: {IMPORT_ERROR}")
        print("\nMake sure you've:")
        print("1. Implemented all three tool functions")
        print("2. Decorated them with @mcp.tool()")
        print("3. Installed dependencies with: uv sync")
        exit(1)
    
    # Run tests
    pytest.main([__file__, "-v"])
````

## File: projects/unit3/build-mcp-server/starter/server.py
````python
#!/usr/bin/env python3
"""
Module 1: Basic MCP Server - Starter Code
TODO: Implement tools for analyzing git changes and suggesting PR templates
"""

import json
import subprocess
from pathlib import Path

from mcp.server.fastmcp import FastMCP

# Initialize the FastMCP server
mcp = FastMCP("pr-agent")

# PR template directory (shared across all modules)
TEMPLATES_DIR = Path(__file__).parent.parent.parent / "templates"


# TODO: Implement tool functions here
# Example structure for a tool:
# @mcp.tool()
# async def analyze_file_changes(base_branch: str = "main", include_diff: bool = True) -> str:
#     """Get the full diff and list of changed files in the current git repository.
#     
#     Args:
#         base_branch: Base branch to compare against (default: main)
#         include_diff: Include the full diff content (default: true)
#     """
#     # Your implementation here
#     pass

# Minimal stub implementations so the server runs
# TODO: Replace these with your actual implementations

@mcp.tool()
async def analyze_file_changes(base_branch: str = "main", include_diff: bool = True) -> str:
    """Get the full diff and list of changed files in the current git repository.
    
    Args:
        base_branch: Base branch to compare against (default: main)
        include_diff: Include the full diff content (default: true)
    """
    # TODO: Implement this tool
    # IMPORTANT: MCP tools have a 25,000 token response limit!
    # Large diffs can easily exceed this. Consider:
    # - Adding a max_diff_lines parameter (e.g., 500 lines)
    # - Truncating large outputs with a message
    # - Returning summary statistics alongside limited diffs
    
    # NOTE: Git commands run in the server's directory by default!
    # To run in Claude's working directory, use MCP roots:
    # context = mcp.get_context()
    # roots_result = await context.session.list_roots()
    # working_dir = roots_result.roots[0].uri.path
    # subprocess.run(["git", "diff"], cwd=working_dir)
    
    return json.dumps({"error": "Not implemented yet", "hint": "Use subprocess to run git commands"})


@mcp.tool()
async def get_pr_templates() -> str:
    """List available PR templates with their content."""
    # TODO: Implement this tool
    return json.dumps({"error": "Not implemented yet", "hint": "Read templates from TEMPLATES_DIR"})


@mcp.tool()
async def suggest_template(changes_summary: str, change_type: str) -> str:
    """Let Claude analyze the changes and suggest the most appropriate PR template.
    
    Args:
        changes_summary: Your analysis of what the changes do
        change_type: The type of change you've identified (bug, feature, docs, refactor, test, etc.)
    """
    # TODO: Implement this tool
    return json.dumps({"error": "Not implemented yet", "hint": "Map change_type to templates"})


if __name__ == "__main__":
    mcp.run()
````

## File: projects/unit3/github-actions-integration/starter/server.py
````python
#!/usr/bin/env python3
"""
Module 2: GitHub Actions Integration - STARTER CODE
Extend your PR Agent with webhook handling and MCP Prompts for CI/CD workflows.
"""

import json
import os
import subprocess
from typing import Optional
from pathlib import Path
from datetime import datetime

from mcp.server.fastmcp import FastMCP

# Initialize the FastMCP server
mcp = FastMCP("pr-agent-actions")

# PR template directory (shared between starter and solution)
TEMPLATES_DIR = Path(__file__).parent.parent.parent / "templates"

# Default PR templates
DEFAULT_TEMPLATES = {
    "bug.md": "Bug Fix",
    "feature.md": "Feature",
    "docs.md": "Documentation",
    "refactor.md": "Refactor",
    "test.md": "Test",
    "performance.md": "Performance",
    "security.md": "Security"
}

# TODO: Add path to events file where webhook_server.py stores events
# Hint: EVENTS_FILE = Path(__file__).parent / "github_events.json"

# Type mapping for PR templates
TYPE_MAPPING = {
    "bug": "bug.md",
    "fix": "bug.md",
    "feature": "feature.md",
    "enhancement": "feature.md",
    "docs": "docs.md",
    "documentation": "docs.md",
    "refactor": "refactor.md",
    "cleanup": "refactor.md",
    "test": "test.md",
    "testing": "test.md",
    "performance": "performance.md",
    "optimization": "performance.md",
    "security": "security.md"
}


# ===== Module 1 Tools (Already includes output limiting fix from Module 1) =====

@mcp.tool()
async def analyze_file_changes(
    base_branch: str = "main",
    include_diff: bool = True,
    max_diff_lines: int = 500
) -> str:
    """Get the full diff and list of changed files in the current git repository.
    
    Args:
        base_branch: Base branch to compare against (default: main)
        include_diff: Include the full diff content (default: true)
        max_diff_lines: Maximum number of diff lines to include (default: 500)
    """
    try:
        # Get list of changed files
        files_result = subprocess.run(
            ["git", "diff", "--name-status", f"{base_branch}...HEAD"],
            capture_output=True,
            text=True,
            check=True
        )
        
        # Get diff statistics
        stat_result = subprocess.run(
            ["git", "diff", "--stat", f"{base_branch}...HEAD"],
            capture_output=True,
            text=True
        )
        
        # Get the actual diff if requested
        diff_content = ""
        truncated = False
        if include_diff:
            diff_result = subprocess.run(
                ["git", "diff", f"{base_branch}...HEAD"],
                capture_output=True,
                text=True
            )
            diff_lines = diff_result.stdout.split('\n')
            
            # Check if we need to truncate (learned from Module 1)
            if len(diff_lines) > max_diff_lines:
                diff_content = '\n'.join(diff_lines[:max_diff_lines])
                diff_content += f"\n\n... Output truncated. Showing {max_diff_lines} of {len(diff_lines)} lines ..."
                diff_content += "\n... Use max_diff_lines parameter to see more ..."
                truncated = True
            else:
                diff_content = diff_result.stdout
        
        # Get commit messages for context
        commits_result = subprocess.run(
            ["git", "log", "--oneline", f"{base_branch}..HEAD"],
            capture_output=True,
            text=True
        )
        
        analysis = {
            "base_branch": base_branch,
            "files_changed": files_result.stdout,
            "statistics": stat_result.stdout,
            "commits": commits_result.stdout,
            "diff": diff_content if include_diff else "Diff not included (set include_diff=true to see full diff)",
            "truncated": truncated,
            "total_diff_lines": len(diff_lines) if include_diff else 0
        }
        
        return json.dumps(analysis, indent=2)
        
    except subprocess.CalledProcessError as e:
        return json.dumps({"error": f"Git error: {e.stderr}"})
    except Exception as e:
        return json.dumps({"error": str(e)})


@mcp.tool()
async def get_pr_templates() -> str:
    """List available PR templates with their content."""
    templates = [
        {
            "filename": filename,
            "type": template_type,
            "content": (TEMPLATES_DIR / filename).read_text()
        }
        for filename, template_type in DEFAULT_TEMPLATES.items()
    ]
    
    return json.dumps(templates, indent=2)


@mcp.tool()
async def suggest_template(changes_summary: str, change_type: str) -> str:
    """Let Claude analyze the changes and suggest the most appropriate PR template.
    
    Args:
        changes_summary: Your analysis of what the changes do
        change_type: The type of change you've identified (bug, feature, docs, refactor, test, etc.)
    """
    
    # Get available templates
    templates_response = await get_pr_templates()
    templates = json.loads(templates_response)
    
    # Find matching template
    template_file = TYPE_MAPPING.get(change_type.lower(), "feature.md")
    selected_template = next(
        (t for t in templates if t["filename"] == template_file),
        templates[0]  # Default to first template if no match
    )
    
    suggestion = {
        "recommended_template": selected_template,
        "reasoning": f"Based on your analysis: '{changes_summary}', this appears to be a {change_type} change.",
        "template_content": selected_template["content"],
        "usage_hint": "Claude can help you fill out this template based on the specific changes in your PR."
    }
    
    return json.dumps(suggestion, indent=2)


# ===== Module 2: New GitHub Actions Tools =====

@mcp.tool()
async def get_recent_actions_events(limit: int = 10) -> str:
    """Get recent GitHub Actions events received via webhook.
    
    Args:
        limit: Maximum number of events to return (default: 10)
    """
    # TODO: Implement this function
    # 1. Check if EVENTS_FILE exists
    # 2. Read the JSON file
    # 3. Return the most recent events (up to limit)
    # 4. Return empty list if file doesn't exist
    
    return json.dumps({"message": "TODO: Implement get_recent_actions_events"})


@mcp.tool()
async def get_workflow_status(workflow_name: Optional[str] = None) -> str:
    """Get the current status of GitHub Actions workflows.
    
    Args:
        workflow_name: Optional specific workflow name to filter by
    """
    # TODO: Implement this function
    # 1. Read events from EVENTS_FILE
    # 2. Filter events for workflow_run events
    # 3. If workflow_name provided, filter by that name
    # 4. Group by workflow and show latest status
    # 5. Return formatted workflow status information
    
    return json.dumps({"message": "TODO: Implement get_workflow_status"})


# ===== Module 2: MCP Prompts =====

@mcp.prompt()
async def analyze_ci_results():
    """Analyze recent CI/CD results and provide insights."""
    # TODO: Implement this prompt
    # Return a string with instructions for Claude to:
    # 1. Use get_recent_actions_events() 
    # 2. Use get_workflow_status()
    # 3. Analyze results and provide insights
    
    return "TODO: Implement analyze_ci_results prompt"


@mcp.prompt()
async def create_deployment_summary():
    """Generate a deployment summary for team communication."""
    # TODO: Implement this prompt
    # Return a string that guides Claude to create a deployment summary
    
    return "TODO: Implement create_deployment_summary prompt"


@mcp.prompt()
async def generate_pr_status_report():
    """Generate a comprehensive PR status report including CI/CD results."""
    # TODO: Implement this prompt
    # Return a string that guides Claude to combine code changes with CI/CD status
    
    return "TODO: Implement generate_pr_status_report prompt"


@mcp.prompt()
async def troubleshoot_workflow_failure():
    """Help troubleshoot a failing GitHub Actions workflow."""
    # TODO: Implement this prompt
    # Return a string that guides Claude through troubleshooting steps
    
    return "TODO: Implement troubleshoot_workflow_failure prompt"


if __name__ == "__main__":
    print("Starting PR Agent MCP server...")
    print("NOTE: Run webhook_server.py in a separate terminal to receive GitHub events")
    mcp.run()
````

## File: units/en/unit0/introduction.mdx
````
# Welcome to the 🤗 Model Context Protocol (MCP) Course

![MCP Course thumbnail](https://huggingface.co/datasets/mcp-course/images/resolve/main/unit0/1.png)

Welcome to the most exciting topic in AI today: **Model Context Protocol (MCP)**!

This free course, built in partnership with [Anthropic](https://www.anthropic.com), will take you on a journey, **from beginner to informed**, in understanding, using, and building applications with MCP.

This first unit will help you onboard:

* Discover the **course's syllabus**.
* **Get more information about the certification process and the schedule**.
* Get to know the team behind the course.
* Create your **account**.
* **Sign-up to our Discord server**, and meet your classmates and us.

Let's get started!

## What to expect from this course?

In this course, you will:

* 📖 Study Model Context Protocol in **theory, design, and practice.**
* 🧑‍💻 Learn to **use established MCP SDKs and frameworks**.
* 💾 **Share your projects** and explore applications created by the community.
* 🏆 Participate in challenges where you will **evaluate your MCP implementations against other students'.**
* 🎓 **Earn a certificate of completion** by completing assignments.

And more!

At the end of this course, you'll understand **how MCP works and how to build your own AI applications that leverage external data and tools using the latest MCP standards**.

Don't forget to [**sign up to the course!**](https://huggingface.co/mcp-course)

## What does the course look like?

The course is composed of:

* _Foundational Units_: where you learn MCP **concepts in theory**.
* _Hands-on_: where you'll learn **to use established MCP SDKs** to build your applications. These hands-on sections will have pre-configured environments.
* _Use case assignments_: where you'll apply the concepts you've learned to solve a real-world problem that you'll choose.
* _Collaborations_: We're collaborating with Hugging Face's partners to give you the latest MCP implementations and tools.
 
This **course is a living project, evolving with your feedback and contributions!** Feel free to open issues and PRs in GitHub, and engage in discussions in our Discord server.

## What's the syllabus?

Here is the **general syllabus for the course**. A more detailed list of topics will be released with each unit.

| Chapter | Topic                                       | Description                                                                                                            |
| ------- | ------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| 0       | Onboarding                                  | Set you up with the tools and platforms that you will use.                                                             |
| 1       | MCP Fundamentals, Architecture and Core Concepts | Explain core concepts, architecture, and components of Model Context Protocol. Show a simple use case using MCP.       |
| 2       | End-to-end Use case: MCP in Action              | Build a simple end-to-end MCP application that you can share with the community. |
| 3       | Deployed Use case: MCP in Action               | Build a deployed MCP application using the Hugging Face ecosystem and partners' services.                                        |
| 4       | Bonus Units                                  | Bonus units to help you get more out of the course, working with partners' libraries and services.                                        |

## What are the prerequisites?

To be able to follow this course, you should have:

* Basic understanding of AI and LLM concepts
* Familiarity with software development principles and API concepts
* Experience with at least one programming language (Python or TypeScript examples will be shown)

If you don't have any of these, don't worry! Here are some resources that can help you:

* [LLM Course](https://huggingface.co/learn/llm-course/) will guide you through the basics of using and building with LLMs.
* [Agents Course](https://huggingface.co/learn/agents-course/) will guide you through building AI agents with LLMs.

<Tip>

The above courses are not prerequisites in themselves, so if you understand the concepts of LLMs and agents, you can start the course now!

</Tip>

## What tools do I need?

You only need 2 things:

* _A computer_ with an internet connection.
* An _account_: to access the course resources and create projects. If you don't have an account yet, you can create one [here](https://huggingface.co/join) (it's free).

## The Certification Process

You can choose to follow this course _in audit mode_, or do the activities and _get one of the two certificates we'll issue_. If you audit the course, you can participate in all the challenges and do assignments if you want, and **you don't need to notify us**.

The certification process is **completely free**:

* _To get a certification for fundamentals_: you need to complete Unit 1 of the course. This is intended for students that want to get up to date with the latest trends in MCP, without the need to build a full application.
* _To get a certificate of completion_: you need to complete the use case units (2 and 3). This is intended for students that want to build a full application and share it with the community.

## What is the recommended pace?

Each chapter in this course is designed **to be completed in 1 week, with approximately 3-4 hours of work per week**.

Since there's a deadline, we provide you a recommended pace:

![Recommended Pace](https://huggingface.co/datasets/mcp-course/images/resolve/main/unit0/2.png)

## How to get the most out of the course?

To get the most out of the course, we have some advice:

1. [Join study groups in Discord](https://discord.gg/UrrTSsSyjb): Studying in groups is always easier. To do that, you need to join our discord server and verify your account.
2. **Do the quizzes and assignments**: The best way to learn is through hands-on practice and self-assessment.
3. **Define a schedule to stay in sync**: You can use our recommended pace schedule below or create yours.

![Course advice](https://huggingface.co/datasets/mcp-course/images/resolve/main/unit0/3.png)

## Who are we

About the authors:

### Ben Burtenshaw

Ben is a Machine Learning Engineer at Hugging Face who focuses on building LLM applications, with post training and agentic approaches. [Follow Ben on the Hub](https://huggingface.co/burtenshaw) to see his latest projects.

### Alex Notov

Alex is Technical Partner Enablement Lead at [Anthropic](https://www.anthropic.com) and worked on unit 3 of this course. Alex trains Anthropic's partners on Claude best practices for their use cases. Follow Alex on [LinkedIn](https://linkedin.com/in/zealoushacker) and [GitHub](https://github.com/zealoushacker).

## Acknowledgments

We would like to extend our gratitude to the following individuals and partners for their invaluable contributions and support:

- [Gradio](https://www.gradio.app/)
- [Continue](https://continue.dev)
- [Llama.cpp](https://github.com/ggerganov/llama.cpp)
- [Anthropic](https://www.anthropic.com)

## I found a bug, or I want to improve the course

Contributions are **welcome** 🤗

* If you _found a bug 🐛 in a notebook_, please [open an issue](https://github.com/huggingface/mcp-course/issues/new) and **describe the problem**.
* If you _want to improve the course_, you can [open a Pull Request](https://github.com/huggingface/mcp-course/pulls).
* If you _want to add a full section or a new unit_, the best is to [open an issue](https://github.com/huggingface/mcp-course/issues/new) and **describe what content you want to add before starting to write it so that we can guide you**.

## I still have questions

Please ask your question in our discord server #mcp-course-questions.

Now that you have all the information, let's get on board ⛵
````

## File: units/en/unit3/conclusion.mdx
````
# Unit 3 Conclusion: The CodeCraft Studios Transformation

## Mission Accomplished!

Congratulations! You've successfully transformed CodeCraft Studios from a chaotic startup into a well-oiled development machine. Let's see how far you've come:

### Before Your Automation System:
- ❌ PRs with descriptions like "stuff" and "fix"
- ❌ Critical bugs reaching production undetected  
- ❌ Teams working in silos, duplicating effort
- ❌ Weekend debugging sessions for already-fixed issues

### After Your Automation System:
- ✅ Clear, helpful PR descriptions that save reviewers time
- ✅ Real-time CI/CD monitoring that catches failures immediately
- ✅ Smart team notifications that keep everyone informed
- ✅ Developers focused on building features, not fighting process problems

The CodeCraft Studios team now has a complete automation system that demonstrates what's possible when you combine MCP's flexibility with Claude's intelligence.

## How You Solved Each Challenge

Your three-module journey tackled real problems that every development team faces:

### Module 1: Solved the PR Chaos
*"Help developers write better pull requests without slowing them down"*
- **PR Agent** with intelligent file analysis
- **Core MCP concepts**: Tools, data collection, and Claude integration
- **Design philosophy**: Provide raw data, let Claude make intelligent decisions
- **Result**: Clear PR descriptions that help reviewers understand changes

### Module 2: Caught the Silent Failures  
*"Never let another critical bug slip through unnoticed"*
- **Webhook server** for capturing GitHub Actions events
- **MCP Prompts** for standardized workflow guidance
- **Event storage system** using simple JSON files
- **Result**: Real-time CI/CD monitoring that prevents production issues

### Module 3: Bridged the Communication Gap
*"Keep the whole team informed about what's happening"*
- **Slack integration** for team notifications
- **Message formatting** using Claude's intelligence
- **Tools + Prompts combination** for powerful automation
- **Result**: Smart notifications that eliminate information silos

## Key MCP Concepts You've Learned

### MCP Primitives
- **Tools**: For data access and external API calls
- **Prompts**: For consistent workflow guidance and formatting
- **Integration patterns**: How Tools and Prompts work together

### Architecture Patterns
- **Separation of concerns**: MCP server vs webhook server
- **File-based event storage**: Simple, reliable, testable
- **Claude as the intelligence layer**: Making decisions from raw data

### Development Best Practices
- **Error handling**: Returning structured JSON even for failures
- **Security**: Environment variables for sensitive credentials
- **Testing**: Validation scripts and manual testing workflows

## Real-World Applications

The patterns you've learned can be applied to many automation scenarios:

<Tip>

**Beyond CI/CD**: The Tools + Prompts pattern works for customer support automation, content moderation, data analysis workflows, and any scenario where you need intelligent processing of external data.

</Tip>

### Common Patterns from Unit 3
1. **Data Collection** → Tools that gather information
2. **Intelligent Analysis** → Claude processes the data
3. **Formatted Output** → Prompts guide consistent presentation
4. **External Integration** → Tools interact with APIs and services

## Next Steps

### Immediate Actions
1. **Experiment** with your workflow automation - try different GitHub events
2. **Extend** the system with additional integrations (Discord, email, etc.)
3. **Share** your MCP server with teammates for real project use

### Advanced Exploration
- **Scale up**: Handle multiple repositories or teams
- **Add persistence**: Use databases for larger event volumes  
- **Create dashboards**: Build web interfaces for your automation
- **Explore other MCP clients**: Beyond Claude Code and Claude Desktop

### Community Involvement
- **Contribute** to the MCP ecosystem with your own servers
- **Share patterns** you discover with the community
- **Build on** existing MCP servers and extend their capabilities

## Key Takeaways

<Tip>

**MCP Philosophy**: The most effective MCP servers don't try to be smart - they provide Claude with rich, structured data and let Claude's intelligence do the heavy lifting. This makes your code simpler and more flexible.

</Tip>

### Technical Insights
- **Simple is powerful**: JSON file storage can handle many use cases
- **Claude as orchestrator**: Let Claude coordinate between your tools
- **Prompts for consistency**: Use prompts to ensure reliable output formats

### Development Insights  
- **Start small**: Build one tool at a time, test thoroughly
- **Think in workflows**: Design tools that work well together
- **Plan for humans**: Your automation should help teams, not replace them

## Resources for Continued Learning

### MCP Documentation
- [Official MCP Protocol](https://modelcontextprotocol.io/)
- [Python SDK Reference](https://github.com/modelcontextprotocol/python-sdk)
- [FastMCP Framework](https://gofastmcp.com/)

### Community Resources
- [MCP Server Directory](https://modelcontextprotocol.io/servers)
- [Example Implementations](https://github.com/modelcontextprotocol)
- [Community Discord](https://discord.gg/modelcontextprotocol)

---

## The CodeCraft Studios Success Story

Three weeks ago, CodeCraft Studios was struggling with:
- Unclear pull requests causing review delays
- Critical bugs slipping into production  
- Teams working in isolation and duplicating effort

Today, they have an intelligent automation system that:
- **Helps developers** write clear, helpful PR descriptions automatically
- **Monitors CI/CD pipelines** and alerts the team to issues immediately  
- **Keeps everyone informed** with smart, contextual team notifications

You've built more than just an MCP server - you've created a solution that transforms how development teams work together.

## Your MCP Journey Continues

The patterns you learned at CodeCraft Studios can solve countless other automation challenges. Whether you're building customer service tools, data analysis pipelines, or any system that needs intelligent processing, you now have the foundation to create powerful, adaptive solutions with MCP.

The future of intelligent automation is in your hands. What will you build next? 🚀
````

## File: projects/unit3/build-mcp-server/solution/server.py
````python
#!/usr/bin/env python3
"""
Module 1: Basic MCP Server with PR Template Tools
A minimal MCP server that provides tools for analyzing file changes and suggesting PR templates.
"""

import json
import os
import subprocess
from typing import Optional
from pathlib import Path

from mcp.server.fastmcp import FastMCP

# Initialize the FastMCP server
mcp = FastMCP("pr-agent")

# PR template directory (shared between starter and solution)
TEMPLATES_DIR = Path(__file__).parent.parent.parent / "templates"

# Default PR templates
DEFAULT_TEMPLATES = {
    "bug.md": "Bug Fix",
    "feature.md": "Feature",
    "docs.md": "Documentation",
    "refactor.md": "Refactor",
    "test.md": "Test",
    "performance.md": "Performance",
    "security.md": "Security"
}

# Type mapping for PR templates
TYPE_MAPPING = {
    "bug": "bug.md",
    "fix": "bug.md",
    "feature": "feature.md",
    "enhancement": "feature.md",
    "docs": "docs.md",
    "documentation": "docs.md",
    "refactor": "refactor.md",
    "cleanup": "refactor.md",
    "test": "test.md",
    "testing": "test.md",
    "performance": "performance.md",
    "optimization": "performance.md",
    "security": "security.md"
}


@mcp.tool()
async def analyze_file_changes(
    base_branch: str = "main",
    include_diff: bool = True,
    max_diff_lines: int = 500,
    working_directory: Optional[str] = None
) -> str:
    """Get the full diff and list of changed files in the current git repository.
    
    Args:
        base_branch: Base branch to compare against (default: main)
        include_diff: Include the full diff content (default: true)
        max_diff_lines: Maximum number of diff lines to include (default: 500)
        working_directory: Directory to run git commands in (default: current directory)
    """
    try:
        # Try to get working directory from roots first
        if working_directory is None:
            try:
                context = mcp.get_context()
                roots_result = await context.session.list_roots()
                # Get the first root - Claude Code sets this to the CWD
                root = roots_result.roots[0]
                # FileUrl object has a .path property that gives us the path directly
                working_directory = root.uri.path
            except Exception:
                # If we can't get roots, fall back to current directory
                pass
        
        # Use provided working directory or current directory
        cwd = working_directory if working_directory else os.getcwd()
        
        # Debug output
        debug_info = {
            "provided_working_directory": working_directory,
            "actual_cwd": cwd,
            "server_process_cwd": os.getcwd(),
            "server_file_location": str(Path(__file__).parent),
            "roots_check": None
        }
        
        # Add roots debug info
        try:
            context = mcp.get_context()
            roots_result = await context.session.list_roots()
            debug_info["roots_check"] = {
                "found": True,
                "count": len(roots_result.roots),
                "roots": [str(root.uri) for root in roots_result.roots]
            }
        except Exception as e:
            debug_info["roots_check"] = {
                "found": False,
                "error": str(e)
            }
        
        # Get list of changed files
        files_result = subprocess.run(
            ["git", "diff", "--name-status", f"{base_branch}...HEAD"],
            capture_output=True,
            text=True,
            check=True,
            cwd=cwd
        )
        
        # Get diff statistics
        stat_result = subprocess.run(
            ["git", "diff", "--stat", f"{base_branch}...HEAD"],
            capture_output=True,
            text=True,
            cwd=cwd
        )
        
        # Get the actual diff if requested
        diff_content = ""
        truncated = False
        if include_diff:
            diff_result = subprocess.run(
                ["git", "diff", f"{base_branch}...HEAD"],
                capture_output=True,
                text=True,
                cwd=cwd
            )
            diff_lines = diff_result.stdout.split('\n')
            
            # Check if we need to truncate
            if len(diff_lines) > max_diff_lines:
                diff_content = '\n'.join(diff_lines[:max_diff_lines])
                diff_content += f"\n\n... Output truncated. Showing {max_diff_lines} of {len(diff_lines)} lines ..."
                diff_content += "\n... Use max_diff_lines parameter to see more ..."
                truncated = True
            else:
                diff_content = diff_result.stdout
        
        # Get commit messages for context
        commits_result = subprocess.run(
            ["git", "log", "--oneline", f"{base_branch}..HEAD"],
            capture_output=True,
            text=True,
            cwd=cwd
        )
        
        analysis = {
            "base_branch": base_branch,
            "files_changed": files_result.stdout,
            "statistics": stat_result.stdout,
            "commits": commits_result.stdout,
            "diff": diff_content if include_diff else "Diff not included (set include_diff=true to see full diff)",
            "truncated": truncated,
            "total_diff_lines": len(diff_lines) if include_diff else 0,
            "_debug": debug_info
        }
        
        return json.dumps(analysis, indent=2)
        
    except subprocess.CalledProcessError as e:
        return json.dumps({"error": f"Git error: {e.stderr}"})
    except Exception as e:
        return json.dumps({"error": str(e)})


@mcp.tool()
async def get_pr_templates() -> str:
    """List available PR templates with their content."""
    templates = [
        {
            "filename": filename,
            "type": template_type,
            "content": (TEMPLATES_DIR / filename).read_text()
        }
        for filename, template_type in DEFAULT_TEMPLATES.items()
    ]
    
    return json.dumps(templates, indent=2)


@mcp.tool()
async def suggest_template(changes_summary: str, change_type: str) -> str:
    """Let Claude analyze the changes and suggest the most appropriate PR template.
    
    Args:
        changes_summary: Your analysis of what the changes do
        change_type: The type of change you've identified (bug, feature, docs, refactor, test, etc.)
    """
    
    # Get available templates
    templates_response = await get_pr_templates()
    templates = json.loads(templates_response)
    
    # Find matching template
    template_file = TYPE_MAPPING.get(change_type.lower(), "feature.md")
    selected_template = next(
        (t for t in templates if t["filename"] == template_file),
        templates[0]  # Default to first template if no match
    )
    
    suggestion = {
        "recommended_template": selected_template,
        "reasoning": f"Based on your analysis: '{changes_summary}', this appears to be a {change_type} change.",
        "template_content": selected_template["content"],
        "usage_hint": "Claude can help you fill out this template based on the specific changes in your PR."
    }
    
    return json.dumps(suggestion, indent=2)


if __name__ == "__main__":
    mcp.run()
````

## File: projects/unit3/github-actions-integration/solution/server.py
````python
#!/usr/bin/env python3
"""
Module 2: GitHub Actions Integration with MCP Prompts
Extends the PR agent with webhook handling and standardized CI/CD workflows using Prompts.
"""

import json
import os
import subprocess
from typing import Optional
from pathlib import Path

from mcp.server.fastmcp import FastMCP

# Initialize the FastMCP server
mcp = FastMCP("pr-agent-actions")

# PR template directory (shared between starter and solution)
TEMPLATES_DIR = Path(__file__).parent.parent.parent / "templates"

# Default PR templates
DEFAULT_TEMPLATES = {
    "bug.md": "Bug Fix",
    "feature.md": "Feature",
    "docs.md": "Documentation",
    "refactor.md": "Refactor",
    "test.md": "Test",
    "performance.md": "Performance",
    "security.md": "Security"
}

# File where webhook server stores events
EVENTS_FILE = Path(__file__).parent / "github_events.json"

# Type mapping for PR templates
TYPE_MAPPING = {
    "bug": "bug.md",
    "fix": "bug.md",
    "feature": "feature.md",
    "enhancement": "feature.md",
    "docs": "docs.md",
    "documentation": "docs.md",
    "refactor": "refactor.md",
    "cleanup": "refactor.md",
    "test": "test.md",
    "testing": "test.md",
    "performance": "performance.md",
    "optimization": "performance.md",
    "security": "security.md"
}


# ===== Original Tools from Module 1 (with output limiting) =====

@mcp.tool()
async def analyze_file_changes(
    base_branch: str = "main",
    include_diff: bool = True,
    max_diff_lines: int = 500,
    working_directory: Optional[str] = None
) -> str:
    """Get the full diff and list of changed files in the current git repository.
    
    Args:
        base_branch: Base branch to compare against (default: main)
        include_diff: Include the full diff content (default: true)
        max_diff_lines: Maximum number of diff lines to include (default: 500)
        working_directory: Directory to run git commands in (default: current directory)
    """
    try:
        # Try to get working directory from roots first
        if working_directory is None:
            try:
                context = mcp.get_context()
                roots_result = await context.session.list_roots()
                # Get the first root - Claude Code sets this to the CWD
                root = roots_result.roots[0]
                # FileUrl object has a .path property that gives us the path directly
                working_directory = root.uri.path
            except Exception:
                # If we can't get roots, fall back to current directory
                pass
        
        # Use provided working directory or current directory
        cwd = working_directory if working_directory else os.getcwd()
        # Get list of changed files
        files_result = subprocess.run(
            ["git", "diff", "--name-status", f"{base_branch}...HEAD"],
            capture_output=True,
            text=True,
            check=True,
            cwd=cwd
        )
        
        # Get diff statistics
        stat_result = subprocess.run(
            ["git", "diff", "--stat", f"{base_branch}...HEAD"],
            capture_output=True,
            text=True,
            cwd=cwd
        )
        
        # Get the actual diff if requested
        diff_content = ""
        truncated = False
        if include_diff:
            diff_result = subprocess.run(
                ["git", "diff", f"{base_branch}...HEAD"],
                capture_output=True,
                text=True,
                cwd=cwd
            )
            diff_lines = diff_result.stdout.split('\n')
            
            # Check if we need to truncate
            if len(diff_lines) > max_diff_lines:
                diff_content = '\n'.join(diff_lines[:max_diff_lines])
                diff_content += f"\n\n... Output truncated. Showing {max_diff_lines} of {len(diff_lines)} lines ..."
                diff_content += "\n... Use max_diff_lines parameter to see more ..."
                truncated = True
            else:
                diff_content = diff_result.stdout
        
        # Get commit messages for context
        commits_result = subprocess.run(
            ["git", "log", "--oneline", f"{base_branch}..HEAD"],
            capture_output=True,
            text=True,
            cwd=cwd
        )
        
        analysis = {
            "base_branch": base_branch,
            "files_changed": files_result.stdout,
            "statistics": stat_result.stdout,
            "commits": commits_result.stdout,
            "diff": diff_content if include_diff else "Diff not included (set include_diff=true to see full diff)",
            "truncated": truncated,
            "total_diff_lines": len(diff_lines) if include_diff else 0
        }
        
        return json.dumps(analysis, indent=2)
        
    except subprocess.CalledProcessError as e:
        return json.dumps({"error": f"Git error: {e.stderr}"})
    except Exception as e:
        return json.dumps({"error": str(e)})


@mcp.tool()
async def get_pr_templates() -> str:
    """List available PR templates with their content."""
    templates = [
        {
            "filename": filename,
            "type": template_type,
            "content": (TEMPLATES_DIR / filename).read_text()
        }
        for filename, template_type in DEFAULT_TEMPLATES.items()
    ]
    
    return json.dumps(templates, indent=2)


@mcp.tool()
async def suggest_template(changes_summary: str, change_type: str) -> str:
    """Let Claude analyze the changes and suggest the most appropriate PR template.
    
    Args:
        changes_summary: Your analysis of what the changes do
        change_type: The type of change you've identified (bug, feature, docs, refactor, test, etc.)
    """
    
    # Get available templates
    templates_response = await get_pr_templates()
    templates = json.loads(templates_response)
    
    # Find matching template
    template_file = TYPE_MAPPING.get(change_type.lower(), "feature.md")
    selected_template = next(
        (t for t in templates if t["filename"] == template_file),
        templates[0]  # Default to first template if no match
    )
    
    suggestion = {
        "recommended_template": selected_template,
        "reasoning": f"Based on your analysis: '{changes_summary}', this appears to be a {change_type} change.",
        "template_content": selected_template["content"],
        "usage_hint": "Claude can help you fill out this template based on the specific changes in your PR."
    }
    
    return json.dumps(suggestion, indent=2)


# ===== New Module 2: GitHub Actions Tools =====

@mcp.tool()
async def get_recent_actions_events(limit: int = 10) -> str:
    """Get recent GitHub Actions events received via webhook.
    
    Args:
        limit: Maximum number of events to return (default: 10)
    """
    # Read events from file
    if not EVENTS_FILE.exists():
        return json.dumps([])
    
    with open(EVENTS_FILE, 'r') as f:
        events = json.load(f)
    
    # Return most recent events
    recent = events[-limit:]
    return json.dumps(recent, indent=2)


@mcp.tool()
async def get_workflow_status(workflow_name: Optional[str] = None) -> str:
    """Get the current status of GitHub Actions workflows.
    
    Args:
        workflow_name: Optional specific workflow name to filter by
    """
    # Read events from file
    if not EVENTS_FILE.exists():
        return json.dumps({"message": "No GitHub Actions events received yet"})
    
    with open(EVENTS_FILE, 'r') as f:
        events = json.load(f)
    
    if not events:
        return json.dumps({"message": "No GitHub Actions events received yet"})
    
    # Filter for workflow events
    workflow_events = [
        e for e in events 
        if e.get("workflow_run") is not None
    ]
    
    if workflow_name:
        workflow_events = [
            e for e in workflow_events
            if e["workflow_run"].get("name") == workflow_name
        ]
    
    # Group by workflow and get latest status
    workflows = {}
    for event in workflow_events:
        run = event["workflow_run"]
        name = run["name"]
        if name not in workflows or run["updated_at"] > workflows[name]["updated_at"]:
            workflows[name] = {
                "name": name,
                "status": run["status"],
                "conclusion": run.get("conclusion"),
                "run_number": run["run_number"],
                "updated_at": run["updated_at"],
                "html_url": run["html_url"]
            }
    
    return json.dumps(list(workflows.values()), indent=2)


# ===== New Module 2: MCP Prompts =====

@mcp.prompt()
async def analyze_ci_results():
    """Analyze recent CI/CD results and provide insights."""
    return """Please analyze the recent CI/CD results from GitHub Actions:

1. First, call get_recent_actions_events() to fetch the latest CI/CD events
2. Then call get_workflow_status() to check current workflow states
3. Identify any failures or issues that need attention
4. Provide actionable next steps based on the results

Format your response as:
## CI/CD Status Summary
- **Overall Health**: [Good/Warning/Critical]
- **Failed Workflows**: [List any failures with links]
- **Successful Workflows**: [List recent successes]
- **Recommendations**: [Specific actions to take]
- **Trends**: [Any patterns you notice]"""


@mcp.prompt()
async def create_deployment_summary():
    """Generate a deployment summary for team communication."""
    return """Create a deployment summary for team communication:

1. Check workflow status with get_workflow_status()
2. Look specifically for deployment-related workflows
3. Note the deployment outcome, timing, and any issues

Format as a concise message suitable for Slack:

🚀 **Deployment Update**
- **Status**: [✅ Success / ❌ Failed / ⏳ In Progress]
- **Environment**: [Production/Staging/Dev]
- **Version/Commit**: [If available from workflow data]
- **Duration**: [If available]
- **Key Changes**: [Brief summary if available]
- **Issues**: [Any problems encountered]
- **Next Steps**: [Required actions if failed]

Keep it brief but informative for team awareness."""


@mcp.prompt()
async def generate_pr_status_report():
    """Generate a comprehensive PR status report including CI/CD results."""
    return """Generate a comprehensive PR status report:

1. Use analyze_file_changes() to understand what changed
2. Use get_workflow_status() to check CI/CD status
3. Use suggest_template() to recommend the appropriate PR template
4. Combine all information into a cohesive report

Create a detailed report with:

## 📋 PR Status Report

### 📝 Code Changes
- **Files Modified**: [Count by type - .py, .js, etc.]
- **Change Type**: [Feature/Bug/Refactor/etc.]
- **Impact Assessment**: [High/Medium/Low with reasoning]
- **Key Changes**: [Bullet points of main modifications]

### 🔄 CI/CD Status
- **All Checks**: [✅ Passing / ❌ Failing / ⏳ Running]
- **Test Results**: [Pass rate, failed tests if any]
- **Build Status**: [Success/Failed with details]
- **Code Quality**: [Linting, coverage if available]

### 📌 Recommendations
- **PR Template**: [Suggested template and why]
- **Next Steps**: [What needs to happen before merge]
- **Reviewers**: [Suggested reviewers based on files changed]

### ⚠️ Risks & Considerations
- [Any deployment risks]
- [Breaking changes]
- [Dependencies affected]"""


@mcp.prompt()
async def troubleshoot_workflow_failure():
    """Help troubleshoot a failing GitHub Actions workflow."""
    return """Help troubleshoot failing GitHub Actions workflows:

1. Use get_recent_actions_events() to find recent failures
2. Use get_workflow_status() to see which workflows are failing
3. Analyze the failure patterns and timing
4. Provide systematic troubleshooting steps

Structure your response as:

## 🔧 Workflow Troubleshooting Guide

### ❌ Failed Workflow Details
- **Workflow Name**: [Name of failing workflow]
- **Failure Type**: [Test/Build/Deploy/Lint]
- **First Failed**: [When did it start failing]
- **Failure Rate**: [Intermittent or consistent]

### 🔍 Diagnostic Information
- **Error Patterns**: [Common error messages or symptoms]
- **Recent Changes**: [What changed before failures started]
- **Dependencies**: [External services or resources involved]

### 💡 Possible Causes (ordered by likelihood)
1. **[Most Likely]**: [Description and why]
2. **[Likely]**: [Description and why]
3. **[Possible]**: [Description and why]

### ✅ Suggested Fixes
**Immediate Actions:**
- [ ] [Quick fix to try first]
- [ ] [Second quick fix]

**Investigation Steps:**
- [ ] [How to gather more info]
- [ ] [Logs or data to check]

**Long-term Solutions:**
- [ ] [Preventive measure]
- [ ] [Process improvement]

### 📚 Resources
- [Relevant documentation links]
- [Similar issues or solutions]"""


if __name__ == "__main__":
    # Run MCP server normally
    print("Starting PR Agent MCP server...")
    print("To receive GitHub webhooks, run the webhook server separately:")
    print("  python webhook_server.py")
    mcp.run()
````

## File: projects/unit3/slack-notification/starter/server.py
````python
#!/usr/bin/env python3
"""
Module 3: Slack Notification Integration
Combines all MCP primitives (Tools and Prompts) for complete team communication workflows.
"""

import json
import os
import subprocess
from typing import Optional
from pathlib import Path

from mcp.server.fastmcp import FastMCP

# Initialize the FastMCP server
mcp = FastMCP("pr-agent-slack")

# PR template directory (shared between starter and solution)
TEMPLATES_DIR = Path(__file__).parent.parent.parent / "templates"

# Default PR templates
DEFAULT_TEMPLATES = {
    "bug.md": "Bug Fix",
    "feature.md": "Feature",
    "docs.md": "Documentation",
    "refactor.md": "Refactor",
    "test.md": "Test",
    "performance.md": "Performance",
    "security.md": "Security"
}

# File where webhook server stores events
EVENTS_FILE = Path(__file__).parent / "github_events.json"

# Type mapping for PR templates
TYPE_MAPPING = {
    "bug": "bug.md",
    "fix": "bug.md",
    "feature": "feature.md",
    "enhancement": "feature.md",
    "docs": "docs.md",
    "documentation": "docs.md",
    "refactor": "refactor.md",
    "cleanup": "refactor.md",
    "test": "test.md",
    "testing": "test.md",
    "performance": "performance.md",
    "optimization": "performance.md",
    "security": "security.md"
}


# ===== Tools from Modules 1 & 2 (Complete with output limiting) =====

@mcp.tool()
async def analyze_file_changes(
    base_branch: str = "main",
    include_diff: bool = True,
    max_diff_lines: int = 500
) -> str:
    """Get the full diff and list of changed files in the current git repository.
    
    Args:
        base_branch: Base branch to compare against (default: main)
        include_diff: Include the full diff content (default: true)
        max_diff_lines: Maximum number of diff lines to include (default: 500)
    """
    try:
        # Get list of changed files
        files_result = subprocess.run(
            ["git", "diff", "--name-status", f"{base_branch}...HEAD"],
            capture_output=True,
            text=True,
            check=True
        )
        
        # Get diff statistics
        stat_result = subprocess.run(
            ["git", "diff", "--stat", f"{base_branch}...HEAD"],
            capture_output=True,
            text=True
        )
        
        # Get the actual diff if requested
        diff_content = ""
        truncated = False
        if include_diff:
            diff_result = subprocess.run(
                ["git", "diff", f"{base_branch}...HEAD"],
                capture_output=True,
                text=True
            )
            diff_lines = diff_result.stdout.split('\n')
            
            # Check if we need to truncate
            if len(diff_lines) > max_diff_lines:
                diff_content = '\n'.join(diff_lines[:max_diff_lines])
                diff_content += f"\n\n... Output truncated. Showing {max_diff_lines} of {len(diff_lines)} lines ..."
                diff_content += "\n... Use max_diff_lines parameter to see more ..."
                truncated = True
            else:
                diff_content = diff_result.stdout
        
        # Get commit messages for context
        commits_result = subprocess.run(
            ["git", "log", "--oneline", f"{base_branch}..HEAD"],
            capture_output=True,
            text=True
        )
        
        analysis = {
            "base_branch": base_branch,
            "files_changed": files_result.stdout,
            "statistics": stat_result.stdout,
            "commits": commits_result.stdout,
            "diff": diff_content if include_diff else "Diff not included (set include_diff=true to see full diff)",
            "truncated": truncated,
            "total_diff_lines": len(diff_lines) if include_diff else 0
        }
        
        return json.dumps(analysis, indent=2)
        
    except subprocess.CalledProcessError as e:
        return json.dumps({"error": f"Git error: {e.stderr}"})
    except Exception as e:
        return json.dumps({"error": str(e)})


@mcp.tool()
async def get_pr_templates() -> str:
    """List available PR templates with their content."""
    templates = [
        {
            "filename": filename,
            "type": template_type,
            "content": (TEMPLATES_DIR / filename).read_text()
        }
        for filename, template_type in DEFAULT_TEMPLATES.items()
    ]
    
    return json.dumps(templates, indent=2)


@mcp.tool()
async def suggest_template(changes_summary: str, change_type: str) -> str:
    """Let Claude analyze the changes and suggest the most appropriate PR template.
    
    Args:
        changes_summary: Your analysis of what the changes do
        change_type: The type of change you've identified (bug, feature, docs, refactor, test, etc.)
    """
    
    # Get available templates
    templates_response = await get_pr_templates()
    templates = json.loads(templates_response)
    
    # Find matching template
    template_file = TYPE_MAPPING.get(change_type.lower(), "feature.md")
    selected_template = next(
        (t for t in templates if t["filename"] == template_file),
        templates[0]  # Default to first template if no match
    )
    
    suggestion = {
        "recommended_template": selected_template,
        "reasoning": f"Based on your analysis: '{changes_summary}', this appears to be a {change_type} change.",
        "template_content": selected_template["content"],
        "usage_hint": "Claude can help you fill out this template based on the specific changes in your PR."
    }
    
    return json.dumps(suggestion, indent=2)


@mcp.tool()
async def get_recent_actions_events(limit: int = 10) -> str:
    """Get recent GitHub Actions events received via webhook.
    
    Args:
        limit: Maximum number of events to return (default: 10)
    """
    # Read events from file
    if not EVENTS_FILE.exists():
        return json.dumps([])
    
    with open(EVENTS_FILE, 'r') as f:
        events = json.load(f)
    
    # Return most recent events
    recent = events[-limit:]
    return json.dumps(recent, indent=2)


@mcp.tool()
async def get_workflow_status(workflow_name: Optional[str] = None) -> str:
    """Get the current status of GitHub Actions workflows.
    
    Args:
        workflow_name: Optional specific workflow name to filter by
    """
    # Read events from file
    if not EVENTS_FILE.exists():
        return json.dumps({"message": "No GitHub Actions events received yet"})
    
    with open(EVENTS_FILE, 'r') as f:
        events = json.load(f)
    
    if not events:
        return json.dumps({"message": "No GitHub Actions events received yet"})
    
    # Filter for workflow events
    workflow_events = [
        e for e in events 
        if e.get("workflow_run") is not None
    ]
    
    if workflow_name:
        workflow_events = [
            e for e in workflow_events
            if e["workflow_run"].get("name") == workflow_name
        ]
    
    # Group by workflow and get latest status
    workflows = {}
    for event in workflow_events:
        run = event["workflow_run"]
        name = run["name"]
        if name not in workflows or run["updated_at"] > workflows[name]["updated_at"]:
            workflows[name] = {
                "name": name,
                "status": run["status"],
                "conclusion": run.get("conclusion"),
                "run_number": run["run_number"],
                "updated_at": run["updated_at"],
                "html_url": run["html_url"]
            }
    
    return json.dumps(list(workflows.values()), indent=2)


# ===== New Module 3: Slack Integration Tools =====

@mcp.tool()
async def send_slack_notification(message: str) -> str:
    """Send a formatted notification to the team Slack channel.
    
    Args:
        message: The message to send to Slack (supports Slack markdown)
    """
    webhook_url = os.getenv("SLACK_WEBHOOK_URL")
    if not webhook_url:
        return "Error: SLACK_WEBHOOK_URL environment variable not set"
    
    try:
        # TODO: Import requests library
        # TODO: Send POST request to webhook_url with JSON payload
        # TODO: Include the message in the JSON data
        # TODO: Handle the response and return appropriate status
        
        # For now, return a placeholder
        return f"TODO: Implement Slack webhook POST request for message: {message[:50]}..."
        
    except Exception as e:
        return f"Error sending message: {str(e)}"


# ===== New Module 3: Slack Formatting Prompts =====

@mcp.prompt()
async def format_ci_failure_alert():
    """Create a Slack alert for CI/CD failures with rich formatting."""
    return """Format this GitHub Actions failure as a Slack message using ONLY Slack markdown syntax:

❌ *CI Failed* - [Repository Name]

> Brief summary of what failed

*Details:*
• Workflow: `workflow_name`
• Branch: `branch_name`  
• Commit: `commit_hash`

*Next Steps:*
• <https://github.com/test/repo/actions/runs/123|View Action Logs>

CRITICAL: Use EXACT Slack link format: <https://full-url|Link Text>
Examples:
- CORRECT: <https://github.com/user/repo|Repository>
- WRONG: [Repository](https://github.com/user/repo)
- WRONG: https://github.com/user/repo

Other Slack formats:
- *text* for bold (NOT **text**)
- `text` for code
- > text for quotes
- • for bullets"""


@mcp.prompt()
async def format_ci_success_summary():
    """Create a Slack message celebrating successful deployments."""
    return """Format this successful GitHub Actions run as a Slack message using ONLY Slack markdown syntax:

✅ *Deployment Successful* - [Repository Name]

> Brief summary of what was deployed

*Changes:*
• Key feature or fix 1
• Key feature or fix 2

*Links:*
• <https://github.com/user/repo|View Changes>

CRITICAL: Use EXACT Slack link format: <https://full-url|Link Text>
Examples:
- CORRECT: <https://github.com/user/repo|Repository>
- WRONG: [Repository](https://github.com/user/repo)
- WRONG: https://github.com/user/repo

Other Slack formats:
- *text* for bold (NOT **text**)
- `text` for code
- > text for quotes
- • for bullets"""


# ===== Prompts from Module 2 (Complete) =====

@mcp.prompt()
async def analyze_ci_results():
    """Analyze recent CI/CD results and provide insights."""
    return """Please analyze the recent CI/CD results from GitHub Actions:

1. First, call get_recent_actions_events() to fetch the latest CI/CD events
2. Then call get_workflow_status() to check current workflow states
3. Identify any failures or issues that need attention
4. Provide actionable next steps based on the results

Format your response as:
## CI/CD Status Summary
- **Overall Health**: [Good/Warning/Critical]
- **Failed Workflows**: [List any failures with links]
- **Successful Workflows**: [List recent successes]
- **Recommendations**: [Specific actions to take]
- **Trends**: [Any patterns you notice]"""


@mcp.prompt()
async def create_deployment_summary():
    """Generate a deployment summary for team communication."""
    return """Create a deployment summary for team communication:

1. Check workflow status with get_workflow_status()
2. Look specifically for deployment-related workflows
3. Note the deployment outcome, timing, and any issues

Format as a concise message suitable for Slack:

🚀 **Deployment Update**
- **Status**: [✅ Success / ❌ Failed / ⏳ In Progress]
- **Environment**: [Production/Staging/Dev]
- **Version/Commit**: [If available from workflow data]
- **Duration**: [If available]
- **Key Changes**: [Brief summary if available]
- **Issues**: [Any problems encountered]
- **Next Steps**: [Required actions if failed]

Keep it brief but informative for team awareness."""


@mcp.prompt()
async def generate_pr_status_report():
    """Generate a comprehensive PR status report including CI/CD results."""
    return """Generate a comprehensive PR status report:

1. Use analyze_file_changes() to understand what changed
2. Use get_workflow_status() to check CI/CD status
3. Use suggest_template() to recommend the appropriate PR template
4. Combine all information into a cohesive report

Create a detailed report with:

## 📋 PR Status Report

### 📝 Code Changes
- **Files Modified**: [Count by type - .py, .js, etc.]
- **Change Type**: [Feature/Bug/Refactor/etc.]
- **Impact Assessment**: [High/Medium/Low with reasoning]
- **Key Changes**: [Bullet points of main modifications]

### 🔄 CI/CD Status
- **All Checks**: [✅ Passing / ❌ Failing / ⏳ Running]
- **Test Results**: [Pass rate, failed tests if any]
- **Build Status**: [Success/Failed with details]
- **Code Quality**: [Linting, coverage if available]

### 📌 Recommendations
- **PR Template**: [Suggested template and why]
- **Next Steps**: [What needs to happen before merge]
- **Reviewers**: [Suggested reviewers based on files changed]

### ⚠️ Risks & Considerations
- [Any deployment risks]
- [Breaking changes]
- [Dependencies affected]"""


@mcp.prompt()
async def troubleshoot_workflow_failure():
    """Help troubleshoot a failing GitHub Actions workflow."""
    return """Help troubleshoot failing GitHub Actions workflows:

1. Use get_recent_actions_events() to find recent failures
2. Use get_workflow_status() to see which workflows are failing
3. Analyze the failure patterns and timing
4. Provide systematic troubleshooting steps

Structure your response as:

## 🔧 Workflow Troubleshooting Guide

### ❌ Failed Workflow Details
- **Workflow Name**: [Name of failing workflow]
- **Failure Type**: [Test/Build/Deploy/Lint]
- **First Failed**: [When did it start failing]
- **Failure Rate**: [Intermittent or consistent]

### 🔍 Diagnostic Information
- **Error Patterns**: [Common error messages or symptoms]
- **Recent Changes**: [What changed before failures started]
- **Dependencies**: [External services or resources involved]

### 💡 Possible Causes (ordered by likelihood)
1. **[Most Likely]**: [Description and why]
2. **[Likely]**: [Description and why]
3. **[Possible]**: [Description and why]

### ✅ Suggested Fixes
**Immediate Actions:**
- [ ] [Quick fix to try first]
- [ ] [Second quick fix]

**Investigation Steps:**
- [ ] [How to gather more info]
- [ ] [Logs or data to check]

**Long-term Solutions:**
- [ ] [Preventive measure]
- [ ] [Process improvement]

### 📚 Resources
- [Relevant documentation links]
- [Similar issues or solutions]"""


if __name__ == "__main__":
    # Run MCP server normally
    print("Starting PR Agent Slack MCP server...")
    print("Make sure to set SLACK_WEBHOOK_URL environment variable")
    print("To receive GitHub webhooks, run the webhook server separately:")
    print("  python webhook_server.py")
    mcp.run()
````

## File: units/en/unit1/sdk.mdx
````
# MCP SDK

The Model Context Protocol provides official SDKs for both JavaScript, Python and other languages. This makes it easy to implement MCP clients and servers in your applications. These SDKs handle the low-level protocol details, allowing you to focus on building your application's capabilities.

## SDK Overview

Both SDKs provide similar core functionality, following the MCP protocol specification we discussed earlier. They handle:

- Protocol-level communication
- Capability registration and discovery
- Message serialization/deserialization
- Connection management
- Error handling

## Core Primitives Implementation

Let's explore how to implement each of the core primitives (Tools, Resources, and Prompts) using both SDKs.

<hfoptions id="server-implementation">
<hfoption id="python">

<Youtube id="exzrb5QNUis" />

```python
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Weather Service")

# Tool implementation
@mcp.tool()
def get_weather(location: str) -> str:
    """Get the current weather for a specified location."""
    return f"Weather in {location}: Sunny, 72°F"

# Resource implementation
@mcp.resource("weather://{location}")
def weather_resource(location: str) -> str:
    """Provide weather data as a resource."""
    return f"Weather data for {location}: Sunny, 72°F"

# Prompt implementation
@mcp.prompt()
def weather_report(location: str) -> str:
    """Create a weather report prompt."""
    return f"""You are a weather reporter. Weather report for {location}?"""


# Run the server
if __name__ == "__main__":
    mcp.run()
```

Once you have your server implemented, you can start it by running the server script.

```bash
mcp dev server.py
```

</hfoption>
<hfoption id="javascript">

```javascript
// index.mjs
import {
  McpServer,
  ResourceTemplate,
} from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Create an MCP server
const server = new McpServer({
  name: "Weather Service",
  version: "1.0.0",
});

// Tool implementation
server.tool("get_weather", { location: z.string() }, async ({ location }) => ({
  content: [
    {
      type: "text",
      text: `Weather in ${location}: Sunny, 72°F`,
    },
  ],
}));

// Resource implementation
server.resource(
  "weather",
  new ResourceTemplate("weather://{location}", { list: undefined }),
  async (uri, { location }) => ({
    contents: [
      {
        uri: uri.href,
        text: `Weather data for ${location}: Sunny, 72°F`,
      },
    ],
  })
);

// Prompt implementation
server.prompt(
  "weather_report",
  { location: z.string() },
  async ({ location }) => ({
    messages: [
      {
        role: "assistant",
        content: {
          type: "text",
          text: "You are a weather reporter.",
        },
      },
      {
        role: "user",
        content: {
          type: "text",
          text: `Weather report for ${location}?`,
        },
      },
    ],
  })
);

// Run the server
const transport = new StdioServerTransport();
await server.connect(transport);
```

Once you have your server implemented, you can start it by running the server script.

```bash
npx @modelcontextprotocol/inspector node ./index.mjs
```

</hfoption>
</hfoptions>

This will initialize a development server running the file `server.py`. And log the following output:

```bash
Starting MCP inspector...
⚙️ Proxy server listening on port 6277
Spawned stdio transport
Connected MCP client to backing server transport
Created web app transport
Set up MCP proxy
🔍 MCP Inspector is up and running at http://127.0.0.1:6274 🚀
```

You can then open the MCP Inspector at [http://127.0.0.1:6274](http://127.0.0.1:6274) to see the server's capabilities and interact with them.

You'll see the server's capabilities and the ability to call them via the UI.

![MCP Inspector](https://huggingface.co/datasets/mcp-course/images/resolve/main/unit1/6.png)

## MCP SDKs

MCP is designed to be language-agnostic, and there are official SDKs available for several popular programming languages:

| Language   | Repository                                                                                               | Maintainer(s)       | Status           |
| ---------- | -------------------------------------------------------------------------------------------------------- | ------------------- | ---------------- |
| TypeScript | [github.com/modelcontextprotocol/typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk) | Anthropic           | Active           |
| Python     | [github.com/modelcontextprotocol/python-sdk](https://github.com/modelcontextprotocol/python-sdk)         | Anthropic           | Active           |
| Java       | [github.com/modelcontextprotocol/java-sdk](https://github.com/modelcontextprotocol/java-sdk)             | Spring AI (VMware)  | Active           |
| Kotlin     | [github.com/modelcontextprotocol/kotlin-sdk](https://github.com/modelcontextprotocol/kotlin-sdk)         | JetBrains           | Active           |
| C#         | [github.com/modelcontextprotocol/csharp-sdk](https://github.com/modelcontextprotocol/csharp-sdk)         | Microsoft           | Active (Preview) |
| Swift      | [github.com/modelcontextprotocol/swift-sdk](https://github.com/modelcontextprotocol/swift-sdk)           | loopwork-ai         | Active           |
| Rust       | [github.com/modelcontextprotocol/rust-sdk](https://github.com/modelcontextprotocol/rust-sdk)             | Anthropic/Community | Active           |
| Dart       | [https://github.com/leehack/mcp_dart](https://github.com/leehack/mcp_dart)                               | Flutter Community   | Active           |

These SDKs provide language-specific abstractions that simplify working with the MCP protocol, allowing you to focus on implementing the core logic of your servers or clients rather than dealing with low-level protocol details.

## Next Steps

We've only scratched the surface of what you can do with the MCP but you've already got a basic server running. In fact, you've also connected to it using the MCP Client in the browser.

In the next section, we'll look at how to connect to your server from an LLM.
````

## File: units/en/unit2/tiny-agents.mdx
````
# Building Tiny Agents with MCP and the Hugging Face Hub

Now that we've built MCP servers in Gradio and learned about creating MCP clients, let's complete our end-to-end application by building an agent that can seamlessly interact with our sentiment analysis tool. This section builds on the project [Tiny Agents](https://huggingface.co/blog/tiny-agents), which demonstrates a super simple way of deploying MCP clients that can connect to services like our Gradio sentiment analysis server.

In this final exercise of Unit 2, we will walk you through how to implement both TypeScript (JS) and Python MCP clients that can communicate with any MCP server, including the Gradio-based sentiment analysis server we built in the previous sections. This completes our end-to-end MCP application flow: from building a Gradio MCP server exposing a sentiment analysis tool, to creating a flexible agent that can use this tool alongside other capabilities.

![meme](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/tiny-agents/thumbnail.jpg)
<figcaption>Image credit https://x.com/adamdotdev</figcaption>

## Installation

Let's install the necessary packages to build our Tiny Agents.

<Tip>

Some MCP Clients, notably Claude Desktop, do not yet support SSE-based MCP Servers. In those cases, you can use a tool such as [mcp-remote](https://github.com/geelen/mcp-remote). First install Node.js. Then, add the following to your own MCP Client config:

</Tip>

Tiny Agent can run MCP servers with a command line environment. To do this, we will need to install `npm` and run the server with `npx`. **We'll need these for both Python and JavaScript.**

Let's install `npx` with `npm`. If you don't have `npm` installed, check out the [npm documentation](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm).

```bash
# install npx
npm install -g npx
```

Then, we need to install the `mcp-remote` package.

```bash
npm i mcp-remote
```

<hfoptions id="tiny-agents">
<hfoption id="typescript">

For JavaScript, we need to install the `tiny-agents` package.

```bash
npm install @huggingface/tiny-agents
```

</hfoption>
<hfoption id="python">

For Python, you need to install the latest version of `huggingface_hub` with the `mcp` extra to get all the necessary components.

```bash
pip install "huggingface_hub[mcp]>=0.32.0"
```

</hfoption>
</hfoptions>

## Tiny Agents MCP Client in the Command Line

Let's repeat the example from [Unit 1](../unit1/mcp-clients.mdx) to create a basic Tiny Agent. Tiny Agents can create MCP clients from the command line based on JSON configuration files.

<hfoptions id="tiny-agents">
<hfoption id="typescript">

Let's setup a project with a basic Tiny Agent.

```bash
mkdir my-agent
touch my-agent/agent.json
```

The JSON file will look like this:

```json
{
	"model": "Qwen/Qwen2.5-72B-Instruct",
	"provider": "nebius",
	"servers": [
		{
			"type": "stdio",
			"config": {
				"command": "npx",
				"args": [
					"mcp-remote",
					"http://localhost:7860/gradio_api/mcp/sse" // This is the MCP Server we created in the previous section
				]
			}
		}
	]
}
```

We can then run the agent with the following command:

```bash
npx @huggingface/tiny-agents run ./my-agent
```

</hfoption>
<hfoption id="python">

Let's setup a project with a basic Tiny Agent.

```bash
mkdir my-agent
touch my-agent/agent.json
cd my-agent
```

The JSON file will look like this:

```json
{
	"model": "Qwen/Qwen2.5-72B-Instruct",
	"provider": "nebius",
	"servers": [
		{
			"type": "stdio",
			"config": {
				"command": "npx",
				"args": [
					"mcp-remote", 
					"http://localhost:7860/gradio_api/mcp/sse"
				]
			}
		}
	]
}
```

We can then run the agent with the following command:

```bash
tiny-agents run agent.json
```

</hfoption>
</hfoptions>

Here we have a basic Tiny Agent that can connect to our Gradio MCP server. It includes a model, provider, and a server configuration.

| Field | Description |
|-------|-------------|
| `model` | The open source model to use for the agent |
| `provider` | The inference provider to use for the agent |
| `servers` | The servers to use for the agent. We'll use the `mcp-remote` server for our Gradio MCP server. |

<Tip>

We could also use an open source model running locally with Tiny Agents. If we start a local inference server with 

```json
{
	"model": "Qwen/Qwen3-32B",
	"endpointUrl": "http://localhost:1234/v1",
	"servers": [
		{
			"type": "stdio",
			"config": {
				"command": "npx",
				"args": [
					"mcp-remote",
					"http://localhost:1234/v1/mcp/sse"
				]
			}
		}
	]
}
```


Here we have a Tiny Agent that can connect to a local model. It includes a model, endpoint URL (`http://localhost:1234/v1`), and a server configuration. The endpoint should be an OpenAI-compatible endpoint.

</Tip>

## Custom Tiny Agents MCP Client

Now that we understand both Tiny Agents and Gradio MCP servers, let's see how they work together! The beauty of MCP is that it provides a standardized way for agents to interact with any MCP-compatible server, including our Gradio-based sentiment analysis server from earlier sections.

### Using the Gradio Server with Tiny Agents

To connect our Tiny Agent to the Gradio sentiment analysis server we built earlier in this unit, we just need to add it to our list of servers. Here's how we can modify our agent configuration:

<hfoptions id="tiny-agents">
<hfoption id="typescript">

```ts
const agent = new Agent({
    provider: process.env.PROVIDER ?? "nebius",
    model: process.env.MODEL_ID ?? "Qwen/Qwen2.5-72B-Instruct",
    apiKey: process.env.HF_TOKEN,
    servers: [
        // ... existing servers ...
        {
            command: "npx",
            args: [
                "mcp-remote",
                "http://localhost:7860/gradio_api/mcp/sse"  // Your Gradio MCP server
            ]
        }
    ],
});
```

</hfoption>
<hfoption id="python">

```python
import os

from huggingface_hub import Agent

agent = Agent(
    model="Qwen/Qwen2.5-72B-Instruct",
    provider="nebius",
    servers=[
        {
            "command": "npx",
            "args": [
                "mcp-remote",
                "http://localhost:7860/gradio_api/mcp/sse"  # Your Gradio MCP server
            ]
        }
    ],
)
```

</hfoption>
</hfoptions>

Now our agent can use the sentiment analysis tool alongside other tools! For example, it could:
1. Read text from a file using the filesystem server
2. Analyze its sentiment using our Gradio server
3. Write the results back to a file

### Deployment Considerations

When deploying your Gradio MCP server to Hugging Face Spaces, you'll need to update the server URL in your agent configuration to point to your deployed space:


```json
{
    command: "npx",
    args: [
        "mcp-remote",
        "https://YOUR_USERNAME-mcp-sentiment.hf.space/gradio_api/mcp/sse"
    ]
}
```


This allows your agent to use the sentiment analysis tool from anywhere, not just locally!

## Conclusion: Our Complete End-to-End MCP Application

In this unit, we've gone from understanding MCP basics to building a complete end-to-end application:

1. We created a Gradio MCP server that exposes a sentiment analysis tool
2. We learned how to connect to this server using MCP clients
3. We built a tiny agent in TypeScript and Python that can interact with our tool

This demonstrates the power of the Model Context Protocol - we can create specialized tools using frameworks we're familiar with (like Gradio), expose them through a standardized interface (MCP), and then have agents seamlessly use these tools alongside other capabilities.

The complete flow we've built allows an agent to:
- Connect to multiple tool providers
- Dynamically discover available tools
- Use our custom sentiment analysis tool
- Combine it with other capabilities like file system access and web browsing

This modular approach is what makes MCP so powerful for building flexible AI applications.

## Next Steps

- Check out the Tiny Agents blog posts in [Python](https://huggingface.co/blog/python-tiny-agents) and [TypeScript](https://huggingface.co/blog/tiny-agents)
- Review the [Tiny Agents documentation](https://huggingface.co/docs/huggingface.js/main/en/tiny-agents/README)
- Build something with Tiny Agents!
````

## File: units/en/unit2/clients.mdx
````
# Building MCP Clients

In this section, we'll create clients that can interact with our MCP server using different programming languages. We'll implement both a JavaScript client using HuggingFace.js and a Python client using smolagents.

## Configuring MCP Clients

Effective deployment of MCP servers and clients requires proper configuration. The MCP specification is still evolving, so the configuration methods are subject to evolution. We'll focus on the current best practices for configuration.

### MCP Configuration Files

MCP hosts use configuration files to manage server connections. These files define which servers are available and how to connect to them.

The configuration files are very simple, easy to understand, and consistent across major MCP hosts.

#### `mcp.json` Structure

The standard configuration file for MCP is named `mcp.json`. Here's the basic structure:

```json
{
  "servers": [
    {
      "name": "MCP Server",
      "transport": {
        "type": "sse",
        "url": "http://localhost:7860/gradio_api/mcp/sse"
      }
    }
  ]
}
```

In this example, we have a single server configured to use SSE transport, connecting to a local Gradio server running on port 7860.

<Tip>

We've connected to the Gradio app via SSE transport because we assume that the gradio app is running on a remote server. However, if you want to connect to a local script, `stdio` transport instead of `sse` transport is a better option.

</Tip>

#### Configuration for HTTP+SSE Transport

For remote servers using HTTP+SSE transport, the configuration includes the server URL:

```json
{
  "servers": [
    {
      "name": "Remote MCP Server",
      "transport": {
        "type": "sse",
        "url": "https://example.com/gradio_api/mcp/sse"
      }
    }
  ]
}
```

This configuration allows your UI client to communicate with the Gradio MCP server using the MCP protocol, enabling seamless integration between your frontend and the MCP service.

## Configuring a UI MCP Client

When working with Gradio MCP servers, you can configure your UI client to connect to the server using the MCP protocol. Here's how to set it up:

### Basic Configuration

Create a new file called `config.json` with the following configuration:

```json
{
  "mcpServers": {
    "mcp": {
      "url": "http://localhost:7860/gradio_api/mcp/sse"
    }
  }
}
```

This configuration allows your UI client to communicate with the Gradio MCP server using the MCP protocol, enabling seamless integration between your frontend and the MCP service.

## Configuring an MCP Client within Cursor IDE

Cursor provides built-in MCP support, allowing you to connect your deployed MCP servers directly to your development environment.

### Configuration

Open Cursor settings (`Ctrl + Shift + J` / `Cmd + Shift + J`) → **MCP** tab → **Add new global MCP server**:

**macOS:**
```json
{
  "mcpServers": {
    "sentiment-analysis": {
      "command": "npx",
      "args": [
        "-y", 
        "mcp-remote", 
        "https://YOURUSENAME-mcp-sentiment.hf.space/gradio_api/mcp/sse", 
        "--transport", 
        "sse-only"
      ]
    }
  }
}
```

**Windows:**
```json
{
  "mcpServers": {
    "sentiment-analysis": {
      "command": "cmd",
      "args": [
        "/c", 
        "npx", 
        "-y", 
        "mcp-remote", 
        "https://YOURUSENAME-mcp-sentiment.hf.space/gradio_api/mcp/sse", 
        "--transport", 
        "sse-only"
      ]
    }
  }
}
```

### Why We Use mcp-remote

Most MCP clients, including Cursor, currently only support local servers via stdio transport and don't yet support remote servers with OAuth authentication. The `mcp-remote` tool serves as a bridge solution that:

- Runs locally on your machine
- Forwards requests from Cursor to the remote MCP server
- Uses the familiar configuration file format

Once configured, you can ask Cursor to use your sentiment analysis tool for tasks like analyzing code comments, user feedback, or pull request descriptions.
````

## File: projects/unit3/slack-notification/solution/server.py
````python
#!/usr/bin/env python3
"""
Module 3: Slack Notification Integration - Complete Solution
Combines all MCP primitives (Tools and Prompts) for complete team communication workflows.
"""

import json
import os
import subprocess
import requests
from typing import Optional
from pathlib import Path

from mcp.server.fastmcp import FastMCP

# Initialize the FastMCP server
mcp = FastMCP("pr-agent-slack")

# PR template directory (shared between starter and solution)
TEMPLATES_DIR = Path(__file__).parent.parent.parent / "templates"

# Default PR templates
DEFAULT_TEMPLATES = {
    "bug.md": "Bug Fix",
    "feature.md": "Feature",
    "docs.md": "Documentation",
    "refactor.md": "Refactor",
    "test.md": "Test",
    "performance.md": "Performance",
    "security.md": "Security"
}

# File where webhook server stores events
EVENTS_FILE = Path(__file__).parent / "github_events.json"

# Type mapping for PR templates
TYPE_MAPPING = {
    "bug": "bug.md",
    "fix": "bug.md",
    "feature": "feature.md",
    "enhancement": "feature.md",
    "docs": "docs.md",
    "documentation": "docs.md",
    "refactor": "refactor.md",
    "cleanup": "refactor.md",
    "test": "test.md",
    "testing": "test.md",
    "performance": "performance.md",
    "optimization": "performance.md",
    "security": "security.md"
}


# ===== Tools from Modules 1 & 2 (Complete with output limiting) =====

@mcp.tool()
async def analyze_file_changes(
    base_branch: str = "main",
    include_diff: bool = True,
    max_diff_lines: int = 500,
    working_directory: Optional[str] = None
) -> str:
    """Get the full diff and list of changed files in the current git repository.
    
    Args:
        base_branch: Base branch to compare against (default: main)
        include_diff: Include the full diff content (default: true)
        max_diff_lines: Maximum number of diff lines to include (default: 500)
        working_directory: Directory to run git commands in (default: current directory)
    """
    try:
        # Try to get working directory from roots first
        if working_directory is None:
            try:
                context = mcp.get_context()
                roots_result = await context.session.list_roots()
                # Get the first root - Claude Code sets this to the CWD
                root = roots_result.roots[0]
                # FileUrl object has a .path property that gives us the path directly
                working_directory = root.uri.path
            except Exception:
                # If we can't get roots, fall back to current directory
                pass
        
        # Use provided working directory or current directory
        cwd = working_directory if working_directory else os.getcwd()
        # Get list of changed files
        files_result = subprocess.run(
            ["git", "diff", "--name-status", f"{base_branch}...HEAD"],
            capture_output=True,
            text=True,
            check=True,
            cwd=cwd
        )
        
        # Get diff statistics
        stat_result = subprocess.run(
            ["git", "diff", "--stat", f"{base_branch}...HEAD"],
            capture_output=True,
            text=True,
            cwd=cwd
        )
        
        # Get the actual diff if requested
        diff_content = ""
        truncated = False
        if include_diff:
            diff_result = subprocess.run(
                ["git", "diff", f"{base_branch}...HEAD"],
                capture_output=True,
                text=True,
                cwd=cwd
            )
            diff_lines = diff_result.stdout.split('\n')
            
            # Check if we need to truncate
            if len(diff_lines) > max_diff_lines:
                diff_content = '\n'.join(diff_lines[:max_diff_lines])
                diff_content += f"\n\n... Output truncated. Showing {max_diff_lines} of {len(diff_lines)} lines ..."
                diff_content += "\n... Use max_diff_lines parameter to see more ..."
                truncated = True
            else:
                diff_content = diff_result.stdout
        
        # Get commit messages for context
        commits_result = subprocess.run(
            ["git", "log", "--oneline", f"{base_branch}..HEAD"],
            capture_output=True,
            text=True,
            cwd=cwd
        )
        
        analysis = {
            "base_branch": base_branch,
            "files_changed": files_result.stdout,
            "statistics": stat_result.stdout,
            "commits": commits_result.stdout,
            "diff": diff_content if include_diff else "Diff not included (set include_diff=true to see full diff)",
            "truncated": truncated,
            "total_diff_lines": len(diff_lines) if include_diff else 0
        }
        
        return json.dumps(analysis, indent=2)
        
    except subprocess.CalledProcessError as e:
        return json.dumps({"error": f"Git error: {e.stderr}"})
    except Exception as e:
        return json.dumps({"error": str(e)})


@mcp.tool()
async def get_pr_templates() -> str:
    """List available PR templates with their content."""
    templates = [
        {
            "filename": filename,
            "type": template_type,
            "content": (TEMPLATES_DIR / filename).read_text()
        }
        for filename, template_type in DEFAULT_TEMPLATES.items()
    ]
    
    return json.dumps(templates, indent=2)


@mcp.tool()
async def suggest_template(changes_summary: str, change_type: str) -> str:
    """Let Claude analyze the changes and suggest the most appropriate PR template.
    
    Args:
        changes_summary: Your analysis of what the changes do
        change_type: The type of change you've identified (bug, feature, docs, refactor, test, etc.)
    """
    
    # Get available templates
    templates_response = await get_pr_templates()
    templates = json.loads(templates_response)
    
    # Find matching template
    template_file = TYPE_MAPPING.get(change_type.lower(), "feature.md")
    selected_template = next(
        (t for t in templates if t["filename"] == template_file),
        templates[0]  # Default to first template if no match
    )
    
    suggestion = {
        "recommended_template": selected_template,
        "reasoning": f"Based on your analysis: '{changes_summary}', this appears to be a {change_type} change.",
        "template_content": selected_template["content"],
        "usage_hint": "Claude can help you fill out this template based on the specific changes in your PR."
    }
    
    return json.dumps(suggestion, indent=2)


@mcp.tool()
async def get_recent_actions_events(limit: int = 10) -> str:
    """Get recent GitHub Actions events received via webhook.
    
    Args:
        limit: Maximum number of events to return (default: 10)
    """
    # Read events from file
    if not EVENTS_FILE.exists():
        return json.dumps([])
    
    with open(EVENTS_FILE, 'r') as f:
        events = json.load(f)
    
    # Return most recent events
    recent = events[-limit:]
    return json.dumps(recent, indent=2)


@mcp.tool()
async def get_workflow_status(workflow_name: Optional[str] = None) -> str:
    """Get the current status of GitHub Actions workflows.
    
    Args:
        workflow_name: Optional specific workflow name to filter by
    """
    # Read events from file
    if not EVENTS_FILE.exists():
        return json.dumps({"message": "No GitHub Actions events received yet"})
    
    with open(EVENTS_FILE, 'r') as f:
        events = json.load(f)
    
    if not events:
        return json.dumps({"message": "No GitHub Actions events received yet"})
    
    # Filter for workflow events
    workflow_events = [
        e for e in events 
        if e.get("workflow_run") is not None
    ]
    
    if workflow_name:
        workflow_events = [
            e for e in workflow_events
            if e["workflow_run"].get("name") == workflow_name
        ]
    
    # Group by workflow and get latest status
    workflows = {}
    for event in workflow_events:
        run = event["workflow_run"]
        name = run["name"]
        if name not in workflows or run["updated_at"] > workflows[name]["updated_at"]:
            workflows[name] = {
                "name": name,
                "status": run["status"],
                "conclusion": run.get("conclusion"),
                "run_number": run["run_number"],
                "updated_at": run["updated_at"],
                "html_url": run["html_url"]
            }
    
    return json.dumps(list(workflows.values()), indent=2)


# ===== New Module 3: Slack Integration Tools =====

@mcp.tool()
async def send_slack_notification(message: str) -> str:
    """Send a formatted notification to the team Slack channel.
    
    Args:
        message: The message to send to Slack (supports Slack markdown)
        
    IMPORTANT: For CI failures, use format_ci_failure_alert prompt first!
    IMPORTANT: For deployments, use format_ci_success_summary prompt first!
    """
    webhook_url = os.getenv("SLACK_WEBHOOK_URL")
    if not webhook_url:
        return "Error: SLACK_WEBHOOK_URL environment variable not set"
    
    try:
        # Prepare the payload with proper Slack formatting
        payload = {
            "text": message,
            "mrkdwn": True
        }
        
        # Send POST request to Slack webhook
        response = requests.post(
            webhook_url,
            json=payload,
            timeout=10
        )
        
        # Check if request was successful
        if response.status_code == 200:
            return "✅ Message sent successfully to Slack"
        else:
            return f"❌ Failed to send message. Status: {response.status_code}, Response: {response.text}"
        
    except requests.exceptions.Timeout:
        return "❌ Request timed out. Check your internet connection and try again."
    except requests.exceptions.ConnectionError:
        return "❌ Connection error. Check your internet connection and webhook URL."
    except Exception as e:
        return f"❌ Error sending message: {str(e)}"


# ===== New Module 3: Slack Formatting Prompts =====

@mcp.prompt()
async def format_ci_failure_alert():
    """Create a Slack alert for CI/CD failures with rich formatting."""
    return """Format this GitHub Actions failure as a Slack message using ONLY Slack markdown syntax:

:rotating_light: *CI Failure Alert* :rotating_light:

A CI workflow has failed:
*Workflow*: workflow_name
*Branch*: branch_name
*Status*: Failed
*View Details*: <https://github.com/test/repo/actions/runs/123|View Logs>

Please check the logs and address any issues.

CRITICAL: Use EXACT Slack link format: <https://full-url|Link Text>
Examples:
- CORRECT: <https://github.com/user/repo|Repository>
- WRONG: [Repository](https://github.com/user/repo)
- WRONG: https://github.com/user/repo

Slack formatting rules:
- *text* for bold (NOT **text**)
- `text` for code
- > text for quotes
- Use simple bullet format without special characters
- :emoji_name: for emojis"""


@mcp.prompt()
async def format_ci_success_summary():
    """Create a Slack message celebrating successful deployments."""
    return """Format this successful GitHub Actions run as a Slack message using ONLY Slack markdown syntax:

:white_check_mark: *Deployment Successful* :white_check_mark:

Deployment completed successfully for [Repository Name]

*Changes:*
- Key feature or fix 1
- Key feature or fix 2

*Links:*
<https://github.com/user/repo|View Changes>

CRITICAL: Use EXACT Slack link format: <https://full-url|Link Text>
Examples:
- CORRECT: <https://github.com/user/repo|Repository>
- WRONG: [Repository](https://github.com/user/repo)
- WRONG: https://github.com/user/repo

Slack formatting rules:
- *text* for bold (NOT **text**)
- `text` for code
- > text for quotes
- Use simple bullet format with - or *
- :emoji_name: for emojis"""


# ===== Prompts from Module 2 (Complete) =====

@mcp.prompt()
async def analyze_ci_results():
    """Analyze recent CI/CD results and provide insights."""
    return """Please analyze the recent CI/CD results from GitHub Actions:

1. First, call get_recent_actions_events() to fetch the latest CI/CD events
2. Then call get_workflow_status() to check current workflow states
3. Identify any failures or issues that need attention
4. Provide actionable next steps based on the results

Format your response as:
## CI/CD Status Summary
- *Overall Health*: [Good/Warning/Critical]
- *Failed Workflows*: [List any failures with links]
- *Successful Workflows*: [List recent successes]
- *Recommendations*: [Specific actions to take]
- *Trends*: [Any patterns you notice]"""


@mcp.prompt()
async def create_deployment_summary():
    """Generate a deployment summary for team communication."""
    return """Create a deployment summary for team communication:

1. Check workflow status with get_workflow_status()
2. Look specifically for deployment-related workflows
3. Note the deployment outcome, timing, and any issues

Format as a concise message suitable for Slack:

🚀 *Deployment Update*
- *Status*: [✅ Success / ❌ Failed / ⏳ In Progress]
- *Environment*: [Production/Staging/Dev]
- *Version/Commit*: [If available from workflow data]
- *Duration*: [If available]
- *Key Changes*: [Brief summary if available]
- *Issues*: [Any problems encountered]
- *Next Steps*: [Required actions if failed]

Keep it brief but informative for team awareness."""


@mcp.prompt()
async def generate_pr_status_report():
    """Generate a comprehensive PR status report including CI/CD results."""
    return """Generate a comprehensive PR status report:

1. Use analyze_file_changes() to understand what changed
2. Use get_workflow_status() to check CI/CD status
3. Use suggest_template() to recommend the appropriate PR template
4. Combine all information into a cohesive report

Create a detailed report with:

## 📋 PR Status Report

### 📝 Code Changes
- *Files Modified*: [Count by type - .py, .js, etc.]
- *Change Type*: [Feature/Bug/Refactor/etc.]
- *Impact Assessment*: [High/Medium/Low with reasoning]
- *Key Changes*: [Bullet points of main modifications]

### 🔄 CI/CD Status
- *All Checks*: [✅ Passing / ❌ Failing / ⏳ Running]
- *Test Results*: [Pass rate, failed tests if any]
- *Build Status*: [Success/Failed with details]
- *Code Quality*: [Linting, coverage if available]

### 📌 Recommendations
- *PR Template*: [Suggested template and why]
- *Next Steps*: [What needs to happen before merge]
- *Reviewers*: [Suggested reviewers based on files changed]

### ⚠️ Risks & Considerations
- [Any deployment risks]
- [Breaking changes]
- [Dependencies affected]"""


@mcp.prompt()
async def troubleshoot_workflow_failure():
    """Help troubleshoot a failing GitHub Actions workflow."""
    return """Help troubleshoot failing GitHub Actions workflows:

1. Use get_recent_actions_events() to find recent failures
2. Use get_workflow_status() to see which workflows are failing
3. Analyze the failure patterns and timing
4. Provide systematic troubleshooting steps

Structure your response as:

## 🔧 Workflow Troubleshooting Guide

### ❌ Failed Workflow Details
- *Workflow Name*: [Name of failing workflow]
- *Failure Type*: [Test/Build/Deploy/Lint]
- *First Failed*: [When did it start failing]
- *Failure Rate*: [Intermittent or consistent]

### 🔍 Diagnostic Information
- *Error Patterns*: [Common error messages or symptoms]
- *Recent Changes*: [What changed before failures started]
- *Dependencies*: [External services or resources involved]

### 💡 Possible Causes (ordered by likelihood)
1. *[Most Likely]*: [Description and why]
2. *[Likely]*: [Description and why]
3. *[Possible]*: [Description and why]

### ✅ Suggested Fixes
**Immediate Actions:**
- [ ] [Quick fix to try first]
- [ ] [Second quick fix]

**Investigation Steps:**
- [ ] [How to gather more info]
- [ ] [Logs or data to check]

**Long-term Solutions:**
- [ ] [Preventive measure]
- [ ] [Process improvement]

### 📚 Resources
- [Relevant documentation links]
- [Similar issues or solutions]"""


if __name__ == "__main__":
    # Run MCP server normally
    print("Starting PR Agent Slack MCP server...")
    print("Make sure to set SLACK_WEBHOOK_URL environment variable")
    print("To receive GitHub webhooks, run the webhook server separately:")
    print("  python webhook_server.py")
    mcp.run()
````

## File: units/en/unit3/introduction.mdx
````
# Advanced MCP Development: Building Custom Workflow Servers for Claude Code

Welcome to Unit 3! In this unit, we'll build a practical MCP server that enhances Claude Code with custom development workflows while learning all three MCP primitives.

If you'd like to hear from the creators of MCP, here's a video they made:

<Youtube id="CQywdSdi5iA" />

In this video Theo Chu, David Soria Parra and Alex Albert dive into the Model Context Protocol (MCP), the standard that's changing how AI applications connect with external data and tools.

## What You'll Build

**PR Agent Workflow Server** - An MCP server that demonstrates how to make Claude Code team-aware and workflow-intelligent:

- **Smart PR Management**: Automatic PR template selection based on code changes using MCP Tools
- **CI/CD Monitoring**: Track GitHub Actions with Cloudflare Tunnel and standardized Prompts
- **Team Communication**: Slack notifications demonstrating all MCP primitives working together

## Real-World Case Study

We'll implement a practical scenario every development team faces:

**Before**: Developer manually creates PRs, waits for Actions to complete, manually checks results, remembers to notify team members

**After**: Claude Code connected to your workflow server can intelligently:
- Suggest the right PR template based on changed files
- Monitor GitHub Actions runs and provide formatted summaries
- Automatically notify team via Slack when deployments succeed/fail
- Guide developers through team-specific review processes based on Actions results

## Key Learning Outcomes

1. **Core MCP Primitives**: Master Tools and Prompts through practical examples
2. **MCP Server Development**: Build a functional server with proper structure and error handling
3. **GitHub Actions Integration**: Use Cloudflare Tunnel to receive webhooks and process CI/CD events
4. **Hugging Face Hub Workflows**: Create specialized workflows for LLM development teams
5. **Multi-System Integration**: Connect GitHub, Slack, and Hugging Face Hub through MCP
6. **Claude Code Enhancement**: Make Claude understand your team's specific workflows

## MCP Primitives in Action

This unit provides hands-on experience with the core MCP primitives:

- **Tools** (Module 1): Functions Claude can call to analyze files and suggest templates
- **Prompts** (Module 2): Standardized workflows for consistent team processes
- **Integration** (Module 3): All primitives working together for complex automation

## Module Structure

1. **Module 1: Build MCP Server** - Create a basic server with Tools for PR template suggestions
2. **Module 2: GitHub Actions Integration** - Monitor CI/CD with Cloudflare Tunnel and Prompts
3. **Module 3: Slack Notification** - Team communication integrating all MCP primitives

## Prerequisites

Before starting this unit, ensure you have:

- Completion of Units 1 and 2 
- Basic familiarity with GitHub Actions and webhook concepts
- Access to a GitHub repository for testing (can be a personal test repo)
- A Slack workspace where you can create webhook integrations

### Claude Code Installation and Setup

This unit requires Claude Code to test your MCP server integration.

<Tip>

**Installation Required:** This unit requires Claude Code for testing MCP server integration with AI workflows.

</Tip>

**Quick Setup:**

Follow the [official installation guide](https://docs.anthropic.com/en/docs/claude-code/getting-started) to install Claude Code and complete authentication. The key steps are installing via npm, navigating to your project directory, and running `claude` to authenticate through console.anthropic.com.

Once installed, you'll use Claude Code throughout this unit to test your MCP server and interact with the workflow automation you build.

<Tip warning={true}>

**New to Claude Code?** If you encounter any setup issues, the [troubleshooting guide](https://docs.anthropic.com/en/docs/claude-code/troubleshooting) covers common installation and authentication problems.

</Tip>

By the end of this unit, you'll have built a complete MCP server that demonstrates how to transform Claude Code into a powerful team development assistant, with hands-on experience using all three MCP primitives.
````

## File: units/en/unit1/mcp-clients.mdx
````
# MCP Clients

Now that we have a basic understanding of the Model Context Protocol, we can explore the essential role of MCP Clients in the Model Context Protocol ecosystem.

 In this part of Unit 1, we'll explore the essential role of MCP Clients in the Model Context Protocol ecosystem.

In this section, you will:

* Understand what MCP Clients are and their role in the MCP architecture
* Learn about the key responsibilities of MCP Clients
* Explore the major MCP Client implementations
* Discover how to use Hugging Face's MCP Client implementation
* See practical examples of MCP Client usage

<Tip>

In this page we're going to show examples of how to set up MCP Clients in a few different ways using the JSON notation. For now, we will use *examples* like `path/to/server.py` to represent the path to the MCP Server. In the next unit, we'll implement this with real MCP Servers.  

For now, focus on understanding the MCP Client notation. We'll implement the MCP Servers in the next unit.

</Tip>

## Understanding MCP Clients

MCP Clients are crucial components that act as the bridge between AI applications (Hosts) and external capabilities provided by MCP Servers. Think of the Host as your main application (like an AI assistant or IDE) and the Client as a specialized module within that Host responsible for handling MCP communications.

## User Interface Client

Let's start by exploring the user interface clients that are available for the MCP.

### Chat Interface Clients

Anthropic's Claude Desktop stands as one of the most prominent MCP Clients, providing integration with various MCP Servers.

### Interactive Development Clients

Cursor's MCP Client implementation enables AI-powered coding assistance through direct integration with code editing capabilities. It supports multiple MCP Server connections and provides real-time tool invocation during coding, making it a powerful tool for developers.

Continue.dev is another example of an interactive development client that supports MCP and connects to an MCP server from VS Code.

## Configuring MCP Clients

Now that we've covered the core of the MCP protocol, let's look at how to configure your MCP servers and clients.

Effective deployment of MCP servers and clients requires proper configuration. 

<Tip>

The MCP specification is still evolving, so the configuration methods are subject to evolution. We'll focus on the current best practices for configuration.

</Tip>

### MCP Configuration Files

MCP hosts use configuration files to manage server connections. These files define which servers are available and how to connect to them.

Fortunately, the configuration files are very simple, easy to understand, and consistent across major MCP hosts.

#### `mcp.json` Structure

The standard configuration file for MCP is named `mcp.json`. Here's the basic structure:

This is the basic structure of the `mcp.json` can be passed to applications like Claude Desktop, Cursor, or VS Code.

```json
{
  "servers": [
    {
      "name": "Server Name",
      "transport": {
        "type": "stdio|sse",
        // Transport-specific configuration
      }
    }
  ]
}
```

In this example, we have a single server with a name and a transport type. The transport type is either `stdio` or `sse`.

#### Configuration for stdio Transport

For local servers using stdio transport, the configuration includes the command and arguments to launch the server process:

```json
{
  "servers": [
    {
      "name": "File Explorer",
      "transport": {
        "type": "stdio",
        "command": "python",
        "args": ["/path/to/file_explorer_server.py"] // This is an example, we'll use a real server in the next unit
      }
    }
  ]
}
```

Here, we have a server called "File Explorer" that is a local script.

#### Configuration for HTTP+SSE Transport

For remote servers using HTTP+SSE transport, the configuration includes the server URL:

```json
{
  "servers": [
    {
      "name": "Remote API Server",
      "transport": {
        "type": "sse",
        "url": "https://example.com/mcp-server"
      }
    }
  ]
}
```

#### Environment Variables in Configuration

Environment variables can be passed to server processes using the `env` field. Here's how to access them in your server code:

<hfoptions id="env-variables">
<hfoption id="python">

In Python, we use the `os` module to access environment variables:

```python
import os

# Access environment variables
github_token = os.environ.get("GITHUB_TOKEN")
if not github_token:
    raise ValueError("GITHUB_TOKEN environment variable is required")

# Use the token in your server code
def make_github_request():
    headers = {"Authorization": f"Bearer {github_token}"}
    # ... rest of your code
```

</hfoption>
<hfoption id="javascript">

In JavaScript, we use the `process.env` object to access environment variables:

```javascript
// Access environment variables
const githubToken = process.env.GITHUB_TOKEN;
if (!githubToken) {
    throw new Error("GITHUB_TOKEN environment variable is required");
}

// Use the token in your server code
function makeGithubRequest() {
    const headers = { "Authorization": `Bearer ${githubToken}` };
    // ... rest of your code
}
```

</hfoption>
</hfoptions>

The corresponding configuration in `mcp.json` would look like this:

```json
{
  "servers": [
    {
      "name": "GitHub API",
      "transport": {
        "type": "stdio",
        "command": "python",
        "args": ["/path/to/github_server.py"], // This is an example, we'll use a real server in the next unit
        "env": {
          "GITHUB_TOKEN": "your_github_token"
        }
      }
    }
  ]
}
```

### Configuration Examples

Let's look at some real-world configuration scenarios:

#### Scenario 1: Local Server Configuration

In this scenario, we have a local server that is a Python script which could be a file explorer or a code editor.

```json
{
  "servers": [
    {
      "name": "File Explorer",
      "transport": {
        "type": "stdio",
        "command": "python",
        "args": ["/path/to/file_explorer_server.py"] // This is an example, we'll use a real server in the next unit
      }
    }
  ]
}
```

#### Scenario 2: Remote Server Configuration

In this scenario, we have a remote server that is a weather API.

```json
{
  "servers": [
    {
      "name": "Weather API",
      "transport": {
        "type": "sse",
        "url": "https://example.com/mcp-server" // This is an example, we'll use a real server in the next unit
      }
    }
  ]
}
```

Proper configuration is essential for successfully deploying MCP integrations. By understanding these aspects, you can create robust and reliable connections between AI applications and external capabilities.

In the next section, we'll explore the ecosystem of MCP servers available on Hugging Face Hub and how to publish your own servers there. 

## Tiny Agents Clients

Now, let's explore how to use MCP Clients within code.

You can also use tiny agents as MCP Clients to connect directly to MCP servers from your code. Tiny agents provide a simple way to create AI agents that can use tools from MCP servers.

Tiny Agent can run MCP servers with a command line environment. To do this, we will need to install `npm` and run the server with `npx`. **We'll need these for both Python and JavaScript.**

Let's install `npx` with `npm`. If you don't have `npm` installed, check out the [npm documentation](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm).

### Setup

First, we will need to install `npx` if you don't have it installed. You can do this with the following command:

```bash
# install npx
npm install -g npx
```

Then, we will need to install the huggingface_hub package with the MCP support. This will allow us to run MCP servers and clients.

```bash
pip install "huggingface_hub[mcp]>=0.32.0"
```

Then, we will need to log in to the Hugging Face Hub to access the MCP servers. You can do this with the `huggingface-cli` command line tool. You will need a [login token](https://huggingface.co/docs/huggingface_hub/v0.32.3/en/quick-start#authentication) to do this.

```bash
huggingface-cli login
```

<hfoptions id="language">
<hfoption id="python">

### Connecting to MCP Servers

Now, let's create an agent configuration file `agent.json`.

```json
{
    "model": "Qwen/Qwen2.5-72B-Instruct",
    "provider": "nebius",
    "servers": [
        {
            "type": "stdio",
            "config": {
                "command": "npx",
                "args": ["@playwright/mcp@latest"]
            }
        }
    ]
}
```

In this configuration, we are using the `@playwright/mcp` MCP server. This is an MCP server that can control a browser with Playwright.

Now you can run the agent:

```bash
tiny-agents run agent.json
```
</hfoption>
<hfoption id="javascript">

First, install the tiny agents package with [npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm).

```bash
npm install @huggingface/tiny-agents
```

### Connecting to MCP Servers

Make an agent project directory and create an `agent.json` file.

```bash
mkdir my-agent
touch my-agent/agent.json
```

Create an agent configuration file at `my-agent/agent.json`:

```json
{
	"model": "Qwen/Qwen2.5-72B-Instruct",
	"provider": "nebius",
	"servers": [
		{
			"type": "stdio",
			"config": {
				"command": "npx",
				"args": ["@playwright/mcp@latest"]
			}
		}
	]
}
```

Now you can run the agent:

```bash
npx @huggingface/tiny-agents run ./my-agent
```

</hfoption>
</hfoptions>

In the video below, we run the agent and ask it to open a new tab in the browser.

The following example shows a web-browsing agent configured to use the [Qwen/Qwen2.5-72B-Instruct](https://huggingface.co/Qwen/Qwen2.5-72B-Instruct) model via Nebius inference provider, and it comes equipped with a playwright MCP server, which lets it use a web browser! The agent config is loaded specifying [its path in the `tiny-agents/tiny-agents`](https://huggingface.co/datasets/tiny-agents/tiny-agents/tree/main/celinah/web-browser) Hugging Face dataset.

<video controls autoplay loop>
  <source src="https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/python-tiny-agents/web_browser_agent.mp4" type="video/mp4">
</video>

When you run the agent, you'll see it load, listing the tools it has discovered from its connected MCP servers. Then, it's ready for your prompts!

Prompt used in this demo:

> do a Web Search for HF inference providers on Brave Search and open the first result and then give me the list of the inference providers supported on Hugging Face 

## Next Steps

Now that you understand MCP Clients, you're ready to:
* Explore specific MCP Server implementations
* Learn about creating custom MCP Clients
* Dive into advanced MCP integration patterns

Let's continue our journey into the world of Model Context Protocol!
````

## File: units/en/unit3/github-actions-integration.mdx
````
# Module 2: GitHub Actions Integration

## The Silent Failures Strike

Week 2 at CodeCraft Studios. Your PR Agent from Module 1 is already helping developers write better pull requests - Sarah's latest PR had a clear description that saved Mike 20 minutes of investigation time. The team is thrilled!

But then disaster strikes.

A critical bug reaches production on Friday afternoon. The payment system is down, customers are complaining, and the team scrambles to investigate. After two stressful hours, they discover the root cause: a test failure in Tuesday's CI run that nobody noticed.

"How did we miss this?" asks the team lead, scrolling through GitHub Actions. "The tests clearly failed, but with 47 repositories and dozens of daily commits, who has time to check every build?"

The team realizes they need real-time visibility into their CI/CD pipeline, but manually checking GitHub Actions across all their projects isn't scalable. They need automation that watches for problems and alerts them immediately.

**Your mission**: Extend your MCP server with webhook capabilities to monitor GitHub Actions and never let another failure slip through unnoticed.

## What You'll Build

This module bridges the gap between static file analysis (Module 1) and dynamic team notifications (Module 3). You'll add real-time capabilities that transform your PR Agent into a comprehensive development monitoring system.

Building on the foundation you created in Module 1, you'll add:
- **Webhook server** to receive GitHub Actions events
- **New tools** for monitoring CI/CD status
- **MCP Prompts** that provide consistent workflow patterns
- **Real-time integration** with your GitHub repository

### Screencast: Real-Time CI/CD Monitoring in Action! 🎯

<Youtube id="XIEnmCicFXk" />

**The Setup**: Watch how CodeCraft Studios' new system catches failures before they reach production:
1. **GitHub Webhooks** - See the actual webhook configuration that sends events to your server
2. **Failed Tests** - Those red X's that used to go unnoticed? Not anymore!
3. **Local Development** - The webhook server and Cloudflare tunnel working together

**MCP Magic in Real-Time**: Claude responds to three key requests:
- **"What GitHub Actions events have we received?"** - Claude uses your new tools to check recent activity
- **"Analyze CI Results"** - Watch Claude dig into test failures and provide actionable insights
- **"Create Deployment Summary"** - See how MCP Prompts guide Claude to create team-friendly updates

**The Silent Failures No More** 🚨: Remember that critical bug from Tuesday's failed test? With this system, Claude would have caught it immediately. The screencast shows exactly how your MCP server turns GitHub's raw webhook data into clear, actionable alerts.

**What Makes This Special**: Your Module 1 PR Agent was static—it analyzed code when asked. This Module 2 enhancement is dynamic—it watches your CI/CD pipeline 24/7 and helps Claude provide real-time insights. No more Friday afternoon surprises!

## Learning Objectives

By the end of this module, you'll understand:
1. How to run a webhook server alongside an MCP server
2. How to receive and process GitHub webhooks
3. How to create MCP Prompts for standardized workflows
4. How to use Cloudflare Tunnel for local webhook testing

## Prerequisites

You'll build directly on your work from Module 1, so make sure you have:
- **Completed Module 1: Build MCP Server** - You'll be extending that same codebase
- **Basic understanding of GitHub Actions** - You should know what CI/CD workflows are
- **A GitHub repository with Actions enabled** - Even a simple workflow file works fine
- **Cloudflare Tunnel (cloudflared) installed** - This will expose your local webhook server to GitHub

## Key Concepts

### MCP Prompts

Prompts are reusable templates that guide Claude through complex workflows. Unlike Tools (which Claude calls automatically), Prompts are user-initiated and provide structured guidance.

Example use cases:
- Analyzing CI/CD results consistently
- Creating standardized deployment summaries
- Troubleshooting failures systematically

### Webhook Integration

Your MCP server will run two services:
1. The MCP server (communicates with Claude)
2. A webhook server on port 8080 (receives GitHub events)

This allows Claude to react to real-time CI/CD events!

<Tip>

**Architecture Insight**: Running separate services for MCP communication and webhook handling is a clean separation of concerns. The webhook server handles HTTP complexity while your MCP server focuses on data analysis and Claude integration.

</Tip>

## Project Structure

```
github-actions-integration/
├── starter/          # Your starting point
│   ├── server.py     # Module 1 code + TODOs
│   ├── pyproject.toml
│   └── README.md
└── solution/         # Complete implementation
    ├── server.py     # Full webhook + prompts
    ├── pyproject.toml
    └── README.md
```

## Implementation Steps

### Step 1: Set Up and Run Webhook Server

Unlike Module 1 where you worked with existing files, this module introduces real-time event handling. The starter code includes:
- **Your Module 1 implementation** - All your existing PR analysis tools
- **A complete webhook server** (`webhook_server.py`) - Ready to receive GitHub events

1. Install dependencies (same as Module 1):
   ```bash
   uv sync
   ```

2. Start the webhook server (in a separate terminal):
   ```bash
   python webhook_server.py
   ```

This server will receive GitHub webhooks and store them in `github_events.json`.

**How webhook event storage works:**
- Each incoming GitHub webhook (push, pull request, workflow completion, etc.) is appended to the JSON file
- Events are stored with timestamps, making it easy to find recent activity
- The file acts as a simple event log that your MCP tools can read and analyze
- No database required - everything is stored in a simple, readable JSON format

### Step 2: Connect to Event Storage

Now you'll connect your MCP server (from Module 1) to the webhook data. This is much simpler than handling HTTP requests directly - the webhook server does all the heavy lifting and stores events in a JSON file.

Add the path to read webhook events:

```python
# File where webhook server stores events
EVENTS_FILE = Path(__file__).parent / "github_events.json"
```

The webhook server handles all the HTTP details - you just need to read the JSON file! This separation of concerns keeps your MCP server focused on what it does best.

<Tip>

**Development Tip**: Working with files instead of HTTP requests makes testing much easier. You can manually add events to `github_events.json` to test your tools without setting up webhooks.

</Tip>

### Step 3: Add GitHub Actions Tools

Just like in Module 1 where you created tools for file analysis, you'll now create tools for CI/CD analysis. These tools will work alongside your existing PR analysis tools, giving Claude a complete view of both code changes and build status.

<Tip>

**Note**: The starter code already includes the output limiting fix from Module 1, so you won't encounter token limit errors. Focus on the new concepts in this module!

</Tip>

Implement two new tools:

1. **`get_recent_actions_events`**: 
   - Read from `EVENTS_FILE`
   - Return the most recent events (up to limit)
   - Return empty list if file doesn't exist

2. **`get_workflow_status`**: 
   - Read all events from file
   - Filter for workflow_run events
   - Group by workflow name and show latest status

These tools let Claude analyze your CI/CD pipeline.

### Step 4: Create MCP Prompts

Now you'll add your first MCP Prompts! Unlike Tools (which Claude calls automatically), Prompts are templates that help users interact with Claude consistently. Think of them as "conversation starters" that guide Claude through complex workflows.

While Module 1 focused on Tools for data access, this module introduces Prompts for workflow guidance.

Implement four prompts that demonstrate different workflow patterns:

1. **`analyze_ci_results`**: Comprehensive CI/CD analysis
2. **`create_deployment_summary`**: Team-friendly updates
3. **`generate_pr_status_report`**: Combined code + CI report
4. **`troubleshoot_workflow_failure`**: Systematic debugging

Each prompt should return a string with clear instructions for Claude to follow.

### Step 5: Test with Cloudflare Tunnel

Now for the exciting part - testing your expanded MCP server with real GitHub events! You'll run multiple services together, just like in a real development environment.

1. Start your MCP server (same command as Module 1):
   ```bash
   uv run server.py
   ```

2. In another terminal, start Cloudflare Tunnel:
   ```bash
   cloudflared tunnel --url http://localhost:8080
   ```

3. Configure GitHub webhook with the tunnel URL

4. Test with Claude Code using the prompts

## Exercises

### Exercise 1: Custom Workflow Prompt
Create a new prompt that helps with PR reviews by combining:
- Code changes from Module 1 tools
- CI/CD status from Module 2 tools
- A checklist format for reviewers

### Exercise 2: Event Filtering
Enhance `get_workflow_status` to:
- Filter by workflow conclusion (success/failure)
- Group by repository
- Show time since last run

### Exercise 3: Notification System
Add a tool that:
- Tracks which events have been "seen"
- Highlights new failures
- Suggests which team member to notify

## Common Issues

### Webhook Not Receiving Events
- Ensure Cloudflare Tunnel is running
- Check GitHub webhook settings (should show recent deliveries)
- Verify the payload URL includes `/webhook/github`

### Prompt Not Working
- FastMCP prompts simply return strings
- Make sure your function is decorated with `@mcp.prompt()`

### Webhook Server Issues
- Ensure webhook_server.py is running in a separate terminal
- Check that port 8080 is free: `lsof -i :8080`
- The events file will be created automatically when first event is received

## Next Steps

Excellent work! You've successfully added real-time capabilities to your MCP server. You now have a system that can:

- **Analyze code changes** (from Module 1) 
- **Monitor CI/CD events in real-time** (from this module)
- **Use MCP Prompts** to provide consistent workflow guidance
- **Handle webhook events** through a clean file-based architecture

### Key achievements in Module 2:
- Built your first webhook integration
- Learned MCP Prompts for workflow standardization  
- Created tools that work with real-time data
- Established patterns for event-driven automation

### What to do next:
1. **Review the solution** in `/projects/unit3/github-actions-integration/solution/` to see different implementation approaches
2. **Experiment with your prompts** - try using them for different types of GitHub events
3. **Test the integration** - combine your Module 1 file analysis tools with Module 2 event monitoring in a single conversation with Claude
4. **Move on to Module 3** - where you'll complete the automation pipeline by adding team notifications through Slack integration

Module 3 will bring everything together into a complete workflow that your team can actually use!

### The story continues...
Your monitoring system is working! CodeCraft Studios now catches CI/CD failures in real-time, and the team feels much more confident about their deployments. But next week brings a new challenge: information silos are causing duplicate work and missed opportunities. Module 3 will complete the automation system with intelligent team notifications that keep everyone in the loop.

## Additional Resources

- [MCP Prompts Documentation](https://modelcontextprotocol.io/docs/concepts/prompts)
- [GitHub Webhooks Guide](https://docs.github.com/en/developers/webhooks-and-events)
- [Cloudflare Tunnel Documentation](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps)
````

## File: units/en/unit2/continue-client.mdx
````
# Using MCP with Local and Open Source Models

In this section, we'll connect MCP with local and open-source models using
Continue, a tool for building AI coding assistants that works with local tools
like Ollama.

## Setup Continue

You can install Continue from the VS Code marketplace.

<Tip>

*Continue also has an extension for [JetBrains](https://plugins.jetbrains.com/plugin/22707-continue).*

</Tip>

### VS Code extension

1. Click `Install` on the [Continue extension page in the Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=Continue.continue)
2. This will open the Continue extension page in VS Code, where you will need to click `Install` again
3. The Continue logo will appear on the left sidebar. For a better experience, move Continue to the right sidebar

![sidebar vs code demo](https://docs.continue.dev/assets/images/move-to-right-sidebar-b2d315296198e41046fc174d8178f30a.gif)

With Continue configured, we'll move on to setting up Ollama to pull local models. 

### Local Models

There are many ways to run local models that are compatible with Continue. Three popular options are Ollama, Llama.cpp, and LM Studio. Ollama is an open-source tool that allows users to easily run large language models (LLMs) locally. Llama.cpp is a high-performance C++ library for running LLMs that also includes an OpenAI-compatible server. LM Studio provides a graphical interface for running local models.


You can access local models from the Hugging Face Hub and get commands and quick links for all major local inference apps.

![hugging face hub](https://cdn-uploads.huggingface.co/production/uploads/64445e5f1bc692d87b27e183/d6XMR5q9DwVpdEKFeLW9t.png)

<hfoptions id="local-models">
<hfoption id="llamacpp">

Llama.cpp provides `llama-server`, a lightweight, OpenAI API compatible, HTTP server for serving LLMs. You can either build it from source by following the instructions in the [Llama.cpp repository](https://github.com/ggml-org/llama.cpp), or use a pre-built binary if available for your system. Check out the [Llama.cpp documentation](https://github.com/ggerganov/llama.cpp) for more information.

Once you have `llama-server`, you can run a model from Hugging Face with a command like this:

```bash
llama-server -hf unsloth/Devstral-Small-2505-GGUF:Q4_K_M
```

</hfoption>
<hfoption id="lmstudio">
LM Studio is an application for Mac, Windows, and Linux that makes it easy to run open-source models locally with a graphical interface. To get started:

1.  [Click here to open the model in LM Studio](lmstudio://open_from_hf?model=unsloth/Devstral-Small-2505-GGUF).
2.  Once the model is downloaded, go to the "Local Server" tab and click "Start Server".
</hfoption>
<hfoption id="ollama">
To use Ollama, you can [install](https://ollama.com/download) it and download the model you want to run with the `ollama run` command.

For example, you can download and run the [Devstral-Small](https://huggingface.co/unsloth/Devstral-Small-2505-GGUF?local-app=ollama) model with:

```bash
ollama run unsloth/devstral-small-2505-gguf:Q4_K_M
```
</hfoption>
</hfoptions>

<Tip>

Continue supports various local model providers. Besides Ollama, Llama.cpp, and LM Studio you can also use other providers. For a complete list of supported providers and detailed configuration options, please refer to the [Continue documentation](https://docs.continue.dev/customize/model-providers).

</Tip>

It is important that we use models that have tool calling as a built-in feature, i.e. Codestral Qwen and Llama 3.1x.

1. Create a folder called `.continue/models` at the top level of your workspace
2. Add a file to this folder to configure your model provider. For example, `local-models.yaml`.
3. Add the following configuration, depending on whether you are using Ollama, Llama.cpp, or LM Studio.

<hfoptions id="local-models">
<hfoption id="llamacpp">
This configuration is for a `llama.cpp` model served with `llama-server`. Note that the `model` field should match the model you are serving.

```yaml
name: Llama.cpp model
version: 0.0.1
schema: v1
models:
  - provider: llama.cpp
    model: unsloth/Devstral-Small-2505-GGUF
    apiBase: http://localhost:8080
    defaultCompletionOptions:
      contextLength: 8192 # Adjust based on the model
    name: Llama.cpp Devstral-Small
    roles:
      - chat
      - edit
```
</hfoption>
<hfoption id="lmstudio">
This configuration is for a model served via LM Studio. The model identifier should match what is loaded in LM Studio.

```yaml
name: LM Studio Model
version: 0.0.1
schema: v1
models:
  - provider: lmstudio
    model: unsloth/Devstral-Small-2505-GGUF
    name: LM Studio Devstral-Small
    apiBase: http://localhost:1234/v1
    roles:
      - chat
      - edit
```
</hfoption>
<hfoption id="ollama">
This configuration is for an Ollama model.

```yaml
name: Ollama Devstral model
version: 0.0.1
schema: v1
models:
  - provider: ollama
    model: unsloth/devstral-small-2505-gguf:Q4_K_M
    defaultCompletionOptions:
      contextLength: 8192
    name: Ollama Devstral-Small
    roles:
      - chat
      - edit
```
</hfoption>
</hfoptions>

By default, each model has a max context length, in this case it is `128000` tokens. This setup includes a larger use of
that context window to perform multiple MCP requests and needs to be able to handle more tokens.

## How it works

### The tool handshake

Tools provide a powerful way for models to interface with the external world.
They are provided to the model as a JSON object with a name and an arguments
schema. For example, a `read_file` tool with a `filepath` argument will give the
model the ability to request the contents of a specific file.

![autonomous agents diagram](https://gist.github.com/user-attachments/assets/c7301fc0-fa5c-4dc4-9955-7ba8a6587b7a)

The following handshake describes how the Agent uses tools:

1. In Agent mode, available tools are sent along with `user` chat requests
2. The model can choose to include a tool call in its response
3. The user gives permission. This step is skipped if the policy for that tool is set to `Automatic`
4. Continue calls the tool using built-in functionality or the MCP server that offers that particular tool
5. Continue sends the result back to the model
6. The model responds, potentially with another tool call, and step 2 begins again

Continue supports multiple local model providers. You can use different models
for different tasks or switch models as needed. This section focuses on
local-first solutions, but Continue does work with popular providers
like OpenAI, Anthropic, Microsoft/Azure, Mistral, and more. You can also run
your own model provider.

### Local Model Integration with MCP

Now that we have everything set up, let's add an existing MCP server. Below is a quick example of setting up a new MCP server for use in your assistant:

1. Create a folder called `.continue/mcpServers` at the top level of your workspace
2. Add a file called `playwright-mcp.yaml` to this folder
3. Write the following contents to `playwright-mcp.yaml` and save

```yaml
name: Playwright mcpServer
version: 0.0.1
schema: v1
mcpServers:
  - name: Browser search
    command: npx
    args:
      - "@playwright/mcp@latest"
```

Now test your MCP server by prompting the following command:

```
1. Using playwright, navigate to https://news.ycombinator.com.

2. Extract the titles and URLs of the top 4 posts on the homepage.

3. Create a file named hn.txt in the root directory of the project.

4. Save this list as plain text in the hn.txt file, with each line containing the title and URL separated by a hyphen.

Do not output code or instructions—just complete the task and confirm when it is done.
```

The result will be a generated file called `hn.txt` in the current working directory.

![mcp output example](https://deploy-preview-6060--continuedev.netlify.app/assets/images/mcp-playwright-50b192a2ff395f7a6cc11618c5e2d5b1.png)

## Conclusion

By combining Continue with local models like Llama 3.1 and MCP servers, you've
unlocked a powerful development workflow that keeps your code and data private
while leveraging cutting-edge AI capabilities. 

This setup gives you the flexibility to customize your AI assistant with
specialized tools, from web automation to file management, all running entirely
on your local machine. Ready to take your development workflow to the next
level? Start by experimenting with different MCP servers from the [Continue Hub
MCP explore page](https://hub.continue.dev/explore/mcp) and discover how
local AI can transform your coding experience.
````

## File: units/en/unit3/slack-notification.mdx
````
# Module 3: Slack Notification

## The Communication Gap Crisis

Week 3 at CodeCraft Studios. Your automation system is already transforming how the team works:
- **PR Agent** (Module 1): Developers are writing clear, helpful pull request descriptions
- **CI/CD Monitor** (Module 2): The team catches test failures immediately, preventing bugs from reaching production

The team is feeling much more confident... until Monday morning brings a new crisis.

The frontend team (Emma and Jake) spent the entire weekend debugging a nasty API integration issue. They tried everything: checked their network calls, validated request formats, even rewrote the error handling. Finally, at 2 AM Sunday, they discovered the backend team had fixed this exact issue on Friday and deployed the fix to staging - but forgot to announce it.

"We wasted 12 hours solving a problem that was already fixed!" Emma says, frustrated.

Meanwhile, the design team finished the new user onboarding flow illustrations last week, but the frontend team didn't know they were ready. Those beautiful assets are still sitting unused while the team ships a temporary design.

The team realizes they have an information silo problem. Everyone's working hard, but they're not communicating effectively about what's happening when.

**Your mission**: Complete the automation system with intelligent Slack notifications that keep the whole team informed about important developments automatically.

## What You'll Build

This final module completes the CodeCraft Studios transformation. You'll integrate Tools and Prompts to create a smart notification system that sends formatted Slack messages about CI/CD events, demonstrating how all MCP primitives work together in a real-world scenario.

Building on the foundation from Modules 1 and 2, you'll add the final piece of the puzzle:
- **Slack webhook tool** for sending messages to your team channel
- **Two notification prompts** that intelligently format CI events
- **Complete integration** showing all MCP primitives working together

### Screencast: The Complete Automation System! 🎉

<Youtube id="sX5qrbDG-oY" />

**The Final Piece**: Watch how your complete automation system prevents those Monday morning surprises that plagued Emma and Jake!

**What You'll See**: 
- **Claude's intelligent workflow** - Notice how Claude breaks down the task: ☐ Check events → ☐ Send notification
- **Real-time MCP tools in action** - `get_recent_actions_events` pulls fresh CI data, then `send_slack_notification` delivers the alert
- **Side-by-side demonstration** - The Slack channel is open in parallel to show the formatted message appearing as Claude sends it

**The Smart Notification**: Claude doesn't just spam the team—it crafts a professional alert with:
- 🚨 Clear urgency indicators and emoji
- **Detailed failure breakdown** (test-auth-service ❌, test-api ❌, test-frontend ⏳)
- **Actionable links** to the pipeline run and pull request
- **Context everyone needs** - repository, PR #1 "various improvements", commit hash

**Why This Matters**: Remember the communication gap crisis? No more! This system ensures that when CI fails on `demo-bad-pr` branch, the whole team knows immediately. No more weekend debugging sessions for issues that were already fixed!

**The Complete Journey**: From Module 1's PR chaos to Module 3's intelligent team notifications—you've built a system that transforms how CodeCraft Studios collaborates. The weekend warriors become informed teammates! 🚀

## Learning Objectives

By the end of this module, you'll understand:
1. How to integrate external APIs with MCP Tools
2. How to combine Tools and Prompts for complete workflows  
3. How to format rich messages using Slack markdown
4. How all MCP primitives work together in practice

## Prerequisites

You'll need everything from the previous modules plus:
- **Completed Modules 1 and 2** - This module directly extends your existing MCP server
- **A Slack workspace** where you can create incoming webhooks (personal workspaces work fine)
- **Basic understanding of REST APIs** - You'll be making HTTP requests to Slack's webhook endpoints

## Key Concepts

### MCP Integration Pattern

This module demonstrates the complete workflow:
1. **Events** → GitHub Actions webhook (from Module 2)
2. **Prompts** → Format events into readable messages
3. **Tools** → Send formatted messages to Slack
4. **Result** → Professional team notifications

### Slack Markdown Formatting

You'll use [Slack's markdown](https://api.slack.com/reference/surfaces/formatting) for rich messages:
- [`*bold text*`](https://api.slack.com/reference/surfaces/formatting#visual-styles) for emphasis
- [`_italic text_`](https://api.slack.com/reference/surfaces/formatting#visual-styles) for details
- [`` `code blocks` ``](https://api.slack.com/reference/surfaces/formatting#inline-code) for technical info
- [`> quoted text`](https://api.slack.com/reference/surfaces/formatting#quotes) for summaries
- [Emoji](https://api.slack.com/reference/surfaces/formatting#emoji): ✅ ❌ 🚀 ⚠️
- [Links](https://api.slack.com/reference/surfaces/formatting#linking-urls): `<https://github.com/user/repo|Repository>`

## Project Structure

```
slack-notification/
├── starter/          # Your starting point
│   ├── server.py     # Modules 1+2 code + TODOs
│   ├── webhook_server.py  # From Module 2
│   ├── pyproject.toml
│   └── README.md
└── solution/         # Complete implementation
    ├── server.py     # Full Slack integration
    ├── webhook_server.py
    └── README.md
```

## Implementation Steps

### Step 1: Set Up Slack Integration (10 min)

1. Create a Slack webhook:
   - Go to [Slack API Apps](https://api.slack.com/apps)
   - Create new app → "From scratch" ([Creating an app guide](https://api.slack.com/authentication/basics#creating))
   - App Name: "MCP Course Notifications"
   - Choose your workspace
   - Go to "Features" → "[Incoming Webhooks](https://api.slack.com/messaging/webhooks)"
   - [Activate incoming webhooks](https://api.slack.com/messaging/webhooks#enable_webhooks)
   - Click "Add New Webhook to Workspace"
   - Choose channel and authorize ([Webhook setup guide](https://api.slack.com/messaging/webhooks#getting_started))
   - Copy the webhook URL

2. Test webhook works (following [webhook posting examples](https://api.slack.com/messaging/webhooks#posting_with_webhooks)):
   ```bash
   curl -X POST -H 'Content-type: application/json' \
     --data '{"text":"Hello from MCP Course!"}' \
     YOUR_WEBHOOK_URL
   ```

3. Set environment variable:
   ```bash
   export SLACK_WEBHOOK_URL="https://hooks.slack.com/services/YOUR/WEBHOOK/URL"
   ```

   **⚠️ Security Note**: The webhook URL is a sensitive secret that grants permission to post messages to your Slack channel. Always:
   - Store it as an environment variable, never hardcode it in your code
   - Never commit webhook URLs to version control (add to .gitignore)
   - Treat it like a password - anyone with this URL can send messages to your channel

<Tip warning={true}>

**Security Alert**: Webhook URLs are sensitive credentials! Anyone with your webhook URL can send messages to your Slack channel. Always store them as environment variables and never commit them to version control.

</Tip>

### Step 2: Add Slack Tool (15 min)

Now that you have a working webhook, you'll add a new MCP tool to your existing server.py from Module 2. This tool will handle sending notifications to Slack by making HTTP requests to the webhook URL.

<Tip>

**Note**: The starter code includes all improvements from Modules 1 & 2 (output limiting, webhook handling). Focus on the new Slack integration!

</Tip>

Add this tool to your server.py:

**`send_slack_notification`**:
- Takes a message string parameter
- Reads webhook URL from environment variable
- Sends POST request to Slack webhook
- Returns success/failure message
- Handles basic error cases

```python
import os
import requests
from mcp.types import TextContent

@mcp.tool()
def send_slack_notification(message: str) -> str:
    """Send a formatted notification to the team Slack channel."""
    webhook_url = os.getenv("SLACK_WEBHOOK_URL")
    if not webhook_url:
        return "Error: SLACK_WEBHOOK_URL environment variable not set"
    
    try:
        # TODO: Send POST request to webhook_url
        # TODO: Include message in JSON payload with "mrkdwn": true
        # TODO: Handle response and return status
        pass
    except Exception as e:
        return f"Error sending message: {str(e)}"
```

### Step 3: Create Formatting Prompts (15 min)

Next, you'll add MCP Prompts to your server - this is where the magic happens! These prompts will work with Claude to automatically format your GitHub webhook data into well-structured Slack messages. Remember from Module 1 that Prompts provide reusable instructions that Claude can use consistently.

Implement two prompts that generate Slack-formatted messages:

1. **`format_ci_failure_alert`**:
   ```python
   @mcp.prompt()
   def format_ci_failure_alert() -> str:
       """Create a Slack alert for CI/CD failures."""
       return """Format this GitHub Actions failure as a Slack message:

   Use this template:
   :rotating_light: *CI Failure Alert* :rotating_light:
   
   A CI workflow has failed:
   *Workflow*: workflow_name
   *Branch*: branch_name
   *Status*: Failed
   *View Details*: <LOGS_LINK|View Logs>
   
   Please check the logs and address any issues.
   
   Use Slack markdown formatting and keep it concise for quick team scanning."""
   ```

2. **`format_ci_success_summary`**:
   ```python
   @mcp.prompt()
   def format_ci_success_summary() -> str:
       """Create a Slack message celebrating successful deployments."""
       return """Format this successful GitHub Actions run as a Slack message:

   Use this template:
   :white_check_mark: *Deployment Successful* :white_check_mark:
   
   Deployment completed successfully for [Repository Name]
   
   *Changes:*
   - Key feature or fix 1
   - Key feature or fix 2
   
   *Links:*
   <PR_LINK|View Changes>
   
   Keep it celebratory but informative. Use Slack markdown formatting."""
   ```

### Step 4: Test Complete Workflow (10 min)

Now comes the exciting part - testing your complete MCP workflow! You'll have all three components working together: webhook capture from Module 2, prompt formatting from this module, and Slack notifications.

1. Start all services (just like in Module 2, but now with Slack integration):
   ```bash
   # Terminal 1: Start webhook server
   python webhook_server.py
   
   # Terminal 2: Start MCP server
   uv run server.py
   
   # Terminal 3: Start Cloudflare Tunnel  
   cloudflared tunnel --url http://localhost:8080
   ```

2. Test the complete integration with Claude Code:
   - **Configure GitHub webhook** with tunnel URL (same as Module 2)
   - **Push changes** to trigger GitHub Actions 
   - **Ask Claude** to check recent events and format them using your prompts
   - **Let Claude send** the formatted message using your Slack tool
   - **Verify** notifications appear in your Slack channel

### Step 5: Verify Integration (5 min)

You can test your implementation without setting up a real GitHub repository! See `manual_test.md` for curl commands that simulate GitHub webhook events.

**Understanding the webhook event flow:**
- Your webhook server (from Module 2) captures GitHub events and stores them in `github_events.json`
- Your MCP tools read from this file to get recent CI/CD activity  
- Claude uses your formatting prompts to create readable messages
- Your Slack tool sends the formatted messages to your team channel
- This creates a complete pipeline: GitHub → Local Storage → Claude Analysis → Slack Notification

**Quick Test Workflow:**
1. Use curl to send fake GitHub events to your webhook server
2. Ask Claude to check recent events and format them
3. Send formatted messages to Slack
4. Verify everything works end-to-end

**Manual Testing Alternative:** For a complete testing experience without GitHub setup, follow the step-by-step curl commands in `manual_test.md`.

## Example Workflow in Claude Code

```
User: "Check recent CI events and notify the team about any failures"

Claude: 
1. Uses get_recent_actions_events (from Module 2)
2. Finds a workflow failure
3. Uses format_ci_failure_alert prompt to create message
4. Uses send_slack_notification tool to deliver it
5. Reports back: "Sent failure alert to #dev-team channel"
```

## Expected Slack Message Output

**Failure Alert:**
```
🚨 *CI Failure Alert* 🚨

A CI workflow has failed:
*Workflow*: CI (Run #42)
*Branch*: feature/slack-integration
*Status*: Failed
*View Details*: <https://github.com/user/mcp-course/actions/runs/123|View Logs>

Please check the logs and address any issues.
```

**Success Summary:**
```
✅ *Deployment Successful* ✅

Deployment completed successfully for mcp-course

*Changes:*
- Added team notification system
- Integrated MCP Tools and Prompts

*Links:*
<https://github.com/user/mcp-course/pull/42|View Changes>
```

## Common Issues

### Webhook URL Issues
- Verify the environment variable is set correctly
- Test webhook directly with curl before integrating
- Ensure Slack app has proper permissions

### Message Formatting
- [Slack markdown](https://api.slack.com/reference/surfaces/formatting) differs from GitHub markdown
- **Important**: Use `*text*` for bold (not `**text**`)
- Include `"mrkdwn": true` in webhook payload for proper formatting
- Test message formatting manually before automating
- Handle special characters in commit messages properly ([formatting reference](https://api.slack.com/reference/surfaces/formatting#escaping))

### Network Errors
- Add basic timeout handling to webhook requests ([webhook error handling](https://api.slack.com/messaging/webhooks#handling_errors))
- Return meaningful error messages from the tool
- Check internet connectivity if requests fail

## Key Takeaways

You've now built a complete MCP workflow that demonstrates:
- **Tools** for external API integration (Slack webhooks)
- **Prompts** for intelligent message formatting
- **Integration** of all MCP primitives working together
- **Real-world application** that teams can actually use

This shows the power of MCP for building practical development automation tools!

<Tip>

**Key Learning**: You've now built a complete MCP workflow that combines Tools (for external API calls) with Prompts (for consistent formatting). This pattern of Tools + Prompts is fundamental to advanced MCP development and can be applied to many other automation scenarios.

</Tip>

## Next Steps

Congratulations! You've completed the final module of Unit 3 and built a complete end-to-end automation system. Your journey through all three modules has given you hands-on experience with:

- **Module 1**: MCP Tools and intelligent data analysis
- **Module 2**: Real-time webhooks and MCP Prompts
- **Module 3**: External API integration and workflow completion

### What to do next:
1. **Test your complete system** - Try triggering real GitHub events and watch the full pipeline work
2. **Experiment with customization** - Modify the Slack message formats or add new notification types
3. **Review the Unit 3 Conclusion** - Reflect on everything you've learned and explore next steps
4. **Share your success** - Show teammates how MCP can automate your development workflows

You now have a solid foundation for building intelligent automation systems with MCP!

### The transformation is complete!
CodeCraft Studios has gone from chaotic development to a well-oiled machine. The automation system you built handles:
- **Smart PR descriptions** that help reviewers understand changes
- **Real-time CI/CD monitoring** that catches failures before they reach production  
- **Intelligent team notifications** that keep everyone informed automatically

The team can now focus on building great products instead of fighting process problems. And you've learned advanced MCP patterns that you can apply to any automation challenge!

## Additional Resources

- [Slack Incoming Webhooks Documentation](https://api.slack.com/messaging/webhooks)
- [Slack Message Formatting Guide](https://api.slack.com/reference/surfaces/formatting)
- [MCP Tools Documentation](https://modelcontextprotocol.io/docs/concepts/tools)
- [MCP Prompts Guide](https://modelcontextprotocol.io/docs/concepts/prompts)
````

## File: units/en/unit3/build-mcp-server.mdx
````
# Module 1: Build MCP Server

## The PR Chaos at CodeCraft Studios

It's your first week at CodeCraft Studios, and you're witnessing something that makes every developer cringe. The team's pull requests look like this:

- "stuff" 
- "more changes"
- "fix"
- "update things"

Meanwhile, the code review backlog is growing because reviewers can't understand what changed or why. Sarah from the backend team spent 30 minutes trying to figure out what "various improvements" actually meant, while Mike from frontend had to dig through 47 files to understand a "small fix."

The team knows they need better PR descriptions, but everyone's too busy shipping features to write detailed explanations. They need a solution that helps without slowing them down.

**Your mission**: Build an intelligent PR Agent that analyzes code changes and suggests helpful descriptions automatically.

### Screencast: The PR Problem in Action 😬

<Youtube id="tskAUPWFPP0" />

**What You'll See**: A real PR at CodeCraft Studios titled "various improvements" and the description simply says "Fixed some stuff and made updates". Classic, right?

**The Confusion**: Watch as teammates struggle:
- **Sarah** (3 hours ago): "What was fixed? I see changes to the User model but can't tell if this is addressing a bug or adding features"
- **Jamie** (3 hours ago): "There are 8 files across 4 services... are these changes related? What should I focus on during review?"

**The Pain Point**: The screencast shows the actual diff—8 files scattered across multiple services with zero context. Reviewers have to piece together the story themselves, wasting precious time and possibly missing critical issues.

**Why This Matters**: This is exactly the PR chaos your MCP server will solve! By the end of this module, you'll turn these cryptic PRs into clear, actionable descriptions that make everyone's life easier.

## What You'll Build

In this first module, you'll create the foundation of CodeCraft Studios' automation system: an MCP server that transforms how the team writes pull requests. This module focuses on core MCP concepts that you'll build upon in Modules 2 and 3.

### Screencast: Your PR Agent Saves the Day! 🚀

<Youtube id="OaAWJLvnlqc" />

**The Solution in Action**: Watch how your MCP server will transform PR chaos into clarity:
1. **`analyze_file_changes`** - Grabs all the changes (453 lines across 8 files!)
2. **`get_pr_templates`** - Shows Claude the 7 templates to choose from
3. **`suggest_template`** - Claude picks "Feature" (smart choice!)

**What You'll See**: Claude doesn't just pick a template—it:
- Writes a clear summary of what actually changed
- Spots security issues (yikes, unhashed passwords!)
- Creates a nice to-do list for follow-up work
- Even prioritizes what needs fixing first

**The "Wow" Moment** ✨: In just seconds, your MCP server helps Claude transform the same branch into a PR that actually explains what's going on. No more confused reviewers, no more "what does this do?" comments.

**This is what you'll build**: A tool that turns PR dread into PR delight—let's get started!

## What You Will Learn

In this foundational module, you'll master:
- **How to create a basic MCP server using FastMCP** - The building blocks for Modules 2 and 3
- **Implementing MCP Tools for data retrieval and analysis** - The core primitive you'll use throughout Unit 3  
- **Letting Claude make intelligent decisions based on raw data** - A key principle for all MCP development
- **Testing and validating your MCP server** - Essential skills for building reliable tools

## Overview

Your PR Agent will solve CodeCraft Studios' problem using a key principle of MCP development: instead of hard-coding rigid rules about what makes a good PR, you'll provide Claude with raw git data and let it intelligently suggest appropriate descriptions.

This approach works because:
- **Flexible analysis**: Claude can understand context that simple rules miss
- **Natural language**: Suggestions feel human, not robotic
- **Adaptable**: Works for any codebase or coding style

You'll implement three essential tools that establish patterns for the entire automation system:

1. **analyze_file_changes** - Retrieves git diff information and changed files (data collection)
2. **get_pr_templates** - Lists available PR templates (resource management)  
3. **suggest_template** - Allows Claude to recommend the most appropriate template (intelligent decision-making)

## Getting Started

### Prerequisites

- Python 3.10 or higher
- Git installed and a git repository to test with
- uv package manager ([installation guide](https://docs.astral.sh/uv/getting-started/installation/))

### Starter Code

Clone the starter code repository:

```bash
git clone https://github.com/huggingface/mcp-course.git
```

Navigate to the starter code directory:

```bash
cd mcp-course/projects/unit3/build-mcp-server/starter
```

Install dependencies:

<Tip>

You might want to create a virtual environment for this project:

```bash
uv venv .venv
source .venv/bin/activate # On Windows use: .venv\Scripts\activate
```
</Tip>

```bash
uv sync --all-extras
```

### Your Task

This is your first hands-on MCP development experience! Open `server.py` and implement the three tools following the TODO comments. The starter code provides the basic structure - you need to:

1. **Implement `analyze_file_changes`** to run git commands and return diff data
   - ⚠️ **Important**: You'll likely hit a token limit error (25,000 tokens max per response)
   - This is a real-world constraint that teaches proper output management
   - See the "Handling Large Outputs" section below for the solution
   - ⚠️ **Note**: Git commands will run in the MCP server's directory by default. See "Working Directory Considerations" below for details
2. **Implement `get_pr_templates`** to manage and return PR templates  
3. **Implement `suggest_template`** to map change types to templates

Don't worry about making everything perfect - you'll refine these skills as you progress through the unit.

### Design Philosophy

Unlike traditional systems that categorize changes based on file extensions or rigid patterns, your implementation should:

- Provide Claude with raw git data (diffs, file lists, statistics)
- Let Claude analyze the actual code changes
- Allow Claude to make intelligent template suggestions
- Keep the logic simple - Claude handles the complexity

<Tip>

**MCP Philosophy**: Instead of building complex logic into your tools, provide Claude with rich data and let its intelligence make the decisions. This makes your code simpler and more flexible than traditional rule-based systems.

</Tip>

## Testing Your Implementation

### 1. Validate Your Code

Run the validation script to check your implementation:

```bash
uv run python validate_starter.py
```

### 2. Run Unit Tests

Test your implementation with the provided test suite:

```bash
uv run pytest test_server.py -v
```

### 3. Test with Claude Code

Configure your server directly in Claude Code:

```bash
# Add the MCP server to Claude Code
claude mcp add pr-agent -- uv --directory /absolute/path/to/starter run server.py

# Verify the server is configured
claude mcp list
```

Then:
1. Make some changes in a git repository
2. Ask Claude: "Can you analyze my changes and suggest a PR template?"
3. Watch Claude use your tools to provide intelligent suggestions

<Tip warning={true}>

**Common first error**: If you get "MCP tool response exceeds maximum allowed tokens (25000)", this is expected! Large repositories can generate massive diffs. This is a valuable learning moment - see the "Handling Large Outputs" section for the solution.

</Tip>

## Common Patterns

### Tool Implementation Pattern

```python
@mcp.tool()
async def tool_name(param1: str, param2: bool = True) -> str:
    """Tool description for Claude.
    
    Args:
        param1: Description of parameter
        param2: Optional parameter with default
    """
    # Your implementation
    result = {"key": "value"}
    return json.dumps(result)
```

### Error Handling

Always handle potential errors gracefully:

```python
try:
    result = subprocess.run(["git", "diff"], capture_output=True, text=True)
    return json.dumps({"output": result.stdout})
except Exception as e:
    return json.dumps({"error": str(e)})
```

<Tip warning={true}>

**Error Handling**: Always return valid JSON from your tools, even for errors. Claude needs structured data to understand what went wrong and provide helpful responses to users.

</Tip>

### Handling Large Outputs (Critical Learning Moment!)

<Tip warning={true}>

**Real-world constraint**: MCP tools have a token limit of 25,000 tokens per response. Large git diffs can easily exceed this limit 10x or more! This is a critical lesson for production MCP development.

</Tip>

When implementing `analyze_file_changes`, you'll likely encounter this error:
```
Error: MCP tool response (262521 tokens) exceeds maximum allowed tokens (25000)
```

**Why this happens:**
- A single file change can be thousands of lines
- Enterprise repositories often have massive refactorings
- Git diffs include full context by default
- JSON encoding adds overhead

This teaches us an important principle: **Always design tools with output limits in mind**. Here's the solution:

```python
@mcp.tool()
async def analyze_file_changes(base_branch: str = "main", 
                              include_diff: bool = True,
                              max_diff_lines: int = 500) -> str:
    """Analyze file changes with smart output limiting.
    
    Args:
        base_branch: Branch to compare against
        include_diff: Whether to include the actual diff
        max_diff_lines: Maximum diff lines to include (default 500)
    """
    try:
        # Get the diff
        result = subprocess.run(
            ["git", "diff", f"{base_branch}...HEAD"],
            capture_output=True, 
            text=True
        )
        
        diff_output = result.stdout
        diff_lines = diff_output.split('\n')
        
        # Smart truncation if needed
        if len(diff_lines) > max_diff_lines:
            truncated_diff = '\n'.join(diff_lines[:max_diff_lines])
            truncated_diff += f"\n\n... Output truncated. Showing {max_diff_lines} of {len(diff_lines)} lines ..."
            diff_output = truncated_diff
        
        # Get summary statistics
        stats_result = subprocess.run(
            ["git", "diff", "--stat", f"{base_branch}...HEAD"],
            capture_output=True,
            text=True
        )
        
        return json.dumps({
            "stats": stats_result.stdout,
            "total_lines": len(diff_lines),
            "diff": diff_output if include_diff else "Use include_diff=true to see diff",
            "files_changed": self._get_changed_files(base_branch)
        })
        
    except Exception as e:
        return json.dumps({"error": str(e)})
```

**Best practices for large outputs:**
1. **Implement pagination**: Break large results into pages
2. **Add filtering options**: Let users request specific files or directories
3. **Provide summaries first**: Return statistics before full content
4. **Use progressive disclosure**: Start with high-level info, allow drilling down
5. **Set sensible defaults**: Default to reasonable limits that work for most cases

## Working Directory Considerations

By default, MCP servers run commands in their installation directory, not in Claude's current working directory. This means your git commands might analyze the wrong repository! 

To solve this, MCP provides [roots](https://modelcontextprotocol.io/docs/concepts/roots) - a way for clients to inform servers about relevant directories. Claude Code automatically provides its working directory as a root.

Here's how to access it in your tool:

```python
@mcp.tool()
async def analyze_file_changes(...):
    # Get Claude's working directory from roots
    context = mcp.get_context()
    roots_result = await context.session.list_roots()
    
    # Extract the path from the FileUrl object
    working_dir = roots_result.roots[0].uri.path
    
    # Use it for all git commands
    result = subprocess.run(
        ["git", "diff", "--name-status"],
        capture_output=True,
        text=True,
        cwd=working_dir  # Run in Claude's directory!
    )
```

This ensures your tools operate on the repository Claude is actually working with, not the MCP server's installation location.

## Troubleshooting

- **Import errors**: Ensure you've run `uv sync`
- **Git errors**: Make sure you're in a git repository
- **No output**: MCP servers communicate via stdio - test with Claude Desktop
- **JSON errors**: All tools must return valid JSON strings
- **Token limit exceeded**: This is expected with large diffs! Implement output limiting as shown above
- **"Response too large" errors**: Add `max_diff_lines` parameter or set `include_diff=false`
- **Git commands run in wrong directory**: MCP servers run in their installation directory by default, not Claude's working directory. To fix this, use [MCP roots](https://modelcontextprotocol.io/docs/concepts/roots) to access Claude's current directory:
  ```python
  # Get Claude's working directory from roots
  context = mcp.get_context()
  roots_result = await context.session.list_roots()
  working_dir = roots_result.roots[0].uri.path  # FileUrl object has .path property
  
  # Use it in subprocess calls
  subprocess.run(["git", "diff"], cwd=working_dir)
  ```
  Claude Code automatically provides its working directory as a root, allowing your MCP server to operate in the correct location.

## Next Steps

Congratulations! You've built your first MCP server with Tools - the foundation for everything that follows in Unit 3.

### What you've accomplished in Module 1:
- **Created MCP Tools** that provide Claude with structured data
- **Implemented the core MCP philosophy** - let Claude make intelligent decisions from raw data
- **Built a practical PR Agent** that can analyze code changes and suggest templates
- **Learned about real-world constraints** - the 25,000 token limit and how to handle it
- **Established testing patterns** with validation scripts and unit tests

### Key patterns you can reuse:
- **Data collection tools** that gather information from external sources
- **Intelligent analysis** where Claude processes raw data to make decisions  
- **Output management** - truncating large responses while preserving usefulness
- **Error handling** that returns structured JSON responses
- **Testing strategies** for MCP server development

### What to do next:
1. **Review the solution** in `/projects/unit3/build-mcp-server/solution/` to see different implementation approaches
2. **Compare your implementation** with the provided solution - there's no single "right" way to solve the problem
3. **Test your tools thoroughly** - try them with different types of code changes to see how Claude adapts
4. **Move on to Module 2** where you'll add real-time webhook capabilities and learn about MCP Prompts for workflow standardization

Module 2 will build directly on the server you created here, adding dynamic event handling to complement your static file analysis tools!

### The story continues...
With your PR Agent working, CodeCraft Studios developers are already writing better pull requests. But next week, you'll face a new challenge: critical CI/CD failures are slipping through unnoticed. Module 2 will add real-time monitoring to catch these issues before they reach production.

## Additional Resources

- [MCP Documentation](https://modelcontextprotocol.io/)
- [FastMCP Guide](https://modelcontextprotocol.io/quickstart/server)
- Solution walkthrough: `unit3/build-mcp-server-solution-walkthrough.md`
````

## File: units/en/unit2/gradio-client.mdx
````
# Gradio as an MCP Client

In the previous section, we explored how to create an MCP Server using Gradio and connect to it using an MCP Client. In this section, we're going to explore how to use Gradio as an MCP Client to connect to an MCP Server.

<Tip>

Gradio is best suited to the creation of UI clients and MCP servers, but it is also possible to use it as an MCP Client and expose that as a UI.

</Tip>

We'll connect to an MCP server similar to the one we created in the previous section but with additional features, and use it to answer questions.

## MCP Client in Gradio

### Connect to an example MCP Server

Let's connect to an example MCP Server that is already running on Hugging Face. We'll use [this one](https://huggingface.co/spaces/abidlabs/mcp-tool-http) for this example. It's a space that contains a collection of MCP tools.

```python
from smolagents.mcp_client import MCPClient

with MCPClient(
    {"url": "https://abidlabs-mcp-tool-http.hf.space/gradio_api/mcp/sse"}
) as tools:
    # Tools from the remote server are available
    print("\n".join(f"{t.name}: {t.description}" for t in tools))

```

<details>
<summary>Output</summary>
<pre>
<code>
prime_factors: Compute the prime factorization of a positive integer.
generate_cheetah_image: Generate a cheetah image.
image_orientation: Returns whether image is portrait or landscape.
sepia: Apply a sepia filter to the input image.
</code>
</pre>
</details>

### Connect to the MCP Server from Gradio

Great, now that you've connected to an example MCP Server. Now, you need to use it in an example application.

First, we need to install the `smolagents`, Gradio and mcp-client libraries, if we haven't already:

```bash
pip install "smolagents[mcp]" "gradio[mcp]" mcp fastmcp
```

Now, we can import the necessary libraries and create a simple Gradio interface that uses the MCP Client to connect to the MCP Server.


```python
import gradio as gr
import os

from mcp import StdioServerParameters
from smolagents import InferenceClientModel, CodeAgent, ToolCollection, MCPClient
```

Next, we'll connect to the MCP Server and get the tools that we can use to answer questions.

```python
mcp_client = MCPClient(
    {"url": "https://abidlabs-mcp-tool-http.hf.space/gradio_api/mcp/sse"} # This is the MCP Client we created in the previous section
)
tools = mcp_client.get_tools()
```

Now that we have the tools, we can create a simple agent that uses them to answer questions. We'll just use a simple `InferenceClientModel` and the default model from `smolagents` for now.

It is important to pass your api_key to the InferenceClientModel. You can access the token from your huggingface account. [check here.](https://huggingface.co/docs/hub/en/security-tokens), and set the access token with the environment variable  `HF_TOKEN`.

```python
model = InferenceClientModel(token=os.getenv("HF_TOKEN"))
agent = CodeAgent(tools=[*tools], model=model)
```

Now, we can create a simple Gradio interface that uses the agent to answer questions.

```python
demo = gr.ChatInterface(
    fn=lambda message, history: str(agent.run(message)),
    type="messages",
    examples=["Prime factorization of 68"],
    title="Agent with MCP Tools",
    description="This is a simple agent that uses MCP tools to answer questions."
)

demo.launch()
```

And that's it! We've created a simple Gradio interface that uses the MCP Client to connect to the MCP Server and answer questions.

<iframe
	src="https://mcp-course-unit2-gradio-client.hf.space"
	frameborder="0"
	width="850"
	height="450"
></iframe>


## Complete Example

Here's the complete example of the usage of an MCP Client in Gradio:

```python
import gradio as gr
import os

from smolagents import InferenceClientModel, CodeAgent, MCPClient


try:
    mcp_client = MCPClient(
        {"url": "https://abidlabs-mcp-tool-http.hf.space/gradio_api/mcp/sse"}
    )
    tools = mcp_client.get_tools()

    model = InferenceClientModel(token=os.getenv("HUGGINGFACE_API_TOKEN"))
    agent = CodeAgent(tools=[*tools], model=model, additional_authorized_imports=["json", "ast", "urllib", "base64"])

    demo = gr.ChatInterface(
        fn=lambda message, history: str(agent.run(message)),
        type="messages",
        examples=["Analyze the sentiment of the following text 'This is awesome'"],
        title="Agent with MCP Tools",
        description="This is a simple agent that uses MCP tools to answer questions.",
    )

    demo.launch()
finally:
    mcp_client.disconnect()
```

You'll notice that we're closing the MCP Client in the `finally` block. This is important because the MCP Client is a long-lived object that needs to be closed when the program exits.

## Deploying to Hugging Face Spaces

To make your server available to others, you can deploy it to Hugging Face Spaces, just like we did in the previous section.
To deploy your Gradio MCP client to Hugging Face Spaces:

1. Create a new Space on Hugging Face:
   - Go to huggingface.co/spaces
   - Click "Create new Space"
   - Choose "Gradio" as the SDK
   - Name your space (e.g., "mcp-client")

2. Update MCP Server URL in the code:

```python
mcp_client = MCPClient(
    {"url": "https://abidlabs-mcp-tool-http.hf.space/gradio_api/mcp/sse"}
)
```

3. Create a `requirements.txt` file:
```txt
gradio[mcp]
smolagents[mcp]
```

4. Push your code to the Space:
```bash
git init
git add app.py requirements.txt
git commit -m "Initial commit"
git remote add origin https://huggingface.co/spaces/YOUR_USERNAME/mcp-client
git push -u origin main
```

Note: While adding remote origin, Refer to [password-git-deprecation](https://huggingface.co/blog/password-git-deprecation) for adding with AccessToken.

## Conclusion

In this section, we've explored how to use Gradio as an MCP Client to connect to an MCP Server. We've also seen how to deploy the MCP Client in Hugging Face Spaces.
````

## File: units/en/_toctree.yml
````yaml
- title: "0. Welcome to the MCP Course"
  sections:
  - local: unit0/introduction
    title: Welcome to the MCP Course
    
- title: "1. Introduction to Model Context Protocol"
  sections:
  - local: unit1/introduction
    title: Introduction to Model Context Protocol (MCP)
  - local: unit1/key-concepts
    title: Key Concepts and Terminology
  - local: unit1/architectural-components
    title: Architectural Components
  - local: unit1/quiz1
    title: Quiz 1 - MCP Fundamentals
  - local: unit1/communication-protocol
    title: The Communication Protocol
  - local: unit1/capabilities
    title: Understanding MCP Capabilities
  - local: unit1/sdk
    title: MCP SDK
  - local: unit1/quiz2
    title: Quiz 2 - MCP SDK
  - local: unit1/mcp-clients
    title: MCP Clients
  - local: unit1/gradio-mcp
    title: Gradio MCP Integration
  - local: unit1/unit1-recap
    title: Unit 1 Recap
  - local: unit1/certificate
    title: Get your certificate!

- title: "2. Use Case: End-to-End MCP Application"
  sections:
  - local: unit2/introduction
    title: Introduction to Building an MCP Application
  - local: unit2/gradio-server
    title: Building the Gradio MCP Server
  - local: unit2/clients
    title: Using MCP Clients with your application
  - local: unit2/continue-client
    title: Using MCP in the Your AI Coding Assistant
  - local: unit2/gradio-client
    title: Building an MCP Client with Gradio
  - local: unit2/tiny-agents
    title: Building Tiny Agents with MCP and the Hugging Face Hub

- title: "3. Advanced MCP Development: Custom Workflow Servers"
  sections:
  - local: unit3/introduction
    title: Building Custom Workflow Servers for Claude Code
  - local: unit3/build-mcp-server
    title: "Module 1: Build MCP Server"
  - local: unit3/github-actions-integration
    title: "Module 2: GitHub Actions Integration"
  - local: unit3/slack-notification
    title: "Module 3: Slack Notification"
  - local: unit3/build-mcp-server-solution-walkthrough
    title: "Unit 3 Solution Walkthrough: Building a Pull Request Agent with MCP"
  - local: unit3/certificate
    title: "Get your certificate!"
  - local: unit3/conclusion
    title: "Unit 3 Conclusion"

- title: "3.1. Use Case: Build a Pull Request Agent on the Hub"
  sections:
  - local: unit3_1/introduction
    title: Build a Pull Request Agent on the Hugging Face Hub
  - local: unit3_1/setting-up-the-project
    title: Setting up the Project
  - local: unit3_1/creating-the-mcp-server
    title: Creating the MCP Server
  - local: unit3_1/quiz1
    title: Quiz 1 - MCP Server Implementation
  - local: unit3_1/mcp-client
    title: MCP Client
  - local: unit3_1/webhook-listener
    title: Webhook Listener
  - local: unit3_1/quiz2
    title: Quiz 2 - Pull Request Agent Integration
  - local: unit3_1/conclusion
    title: Conclusion
````
