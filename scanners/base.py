class Scanner:
    def __init__(self, name):
        self.name = name

    def run(self, target_path):
        """Run the scanner on the target path. To be implemented by subclasses."""
        raise NotImplementedError("run() must be implemented by subclasses.") 