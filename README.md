# Polly and Sam
<br>

## What are the two numbers?

Polly and Sam are visited by a friend. The friend, having thought of two numbers between 2 and 800 inclusive, whispers their product to Polly and their sum to Sam. The following dialogue takes place:
<br>
**Polly**:     "_I don’t know the two numbers_"
<br>
**Sam**:      "_I know, and neither do I_"
<br>
**Polly**:     "_I know the two numbers_"
<br>
**Sam**:      "_So do I_"
<br>

What are the two numbers?

<br>

## Solution
There is a lot of “hidden” information in this problem. Or more accurately, it is a lot of information hidden in plain sight. 
Initially this dialogue may seem impossible since the numbers could be any two numbers between $2$ and $800$ inclusive, and neither of Polly or Sam have a clue what the numbers are. 
<br>
How could they then suddenly out of the blue know the two numbers?

When we look a bit closer to this problem we will see that there is information we can use to start eliminating some pairs of numbers 
until we finally will find that there is only one possible option. 
We will take this step by step from the information we have:
<br>
<br>

### Initial Condition
We are looking for $2$ numbers, $x$ and $y$, that can each be in the range $[2,800]$. In other words, we are looking for a pair 
$(x,y)$, where $$x,y∈N$$ $$2≤x,y≤800$$
There are $799\cdot799=638401$ possible such pairs of $(x,y)$
<br>
<br>

### Redundant Pairs
We know that Polly knows the product of these numbers and Sam knows the sum of these numbers. Both multiplication and addition are commutative operations. In other words: 
$$x\cdot y=y\cdot x$$
$$x+y=y+x$$
This means that the pair $(x,y)$ is the same as $(y,x)$. With this, almost half of the 638401 possible pairs are redundant so we can get rid of them. 
<br>
For $x=2$, $y$ can be in the range $2≤y≤800 ⇒799$ pairs $(x,y)$
<br>
For $x=3$, $y$ can be in the range $3≤y≤800 ⇒798$ pairs $(x,y)$
<br>
For $x=4$, $y$ can be in the range $4≤y≤800 ⇒797$ pairs $(x,y)$, and so on...
<br>
This is $799+798+797+⋯+1=\frac{799+1}{2}\cdot799=400\cdot799=319600$ possible pairs remaining. 
