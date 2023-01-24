import spacy
nlp = spacy.load('en_core_web_md')

hulk = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."
hulk_nlp = nlp(hulk)


def what_movie():
    print(f"\nThe movie most similar to the one you have just watched, Planet Hulk, is:\n")
    # movies will be stored in list as a tuple then converted to a dict to allow for easier indexing later
    movie_list = []
    with open('movies.txt', 'r') as file:
        for lines in file.readlines():
            line = lines.strip().split(' :')
            movie = line[0]
            desc = line[1]
            movie_list.append((movie, desc))
    
    movie_dict = dict(movie_list)
    
    # each similarity figure will be stored in a list so a max calculation can be executed
    similarities = []
    for values in movie_dict.values():
        similarity = nlp(values).similarity(hulk_nlp)
        similarities.append(similarity)
        # keeping this calculation in the for loop so for each iteration if a higher number is found, the value can be overridden
        highest_sim = max(similarities)
    
    # now matching the individual similarity to the max value so we can identify the tuple
    for values in movie_dict.values():
        similarity = nlp(values).similarity(hulk_nlp)
        if similarity == highest_sim:
            # using the keys to find the value which matches with above
            for keys in movie_dict.keys():
                if movie_dict[keys] == values:
                    print(f"{keys}: {values}")
                    print(f"\nThis movie has a similarity score of: {highest_sim}")
            

what_movie()