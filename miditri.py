#!/usr/bin/env python3
#-*- coding:utf8 -*-

import click
import mido
from os.path import basename
import pandas as pd
    
NOTES_PER_OCTAVE = 12

class Miditri(object):

    def __init__(self, infile, outfile, track_num):
        self.infile = infile
        self.midifile = mido.MidiFile(infile)
        self.track_num = track_num
        self.midi_inf = pd.DataFrame()
        self._init_midi_information()
        self._init_noteclass_lut()
        if outfile is None:
            self.outfile = basename(infile).split('.mid')[0] + '.csv'
        else:
            self.outfile = outfile

    def write_results(self):
        """Write results to a .csv file"""
        self.midi_inf.to_csv(self.outfile, index=False)

    def _init_midi_information(self):
        """
        Get the note values and time deltas for all played notes in the 
        specified track. This is run at object setup since these are the
        needed information for all kind of later processing.
        """
        tmp_notes = list()
        for m in self.midifile.tracks[self.track_num]:
            if 'note' in m.type:
                tmp_notes.append((m.note, m.type, m.time))
        self.midi_inf = pd.DataFrame(tmp_notes)
        self.midi_inf.columns = ['note_value', 'note_type', 'time_delta']

    def _init_noteclass_lut(self):
        """Initialise the lookup table for note classes"""
        notes = ['c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#', 'a', 'a#', 'b']
        self.note_class_lut = dict(zip(range(12), notes))

    def find_note_classes(self):
        """
        Determine the note class for all stored notes. The note class is the 
        name of the note (e.g. 'c') opposed to the pitch (e.g 'c4') that is
        denoted by the note value in a midi file track.
        """
        self.midi_inf['note_class'] = self.midi_inf['note_value'] \
            .apply(lambda x: self.note_class_lut[x % NOTES_PER_OCTAVE]) 


@click.command()
@click.argument('infile', type=click.Path(exists=True), required=True)
@click.option('--outfile', type=str, default=None,
              help='Path to write results to (in .csv format)')
@click.option('--track_num', type=int, default=1,
              help='Index of track that contains the notes (zero-based)')
@click.option('--find_classes', is_flag=True,
              help='Determine note classes')
def cli(infile, outfile, track_num, find_classes):
    """
    Extract various melody-related information from given MIDI file `INFILE`.
    !NOTE!: operates only on a single track in the file

    Default operation is to write note and time values for all `note_on` messages 
    in file given with `--outfile` option. If no outfile is given, an `INFILE.csv`
    file is used.
    """
    miditri = Miditri(infile, outfile, track_num)
    if find_classes:
        miditri.find_note_classes()
    miditri.write_results()
