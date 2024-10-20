# TODO Найдите количество книг, которое можно разместить на дискете
disk_size = 1.44
pages_book = 100
lines_book = 50
symbols_book = 25
bytes_for_symbols = 4

disk_size_bytes = disk_size * 1024 * 1024

len_symvols = 100 * 25 * 50
book_size_bytes = len_symvols * 4
len_books = round(disk_size_bytes / book_size_bytes)
print("Количество книг, помещающихся на дискету:", len_books)
