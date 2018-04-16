# Miditri
Little cli tool, that takes a midi file and prints out the note and time values of all the note in a specified track in the file.
Written for this specific purpose, so may not be very extensible (yet?).

Also bad pun on a slavic first name.

### Installation
Simply install (e.g. in a virtualenv) with
```
cd miditri 
pip install .
```

### Usage
```
Usage: miditri [OPTIONS] INFILE

  Extract various melody-related information from given MIDI file `INFILE`.
  !NOTE!: operates only on a single track in the file

  Default operation is to write note and time values for all `note_on`
  messages  in file given with `--outfile` option. If no outfile is given,
  an `INFILE.csv` file is used.

Options:
  --outfile TEXT       Path to write results to (in .csv format)
  --track_num INTEGER  Index of track that contains the notes (zero-based)
  --find_classes       Determine note classes
  --help               Show this message and exit.
```
