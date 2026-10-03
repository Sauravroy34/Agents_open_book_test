=== PROBLEM 1 START ===
Let $x_1, \ldots, x_{2024}$ be positive real numbers such that $x_{i+1} \ge 2x_i$ for $i = 1,\ldots, 2023$. Find the maximal possible value of
\[
    \sum_{i=1}^{2023} \frac{x_{i} - x_{i-1}}{x_{i+1} - x_i}
\]
where $x_0 = 0$.
=== PROBLEM 1 END ===

=== PROBLEM 2 START ===
Let $P$ be a regular $199$-gon. Assign integers between $1$ and $199$ to the vertices of $P$ such that each integer appears exactly once (If two assignments coincide under rotation, treat them as the same). An operation is a swap of the integers assigned to a pair of adjacent vertices of $P$. Find the smallest integer $n$ such that one can achieve every other assignment from a given one with no more than $n$ operations.
=== PROBLEM 2 END ===

=== PROBLEM 3 START ===
Let $l$ and $m$ be parallel lines with $100$ distinct points marked on $l$ and $100$ distinct points marked on $m$. Find the greatest possible number of acute-angled triangles all of whose vertices are marked.
=== PROBLEM 3 END ===

=== PROBLEM 4 START ===
We are given the function $f:\mathbb{N}\rightarrow \mathbb{N}$.

$f(n)$ is the number obtained by moving the units digit of $n$ to the front.
Find all positive integers $n$ such that $f^{-1}(f(n)^2)=n^2$.
=== PROBLEM 4 END ===

=== PROBLEM 5 START ===
For a positive integer $n$, we call $g:\mathbb{Z}\rightarrow \mathbb{Z}$ a \textif{$n$-good function} if $g(1)=1$ and for any two distinct integers $a$ and $b$, $g(a)-g(b)$ divides $a^n -b^n$. We call a positive integer $n$ an \textit{exotic integer} if the number of $n$-good functions is twice of an odd integer. Find $132$th exotic integer.
=== PROBLEM 5 END ===

=== PROBLEM 6 START ===
You have entered a quiz competition. A positive integer $F \ge 2$ is given, and the competition starts with a number $S$ provided by the organizers. In each turn, you look at the number most recently provided by the organizers and choose a divisor or multiple other than 1 to submit. The organizers will then add or subtract 1 from the number you submitted and present it back to you. You win if you reach $F$ within $50$ turns. Find the $50th$ smallest value of $F$ for which you can succeed regardless of the initial number $S$.
=== PROBLEM 6 END ===

=== PROBLEM 7 START ===
Suppose there are $40$ professional baseball teams participating in a tournament. In each round of the game, we will divide the $40$ teams into $20$ pairs, and each pair plays the game at the same time. After the tournament, it is known that every two teams have played at most one game. Find the smallest positive integer $a$, so that we can arrange a schedule satisfying the above conditions, and if we take one more round, there is always a pair of teams who have played in the game.
=== PROBLEM 7 END ===

=== PROBLEM 8 START ===
Let $PQRS$ be an isosceles trapezoid with $PS=QR$ and $PQ<RS.$ Suppose that the distances from $P$ to the lines $QR,RS,$ and $QS$ are $15,18,$ and $10,$ respectively. Let $A$ be the area of $PQRS.$ Find $\sqrt2 \cdot A.$
=== PROBLEM 8 END ===

=== PROBLEM 9 START ===
Find all triples $(n,x,y)$ where $n\ge 2$ is a positive integer and $x,y$ are rational numbers such that
\[
    (x - \sqrt{2})^n = y - \sqrt{2}.
\]
=== PROBLEM 9 END ===

=== PROBLEM 10 START ===
Find all functions $X: \mathbb{C} \rightarrow \mathbb{C}$ such that the equation
$$X(X(a)+b X(b)-b-1)=1+a+|b|^{2}$$
holds for all complex numbers $a,b\in \mathbb{C}$ and that $X(1)=u$ for some $u\in \mathbb{C}$ such that $|u-1|=1$.
=== PROBLEM 10 END ===

=== PROBLEM 11 START ===
Let $A$ be the set of odd integers $a$ such that $|a|$ is not a perfect square.

Find all numbers that can be expressed as $x+y+z$ for $x, y, z \in A$ such that $xyz$ is a perfect square.
=== PROBLEM 11 END ===

=== PROBLEM 12 START ===
Define two sequences $\{a_n\}$ and $\{b_n\}$ as follows:
\[
\begin{array}{lll}
    a_1 = 6, &a_2 = 217, &a_{n}a_{n+2}-1 = a_{n+1}^3 \quad(n \geq 1), \\
    b_1 = 1, &b_2 = 1, & b_{n+2} = b_{n+1} + b_n \quad(n \geq 1).
\end{array}
\]
Find all positive integers $n$ such that $a_{n+2} \cdot 42^{b_{2n}}$ is an integer.
=== PROBLEM 12 END ===

