# Spoonium Documentation

This is the official Git repository for Spoonium's public documentation. 

Live version of the docs can be found at http://spoonium.net/docs

## Writing the Docs

### Style Guide

When contributing to the docs on Spoonium, please take the following style guidelines into consideration. 

**Code and Command-line Styling**

- Command-line comment: All comments should have a # followed by a space and the first word should be capitalized.

```
# this is formatted properly :)

#this is not :( 
```

- Command-line input

```
> spoon build -n="my image" /path/to/spoon.me
```

- Command-line output


- Command-line spacing



```
building "my image" from /path/to/spoon.me
```

- Always use `spoon` not `spn` in the command line documentation.
- All code blocks should be 'fenced' with 3 backticks (a la [GFM](http://github.com/github-flavored-markdown)). Inline code styles (i.e. this is a sample command: `spoon run`) only use 1 backtick. The syntax highlighting to use can be specified after the top 3 backticks (not available for inline code). 
- Use inline code styles sparingly. 

**Other Styling**

- Inline paths should be **bolded**. --> Example: navigate to **C:\Users** 
- Internal links to other sections of the doc should be relative paths
	* Other doc links: /docs/[topic]#[section]
	* To the hub: /hub
	* To contact page: /contact

### Adding images

- Put the image in the same folder as the md file
- Modify the path in the link based on the example below
- If you need to specify image dimensions, use HTML

```
# GitHub location
https://github.com/spoonium/docs/tree/master/doc/getting_started/tour_ii/image.png

# Markdown would be
![](/components/docs/getting_started/tour_ii/image.png)
```

### Contributing 

#### How to Contribute

If you are not a member of the **spoonium** org (AKA you don't work at Spoon), fork this repo, make changes, commit, and submit a pull request.

Some basic terminology:
- Topic: The horizontal items in the top nav items.
- Document: An item on the left nav, a topic contains a list of documents
- Section: A document consists of 1 or more sections. If you define sections in docs.yaml the left nav will become expandable.

The path to store your document is the /<topic>/<title>. 
Since the topic and title of the document can contain illegal file system characters, it must be normalized.
This is done by lower casing the path, replacing spaces with '_', and deleting illegal windows file system characters.
For example, the "What is Spoonium?" document under the topic "Getting Started" is stored in the directory "/getting_started/what_is_spoonium". The md file names inside of the directory can be *.md

#### Creating a New Topic

To add a new topic to the top navbar, first create a new folder in the directory corresponding to your topic. Then, edit the **docs.yaml** file, adding your new topic and rearranging the topic `ordering` as you see fit. Follow existing patterns when editing this file. 

#### Adding a document

If adding a document to an *existing topic*, find the (a) corresponding folder in the /<topic>/<title> folder and add your new **.md** file to it. 

You are allowed to divide a single document into multiple .md files. They will be assembled to a single document in the order they appear on the file system.

### docs.yaml

The overall structure of the page is dicated by the **docs.yaml** file, located at /docs.yaml.
Each document in the yaml file specifies a topic that will appear in the top navbar of the docs page. A topic has the following properties:

1. A `topic`. This is the actual wording that will appear in the top nav bar
2. A list of `documents`. This list is used to populate the topic's documents.
3. A list of 'sections'. This list is used to navigate within a document.