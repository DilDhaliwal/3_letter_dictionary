#Dil Dhaliwal
def h_table(): 
    ht = {}
    for x in range(26):
        ht[x] = {}
        for y in range(26):
            ht[x][y] = {}
            for z in range(26):
                ht[x][y][z] = []
    return ht

def h_function(letter):
    letter = letter.lower()
    y = ord(letter) - ord('a')
    return y

def h_insertion(ht, value, definition):
    if len(value) != 3:
        print("Invalid Entry!")
        return
    x = h_function(value[0])
    y = h_function(value[1])
    z = h_function(value[2])
    if ht[x][y][z] == []:
        ht[x][y][z].append(definition)
    else:
        print("Already Filled!")
    return

def h_deletion(ht, value):
    if len(value) != 3:
        print("Invalid Entry!")
        return
    x = h_function(value[0])
    y = h_function(value[1])
    z = h_function(value[2])
    if ht[x][y][z] != []:
        ht[x][y][z].pop()
    else:
        print("Already Empty!")
    return

def h_search(ht, value):
    if len(value) != 3:
        print("Invalid Entry!")
        return
    x = h_function(value[0])
    y = h_function(value[1])
    z = h_function(value[2])
    if ht[x][y][z] != []:
        return ht[x][y][z][0]
    else:
        return "Empty!"

def main():
    ht = h_table()
    fv = open("sample_words.txt", "r")
    lines = fv.readlines()
    #load hash table using txt file
    for line in lines:
        x = line.strip().split("-")
        h_insertion(ht, x[0], x[1])
    fv.close()

    #new insert 
    h_insertion(ht, "tar", "a dark, thick, flammable liquid distilled from wood or coal, consisting of a mixture of hydrocarbons, resins, alcohols, and other compounds. It is used in roadmaking and for coating and preserving timber")
    #search new insert (returns definition)
    print(h_search(ht, "tar"))
    #insert new insert again (returns already filled)
    h_insertion(ht, "tar", "a dark, thick, flammable liquid distilled from wood or coal, consisting of a mixture of hydrocarbons, resins, alcohols, and other compounds. It is used in roadmaking and for coating and preserving timber")
    
    #delete 
    h_deletion(ht, "tar")
    #search post deletion (returns empty)
    print(h_search(ht, "tar"))
    #delete when already empty (returns already empty)
    h_deletion(ht, "tar")
    
    #search word from txt file (returns definition)
    print(h_search(ht, "sly"))

    #insert invalid word (returns invalid entry)
    h_insertion(ht, "bdhjdsb", "gibberish")

    #show h_table data structure (26^3 entries)
    print(ht)

if __name__ == "__main__":
    main()