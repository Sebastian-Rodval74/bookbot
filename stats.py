def count_words(text):
    count = 0
    words = text.split()
    for word in words:
        count += 1
    return count
def each_character(text):
    new = {}
    for i in text:
        i = i.lower()
        if i in new:
            new[i] += 1
        else:
            new[i] = 1
    sorted_characters = sorted(new.items(), key=lambda x: x[1], reverse=True)
    output = "\n".join([f"{char}: {count}" for char, count in sorted_characters])
    return output

            

