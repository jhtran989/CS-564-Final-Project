# CS 564 - G09
## Final Project
### Information Extraction from Case Reports
#### Mike Dinh, John Tran

---------

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



