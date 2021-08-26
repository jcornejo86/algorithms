# K-Nearest Neighbors

KNN is used for classification and regression and involves looking at the k-nearest neighbors.

**How to calculate the distance between 2 neighbors ?**
Using the Pythagorean formula:
√(x1 - x2)^2 + (y1-y2)^2

The distance formula is flexible: you could have a set of a million numbers and still use the same old distance formula to find the distance.

For example you could calculate the distance across 4 dimensions:
√(x1 - x2)^2 + (y1-y2)^2 + (z1-z2)^2 + (w1-w2)^2

**Another formula to take a look is Cosine similarity**

When you’re working with KNN, it’s really important to pick the right features to compare against. Picking the right features means:
- Features that directly correlate to the thing you’re trying to recommend
- Features that don’t have a bias (for example, if you ask the users to only rate comedy movies, that doesn’t tell you whether they like action movies)

# Regression

Predicting a response (like a number).
**There is obviously a lot more to say about regression. Should be look it up to learn more about it.**

# Recap

- KNN is used for classification and regression and involves looking at the k-nearest neighbors.
- Classification = categorization into a group.
- Regression = predicting a response (like a number).
- Feature extraction means converting an item (like a fruit or a user) into a list of numbers that can be compared.
- Picking good features is an important part of a successful KNN algorithm.
