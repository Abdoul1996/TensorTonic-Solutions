Problem:

Given two PyTorch float32 tensors and an operation name, compute the selected result. The operations add, multiply, power, and max mean element-wise addition, multiplication, first input raised to the second input, and maximum. These operations follow PyTorch broadcasting rules. The matmul operation means matrix multiplication. Return the result as a float32 PyTorch tensor with the shape determined by the operation.



Break Down:



Operation:

- torch.add(x,y)
- torch.mul(x,y)
- torch.matmul(x,y)
- torch.pow(x,y)
- torch.max(x,y)





example: 

Input: x = [1, 2, 3], y = [4, 5, 6], op = "add"



if op == 'add':

   torch.add(x,y)



x = [1,2,3] 

y = [4,5,6]

x + y = (1+4), (2+5), (3+6) = 5, 7, 9



Output: [5.0, 7.0, 9.0]

Explanation: Each output is the sum of the values at the same position.