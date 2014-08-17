import os, yaml
from BeautifulSoup import BeautifulSoup
from markdown2 import markdown
from jinja2 import Environment, FileSystemLoader
from _classes import DocTemplate, DocTopic, DocSection

def mutate_path_for_web(file_path, _dir):
    """Mutates the file path provided and turns it into a
    suitable path for incorporation into the spoonium docs page
    """
    return file_path.replace(_dir, "components/docs").replace("\\", "/")


def process_metafile(meta_file):
    """Processes the meta file and returns the section name
    """
    with open(meta_file, 'r') as f:
        text = f.read()
    meta = markdown(text, extras=['metadata'])
    return meta.metadata['section']


def process_markdown_file(markdown_file):
    """Processes the markdown file and returns HTML in "Spoonium" format
    """
    #convert to html
    with open(markdown_file, 'r') as f:
        text = f.read()
    html = markdown(text)
    #process the html for spoonium
    soup = BeautifulSoup(html)
    for h1 in soup.findAll('h1'):
        h1['id'] = h1.string.replace(' ', '_')
    return '<div class="wiki-content">\n' + str(soup) + '\n</div>'


def create_doc_from_yaml(yaml_file):
    """Creates a DocTemplate from a yaml file
    Returns the new DocTemplate
    """
    doc = DocTemplate()
    with open(yaml_file, 'r') as f:
        topics = yaml.load_all(f)
        for topic in topics:
            #create a new DocTopic
            _topic = DocTopic(topic['display_name'], topic['ordering'], topic['link'])
            for section in topic['sections']:
                #create a new topic
                _section = DocSection(section['display_name'], section['ordering'], section['pages'])
                #add it to the _topic
                _topic.add_section(_section)
            #add the topic to the doc
            doc.add_topic(_topic)
    return doc


def process_dir(dirpath, files, root_build_dir, doc_template):
    """Processes a directory, adding all of the pages in the directory
    to the appropriate section of the docs

    Within this function, the markdown is also converted to HTML and added
    to the parallel folder in the build directory
    """
    #generate an output directory for the files, if one doesn't already exist
    output_dir = dirpath.replace("\\doc\\", "\\build\\")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    #read the meta.md file and process it
    section_name = process_dir_meta(os.path.join(dirpath, "meta.md"))
    for topic in doc_template.topics:
        if section_name.lower() in [name.lower() for name in topic.get_section_names()]:  #case-insensitive compare
            section = topic.get_section_named(section_name)
            #add all the files in this dir into the section
            for f in files:
                if f == "meta.md":
                    #don't process it!
                    continue
                else:
                    #generate html and add to build dir
                    html = process_markdown_file(os.path.join(dirpath, f))
                    output_file_path = os.path.join(output_dir, f[:-2] + "html")
                    write_to_file(output_file_path, html)
                    #add to doc template
                    mutated_path = mutate_path_for_web(output_file_path, root_build_dir)
                    section.add_page(mutated_path)
            return doc_template
        else:
            continue
        raise NoSuchSectionError(dirpath)


def process_dir_meta(meta_file):
    with open(meta_file, 'r') as f:
        text = f.read()
    meta = markdown(text, extras=['metadata'])
    return meta.metadata['section']


def write_docshtml(doc_template, build_dir):
    """renders a jinja2 template for the docs
    and writes it to an html file
    """
    root_dir = os.path.abspath(os.path.join(build_dir, os.pardir))
    print(root_dir)
    env = Environment(loader=FileSystemLoader(os.path.join(root_dir, "templates")))
    template = env.get_template('docs_temp.html')
    docs_html = template.render(doc_template=doc_template)
    #write to a file
    write_to_file(os.path.join(build_dir, "docs.html"), docs_html)


def write_to_file(file_path, text):
    """Write the contents of the input text to a file
    at the given file_path
    """
    with open(file_path, 'w') as f:
        f.write(text)