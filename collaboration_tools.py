```python
import json

class CollaborationTools:
    def __init__(self, config):
        self.config = config
        self.tools = self.config['collaboration_tools']

    def start_collaboration(self):
        print("Starting collaboration...")
        print("Available collaboration tools:")
        for i, tool in enumerate(self.tools):
            print(f"{i+1}. {tool}")
        selected_tool = input("Enter the number of your selected tool: ")
        self.launch_tool(self.tools[int(selected_tool) - 1])

    def launch_tool(self, tool_name):
        # This function launches the selected collaboration tool.
        # In a real-world scenario, this would involve tasks such as opening the tool's interface, logging in, etc.
        print(f"Launching collaboration tool '{tool_name}'...")
        # Implement tool launching functionality here
        print(f"Collaboration tool '{tool_name}' launched successfully.")
```
