# headerforge_core/cli.py
import click, json, sys
from pathlib import Path
from .generator import FlashHeaderGenerator

@click.command()
@click.option("-c", "--config", "config_file", type=click.Path(exists=True), required=True)
@click.option("-o", "--output", "out_file",   type=click.Path(), default="header.bin")
def main(config_file, out_file):
    cfg = json.loads(Path(config_file).read_text())
    layout = cfg.pop("_layout")                 # 或从模板加载
    gen = FlashHeaderGenerator(layout, cfg)
    try:
        hdr = gen.generate()
        Path(out_file).write_bytes(hdr)
        click.echo(f"[OK] Header saved to {out_file}")
    except Exception as e:
        click.echo(f"[ERR] {e}", err=True)
        sys.exit(1)
