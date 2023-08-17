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
There is a lot of “hidden” information in this problem. Or more accurately, there is a lot of information hidden in plain sight. 
Initially this dialogue may seem impossible since the numbers could be any two numbers in the range of $2$ to $800$ inclusive, and neither of Polly or Sam have a clue what the numbers are. 
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
This means that the pair $(x,y)$ is the same as $(y,x)$. With this knowledge, almost half of the 638401 possible pairs are redundant so we can get rid of them. 
<br>
For $x=2$, $y$ can be in the range $2≤y≤800 ⇒799$ pairs $(x,y)$
<br>
For $x=3$, $y$ can be in the range $3≤y≤800 ⇒798$ pairs $(x,y)$
<br>
For $x=4$, $y$ can be in the range $4≤y≤800 ⇒797$ pairs $(x,y)$, and so on...
<br>
This is $799+798+797+⋯+1=\dfrac{799+1}{2}\cdot799=400\cdot799=319600$ possible pairs remaining. 
<br>
<br>

### Polly does not know the two numbers
Now Polly says: “_I don’t know the two numbers._”
This tells us two things things:
1. Both numbers cannot be prime numbers
2. The two numbers cannot be a prime number and that prime number squared

#### Both numbers cannot be prime numbers
If both numbers were prime numbers then Polly would immediately know the two numbers, since this would be the only way to split the product Polly was told into factors. For example, if Polly is told that the product is $35$, then she immediately knows that the two numbers are $5$ and $7$. But she doesn't know the two numbers, so with this information we can eliminate all the pairs $(x,y)$ where both $x$ and $y$ are prime numbers.
There are $139$ prime numbers, $p$, in the range $2≤p≤800$. This means that we have $139+138+137+⋯+1=\dfrac{139+1}{2}\cdot139=9730$ pairs that are two prime numbers. We can eliminate all of those.
<br>
Now that we can eliminate $9730$ pairs, we have $309870$ remaining possible pairs.

#### The two numbers cannot be a prime number and that prime number squared
If $p$ is that prime number, then Polly would be told that the product is $p^3$. If so the two numbers can only be either $(p,p^2)$ or $(p^2,p)$. These are the only two ways you can split up $p^3$ into factors and having the two numbers in the range $[2,800]$. We have already eliminated $(p^2,p)$ since the order doesn’t matter due to the commutative properties of multiplication and addition. So, if Polly is given a product that is a prime number to the power of three, then she immediately knows that the two numbers are $p$ and $p^2$. Since she doesn’t know the two numbers we can now also eliminate all pairs $(p,p^2)$, where $p$ is a prime number and both $p$ and $p^2$ are in the range $[0,800]$.
<br>
This will eliminate $9$ pairs. Now we have $309861$ possible pairs remaining.
<br>
<br>

### Sam knows that Polly doesn't know the two numbers
Next Sam says: “_I know…_” in response to Polly's statement: “_I don’t know the two numbers._”
<br>
Now, if Sam knows that Polly doesn't know the two numbers, then the sum that Sam is told can't be any number. For some sums Sam can't be sure that Polly doesn't know the two numbers. But since he knows that Polly doesn't know the two numbers, then it tells us two things about the sum:
1. The sum cannot be a sum of two prime numbers
2. The sum of the pair cannot be greater than 401

#### The sum cannot be a sum of two prime numbers
The sum cannot be a number that could be created by adding two prime numbers. Otherwise, Sam couldn’t know for sure that Polly didn’t know the two numbers. This means that the sum cannot be even. Goldbach's conjecture says that every even integer greater than $2$ can be written as the sum of two primes. While the conjecture is not proven it is known to be true for even integers up to $10^{18}$, which is way more than $800$. By this we can now also eliminate every pair $(x,y)$ that produces an even sum $x+y$. Because if the sum is even, then Sam cannot know for sure that Polly didn’t know the two numbers.
<br>
We can now eliminate another $150399$ pairs. This leaves us with $159462$ possible remaining pairs.

In addition to eliminating the pairs due to their sum being even, there are some odd sums that also can be eliminated for the same reason. $2$ is also a prime number. If the sum is a number that is a prime number plus $2$, then the two numbers could possibly be that prime number and $2$, which means that Polly from her product would know the two numbers. But since Sam knows from his sum that Polly doesn’t know the two numbers, then the sum cannot be a prime number plus $2$. With this we can eliminate all the pairs that has a sum that is $p+2$, where $p$ is a prime number.
<br>
This will eliminate $24831$ pairs. We now have $134631$ remaining possible pairs.

