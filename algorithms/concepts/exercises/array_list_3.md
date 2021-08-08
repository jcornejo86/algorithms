# Problem

Suppose you’re building an app for restaurants to take customer orders.

Your app needs to store a list of orders. Servers keep adding orders to this list, and chefs take orders off the list and make them.
It’s an order queue: servers add orders to the back of the queue, and the chef takes the first order off the queue and cooks it.

Would you use an array or a linked list to implement this queue?

# Solution

I would use a linked list.

# Explanation

Since servers will be inserting a lot of order, I would prioritize the insertion operation.

Reading must be sequential, so lists are a perfect fit.
