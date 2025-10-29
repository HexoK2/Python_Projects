from os import remove


def add_article():
    article = input("Add an article to your list")
    Name_List.append(article)


def remove_article():
    print(Name_List)
    suppr = input("Witch article want you to remove ? (1,2,3...)")
    if suppr in Name_List:
        Name_List.remove(suppr)
    else:
        print("There are any article which called like that !")


print("Welcome to this program !")
Name_List = input("Give a name to your Shopping list...")
print(f"Now, your List is called: {Name_List} !")
Name_List = []
add_article()
remove_article()


# Not finished


