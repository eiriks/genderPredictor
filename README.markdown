# genderPredictor #
GenderPredictor is a wrapper around [NLTK](http://www.nltk.org/)'s [Naive Bayes](http://en.wikipedia.org/wiki/Naive_Bayes_classifier) classifier for predicting the gender given a name.

This problem is common when dealing with incomplete contact information for users.

Currently it appears to be about 82% accurate on American names but this is just the framework.
The name files are from the [US Social Security Administration](http://www.ssa.gov/oact/babynames/limits.html) and are likely in the public domain. The processed files are distributed under the same rules as the original data (which is likely public domain...).

The code is under the [Apache 2.0](http://www.apache.org/licenses/LICENSE-2.0) license.

Comments and suggestions are welcome at [stephen.holiday@gmail.com](mailto:stephen.holiday@gmail.com),

Stephen Holiday
[stephenholiday.com](http://stephenholiday.com)



### Hva med norske navn?

Test om denne metoden funker på Norske navn:


Med amerikans treningsdata klarer metoden 
- Kvinner: 68 av 100 (av 100 vanligste norske)
- Menn: 85 av 100 (av 100 vanligste norske)
Trening & test:
- 32031 male names loaded, 56347 female names loaded
- Accuracy: 0.807932


Med SSB data fra siste 10 år klarer metoden
- Kvinner: 67 av 100 (av 100 vanligste norske)
- Menn: 90 av 100 (av 100 vanligste norske)

Trening & test:
- 538 male names loaded, 584 female names loaded
- Accuracy: 0.808889



####Status: de features som hentes ut som betydningsfulle er ikke veldig gode. 

####Tiltak: bruk ordlister (lookup) på navn som ikke brukes på begge kjønn først
        så bruk eventuellt denne metoden på "røkla"...