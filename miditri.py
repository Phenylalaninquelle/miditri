#!/usr/bin/env python3
#-*- coding:utf8 -*-

import click
import mido
from os.path import basename


class Miditri(object):

    def __init__(self, infile, outfile):
        self.infile = infile
        self.midifile = mido.MidiFile(infile)
        if outfile is None:
            self.outfile = basename(infile).split('.mid')[0]
        else:
            self.outfile = outfile

    def write_results(self):
        with open(self.outfile, 'w') as f:
            f.write('hello')

@click.command()
@click.argument('infile', type=click.Path(exists=True), required=True)
@click.option('--outfile', type=str, default=None,
              help='Path to write results to (in .csv format)')
def cli(infile, outfile):
    """Extract various melody-related information from a given MIDI file (INFILE)."""
    miditri = Miditri(infile, outfile)
    miditri.write_results()
