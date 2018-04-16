#!/usr/bin/env python3
#-*- coding:utf8 -*-

import click
import mido


class Config(object):

    def __init__(self, infile, outfile):
        self.infile = infile
        self.midifile = mido.MidiFile(infile)
        self.outfile = outfile

@click.command()
@click.argument('infile', type=click.Path(exists=True), required=True)
@click.option('--outfile', type=click.File('w'), default=None,
              help='Path to write results to (in .csv format)')
def cli(infile, outfile):
    """Extract various melody-related information from a given MIDI file (INFILE)."""
    cfg = Config(infile, outfile)
    click.echo(cfg.infile)
    click.echo(cfg.outfile)

def write_results(outfile):
    if outfile is None:
        pass
