import asyncio
import os 
from dotenv import load_dotenv
load_dotenv() 
from browser_use import Agent, Controller
from browser_use.mcp.client import MCPClient
from browser_use.llm import ChatOpenAI

async def main():
       controller = Controller()

       filesystem_client = MCPClient(
        server_name="filesystem",
        command="npx", # 'npx' is used to run Node.js packages
        args=["-y", "@modelcontextprotocol/server-filesystem", r"C:\Users\subar\OneDrive\Desktop\internship\my_ai_project"]
    )

       github_client = MCPClient(
        server_name="github",
        command="npx",
        args=["-y", "@modelcontextprotocol/server-github"],
        env={"GITHUB_TOKEN": os.environ.get("GITHUB_TOKEN")}     )

       print("Connecting to filesystem client...")
    await filesystem_client.connect() # Start the filesystem client
    await filesystem_client.register_to_controller(controller) 
    print("Filesystem client connected and ready.")

    print("Connecting to GitHub client...")
    await github_client.connect() # Start the GitHub client
    await github_client.register_to_controller(controller) 
    print("GitHub client connected and ready.")

        agent = Agent(
        task="Find the latest report.pdf in my documents and create a GitHub issue about it. In the issue, specify the full path of the found file and mention it's a new report.",
        llm=ChatOpenAI(model="gpt-4o"), 
        controller=controller      )

    
    print("Running the AI agent to complete the task...")
    await agent.run() 
    print("AI agent finished its task.")

        print("Disconnecting clients...")
    await filesystem_client.disconnect()
    await github_client.disconnect()
    print("Clients disconnected. All done!")

if __name__ == "__main__":
    asyncio.run(main())