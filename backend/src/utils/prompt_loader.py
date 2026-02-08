import os

class PromptLoader:
    def __init__(self, prompt_path="prompts/system_prompt.txt"):
        self.prompt_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../', prompt_path))
        self.content = ""
        self.layers = {}

    def load_prompt(self):
        """Loads the system prompt from file."""
        if not os.path.exists(self.prompt_path):
            raise FileNotFoundError(f"System prompt not found at {self.prompt_path}")
            
        with open(self.prompt_path, 'r', encoding='utf-8') as f:
            self.content = f.read()
            
        self._parse_layers()
        return self.content

    def _parse_layers(self):
        """Simple parser to extract layers defined by ## LAYER X headers."""
        lines = self.content.split('\n')
        current_layer = None
        buffer = []
        
        for line in lines:
            if line.startswith("## LAYER"):
                if current_layer:
                    self.layers[current_layer] = "\n".join(buffer).strip()
                current_layer = line.strip().replace("#", "").strip()
                buffer = []
            else:
                buffer.append(line)
                
        if current_layer:
             self.layers[current_layer] = "\n".join(buffer).strip()

    def get_layer(self, layer_name):
        """Retrieve specific layer content."""
        # Normalize keys if needed
        for key in self.layers:
            if layer_name.lower() in key.lower():
                return self.layers[key]
        return None

    def validate_integrity(self):
        """Check if all required layers are present."""
        required_layers = ["IDENTITY", "PLANNING", "CODE QUALITY"]
        missing = []
        for req in required_layers:
            found = False
            for key in self.layers:
                if req in key:
                    found = True
                    break
            if not found:
                missing.append(req)
        
        return len(missing) == 0, missing

if __name__ == "__main__":
    loader = PromptLoader()
    try:
        print("Loading prompt...")
        content = loader.load_prompt()
        print("Prompt loaded successfully.")
        
        valid, missing = loader.validate_integrity()
        if valid:
            print("Integrity Check: PASS")
        else:
            print(f"Integrity Check: FAIL - Missing {missing}")
            
        print("\n--- Identity Layer ---")
        print(loader.get_layer("IDENTITY"))
        
    except Exception as e:
        print(f"Error: {e}")
