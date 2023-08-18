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

print(Anti_causal);

display(Anti_causal);

% from mid
max_ind = 4;
ind = find(max_ind==x);
Non_Causal = 0;
for i=1:length(x)
    Non_Causal = Non_Causal + x(i)*y^(ind-i);
end

print(Non_Causal);

display(Non_Causal);