Problem:

Rank models independently within each dataset, with the highest accuracy at rank one. Equal accuracies share both ranks: accuracy_rank leaves gaps after ties, while accuracy_dense_rank uses consecutive ranks without gaps. Model names affect only the final display order, not the assigned ranks.



 Return model_name, dataset, accuracy, accuracy_rank, and accuracy_dense_rank, in that column order, sorted by dataset ascending, accuracy descending, then model_name ascending.



Break Down:

1. 1. Goal: What are we trying to calculate for each model?

1. we are trying to rank their metrics by applying RANK and DENSE_RANK
2. PARTITION BY: Which column should we partition by, and why?

1. I think the column we partition is dataset because we are trying to rank models indepedent within each dataset
3. ORDER BY inside OVER(): Which column determines the ranking, and should it be `ASC` or `DESC`?

1. for RANK we are using accuracy DESC
4. Functions: Why do we need both `RANK()` and `DENSE_RANK()`?

1. The reason we need both ranks we are creating two ranks for each function
5. Final ORDER BY: Why does the problem mention `model_name` even though it shouldn't affect the ranks?

1. im not sure this one