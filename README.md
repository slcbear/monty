# A no-frills Monty Hall simulation

This unlikely scenario takes place in a magical land known as mid-20th century America. Contestants are
chosen from the audience based on the outlandishness of their costumes, their camera-readiness and their 
ability to project emotions such as "enthusiasm" and "disappointment"—so, basically any average American.

Finding themselves onstage, each contestant is confronted by Monty Hall, a genial, unemotional man wearing 
a nice suit. This presents each contestant with a humiliating moment of self-awareness, but before they can
think about that for very long, Monty Hall instructs them to choose one of three doors. One of the doors 
conceals a desirable commodity such as a car, while behind both of the other two doors is an goat, innocently 
chewing its cud, and it didn't ask to be placed in such a situation; in fact, none of this is the goat's fault
and previous versions of the show in which the goat was sacrificed to Baal did not test well with audiences.

Nevertheless, there is a goat[<sup>1</sup>](#numgoat). If the contestant chooses the goat, the contestant loses. It seems important
to point out that the goat is unaffected by the choice—in any case, it remains a goat, and has very little 
to say about any of this.

The contestant chooses what's behind either Door No. 1, Door No. 2, or Door No. 3 and announces their choice 
in front of witnesses, including Monty Hall and the audience.

At this point, Monty Hall, looking cool and unruffled in plaid-pattern polyster, opens one of the unchosen doors, 
a trombone sounds a derisive descending note, and a goat stands there looking moderately surprised[<sup>2</sup>](#montychoice). 
<em>It is not the goat's fault.</em>

Monty Hall then gives the contestant a choice of switching to the remaining door. Intuitively, we might assume that 
this is of no consequence, and that the contestant has the same chance of winning whether they switch or not, but 
in fact, for reasons our brains seem ill-equipped to understand, should the contestant switch, they double their
chances of winning.

Here, "prizes" and "winnings" are valued according to one mid-20th century utility scheme 
in which a "car" was a win, and a "goat" was a loss[<sup>3</sup>](#goatnote). 

| Car | Goat |
| --- | ---- |
| 1 | 0 |

The surprising thing and the whole point of this is that
when ``` switch_strategy == True ``` the expected win
is twice that as in the alternative.  

| Switch Strategy | Expected Win |
| --------------- | ------------ |
| True | 2/3 | 
| False | 1/3 |


***


### Goatnotes:

<span id="numgoat">1</span>: In fact, recall that there are two goats: One each behind either of the two doors not concealing a car.

<span id="montychoice">2</span>: It may seem to a casual viewer—and there are seldom any other kind—that Monty Hall makes this choice
  freely, but if we consider that he is always going to reveal a goat, the only time he has a choice is when the contestant
  chooses the car, leaving two goats unchosen. Otherwise, he is obligated to open one and only door: The one that has
  The Goat Not Chosen[<sup>4</sup>](#poem).

<span id="goatnote">3</span>: This is misleading and unfair to goats, as they certainly have worth and 
  indeed are among the most charming, inquisitive and affectionate of the farm animals. 
  (The pigs get all the attention at the State Fair, but let's face it: Pigs are scary and smell bad.
  Goats are clean and smell nice, and will butt you playfully when you're not looking.)

  Many situations are possible, in fact, in which a goat is the better prize.

<span id="poem">4</span>: *Two goats diverged in the woods, and I,  
  I took the goat less traveled by,  
  And that has made all the difference.*  

  --(From *The Goat Not Taken*, not by Robert Frost) 
 
  #### Goats Are Cool, Cars Drool