#### The sum of the pair cannot be greater than 401
If $(x,y)$ is the pair, then $x+y≤401$.
<br>
The reason for this is that $401$ is a prime number and $401$ is greater than $\dfrac{800}{2}=400$. We have already excluded all the even sums due to Goldbach’s conjecture. Now we can also exclude all the odd sums above 401. If the sum was $403$ then it could be the numbers $401$ and $2$, which is already excluded in prime number plus $2$ above. If the sum is $405$, then the two numbers could be $401$ and $4$. If Polly is told that the product is $1604$, then she immediately knows that the two numbers are $401$ and $4$. The prime factors of $1604$ are $2$, $2$, and $401$. But since the two numbers have to be within $2$ and $800$, then they can’t be $2$ and $802$. So, from the product $1604$ Polly would immediately know that the two numbers are $4$ and $401$. If $401$ is a factor in the product told to Polly, then the only way to split the factors into two numbers is that $401$ by one of the numbers and the remaining factors be the other number. Otherwise, the numbers will not be in the range $[2,800]$. Now, every odd sum above $401$ can be created as $401+2n$, where $n∈N$, $n≥1$. If Polly is told that the product is $401\cdot2\cdot n$, then she immediately knows that the two numbers are $2n$ and $401$. If you move any factor from $2n$ over to $401$, then it would exceed $800$, which is out of the range. Since a pair with an odd sum greater than $401$ can be created as $(2n,401)$, then every odd sum greater than $401$ could potentially be the sum of $401$ and $2n$, which means that Sam cannot be sure that Polly doesn’t know the two numbers. This now means that we can eliminate all the pairs which have a sum greater than $401$.
<br>
With this step we can eliminate $121635$ pairs. We have $12996$ remaining possible pairs.
<br>
<br>

### Sam does not know the two numbers
After Sam has claimed that he knows that Polly doesn't know the two numbers he goes on saying: “_…and neither do I_”
<br>
That Sam doesn’t know the two numbers doesn’t actually give us any further information that we can use to eliminate any pairs. The only possibility that Sam would know the two numbers from the sum is if there are pairs that produce a sum that can only be produced by that specific pair of the remaining pairs. However, none of the sums produced by any of the remaining pairs can uniquely be produced by a single pair. Any sum that Sam has been given can be produced by more than one of the remaining pairs. This means that we cannot eliminate any pair from this information.
<br>
No pairs were eliminated by this information.
<br>
<br>

### Polly now knows the two numbers
Polly now says: “_I know the two numbers_”
<br>
This means that the product that Polly has been given can only be created in one way from the remaining possible pairs. We can therefore eliminate all pairs that have the same product as some other remaining pair.
<br>
With this information we can eliminate $8525$ pairs. We now have $4471$ possible pairs remaining.
<br>
<br>

### Sam also now knows the two numbers
Now Sam says: “_So do I_”
<br>
This means in the same way that Sam must have been given a sum that can only be created in one way from the remaining pairs. We can eliminate all pairs that have the same sum as some other pair. Otherwise he couldn't know for sure which pair would be correct.
<br>
With this step we can eliminate $4470$ pairs. We have only $1$ possible pair remaining. 
<br>
<br>

### We know the two numbers
Since we only have one possible pair left, it means that also we, from their conversation, know what the two number are!
<br>
**Far Out!!!**

That remaining pair is the solution!

<br>
<br>

## The Python Program
The Python program, `polly_n_sam.py` follows the steps above eliminating  pairs with each piece of information. The code is not optimized for speed, memory usage, or number of lines. Instead, it is created to clearly illustrate how the information in each piece of the conversation can be used to eliminate some pairs. This also makes it possible to analyze each piece of information and the effect it has more thoroughly for the curious one.
<br>
The program will at the end print out the solution, the only remaining pair, which are the two numbers we are looking for.

<br>
<br>

## If you want to try this at home
There is no danger in trying this at home. If someone wants to try this on his/her own, here is a similar "impossible" problem:

Calle Johansson and Leif Persson are visited by their very good friend Professor Gunnar Haxell. Professor Haxell, having thought of two natural numbers, says that he will tell Calle the sum of the numbers and Leif the sum of the squares of the numbers. He then whispers the sum of the numbers to Calle so no one else can hear and then the sum of the squares of the numbers to Leif so no one else can hear. Then the following conversation takes place:
<br>
**Leif**:	“_I don’t know the numbers_”
<br>
**Calle**:	“_I don’t know the numbers_”
<br>
**Leif**:	“_I don’t know the numbers_”
<br>
**Calle**:	“_I don’t know the numbers_”
<br>
**Leif**:	“_I don’t know the numbers_”
<br>
**Calle**:	“_I don’t know the numbers_”
<br>
**Leif**:	“_I know the numbers!_”
<br>
**Calle**:	“_Men att seså seså, det har jag aldrig hört förut!_”

What are the two natural numbers?

Enjoy!

