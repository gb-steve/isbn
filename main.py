# Look up ISBNs
# Input: csv with Author and Title
# Output: csv with added ISDN, author and title check

import isbnlib
import pandas as pd


def isb_ch(text):
    return isbnlib.isbn_from_words(text)


df = pd.read_csv('kartas1.csv')


rc = 0
df.insert(loc=2, column='ISBN', value='')
df.insert(loc=3, column='Title Check', value='')
df.insert(loc=4, column='Author Check', value='')

for row in df.index:
    try:
        isbn = isb_ch(df['Title'][rc])
        df['ISBN'][rc] = isbn
        df['Title Check'][rc] = isbnlib.meta(isbn)['Title']
        df['Author Check'][rc] = isbnlib.meta(isbn)['Authors'][0]
    except Exception:
        pass
    rc += 1
df.to_csv('with_isbn.csv', index=False)