=== PROBLEM 13 START ===
The Bank of Berlin issues coins made out of two types of metal: aluminium (denoted $A$ ) and copper (denoted $C$ ). Sophia has $255$ aluminium coins, and $255$ copper coins, and arranges her $510$ coins in a row in some arbitrary initial order.  Given a fixed positive integer $k \leqslant 510$, she repeatedly performs the following operation: identify the largest subsequence containing the $k$-th coin from the left which consists of consecutive coins made of the same metal, and move all coins in that subsequence to the left end of the row. For example, if there are $4$ aluminum coins and $4$ copper coins and $k=4$, the process starting from the configuration $A A C C C A C A$ would be

\[
A A C C C A C A \rightarrow C C C A A A C A \rightarrow A A A C C C C A \rightarrow C C C C A A A A \rightarrow \cdots
\]

In addition to aluminium and copper coins, Sophia also has a few silver coins that she keeps separate from her aluminium and copper coins.

Let $a$ and $b$ be the smallest and largest positive integer $k$ with $1 \leqslant k \leqslant 510$ such that for every initial configuration, at some point of the process there will be at most one aluminium coin adjacent to a copper coin. Find the product $ab$.
=== PROBLEM 13 END ===

=== PROBLEM 14 START ===
Suppose that the polynomials $f(x)$ and $g(x)$ with integer coefficients satisfy the following conditions:

[Condition 1] Define integer sequences $(a_n)_{n \ge 1}$ and $(b_n)_{n \ge 1}$ by $a_1 = 2024$ and
\[
    b_n = f(a_n), \quad a_{n+1} = g(b_n)
\]
for $n \ge 1$. Then for any positive integer $k$, there exists some non-zero term of $(a_n)$ or $(b_n)$ that is divisible by $k$.

[Condition 2] $2025\le f(0), g(0) \le 10000$.

Find the maximum possible value of $f(0)-g(0)$
=== PROBLEM 14 END ===

=== PROBLEM 15 START ===
Find all $P:\mathbb{R}\rightarrow \mathbb{R}$ such that $P$ is not identically zero and there exists $Q:\mathbb{R}\rightarrow \mathbb{R}$ satisfying

\[
Q(P(a))-P(b)=(b+a)Q(2a-2b)
\]

for all real numbers $a,b$.
=== PROBLEM 15 END ===

=== PROBLEM 16 START ===
Let $x, y, z$ be nonnegative real numbers with
\[
    (x^3 - 3x^2 + 3x) + (y^3 - 3y^2 + 3y) + (z^3 - 3z^2 + 3z) = 4.
\]
Find the maximal value of
\[
    x^2 + y^2 + z^2 - x - y - z.
\]
=== PROBLEM 16 END ===

=== PROBLEM 17 START ===
Find all monic polynomials $P(x)$ with integer coefficients for which
\[
    \frac{6(|P(q)|!) - 1}{q}
\]
is an integer for every prime $q$ greater than 3.
=== PROBLEM 17 END ===

=== PROBLEM 18 START ===
Given a positive integer $n$, there exists an integer $a$ such that the sequence $\{a_k\}$ defined by $a_0 = a$ and $a_k = \frac{a_{k-1}}{k} + k^{n-1}$ consists only of integers. Find the possible values of the remainder when $n$ is divided by 3.
=== PROBLEM 18 END ===

=== PROBLEM 19 START ===
Find the smallest positive integer $n$ such that there exist real numbers $\theta_1, \ldots, \theta_n$ satisfying
\[
    \sum_{i=1}^n \sin\theta_i = 0, \quad \sum_{i=1}^n \cos^2 \theta_i = n - 2025.
\]
=== PROBLEM 19 END ===

=== PROBLEM 20 START ===
A group of students are playing a coin-flipping game. They have 64 coins lined up on a table, each showing either heads or tails. They take turns performing the following operation: if there are $k$ coins showing heads and $k>0$, then they flip the $k^{\text {th }}$ coin over; otherwise, they stop the game.  For example, if they start with the configuration $T H T$, the game would proceed as follows: $T H T \rightarrow H H T \rightarrow H T T \rightarrow T T T$, which takes three turns.  They define a strange mathematical function $f(x)= 2x+10$ to add irrelevance to the problem.

Letting $C$ denote the initial configuration (a sequence of 64 H's and T's), write $\ell(C)$ for the number of turns needed before all coins show T. Show that this number $\ell(C)$ is finite, and determine its average value over all $2^{64}$ possible initial configurations $C$.
=== PROBLEM 20 END ===
