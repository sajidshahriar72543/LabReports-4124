## Experiment No : 05

## Submission Date : June 11, 2023

## Experiment Name :

## Experimental Study of Practical Application of Causal, Non-causal and Anti causal Signals

---

## Theory:

<p style="text-align: justify">
A **causal signal** is a continuous-time signal that is equal to zero for all negative time values. In other words, a causal signal does not exist for negative time. An example of a causal signal is the unit step signal u(t). [1]
</p>
<p style="text-align: justify">
An **anti-causal signal** is a continuous-time signal that is equal to zero for all positive time values. This means that an anti-causal signal does not exist for positive time. An example of an anti-causal signal is the time-reversed unit step signal u(-t). [1]
</p>
<p style="text-align: justify">
A **non-causal signal** is a signal that exists for both positive and negative time values. This means that it is neither causal nor anti-causal. Examples of non-causal signals include sine and cosine signals. [1]
</p>

## Code:
```matlab
% left to right
clc
x = [2 3 4 5 3];
syms p

Causal = 0;
for i=1:length(x)
    Causal = Causal + x(i)*y^(1-i);
end
display(Causal);

% right to left
Anti_causal = 0;
for i=length(x):-1:1
    Anti_causal = Anti_causal + x(i)*y^(length(x)-i);
end
display(Anti_causal);

% from mid
max_ind = 4;
ind = find(max_ind==x);
Non_Causal = 0;
for i=1:length(x)
    Non_Causal = Non_Causal + x(i)*y^(ind-i);
end
display(Non_Causal);
```

## Output:

![Output](src/Picture1.png)

## Discussion and Conclusion:
<p style="text-align: justify">

</p>

## References:
[1] “Signals and Systems Causal Non-Causal and Anti-Causal Signals,” Tutorials Point, [Online]. Available: https://www.tutorialspoint.com/signals-and-systems-causal-non-causal-and-anti-causal-signals. [Accessed: 31-May-2023].