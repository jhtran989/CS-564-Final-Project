# CS 564 - G09
## Final Project
### Information Extraction from Case Reports
#### Mike Dinh, John Tran

---------

## Required Programming Language/Packages

Any current version of `Python` should work.

### Packages
- `re` (regular expressions)
- `docx` (to parse the text in the case report documents in `.docx` format)
- `nltk` (Natural Language Toolkit for Natual Language Processing)

### Notes

- The template is ***highly*** structured, so no natural language processing 
  (NLP) was used
- To expand the code, maybe the sample case report given (i.e., `FA802` file)
  could be used with NLP?
- The template had to be converted from the given `.doc` to `.docx` format, 
  which was as easy as using the export feature of MS Word.
- In addition, to properly parse the tables, the layout of the tables had to 
  be modified manually since one of the tables had uneven cell separators, 
  causing some of the cells to be duplicated when parsing them
- FIXME: for now, all numbers are parsed in as a string (since the template 
  didn't have any numbers, just a placeholder -- "XX")
- FIXME: for notes sections, only ***one*** line was taken (for multiple 
  lines, need some other pattern to match -- e.g., make sure two consective 
  new lines follow immediately after with no match in between paragraphs of 
  the same section)
- For nested `regex` patterns, the overall outer-most pattern is represented 
  as the first group, and then goes into the inner groups (i.e., to get to 
  the two inner groups below, we skip the first group, `group(0)` take 
  the next two groups, `group(1)` and `group(2)`)

```python
abc((.*)-(.*))abc
```

- In terms of NLP stuff and implementing it...the things we want to extract 
  are pretty specific, so there isn't much to leverage:

For example, say we to get a method in-text citation (e.g., "Bob (2022)"). 
The easiest way to start is to pattern match a given section of text using 
`regex` `(.*?) \(\number\)` and only after that, can we use NLP tools. 
However, this narrows things down quite a bit for us and the only thing we 
need to check is the last name of the author. There is one thing though...
NLP can search for nouns, but proper nouns is a little tricky. Since, you 
have to specify a ***language*** (e.g., English), it can be hard to look for 
a variety of names from different languages since ***multiple*** languages 
cannot be mixed while classifying the words (assuming the last names are 
even in the NLP library for `Python`).

However, if we have something like "(found in 1990)", then it would match 
the above `regex` pattern, but this is clearly not a method. So, from here, 
we have a situation where NLP would be useful. This assumes a year was 
assigned for all given methods...However, we can only match 
individual words and their parts of speech. See the code (`parse_doc_FA802.
py`) for more details.

- Really hard to learn a lot about NLP given the short amount of time (and 
  the nuances of the library in `Python` for that matter), so we can only 
  extract simple info with it (i.e., nothing with analyzing the context 
  presented in a given section, having to rely on section headers).

- For NLTK, it will be hard to find a workaround typos

- There is a problem when encountering a hyphenated (extended) last name 
  where NLTP will interpret as a `JJ` parts of speech (POS) tag -- 
  "adjective or numeral, ordinal" and for instance, still-to-be-named. An 
  example of this would be "Tersigni-Terrant".

