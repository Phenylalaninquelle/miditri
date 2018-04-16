#!/usr/bin/env python3
#-*- coding:utf8 -*-

import click
import mido
from os.path import basename
import numpy as np

class Miditri(object):

    def __init__(self, infile, outfile, track_num):
        self.infile = infile
        self.midifile = mido.MidiFile(infile)
        self.track_num = track_num
        self.midi_inf = None
        self._get_midi_information()
        if outfile is None:
            self.outfile = basename(infile).split('.mid')[0]
        else:
            self.outfile = outfile

    def write_results(self):
        with open(self.outfile, 'w') as f:
            for tup in self.midi_inf:
                f.write('{}, {}\n'.format(tup[0], tup[1]))

    def _get_midi_information(self):
        tmp = list()
        for m in self.midifile.tracks[self.track_num]:
            if m.type == 'note_on':
                tmp.append((m.note, m.time))
        self.midi_inf = np.asarray(tmp)



@click.command()
@click.argument('infile', type=click.Path(exists=True), required=True)
@click.option('--outfile', type=str, default=None,
              help='Path to write results to (in .csv format)')
@click.option('--track_num', type=int, default=1,
              help='Index of track that contains the notes (zero-based)')
def cli(infile, outfile, track_num):
    """Extract various melody-related information from a given MIDI file (INFILE)."""
    miditri = Miditri(infile, outfile, track_num)
    miditri.write_results()
