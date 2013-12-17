# Resources

This chapter outlines a set of staple tools for data-driven research, explaining what it&rsquo;s useful for and what the barrier to entry is.

## Key to levels

* Basic. An off-the-shelf tool that can be learned and used independently within a day. No advanced installation (e.g. installation on servers) required.
* Intermediate. Between one day and one week to master basic functionality. May require tweaking of code.
* Advanced. Requires programming ability.

## Stage 1: Extracting and getting data

<table border="1">
<tbody>
<tr>
<td><strong>Issue</strong></td>
<td><strong>Tools</strong></td>
<td><strong>Level</strong></td>
<td><strong>Notes</strong></td>
</tr>
<tr>
<td>Data not available</td>
<td>Freedom of Information Portals (e.g. <a href="https://www.whatdotheyknow.com/">What Do They Know</a>, <a href="https://fragdenstaat.de/">Frag den Staat</a>)</td>
<td>Basic&mdash;though some education may be required to inform people that they have the right to ask, how to phrase an FOI request, whether it is possible to submit these requests electronically, etc.</td>
<td>While Freedom of Information portals are a good way of getting data, results often end up scattered. It would be useful to have results structured into data directories so that it was possible to search successful responses together with proactively released data so that there is one common source for data.</td>
</tr>
<tr>
<td>Data available online but not downloadable (e.g. in HTML tables on webpages)</td>
<td><em>For simple sites</em> (e.g. information on an individual webpage), Google Spreadsheets and ImportHTML Function, or the <a href="https://chrome.google.com/webstore/detail/scraper/mbigbapnjcgaffohmbkdlecaccepngjd?hl=en">Google scraper extension</a> (basic).
<p><em>For more complex webpages</em> (information spread across numerous pages), a scraper will be required. Scrapers are ways to extract structured information from websites using code. There is a useful tool to make doing this easier online &ndash; <a href="https://scraperwiki.com/">Scraperwiki</a> (advanced).</p>
</td>
<td>
<p>For the basic level, anyone who can use a spreadsheet and functions can use it. It is not, however, a well-known command, and awareness must be spread about how it can be used&mdash;people are often unnecessarily daunted because they presume scraping involves code.</p>
<p>Scraping using code is advanced and requires knowledge of at least one programming language.</p>
</td>
<td>
<p>In the Open Knowledge Foundation's international interviews with data-driven researchers, the need to be able to scrape was mentioned in <em>every</em> country interviewed.</p>
For more information or to learn to start scraping, see the <a href="http://schoolofdata.org/handbook/courses/scraping/">School of Data course on Scraping</a>.</td>
</tr>
<tr>
<td>Data available only in PDFS or images</td>
<td>A variety of tools are available to extract this information. Most promising non-code variants are <a href="http://finereader.abbyy.com/">ABBYY Finereader</a> (not free) and <a href="http://tabula.nerdpower.org/">Tabula</a> (new software, still a bit buggy and requires people to be able to host it themselves to use).</td>
<td>Advanced. Most tools require knowledge of coding. Some progress is being made on non-technical tools. For more info and to see some of the advanced methods, see the <a href="http://blog.openspending.org/research/osi/appendix/tool-ecosystem/">School of Data course</a>.</td>
<td>
<p>These tools are still imperfect, and it is still vastly preferable to advocate for data in the correct formats rather than to teach people how to extract.</p>
<p>Recently published <a href="https://www.gov.uk/service-manual/design-and-content/choosing-appropriate-formats.html">guidelines</a> coming directly from government in the UK and US can now be cited as examples to get data in the required formats.</p>
</td>
</tr>
<tr>
<td>Leaked data</td>
<td>Several projects make use of secure dropboxes and services for whistleblowers</td>
<td>Advanced. Security of utmost concern.</td>
<td>
<p>For example, <a href="http://atlatszo.hu/magyarleaks/">MagyarLeaks</a>.</p>
</td>
</tr>
<tr>
<td>Data no longer available online</td>
<td>Internet Archive <a href="http://archive.org/web/web.php">Wayback Machine</a></td>
<td>Basic </td>
<td> </td>
</tr>
</tbody>
</table>

## Stage 2: Cleaning, Working with and Analyzing Data<

