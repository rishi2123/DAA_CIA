CIA 1 Assignment for DAA

An alignment matrix is a two-dimensional table used in bioinformatics to compare two sequences (such as DNA or protein sequences) 
and determine the similarity between them. Each cell in the matrix represents the similarity score between a pair of characters from 
the two sequences, typically calculated using a scoring system such as the Needleman-Wunsch or Smith-Waterman algorithm. The matrix is
used to guide the construction of an optimal alignment, which is a representation of the sequences that highlights their similarities 
and differences.

There are several ways to implement an alignment matrix, but one common approach is to use the Needleman-Wunsch or Smith-Waterman algorithm.

The Smith-Waterman algorithm is used for local alignment, where the goal is to align only the regions of high similarity. The algorithm works
in a similar way to the Needleman-Wunsch algorithm, but instead of starting at the top-left corner, it starts at the cell with the highest score
and traces back through the matrix along the path of highest scores.

