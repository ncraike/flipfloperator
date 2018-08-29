
With this module, you can write the equivalent of this Ruby code:

```ruby
l = []
(1..20).each do |x|
    l.push(x) if (x == 5) .. (x == 10)
end
l == [5, 6, 7, 8, 9, 10]
```

...like this in Python:

```python
from flipfloperator import PowerSyntax as _

l = []
for x in range(1, 20):
    if _(x == 5) ** (x == 10): l.append(x)
l == [5, 6, 7, 8, 9, 10]
```

...or alternatively like this

```python
from flipfloperator import SliceSyntax as _

l = []
for x in range(1, 20):
    if _[x == 5 :: x == 10]: l.append(x)
l == [5, 6, 7, 8, 9, 10]
```
