1. Convert X and W to float64 NumPy arrays.

2. Linear transformation:

      Z = X @ W

   Shape:

      (n,d) @ (d,k) → (n,k)

3. Calculate L2 norm for EACH ROW of Z:

      square

      → sum across columns

      → square root

   Result:

      norms.shape = (n,)

4. Create gate:

      norm &gt;= threshold → True/1

      norm &lt; threshold  → False/0

   Result:

      gate.shape = (n,)

5. Reshape/expand gate so it can multiply

   each entire row of Z.

6. Apply gate to Z:

      Y = gate * Z

7. Return Y as float64.

   Y.shape = (n,k)