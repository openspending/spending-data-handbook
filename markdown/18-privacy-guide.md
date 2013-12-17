# How to publish spending data without disclosing personal information

This guide is intended to help governments to publish spending data without compromising personal information. It has been drafted with UK local councils and other public authorities who wish to publish transactional spending in accordance with UK regulations but who are concerned about the personal information in their data (such as personal names and addresses).

While we recognise that governmental accounting systems as well as privacy regulations differ vastly across countries, we think this guide provides key practical advice which should to some extent be widely replicable.

## Background

In [January 2013](http://openspending.org/blog/2013/01/09/privacy.html), a freelance data specialist from the OpenSpending community used OpenSpending to identify a number of privacy breaches in an individual dataset published by a local council. This was due to inconsistent redaction of sensitive data by the local authority. While the majority of these payments were to organisations (and hence probably were not highly sensitive), there were also a few unredacted payments to individuals. The person who uploaded the data immediately notified their local council, who in turn referred this to their audit committee. As a precaution, the dataset in question, the UK Local Council £500 spending data, was taken offline immediately. 

Data privacy should never be a valid justification for shutting off access to public spending information, as there should be simple processes in place to prevent private data from being published. As more spending data becomes public, government agencies will have to implement release procedures which prevent privacy breaches. For the financial transparency community, the data privacy issue represents a challenge, as governments might be tempted to use this as a reason for limiting public disclosures. 

## Why are we writing this guide? 

1. we care about [privacy of individual citizens](http://blog.okfn.org/2013/02/22/open-data-my-data/)
2. we care about Open Data: we think it is vital part of making government transparent and accountable
3. the presence of personal data within transactional spending data has been identified as a barrier for making such data available to the public

Privacy concerns have already presented serious obstacles to transparency. For example, in April 2013, the Copenhagen City Council rejected a Freedom of Information request for 1 mi. transactions worth EUR 2.5 bn due to the fact that the data contained personal data which could not be removed without extensive use of personnel resources.

## What are the rules on data privacy and obligations for publishing transactional-level spending data? 

Incidents of privacy breaches highlight the importance of proper procedures to ensure that data from public sector bodies is properly redacted before being published.

The UK government produces a [guideline document for data publishers](http://data.gov.uk/blog/local-spending-data-guidance), which ensures that issues like this are prevented and hence very rare. The Local Governments Association (UK) has published this [guide](http://localnewcontracts.readandcomment.com/appendix-c-inclusions-and-exemptions-for-publishing-data-2/). 

## Understanding the problem

In a broad sense, the law is quite simple: you can’t publish anything that might identify an individual. Complying with the law is less straightforward. It would be nice if we could just search files for for all occurrences of "Mr.", "Mrs.", or "Miss" and redact accordingly, but personal data is often quite difficult to locate, and successfully repressing the data requires diligent checking and good organisational practices. 

To complicate matters, many companies and organisations use personal names as their identifiers. Many companies in the Companies House register include “Mr.” in their name, and there’s still more companies with titles that could be confused with personal names. 

## Where personal information is usually found in spending data 

The primary source of personal data is in the "name" field from the transaction. Ensuring that this data has been cleansed is likely to ensure that most potential privacy breaches are resolved.

However, at times transactions can include privacy-sensitive information in the "description" field of the invoice, which could include names, case files, or social security numbers. For this reason, all columns in the dataset should be analysed.

Columns to pay special attention to include:

* Name
* Address
* Description
* Department
* Category

### Identifying names

There are a number of typical indicators that the payment is made to an individual:

* Use of "Mr", "Mrs", "Miss" etc. at the start of the supplier name
* Use of an initial followed by a name, e.g. "D. Harrison"
* Payment is not associated with an invoice
* The payment instruction details specify a refund or specifics such as "Direct Payment"

It is possible to use a procedure called "pattern matching" that can highlight any items in a database that match a certain pattern of characters. Using these routines will make it possible to highlight entries that may include personal name data.

## How to address the issue of personal data?

As mentioned before, the most important field in spending data is the supplier name, as this will most likely contain the most valuable personal data. Publishers need to be aware, however, of the potential for identities to be triangulated from additional data such as narratives and transaction descriptions. It is therefore necessary to review all fields in a data set.

### Step 1: Flagging at source

Evaluating the entries in the supplier name field to assess whether the data includes an individual's name is an inefficient and largely ineffective method for flagging personal data breaches. Instead, the most effective method of suppressing publication of this data is to ensure that personal data is flagged as such when payments are made. Every department will have a legitimate reason for issuing payments to an individual, so it is advisable to establish an organisation-wide protocol for flagging payments to individuals.

### Step 2: Monitoring the Supplier Database

The data used in payment reports will originate from the organisation's finance system, which includes a record of suppliers to whom payments are made. To prevent fraud, there is normally a strict procedure for adding suppliers to this database. This procedure should include a requirement that any personal data is flagged for later suppression, effectively creating a second filter to prevent personal data breaches.

It is important to note that this procedure should not form the primary prevention mechanism, as the name in the supplier field is often simply not enough to identify whether a payment is for an individual or not. This step should be used in order to flag any payments that appear to be to an individual, however.

### Step 3: Pre-publication reviews 

All data that is to be published should go through a two-stage pre-publication review. The first part should include an automated review of the data, where a script is used to select entries that look like they may include personal data.

The scripts should be capable of screening for the following:

* Pre-determined flags that show that a payment is to an individual
* Common pattern matches used in names (e.g. "Miss")
* Names of known payees (e.g. payees that have been identified in personal payments before)
* Any specific funding codes that are likely to indicate that a payment is going to an individual (e.g. Social Care Direct Payments).

Once data has been selected, it should be reviewed manually to confirm whether the data provides sufficient information to identify an individual. There is no need to manually review data that has already been flagged as an individual by the department making the payment or has been previously been identified as an individual through previous work to prevent breaches. Data that has been flagged because it triggered a pattern match or through a funding code should be checked manually.

Once a data line has been identified as a payment to an individual, then the key pieces of text should be stored as a record that allows the council to suppress that data in the future and allows for use in the automated flagging procedures in the following months.

A further manual review needs to be undertaken to ensure that personal payments are not missed. Typically payments to individuals will involve small sums (relative to the amount paid to companies) in a small number of transactions. It is therefore possible to order the data by the lowest value transactions and then look through the payment lines to try and identify payments to individuals. Care should be taken to ensure that reviewers are aware of the potential for foreign names to appear in the text, and steps should be taken to ensure that a foreign language review is undertaken where necessary. Although this work sounds onerous, in reality it is a very small task: a regular monthly review should occupy just minutes of staff time, not hours.

### Step 4: Removing data 

You should never delete whole rows of data. Instead you should overwrite any data that might constitute a data breach. In particular, there should be no reason for removing either date or value fields from a transaction as these cannot be used to identify an individual. Additional data such as department and narrative information should only be overwritten if it contains data that could identify an individual.

Steps should also be taken to explain why the data has been censored. For example, it would be suitable to replace a person's name with an explanation like "Redacted to comply with the Data Protection Act". Providing this additional information gives the data user a good understanding of the nature of the underlying data and advises data consumers that the data producer is undertaking its role responsibly.

## Summary

The world is just getting used to the existence of open spending data, but as the data attracts increased usage governments will come under greater pressure to create dependable, consistent and accurate datasets. Now is the time to ensure that your data is correctly presented, free of data that may breach regulations and can be used by organisations like openspending.org