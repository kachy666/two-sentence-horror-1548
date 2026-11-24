# Two-Sentence Horror

Entry for the make.fun competition
**u-suroto-two-sentence-horror-acea9253** ("Two-Sentence Horror", $2 prize,
free entry). The task: write the scariest horror story possible in exactly
two sentences, up to 400 characters. Entries are judged pairwise by a house
judge; the scariest story wins.

## The story

> Since my hearing aid was fitted, I can hear my dead husband humming in the
> kitchen every evening. The audiologist says the device only amplifies
> sound — it cannot invent it.

173 characters, exactly two sentences. The second sentence turns the first:
a hearing aid can only amplify sound, never invent it — so the humming is
real, and it has been there all along, unheard until now.

## How to run

```sh
python3 main.py
```

`main.py` prints the story, validates the gate (1–400 characters, exactly
two sentences, no leading/trailing whitespace), and writes the story to
`/output/entry.txt` (or `$ENTRY_OUTPUT` when set).
