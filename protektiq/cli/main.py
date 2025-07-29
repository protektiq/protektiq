import typer

def pipeline():
    typer.echo("[Protektiq] Running pipeline (placeholder)...")

app = typer.Typer()
app.command()(pipeline)

if __name__ == "__main__":
    app() 