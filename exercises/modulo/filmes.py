def print_filmes(the_list):
    for cada_item in the_list:
        if isinstance(cada_item, list):
            print_filmes(cada_item)
        else:
            print(cada_item)