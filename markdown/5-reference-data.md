# Reference data

Spending data isn't the only kind of data you should be interested in. One of the most powerful ways of making spending data more meaningful is to combine it with *reference data*.

Unlike spending data, reference data does not describe observations about reality. It contains additional details on category schemes, government programmes, persons, companies, or places mentioned in data. It is data about data, also known as *metadata*.

The main groups of reference data that are used with government finance are classification codesheets, geographic identifiers, and identifiers for companies and other organizations.

### Classification reference data

Classification datasets are dictionaries for the categorizations used in a financial dataset. They may include descriptions of government programmes; economic, functional or institutional classification schemes; charts of account; and many other types of schemes used to classify expenditures.

Some classification schemes are standardized beyond individual countries. These include the UN's [classification of functions of government (COFOG)](http://unstats.un.org/unsd/cr/registry/regcst.asp?Cl=4) and the [OECD DAC Sector codes](http://www.oecd.org/dac/aidstatistics/dacandcrscodelists.htm). Most classification schemes, however, are particular to individual governments. For this reason, it is often useful to request access to the classification scheme used internally by governments, including revisions over time that may have changed how certain programmes were classified.

A library of reference data that can be re-used across different projects and it is a valuable asset for any organization working with government finance. Sharing such data with others is crucial, as it will help to enable comparable outputs and open up options for future data integration. Existing repositories include the [IATI](http://iatistandard.org/) Registry and [datahub.io](http://datahub.io).

### Geographic identifiers and shapefiles

Geographic identifiers are used to describe administrative boundaries or specific locations identified in a dataset. Some regional classifications are available on the web, including the [EU NUTS Codes](http://epp.eurostat.ec.europa.eu/portal/page/portal/nuts_nomenclature/introduction). There is also an increasing number of open databases which contain geographic names, including [geonames.org](http://www.geonames.org) and the recently developed [world.db](https://github.com/geraldb/world.db).

Besides geographical codes, many countries have released *shapefiles* of their political and geographic districts. Shapefiles are datasets describing the shapes of geographical regions, and they can be imported into mapping applications like [TileMill](http://mapbox.com/tilemill/) and combined with other data to produce maps.

### Organisational identifiers

As you look into spending data that includes recipients outside the government, you'll find companies which act as suppliers to government, but also other types of entities including charities, associations, foreign governments, political parties, and even individuals.

Identifying such entities is notoriously hard, since the only information kept by government is often a simple name (which may not uniquely identify the beneficiary, for example "MS"). While most (if not all) countries maintain company registers that assign some type of unique identifier to a company, these databases are often not accessible in bulk and not used coherently across different parts of government. Alternative identifiers, such as tax identifiers and company IDs from private business information suppliers (such as Dun & Bradstreet in the US, which maintains the intellectual property rights over their data), further complicate the identification process.

As an alternative to these country-specific and idiosyncratic company registers, open registries that compile organisational identifiers in a form that is easy to reuse are beginning to appear. Databases which have been augmented with such open information can be easily shared.

[OpenCorporates](http://opencorporates.com) is an example of such an open registry of organisational identifiers. OpenCorporates is a startup that collects information from companies worldwide and provides a convenient API to match datasets with the list of known countries. They offer a service to "reconcile" companies to link information about a company to a company name. This is especially useful when you have an exist spreadsheet or dataset featuring lots of companies. Matching (or reconciling) to legal entities allows you to get more information about the companies (for example, their registered address or statutory filings) and makes it easier to match with other datasets or exchange with other organisations.

The [IATI](http://www.aidtransparency.net) project for aid transparency is working towards similar standards for other organisations such as foreign governments and charities active in the development space.