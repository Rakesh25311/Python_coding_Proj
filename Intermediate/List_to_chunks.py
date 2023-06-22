#Break a List Into Chunks:
def break_into_chunks(lst, chunk_size):
    chunks = [lst[i:i+chunk_size] for i in range(0, len(lst), chunk_size)]
    return chunks

# Example usage
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
chunked_list = break_into_chunks(my_list, 3)
print(chunked_list)  # Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#Code by @Rakesh Roshan Rath