<table border="1">
<tbody>
<tr>
<td><strong>Issue</strong></td>
<td><strong>Tools</strong></td>
<td><strong>Level</strong></td>
<td><strong>Notes</strong></td>
</tr>
<tr>
<td>Messy data, typos, blanks (various)</td>
<td>Spreadsheets, <a href="http://openrefine.org/">Open Refine</a>, Powerful text editors (e.g. <a href="http://www.barebones.com/products/textwrangler/">Text Wrangler</a>) plus knowledge of Regular Expressions; <a href="http://okfnlabs.org/blog/2012/10/22/messytables.html">messytables</a></td>
<td>
<p>Basic: spreadsheets</p>
<p>Intermediate: Open Refine</p>
<p>Advanced: messytables, regular expressions</p>
</td>
<td> </td>
</tr>
<tr>
<td>Managing and transforming data with code</td>
<td><a href="http://misoproject.com/">Miso</a>, <a href="http://reclinejs.com/">Recline.js</a></td>
<td>Advanced </td>
<td> </td>
</tr>
<tr>
<td>Reconciliation of entity names</td>
<td><a href="http://nomenklatura.okfnlabs.org/">Nomenklatura</a>, <a href="http://opencorporates.com/">OpenCorporates</a></td>
<td>Advanced</td>
<td>
<p>Reconciling entities is complicated both due to the tools needed as well due to the often corrupt state of the data.</p>
<p> </p>
</td>
</tr>
<tr>
<td>Mapping names to geographic data</td>
<td><a href="http://www.geonames.org/">GeoNames</a></td>
<td> </td>
<td> </td>
</tr>
<tr>
<td>Visualizing networks and relationships between entities</td>
<td>Gephi</td>
<td>Intermediate to Advanced</td>
<td> </td>
</tr>
<tr>
<td>Need to be able to work with many many lines of data (too big to be able to fit in Excel)</td>
<td><a href="http://openspending.org">OpenSpending.org</a>, Other database software (PostGres, MySQL), command line tools</td>
<td>Basic to Advanced</td>
<td>As few countries currently release transaction-level data, this is not a frequent problem, but it is already problematic in places such as Brazil, the US, and the UK. As we push for greater disclosure, this will be needed ever more.</td>
</tr>
<tr>
<td>Performing repetitive tasks or modelling</td>
<td>Excel macros</td>
<td>Basic to Intermediate</td>
<td> </td>
</tr>
<tr>
<td>Slicing and dicing CSV files</td>
<td><a href="http://pypi.python.org/pypi/csvkit">CSVkit Python library</a></td>
<td>Advanced </td>
<td> </td>
</tr>
<tr>
<td>Entity extraction (e.g. from large bodies of documents)</td>
<td><a href="http://www.opencalais.com/">Open Calais</a>, <a href="http://developer.yahoo.com/contentanalysis/">Yahoo/YQL Content Analysis API</a>, <a href="http://openup.tso.co.uk/des">TSO data enrichment service</a></td>
<td>Intermediate</td>
<td>This is far from a perfect method, and it would be vastly easier to answer questions relating to entities if they were codified by a unique identifier.</td>
</tr>
<tr>
<td>Analysis needs to be performed on datasets that are published in different languages (e.g. in India)</td>
<td>To some extent, Google Translate for web based data</td>
<td>Basic</td>
<td>Still searching for a solution to automatically translate offline spreadsheets.</td>
</tr>
<tr>
<td>Figures change in data after publication</td>
<td>
<p>For non-machine readable data &ndash; tricky.</p>
<p>For simple, machine-readable file formats, such as CSV &ndash; version control tools (e.g. <a href="http://git-scm.com">Git</a>, <a href="http://mercurial.selenic.com">Mercurial</a>).</p>
<p>For web-based data &ndash; some scrapers can be configured to trigger (e.g. email someone) whenever a field changes.</p>
</td>
<td>Intermediate to Advanced</td>
<td>Future projects that are likely to tackle this problem: <a href="http://dansinker.com/post/49856260511/opennews-code-sprints-do-some-spring-cleaning-on-data">DeDupe</a>.</td>
</tr>
<tr>
<td>Finding statistical patterns in spending data </td>
<td><a href="http://www.r-project.org">R</a> (free), <a href="http://www-01.ibm.com/software/analytics/spss/">SPSS</a> (proprietary) and other statistical software for clustering and anomaly detection (also see note)</td>
<td>Advanced</td>
<td>Examples: Data from <a href="https://www.kpk-rs.si/en/project-transparency/supervizor-73">Supervizor</a> has been used to track changes in spending on contractors changes in government.
<p><em>A note on statistical analysis software can be found below.</em></p>
</td>
</tr>
</tbody>
</table>

