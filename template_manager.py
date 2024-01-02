```python
import json
import os

class TemplateManager:
    def __init__(self, config):
        self.config = config
        self.templates = self.load_templates()

    def load_templates(self):
        # This function loads the available templates from a predefined directory.
        # In a real-world scenario, this directory would contain template files for different types of projects.
        templates_dir = 'templates/'
        templates = [f for f in os.listdir(templates_dir) if os.path.isfile(os.path.join(templates_dir, f))]
        return templates

    def load_template(self, template_name):
        # This function loads the selected template.
        # In a real-world scenario, this would involve tasks such as setting up the project structure, initializing files, etc.
        if template_name not in self.templates:
            print(f"Template '{template_name}' not found.")
            return
        print(f"Loading template '{template_name}'...")
        template_path = os.path.join('templates/', template_name)
        with open(template_path, 'r') as file:
            template = json.load(file)
        print(f"Template '{template_name}' loaded successfully.")
        return template
```
