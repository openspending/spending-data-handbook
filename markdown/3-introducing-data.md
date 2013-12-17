# Introducing data

In the previous section of the Handbook, you learned about the data-driven research workflow. Now you're probably eager to start answering the big questions about spending using data.

But what do we mean by "spending data", anyway? Is spending data the only kind of data you need in order to investigate spending? And what's the difference between "data" and other ways of presenting information?

This section of the Handbook answers these important questions by explaining the ins and outs of spending data itself. It contains the following chapters:

* [*Types of spending data*](../types-of-spending-data/). The difference between *budgets* and proper *spending data*, and the different kinds of investigations that each is useful for.
* [*Reference data*](../reference-data/). Other kinds of datasets that are useful for specific kinds of investigations.
* [*Machine-readable and useable data*](../machine-readable-data/). What makes an informative file "data", and what you should ask for when requesting data from governments or other sources.
With these lessons in hand, you'll be ready to move on to the next section of the Handbook, where we learn how to find, process, and analyse spending data.
 
But there's a big question we need to address before we get to all that, namely...

## What is data?

Data is all around us. But what exactly is it?

Data is a value assigned to a thing. Consider, for example, the balls in the picture below.

![Golf balls at a market (CC) by Kaptain Kobold on Flickr.](http://farm9.staticflickr.com/8301/7871270682_ded37461a0_o_d.jpg)

What can we say about these? They're golf balls, right? So one of the first data points we have is that they are used for golf. Golf is a category of sport, so this helps us to put the ball in a taxonomy. But there is more to them. We have their colour (white) and their condition (used). They all have a size, there is a certain number of them, they each have some monetary value, and so on.

Even unremarkable objects have a lot of data attached to them. You do, too: you have a name (most people have given and family names), a date of birth, weight, height, nationality, and so on. All these things are data.

In the example above, we can already see that there are different types of data. The two major categories are *qualitative* and *quantitative* data.

*Qualitative data* is everything that refers to the quality of something: a description of colours, the texture and feel of an object, a description of experiences, and an interview are all qualitative data.

*Quantitative data* is data that refers to a number, e.g. the number of golf balls, the size, the price, a score on a test, etc.

There are also other categories that you will most likely encounter:

*Categorical data* puts the item you are describing into a category. In our example, the condition "used" would be categorical (with other categories such as "new", "used", "broken", etc.)

*Discrete data* is numerical data that has gaps in it, e.g. the count of golf balls. There can only be whole numbers of golf ball (there is no such thing as 0.3 golf balls). Other examples are scores in tests (where you might receive, for example, 7/10) or shoe sizes.

*Continuous data* is numerical data with a continuous range. The size of the golfballs, for example, can be any value (e.q. 10.53mm or 10.54mm but also 10.536mm), as can the size of your foot (as opposed to your shoe size, which is discrete).

### Unstructured vs. Structured data

#### Data for Humans

A plain sentence – “we have 5 white used golf balls with a diameter of 43mm at 50 cents each” – might be easy for a human to understand, but for a computer, it is very difficult. The above sentence is what we call *unstructured data*. Unstructured data has no transparent underlying structure—it's impossible to mechanically figure out exactly what refers to what. Likewise, PDFs and scanned images may contain information which is pleasing to the human eye as it is laid-out nicely, but they are not *machine-readable* or *structured* presentations of data.

#### Data for Computers

Computers are inherently different from humans. It can be exceptionally hard to make computers extract information from certain sources. Some tasks that humans find easy are still difficult to automate. For example, interpreting text that is presented as an image is still a challenge for a computer.

If you want your computer to process and analyse your data, it has to be able to read and process it. This means it needs to be *structured* and *machine-readable*. We'll explain more about what this means in [a later chapter](../machine-readable-data/).

One of the most commonly used formats for exchanging data is CSV, which stands for "comma separated values". If we wanted to express the information in the sentence in the previous section in CSV form, it might look like this:

    “quantity”, “color”, “condition”, “item”, “category”, “diameter (mm)”, “price per unit (AUD)”
    5,”white”,”used”,”ball”,”golf”,43,0.5

Data formatted like this is *tabular data*, data which forms a table consisting of rows and columns. Think of each line in the CSV as a *row*, and think of each part of a line separated by a comma as part of a *column*. Each row represents a single data item, and each column represents a property—the only exception is the first row, which gives the names of the columns.

This is way simpler for your computer to understand and can be read directly by spreadsheet software. Tabular data is probably the commonest machine-readable data format you will encounter. But there are many other machine-readable formats out there. To learn more about data file formats, machine-readable and otherwise, check out the [file formats chapter](http://opendatahandbook.org/en/appendices/file-formats.html) of the [Open Data Handbook](http://opendatahandbook.org/en/appendices/file-formats.html).