def generate_concept_HTML(concept_title, concept_description, concept_example):
    if concept_example <> "":
        html_text_1 = '''
    <div class="lesson-content">
        <h2>''' + concept_title
        html_text_2 = '''</h2>
            ''' + concept_description
        html_text_3 = '''
        <div class="example">
            ''' + concept_example
        html_text_4 = '''
        </div> 
    </div>'''
    else:
        html_text_1 = '''
    <div class="lesson-content">
        <h2>''' + concept_title
        html_text_2 = '''</h2>
            ''' + concept_description
        html_text_3 = ""
        html_text_4 = '''   
    </div>'''
    
    full_html_text = html_text_1 + html_text_2 + html_text_3 + html_text_4
    return full_html_text

def make_HTML(concept):
    concept_title = concept[0]
    concept_description = concept[1]
    concept_example = concept[2]
    return generate_concept_HTML(concept_title, concept_description, concept_example)

EXAMPLE_LIST_OF_CONCEPTS = [ ['Python', "We will be using Python because it's a relatively simple but powerful programming language.",""],
                             ['Numbers in Python', 'It is important to note that decimal places are important when creating mathematical functions in Python. For example:', '5/2 = 2 <br> 5.0/2 = 2.5 <br>5/2.0 = 2.5 <br>']]

def make_HTML_for_many_concepts(list_of_concepts):
    output = ""
    for i in list_of_concepts:
        concept_html = make_HTML(i)
        output = output + concept_html
    return output

print make_HTML_for_many_concepts(EXAMPLE_LIST_OF_CONCEPTS)
