# Getting data

Data can be acquired for a research project by many different means. Some ways of acquiring data, like using data portals or submitting Freedom of Information requests, rely on government cooperation. Others, like data scraping, use technology to bridge the gap between how information is shared and what is necessary for doing research.

![The data processing pipeline: getting data](http://i.imgur.com/i6O2gJG.jpg)

## Data portals

More and more governments accept the need for proactive transparency. Many countries have set up dedicated open data portals, websites which provide easy and centralized access to all published datasets and relevant metadata (e.g. information about when a dataset was last updated, who published it, and where documentation regarding format and contents can be found). Using these portals as a data source is not only easy but often provides a more authoritative base for analysis.

If you are looking for data from a particular country, see if that country has its own data portal. The [Open Data Census](http://census.okfn.org/catalogs/) and [datacatalogs.org](http://datacatalogs.org/) are two indexes which can help you locate a particular portal. The Guardian also provides a [world government data search engine](http://www.guardian.co.uk/world-government-data) which allows you to search numerous state data portals simultaneously.

![datacatalogs.org](http://farm8.staticflickr.com/7127/7631434818_d8f903252c_z.jpg)

Comparative data on a large number of states is available from the data portals of the [United Nations](http://data.un.org/), [World Bank](http://data.worldbank.org/), and [World Health Organization](http://www.who.int/research/en/). Regional portals like [Africa Open Data](http://africaopendata.org/), [OpenData Latinoamérica](http://www.opendatalatinoamerica.org/home/), and the [European Union open data portal](http://open-data.europa.eu/) aggregate data from groups of states.

A lot of government data is indexed by ordinary web search engines. The trick to finding this data is anticipating its file format. If you limit your searches to machine-readable file formats specific to the type of data you want (e.g. CSV or XLS for tabular data, SQL or DB for databases), your search results are likely to be relevant data. Add "+filetype:extension" to your Google query to look for files with a specific extension, e.g. "+filetype:csv" to look for CSV files.

You may not be the first person to think of collecting the data you're interested in. Check the Open Knowledge Foundation's [Data Hub](http://datahub.io/), "a community-run catalogue of useful sets of data on the Internet", to see if anyone else has put up the data you're looking for.

### APIs

Open data is sometimes provided through an application programming interface (API). This is a web-based method for retrieving, searching, or even updating data dynamically from within a programming language environment. APIs provide up-to-date data in a granular and filtered form, removing the need to repeatedly process and update source files.

A common use case for APIs is relatively time-sensitive information, such as procurement calls and contracts which are released every day. In the UK, [BusinessLink](http://www.contractsfinder.businesslink.gov.uk/data-feed.aspx) provides a number of data feeds which contain information about procurement notices. Similarly, the [USASpending](http://usaspending.gov/data) portal provides a set of APIs that can be used to retrieve up-to-date grants information for the US federal government.

## Freedom of information

Even before the rise of open data, many countries decided to increase the transparency of their governments by introducing Freedom of Information (FoI) legislation. Such laws enable every citizen to request documents and other material from parts of the government which do not merit special protection (e.g. due to concerns over privacy, national security, or commercial confidentiality).

FoI requests may be necessary when you want to get more detail on the projects that government money is funding. Often the transactional spending data that the government releases will include only a brief description of the project, if any description at all. For instance, if you have the high-level payment information for a contract that includes the recipient, location, and total amount, but you want to know the details of the contract deliverables, you will probably need to submit an FoI request for the full contract.

A good example of this process is the Sunlight Foundation's request for information on the Airport Improvement Program in the United States. The program accepts applications from airports around the country for infrastructure improvement grants, such as repaving a runway. Each project is assigned a safety priority rating and is prioritized in a queue. The high level spending information for this program was available in USASpending.gov, but since the priority ratings are specific to this program and not spending data in general, they were not included in that dataset. The Sunlight Foundation submitted a FoI request for the full dataset, including the priority ratings. After that, they were able to determine when airports with low priority projects were getting money and how often.

If you see some interesting patterns in your high-level spending data, don't be afraid to dig deeper and ask for more detailed program information.

### Preparing FoI requests

Want to submit an FoI request, but not sure where to start, who to address your request to, or how to write it? [Access Info](http://www.access-info.org/) is an organisation that works to help people obtain the information they require from the public bodies that hold it. They have also produced a [toolkit for FoI requests](http://www.legalleaks.info/toolkit.html). It's primarily aimed at journalists, but most of the tips are equally relevant for other researchers.

Before submitting your FoI request, consider whether you could acquire the data by some other route. Journalists, activists, and CSOs have long had their own channels of acquiring information. Sometimes having a good relationship with a press officer or a civil servant is good enough, and making a formal request for information is unnecessary—your friendly press-officer may even feel offended if you don't ask them nicely first. FoIs generate a lot of paperwork (hence grumpy civil servants), so if you do have the contacts, it may be a good idea to ask nicely first!

If an FoI request is your best option, make sure to invest some preparation in formulating your request. The documents or databases that are requested should be clearly identified, you should be aware of the department or unit in charge of the request, and you should address possible concerns over privacy or commercial confidentiality in your request.

Don't count on receiving data in a machine-readable form. The FoI legislation in force in many countries was established before the need for structured data became apparent, and many laws do not allow the citizen to request a particular format. Many governments choose to release information on paper rather than in a structured digital form, which makes the data processing step more painful.

## Data scraping

Unlike open data or freedom of information requests, data scraping does not rely on the cooperation of the authorities. Scraping refers to transforming unstructured documents (online database interfaces, PDF files, or even printed documents) into a structured form that is ready for computational processing and analysis.

Although many easy-to-use scraping tools which do not require much technical know-how exist, many of the most rewarding data scraping tasks – such as the automated scraping of thousands or millions of web sites or the mass interpretation of PDF files – require some programming ability.

A great way to start learning about data scraping is with [ScraperWiki](https://scraperwiki.com/). ScraperWiki is not only a source of excellent tutorials but also a convenient tool. The ScraperWiki platform is a web application that allows you to write and run code (in Python, PHP, or Ruby) to scrape data from the web and store the result in a simple database. Using Scraperwiki has the additional benefit of making anything that you scrape available to others, as most scraped data goes into a public data store.

Another very accessible guide to scraping is Paul Bradshaw's [Scraping for Journalists](https://leanpub.com/scrapingforjournalists), available from Leanpub for a minimum payment of $15.10. Like many data-acquiring tutorials, it is marketed to journalists, but scraping is scraping, and it is a worthwhile read for anyone doing research with data.

### Getting data out of scanned documents

In some cases, the only way to gain access to a dataset is through the digitization of printed material. While scanners and optical character recognition software can be used to import such documents, the high cost and low data quality generated through this approach often make it an unattractive one.

When you deal with scanned documents, the crucial step in the extraction process is to have the computer attempt to recognise any characters - letters, numbers and other signs. Optical character recognition software is built to do this, accepting scanned pictures and PDF documents as an input. There are both commercial software products for OCR such as [ABBYY FineReader](http://finereader.abbyy.com/), and some open-source software packages, such as Google's [Tesseract](http://code.google.com/p/tesseract-ocr/).

In general, the quality of all automatic recognition is limited, and you should make sure to cross-check any numbers coming from scanned material against the printed documents.

## Keeping the data around

As you retrieve data, you may be tempted to consider the sources it has gathered from as a permanent resource. But experience has shown that data *does* disappear, whether through the government redesigning its web sites, new policies that retract transparency rules, or simple system failures.

You can help prevent the disappearance of data by keeping your own archival copies. For data found on the web, this means downloading complete copies of web sites – a process called *mirroring* – which is a fairly well established technique that can easily be deployed by civil society organisations and other researchers. Mirroring involves using a computer program called a [web crawler](http://en.wikipedia.org/wiki/Web_crawler) to harvest all the web pages from a specified web page, e.g. a ministry home page.

In most cases, it is also possible to find old versions of web sites via the Internet Archive's [Wayback Machine](http://archive.org/web/web.php), a project that aims to create up-to-date copies of all public web sites and archive them forever.