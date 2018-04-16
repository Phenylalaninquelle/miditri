#!/usr/bin/env python3
#-*- coding:utf8 -*-

import click
import mido
from os.path import basename
import pandas as pd

class Miditri(object):

    def __init__(self, infile, outfile, track_num):
        self.infile = infile
        self.midifile = mido.MidiFile(infile)
        self.track_num = track_num
        self.midi_inf = pd.DataFrame()
        self._init_midi_information()
        if outfile is None:
            self.outfile = basename(infile).split('.mid')[0] + '.csv'
        else:
            self.outfile = outfile
        print(self.midi_inf)

    def write_results(self):
        self.midi_inf.to_csv(self.outfile, index=False)

    def _init_midi_information(self):
        tmp_notes = list()
        for m in self.midifile.tracks[self.track_num]:
            if 'note' in m.type:
                tmp_notes.append((m.note, m.type, m.time))
        self.midi_inf = pd.DataFrame(tmp_notes)
        self.midi_inf.columns = ['note_value', 'note_type', 'time_delta']



@click.command()
@click.argument('infile', type=click.Path(exists=True), required=True)
@click.option('--outfile', type=str, default=None,
              help='Path to write results to (in .csv format)')
@click.option('--track_num', type=int, default=1,
              help='Index of track that contains the notes (zero-based)')
def cli(infile, outfile, track_num):
    """
    Extract various melody-related information from given MIDI file `INFILE`.
    !NOTE!: operates only on a single track in the file

    Default operation is to write note and time values for all `note_on` messages 
    in file given with `--outfile` option. If no outfile is given, an `INFILE.csv`
    file is used.
    """
    miditri = Miditri(infile, outfile, track_num)
    miditri.write_results()
