# spaCy Semantic Similarity Exploration

This repository contains two programs using spaCy to explore the semantic similarities between texts.

## semantic.py

This program demonstrates the use of the `en_core_web_md` spaCy model to find the semantic similarities between different words and phrases. The program calculates the similarity between different pairs of words and prints the results to the console. It also prints a matrix of similarity scores for a list of tokens.

The second part of the program discusses the differences between the `en_core_web_md` and `en_core_web_sm` models and their impact on the output.

## watch_next.py

This program reads data from an external text file, `movies.txt`, and uses spaCy's `en_core_web_md` model to find the movie in the file that is most similar to the plot of the movie "Planet Hulk." The program prints the name of the movie with the highest similarity score and the similarity score itself.

The program first reads the `movies.txt` file and stores the movies and descriptions in a dictionary. It then calculates the similarity between each description and the description of the "hulk" movie. The program stores each similarity figure in a list so a max calculation can be executed. It then matches the individual similarity to the max value so it can identify the movie with the highest similarity score. Finally, it prints the movie title and description with the highest similarity score to the console.

## Usage

To run the program, simply execute the script in your preferred Python environment.

## Requirements

This repository requires spaCy version 2.3.2 or higher. Additionally, it requires the spaCy models "en_core_web_md" and "en_core_web_sm".
