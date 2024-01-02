```python
import json

class VersionControl:
    def __init__(self, config):
        self.config = config
        self.version_control_tools = self.config['version_control_tools']

    def manage_versions(self):
        print("Managing versions...")
        print("Available version control tools:")
        for i, tool in enumerate(self.version_control_tools):
            print(f"{i+1}. {tool}")
        selected_tool = input("Enter the number of your selected tool: ")
        self.launch_tool(self.version_control_tools[int(selected_tool) - 1])

    def launch_tool(self, tool_name):
        # This function launches the selected version control tool.
        # In a real-world scenario, this would involve tasks such as opening the tool's interface, logging in, etc.
        print(f"Launching version control tool '{tool_name}'...")
        # Implement tool launching functionality here
        print(f"Version control tool '{tool_name}' launched successfully.")
```
