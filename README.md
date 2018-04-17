# Miditri
Little cli tool that takes a midi file and prints out the note and time values of all the notes in a specified track to a .csv file.
Written for this specific purpose, so may not be very extensible (yet?).

Also bad pun on a slavic first name.

### Installation
After cloning this repository, installation happens with
```
cd miditri 
pip install .
```

### Usage
`miditri --help` tells you:
```
Usage: miditri [OPTIONS] INFILE

  Extract various melody-related information from given MIDI file `INFILE`.
  !NOTE!: operates only on a single track in the file

  Default operation is to write note and time values for all `note_on`
  messages  in file given with `--outfile` option. If no outfile is given,
  an `INFILE.csv` file is used.

Options:
  --outfile TEXT       Path to write results to (in .csv format)
  --track_num INTEGER  Index of track to read from (zero-based)
  --find_classes       Add note classes to output
  --use_note_offs      If given, output file will contain information from
                       note_offmessages
  --help               Show this message and exit.
```
