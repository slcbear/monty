# A no-frills Monty Hall simulation

A recent discussion in the comments section of a [Vsauce2 YouTube video](https://youtu.be/ytfCdqWhmdg) revealed that a lot of people wrote at one time a program to simulate the Monty Hall problem. I did too, when I was studying CompSci in college and first encountered this in a probability course. Of course in those days, everything was different. We had to use CVS for version control, and my favorite scripting language was Perl.  

Nowadays, of course, it's all about Git and Python. But other than that ~~not much has changed~~ *everything* has changed.

### What is this about?

At issue here is a television game show that was watched by many Grandmothers, called *Let's Make a Deal*, and it took place in a magical land known as mid-20th century America. 

Contestants were chosen from the audience based on the outlandishness of their costumes, their camera-readiness and their ability to project emotions such as "enthusiasm" and "disappointment"—so, basically any average American.

Emerging onstage, blinking under the white-hot studio lights, each contestant is confronted by Monty Hall, a genial, unemotional man not dressed, as the contestant was likely to be, as a chicken; but in a polyester suit, considered very swanky at the time. This presented each contestant with a humiliating moment of self-awareness, but before they could
think about that for very long, Monty Hall instructed them to choose one of three doors. 

### Cars vs. Goats

One of the doors concealed a desirable commodity such as a car, while behind both of the other two doors was a goat, innocently 
chewing its cud, and it didn't ask to be placed in such a situation; in fact, none of this is the goat's fault
and previous versions of the show in which the goat was sacrificed to Baal did not test well with audiences.

Nevertheless, there was a goat[<sup>1</sup>](#numgoat). If the contestant chose a goat, the contestant lost. It seems important
to point out that the goat was unaffected by the choice—in any case, it remained a goat, and had very little 
to say about any of this.

The contestant chose what was behind Door No. 1, Door No. 2, or Door No. 3, announcing their choice in front of witnesses, including Monty Hall and the audience.

At that point, Monty Hall, looking cool and unruffled in plaid-pattern polyster, opened one of the unchosen doors, 
as a trombone sounded a derisive descending note, to reveal a goat standing there, moderately surprised[<sup>2</sup>](#montychoice).  

It was not the goat's fault. *It was never the goat's fault.* 

Monty Hall then gave the contestant a choice of switching to the remaining door. Intuitively, we might assume that 
this was of no consequence, and that the contestant had the same chance of winning whether they switched or not, but 
in fact, for reasons our brains seem ill-equipped to understand, if the contestant switched, they doubled their chances of winning.

### A Mid-20th Century Utility Scheme

Here, "prizes" and "winnings" are valued according to one mid-20th century utility scheme in which a "car" was a win, and a "goat" was a loss[<sup>3</sup>](#goatnote). 

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

  Many situations are possible, in fact, in which a goat is the prize much preferable to a car. For instance:

  - Post-apocalyptic hellscape  
  - Amish upbringing  
  - Gas crisis  
  - ... and more!  

<span id="poem">4</span>: *Two goats diverged in the woods, and I,  
  I took the goat less traveled by,  
  And that has made all the difference.*  

  --(From *The Goat Not Taken*, not by Robert Frost) 
 
  #### Goats Are Cool, Cars Drool