**Note on SPSS and R:** It's our impression that interviewees seemed largely to have been trained to use SPSS. R is important to mention, however, as it offers free access to a broad section of the same models, though based on a programming interface.

A few examples of analysis of spending data, which can be done with statistical software such as SPSS or R:

* [Hidden Markov Models](http://en.wikipedia.org/wiki/Hidden_Markov_model): Hidden Markov Models were originally developed for finding patterns in bioinformatics, but they have turned out to be useful for predicting fraudulent and corrupt behaviour as well. They were, for example, used to analyse spending data from 50 mio transactions in the Slovenian platform [Supervizor](https://www.kpk-rs.si/en/project-transparency/supervizor-73). Using Hidden Markov Models requires high quality data.</p>
* [Benford's law](http://en.wikipedia.org/wiki/Benford%27s_law): Benford's law checks the distribution of figures in your data against how it should actually look. Diversions from the normal distribution can help detect fraudulent reporting (eg. if companies tend to report ernings less than $500 mio. in order to fit a particular regulation, Benford&rsquo;s law could be a tool to detect that). Check out this example using Benford&rsquo;s law to test the release of all [Danish corporate tax filings](http://friism.com/tax-records-for-danish-companies), and check out this [R blog post on the topic](http://friism.com/tax-records-for-danish-companies).

Though SPSS is fairly easy to get started using, it can be difficult to collaborate around, as it applies its own SPSS data format. Some models might also be unavailable from the basic SPSS package. R is a free alternative where all extensions are accessible and where community support and code samples are widely available. One possible compromise bridging the convenience of SPSS and the wide usability of R is the proprietary software [R Revolution](http://www.revolutionanalytics.com/).

## Stage 3: Presenting Data

<table border="1">
<tbody>
<tr>
<td><strong>Issue</strong></td>
<td><strong>Tools</strong></td>
<td><strong>Level</strong></td>
<td><strong>Notes</strong></td>
</tr>
<tr>
<td>Basic visualisations, time series, bar charts</td>
<td><a href="http://datawrapper.de/">DataWrapper</a>, <a href="http://www.tableausoftware.com/public/">Tableau Public</a>, <a href="http://www-958.ibm.com/software/analytics/manyeyes/">Many Eyes</a>, Google Tools</td>
<td>Basic</td>
<td> </td>
</tr>
<tr>
<td>More advanced visualisation</td>
<td><a href="http://d3js.org/">D3.js</a>, <a href="http://raphaeljs.com/">Raphael</a>, <a href="http://code.shutterstock.com/rickshaw/">Rickshaw</a></td>
<td>Advanced</td>
<td>Used in e.g. <a href="http://openbudgetoakland.org/2012-2013-sankey.html">OpenBudgetOakland</a></td>
</tr>
<tr>
<td>Mapping</td>
<td><a href="http://www.mapbox.com/tilemill/">TileMill</a>, <a href="http://www.google.com/drive/apps.html#fusiontables">Fusion Tables</a>, <a href="http://kartograph.org/">Kartograph</a> <a href="http://www.qgis.org/">QGIS</a></td>
<td>Basic to Advanced</td>
<td> </td>
</tr>
<tr>
<td>Creating a citizen&rsquo;s budget</td>
<td>OpenSpending.org: Disqus commenting module added to OS for commenting and feedback</td>
<td>
<p>OpenSpending.org &ndash; making a custom visualisation &ndash; basic.</p>
<p>Making a custom site enabling discussion &ndash; advanced.</p>
</td>
<td>Used in e.g. <a href="http://openbudgetoakland.org/2012-2013-sankey.html">OpenBudgetOakland</a></td>
</tr>
</tbody>
</table>

## Publishing Data

<table border="1">
<tbody>
<tr>
<td><strong>Issue</strong></td>
<td><strong>Tools</strong></td>
<td><strong>Level</strong></td>
<td><strong>Notes</strong></td>
</tr>
<tr>
<td>Need a place online to store and manage raw data, especially from Freedom of Information requests</td>
<td>DataNest, CKAN, Socrata, various Data Portal Software options</td>
<td>Basic to use. Intermediate to advanced to install.</td>
<td>Can require a programmer to get running and set up a new instance.</td>
</tr>
<tr>
<td>Individual storage of and online collaboration around datasets</td>
<td>Google Spreadsheets, Google Fusion Tables, GitHub</td>
<td>
<p>GitHub: intermediate.</p>
<p>All others: basic.</p>
</td>
<td> </td>
</tr>
</tbody>
</table>