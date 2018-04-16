#!/usr/bin/env python3
#-*- coding:utf8 -*-

import click
import mido

@click.command()
@click.argument('infile', type=click.Path(exists=True), required=True)
@click.option('--outfile', type=click.File('w'))
def cli(infile, outfile):
    """Extract various melody-related information from a given MIDI file."""
    mf = mido.MidiFile(infile)
    click.echo('done')
