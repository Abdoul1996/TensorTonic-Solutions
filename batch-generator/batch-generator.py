import numpy as np

def batch_generator(X: list, y: list, batch_size: int, seed: int = 42, drop_last: bool = False):
    """
    Returns a generator of (X_batch, y_batch) tuples.
    """
    # Write code here
    # step 1: convert input to numpy arrays 
    X = np.asarray(X)
    y = np.asarray(y)

    # Step 2: Get the number of samples
    N = len(X)

    # step 3: Generate and shuffle indices 
    indices = np.arange(N)
    rng = np.random.default_rng(seed)
    rng.shuffle(indices)

    # Step 4: Apply shuffled indices to X and y
    X_shuffle = X[indices]
    y_shuffle = y[indices]

    # Step 5: Create mini-batches
    for start in range(0,N,batch_size):
      end = start + batch_size
      
      if drop_last == True and end > N:
        break

      X_batch = X_shuffle[start:end]
      y_batch = y_shuffle[start:end]

      yield X_batch,y_batch
          