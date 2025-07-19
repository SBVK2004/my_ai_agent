# my_ai_agent
#### Ai agent for control browser use
## what you need to do to get started is:

### 1. Open your terminal/command prompt.

### 2. Install the main tool: Type " pip install browser-use "  and press Enter.

### 3. Install the browser it will control: Type " playwright install chromium --with-deps --no-shell " and press Enter.

### 4.Create a file named .env in a folder. Inside it, put your API keys like OPENAI_API_KEY=YOUR_KEY.
The .env file which is provided here, make sure you give your own api keys 
#### To get a GitHub Personal Access Token (PAT), follow these steps:

Log in to GitHub: Go to github.com and log in to your account.

Go to Settings:

Click on your profile picture in the upper-right corner of the page.

From the dropdown menu, select "Settings."

Navigate to Developer settings:

In the left sidebar, scroll down and click on "Developer settings."

Select Personal access tokens:

In the "Developer settings" menu, click on "Personal access tokens."

Then, click on "Tokens (classic)" (this is generally what people are referring to when they ask for a "GitHub token key"). While "Fine-grained tokens" exist, "Tokens (classic)" are more commonly used for general API access and often what you need when a tool asks for a "GitHub token."

Generate new token:

Click the "Generate new token" button.

Then choose "Generate new token (classic)".

Configure your new token:

Note: Give your token a descriptive name (e.g., "My CLI Token," "VS Code Token," "Deployment Script Token"). This helps you remember what it's for later.

Expiration: Set an expiration for your token. It's generally a good security practice not to have tokens that never expire. You can choose 7 days, 30 days, 60 days, 90 days, or a custom date.

Select scopes (permissions): This is crucial. You need to select the appropriate scopes for what you intend to do with the token.

If you're using it for basic Git operations (clone, push, pull), you'll likely need repo scope (full control of private repositories).

If you're doing more specific things (like managing Gist, user profiles, or organizations), you'll need to select those specific scopes.

Be careful: Only select the scopes you absolutely need. Granting too many permissions increases the risk if your token is compromised.

Generate token:

After configuring the name, expiration, and scopes, click the "Generate token" button at the bottom of the page.

Copy your token:

IMPORTANT: Once the token is generated, you will see it displayed only once. Copy it immediately and save it in a secure place (like a password manager). If you navigate away from the page, you won't be able to retrieve it again. You'll have to generate a new one.
#### to get your api key 
 OpenAI API Key (OPENAI_API_KEY)
Go to: platform.openai.com

Sign Up/Log In: Create an account or log in.

Navigate: Click on your profile icon in the top right corner.

Select: Choose "View API keys" from the dropdown.

Generate: Click the "Create new secret key" button.

Copy: Copy the key displayed. Remember, you won't see it again.

Billing: Ensure you have billing set up (even a small amount of credit) for the key to be active.

### 5.Create a Python file (e.g., my_browser_agent.py) in the same folder as your .env file.

### 6.Paste the "Spin up your agent" code into my_browser_agent.py.

### 7.Run your Python code: In your terminal, navigate to that folder and type "python my_browser_agent.py" and press Enter.
