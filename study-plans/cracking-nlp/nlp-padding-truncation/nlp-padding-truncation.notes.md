Problem:

Give every integer sequence the requested maximum length. Keep its first max_length values when it is too long; append pad_value on the right when it is too short. A sequence already at the target length keeps all its values. Preserve the batch order and leave the input lists unchanged.



Return a Python list of integer lists, with one row per input sequence and exactly max_length entries per row. An empty batch returns an empty list.







Input: sequences = [[1, 2, 3], [4, 5], [6, 7, 8, 9]], max_length = 3, pad_value = 0

Output: [[1, 2, 3], [4, 5, 0], [6, 7, 8]]

Explanation: The first row stays unchanged, the second gains a zero, and the third loses its final value.

Breakdown:

Conditions:

`len(seq) &lt; max_length`

- Add padding

`len(seq) &gt; max_length`

- Truncate

`len(seq) == max_length`

- Keep unchanged