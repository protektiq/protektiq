#!/usr/bin/env python
import typer
from orchestrator.main import Orchestrator

app = typer.Typer()

@app.command()
def pipeline(target_path: str = typer.Option(".", "--target-path", help="Path to scan (default: current directory)")):
    orchestrator = Orchestrator()
    orchestrator.run_pipeline(target_path)

def main():
    app()

if __name__ == "__main__":
    main() 