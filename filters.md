# Introduction
This file gives an overview of how the storage options are mapped onto each filter in the storage finder. When an x is marked in the filter column for a specific storage option, this indicates that this storage option can provide the service that the filter refers to and that the storage option will not be excluded when the filter is applied in the storage finder tool.
Please note that for the purposes of the table the filter options are not separated by 'category'.

## Filters
Available filters are:

**Data classification**
Filter type: single
- Low
- Medium
- High
- Very high / secret
 
**Data sharing**
Filter type: single
- Not necessary
- With VU researchers
- With anyone

**Data volume**
Filter type: single
- < 500 GB
- \> 500 GB

**Features**
Filter type: multiple
- Basic storage
- Compute/HPC
- Collaboration tools
- Archiving/Publishing

## Filters overview

| Tool                          | Low | Medium | High | Very high / secret | Not necessary | VU | Anyone | <500 GB | >500 GB | Basic storage | Compute/HPC | Collaboration tools | Fine-grained access rights | Archiving/Publishing |
| ----------------------------- | --- | ------ | ---- | ------------------ | ------------- | -- | ------ | ------- | ------- | ------------- | ----------- | ------------------- | -------------------------- | -------------------- |
| Custom solution               | x   | x      | x    | x                  | x             | x  | x      | x       | x       |   x           | x           | x                   | x                | x |
| Encrypted portable storage    | x   | x      |      |                    | x             |    |        | x       | x       |   x           |   |  |  |  |
| Google Drive (campus licence) | x   |        |      |                    | x             | x  | x      | x       | x       |   x           |             | x           | x          |   
| Microsoft SharePoint (Teams)  | x   | x      |      |                    | x             | x  |        | x       | x       |   x           |                     | x           | x |  |
| OneDrive                      | x   | x      |      |	                   | x             | x  | x      | x       | x       |   x           |  | x | x | x |
| Open Science Framework        | x   |        |      |                    | x             | x  | x      | x       |         |               |   | x | x | x |
| Research Drive                | x   | x      | x    |                    | x             | x  | x      | x       | x       |   x           |  | x | x |  |
| SciStor                       | x   | x      |      |                    | x             | x  |        | x       | x       |   x           | x |   |   |   |
| Surfdrive                     | x   | x      |      |                    | x             | x  | x      | x       |         |   x           |  | x | x |   |
| Yoda                          | x   | x      | x    |                    | x             | x  | x      | x       | x       |   x           |   |   |   | x |


## Information about each filter

### Data classification
Data classification **here** refers to the type of data regarding privacy and confidentiality. It is meant to provide guidelines for storing, accessing, and processing data in a secure and responsible manner.

The [data classification tool](https://vu.nl/en/research/dataclassification) can help you to determine the classification for Availability, Integrity and Confidentiality.

The data steward for the Faculty of Behavioural and Movement Sciences (FGB) has also created a guide about [privacy and confidentiality risks](https://fgb-rdm.nl/Security/PrivacyRisks.html) that could help you to determine a classification for your data. The information on that page is geared towards FGB researchers but can also be helpful for other researchers.

If, using the information above, you are not sure which category fits your data or would like to know more about matters related to data classification, please contact us at the Research Data Management Support Desk: rdm@vu.nl.

### Data sharing

Indicate here whether you need to share your data and with whom. Note: this refers to data sharing *during* the research process and not to publishing data after the research is finished.

### Data volume

Indicate the (estimated) size of your dataset here.

### Features
A number of the storage options have additional features and/or functionality.

Select Basic storage if you have no specific needs and just want to store and access your files.

Select Compute/HPC if you plan to process your data using the high-performance computing facilities offered by the VU.

Select Collaboration tools to highlight solutions that facilitate collaboration via integrated tools and interfaces (OnlyOffice, Jupyter Notebooks). Note: not all collaboration tools will be available for each highlighted storage option

Select Fine-grained access rights if you need to give collaborators access to only certain folders, and not the entire project. Note: some tools may not offer fine-grained access rights but still offer the possibility to invite collaborators (this is, for example, the case for Yoda).

Select Archiving/Publishing if it is absolutely necessary that a storage tool also allows you to preserve your data FAIRly for the long term. Note that the VU also offers specialised archiving and publishing tools that were not included in the storage finder. You can use these tools also if you use any storage tool for project storage: you would then just need to migrate your data at the end of the project. The University Library can help you with this and advise you about what tool is most suitable for preserving your data. You can reach us via <rdm@vu.nl>.
