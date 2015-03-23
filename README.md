# pygutil

A collection of helpful classes for developing games with [pygame](http://pygame.org). 

## Timer

pygame's `time` module has been wrapped up into a self-contained class that gives applications easy access to elapsed time. Elapsed time is established when the timer is created or when `reset` is called.

## Interpolators

Using the `Timer` class, a set of interpolators run the length of defined ranges in different ways. The following implementations are available.

```
Linear 
f(x) = x

Trigonmetric 
f(x) = sin (x * π / 2)

Logarithmic
f(x) = log10 (1 + (x * 9))
```

## Spritemap

The `Spritemap` helper class bundles the loading of a sprite along with rectangle definitions to give a large sprite map image symbolic meaning. Ad-hoc sprites can be defined along with sets of arbitrarily defined regions as well as regions that are consecutively defined.

