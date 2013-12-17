# Machine-readable and useable data

Not all spending datasets are equally useful. At its best, spending data is available in a *machine-readable* form that can easily be automatically processed, but far too often it is only available as an unstructured document that can only be processed by hard manual labour. Spending data is also ideally consistent, error-free, and straightforwardly interpretable, but it often falls far short of this standard.

This chapter provides a quick overview of the concept of machine-readability and its importance to data-driven research. It also explains useful criteria of data useability that you should keep in mind when requesting data.

## Machine-readable data

When we speak about "data", what we usually mean is [machine-readable data](http://en.wikipedia.org/wiki/Machine-readable_data). Machine-readable data is data which is structured in such a way as to be transparent for computational processing. Machine-readable data can be used with spreadsheet software, statistics software, and custom-written code without any fuss.

Many of the most popular formats for policy papers and spending reports are not machine-readable. Popular formats like PDF, Word documents, and HTML pages do not have a structure that lends itself to automated analysis. They are instead useful for displaying information on a screen or printing it on a page. They make it very difficult – even nearly impossible – to mechanically reconstruct their contents and process them.

Machine-readable file formats have a structure which makes it easy to compute with their contents. Excel spreadsheets and CSV files, for example, have a "tabular" structure which computer programs can recognise and use, allowing you to easily add up columns of numbers, compute statistics, and so on. Other machine-readable formats such as XML documents and JSON files are much more flexible than spreadsheets. They are the glue that connects different systems on the web, allowing databases to work together seamlessly online.

### Why is this so important?

If you ever have to deal with data that is stored in a non-machine-readable format, you will quickly learn why machine readability is crucial. Extracting data from unstructured documents is enormously time-consuming – in fact, it is often the most laborious part of a data-driven research project – and tends to introduce unnecessary errors.

Users of spending data should demand that their governments release it in a machine-readable, transparent form.

## Data useability: what to demand

In the chapter [*Getting data*](../getting-data/) of the next section of the Handbook, we will deal with asking governments for data (or getting it by other means). To set the scene for this and to work out whether your government actually publishes usable data already, have a quick look at the following questions:

* **Is the government's data published in a machine-readable format?** E.g. CSV, XML, JSON. While there is nothing wrong with publishing a PDF to support a data release – in fact, it is often nice to have a nicely formatted document to cross-reference and sanity-check data – it shouldn't be the only thing published. If you are asking for a policy document, ask for the underlying data in a spreadsheet so you can check the numbers.
* **Does the government publish a "data dictionary" to explain the terms used in the dataset?** This should include definitions of column headers, explanations of terms and ranges used within the main body of the data, and explanations of any changes in terminology which have been introduced since last time the dataset was released. See also the preceding chapter on [reference data](../reference-data/).
* **How is the data that is being published *actually used* internally by governments?** Do some sanity checks on the minimum and maximum values of different columns to make sure they fall into the documented ranges and don't seem out of place. Do you see negative values when you don't think you should? Negative values usually mean money owed.
* **Is the structure of the data the same across years? If not, is there a description of how it changes?** It never hurts to contact the publisher and ask questions about the change and why it occurred. The publisher may have their name and contact details on the report or webpage. If there is no named contact, then call the department's enquires number or send a message to their email address asking to meet or discuss the data.
* **How aggregated is the data?** What is the number of real-world financial transactions that are expressed by a single line of the dataset you have? For budgets, this will mostly be hard to tell, but with transactional expenditure, you want to make sure that the data is fairly *disaggregated*. Ideally, each entry represents a transaction—but even if this isn't true, you'll still want to ensure the number is not in the tens or hundreds of thousands (e.g. covering government programmes as a whole).
* **Is there reference data?** If your budget or spending data is augmented with reference data, make sure you have access to it. This might include functional or category codes on budget line items, location codes for describing recipient location, or codes that indicate the status of the record. See [the preceding chapter](../reference-data/) for more details.
* **What guidelines were people given when creating the dataset?** This will make it easier to understand what is included within the data, e.g. whether the numbers are in thousands or millions. 
* **Is the scope of your inquiry narrow enough?** Your chances of success will be higher if you narrow the scope of the data you're requesting from the government and be specific. Government is the de facto keeper of all kinds of data, so parameters that narrow your request are always helpful.