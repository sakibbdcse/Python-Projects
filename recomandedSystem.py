import pandas as pd

books = pd.read_csv('data/BX-Books.csv', sep=';', on_bad_lines='skip', encoding='latin-1')
books = books[['ISBN', 'Book-Title', 'Book-Author', 'Year-Of-Publication', 'Publisher','Image-URL-L']]
books.rename(columns={
    'Book-Title':'Title',
    'Book-Author':'Author',
    'Year-Of-Publication':'Year',
    'Image-URL-L':'Img-url',
}, inplace=True)

print(books.columns)

