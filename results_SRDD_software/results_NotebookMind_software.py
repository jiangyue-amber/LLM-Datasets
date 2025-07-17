# Software Name: NotebookMind
# Category: Notebook
# Description: NotebookMind is a software application that provides users with a platform to create and organize digital notebooks specifically designed for brainstorming and creative ideation. Users can create new pages within the notebook and use various brainstorming tools such as mind maps, flowcharts, and visual diagrams to capture and organize their ideas. NotebookMind also offers features like color coding, labeling, and searching to enhance the organization and retrieval of ideas within the notebooks.

import json

class NotebookMind:
    def __init__(self, notebook_name="My Notebook"):
        self.notebook_name = notebook_name
        self.pages = {}

    def create_page(self, page_name):
        if page_name not in self.pages:
            self.pages[page_name] = {
                "content": [],
                "mind_map": {},
                "flowchart": [],
                "visual_diagram": [],
                "labels": [],
                "color_code": None
            }
            return f"Page '{page_name}' created."
        else:
            return f"Page '{page_name}' already exists."

    def add_content(self, page_name, content):
        if page_name in self.pages:
            self.pages[page_name]["content"].append(content)
            return "Content added to page."
        else:
            return "Page not found."

    def add_mind_map_node(self, page_name, node_id, text, parent_id=None):
        if page_name in self.pages:
            if "mind_map" not in self.pages[page_name]:
                self.pages[page_name]["mind_map"] = {}

            self.pages[page_name]["mind_map"][node_id] = {"text": text, "parent": parent_id, "children": []}

            if parent_id and parent_id in self.pages[page_name]["mind_map"]:
                self.pages[page_name]["mind_map"][parent_id]["children"].append(node_id)
            return "Mind map node added."
        else:
            return "Page not found."

    def add_flowchart_element(self, page_name, element_type, description):
        if page_name in self.pages:
            self.pages[page_name]["flowchart"].append({"type": element_type, "description": description})
            return "Flowchart element added."
        else:
            return "Page not found."

    def add_visual_diagram_element(self, page_name, element_type, details):
        if page_name in self.pages:
            self.pages[page_name]["visual_diagram"].append({"type": element_type, "details": details})
            return "Visual diagram element added."
        else:
            return "Page not found."

    def add_label(self, page_name, label):
        if page_name in self.pages:
            if label not in self.pages[page_name]["labels"]:
                self.pages[page_name]["labels"].append(label)
                return "Label added."
            else:
                return "Label already exists on this page."
        else:
            return "Page not found."

    def set_color_code(self, page_name, color_code):
        if page_name in self.pages:
            self.pages[page_name]["color_code"] = color_code
            return "Color code set."
        else:
            return "Page not found."

    def search_content(self, search_term):
        results = {}
        for page_name, page_data in self.pages.items():
            if search_term.lower() in ' '.join(page_data["content"]).lower():
                results[page_name] = page_data["content"]
        return results

    def get_page(self, page_name):
        if page_name in self.pages:
            return self.pages[page_name]
        else:
            return None

    def save_notebook(self, filename="notebook.json"):
        with open(filename, 'w') as f:
            json.dump({
                "notebook_name": self.notebook_name,
                "pages": self.pages
            }, f, indent=4)
        return f"Notebook saved to {filename}"

    def load_notebook(self, filename="notebook.json"):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.notebook_name = data.get("notebook_name", "My Notebook")
                self.pages = data.get("pages", {})
            return f"Notebook loaded from {filename}"
        except FileNotFoundError:
            return "File not found."

if __name__ == '__main__':
    notebook = NotebookMind("My Brainstorming Notebook")

    notebook.create_page("Project Ideas")
    notebook.add_content("Project Ideas", "Develop a new mobile app for task management.")
    notebook.add_content("Project Ideas", "Explore AI applications in education.")
    notebook.add_label("Project Ideas", "Mobile App")
    notebook.set_color_code("Project Ideas", "blue")
    notebook.add_mind_map_node("Project Ideas", "1", "Project Ideas", None)
    notebook.add_mind_map_node("Project Ideas", "2", "Mobile App", "1")
    notebook.add_mind_map_node("Project Ideas", "3", "AI in Education", "1")

    notebook.create_page("Marketing Strategy")
    notebook.add_content("Marketing Strategy", "Define target audience.")
    notebook.add_content("Marketing Strategy", "Create engaging content.")
    notebook.add_flowchart_element("Marketing Strategy", "Start", "Define Objectives")
    notebook.add_flowchart_element("Marketing Strategy", "Process", "Market Research")
    notebook.add_label("Marketing Strategy", "Content Marketing")
    notebook.set_color_code("Marketing Strategy", "green")

    results = notebook.search_content("mobile")
    print("Search results:", results)

    print(notebook.get_page("Project Ideas"))

    print(notebook.save_notebook("my_notebook.json"))

    notebook2 = NotebookMind()
    print(notebook2.load_notebook("my_notebook.json"))
    print(notebook2.notebook_name)
    print(notebook2.get_page("Project Ideas"))