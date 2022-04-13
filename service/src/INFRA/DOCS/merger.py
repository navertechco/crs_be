import json
import os
from mailmerge import MailMerge
from docx import Document
from docxcompose.composer import Composer
from docx.shared import Inches
from docx.shared import Pt



ROOT_DIR = os.path.dirname(__file__)
DATA_PATH = os.path.join(ROOT_DIR, ('data.json'))
DOCS = []


def gen_tour_doc(data):
    header = gen_header(data)
    gen_cover_doc(header, 'tour_id')
    gen_dest(data)
    # doc_compose(DOCS, 'tour_id')
    # combine_word_documents(DOCS)


def gen_header(data):
    #HEADER
    customer_data = data["customer"]
    tour_data = data["tour"]
    logistic_data = data["logistic"]
    header = {**customer_data, **tour_data, **logistic_data}
    return header

def replace_word(document, key, word):
    for paragraph in document.paragraphs:
        if key in paragraph.text:
            paragraph.text = paragraph.text.replace(key, word)

def gen_cover_doc(header, name): 
    doc_template = os.path.join(ROOT_DIR, (f"cover.docx"))
    doc_output = os.path.join(ROOT_DIR, (f'cover-{name}-output.docx'))
    document = Document(doc_template)
    replace_word(document, "NIGHTS", "9")
    replace_word(document, "DAYS", "10")
    replace_word(document, "CUSTOMER", "CUSTOMER NAME TEST")
    replace_word(document, "LEGAL_NAME", "CUSTOMER NAME TEST")
    replace_word(document, "PAX", "10")
    replace_word(document, "VALID", "12-31-2022")
    document.save(doc_output)
    DOCS.append(doc_output)


def gen_dest(data):
    dest_template = os.path.join(ROOT_DIR, ("dest.docx"))
    destinations = data["destinations"]
    name = 'tour_id'
    for dest_name in destinations:
        destination = destinations[dest_name]
        dest_output = MailMerge(dest_template)
        doc = Document()
        run = doc.add_heading(f'{dest_name.capitalize()}', 0).add_run()
        font = run.font
        font.name = 'Calibri'
        font.size = Pt(12)
        days = destination["daysData"]
        dest_output.merge_pages(days.values())
        for day_name in days:
            day = days[day_name]
            experiences = day["experiences"]
            meals = day["meals"]
            if day_name == '0':
                doc.add_heading(f'Arrival', 1)
                meals = 'D/O'
            else:
                doc.add_heading(f'Day {day_name}', 1)
            doc.add_heading(f'Experiences', 2)
            for i, exp_name in enumerate(experiences):
                experience = experiences[exp_name]
                run = doc.add_heading(exp_name, 3).add_run()
                font = run.font
                font.name = 'Calibri'
                font.size = Pt(12)
                run = doc.add_paragraph(experience["description"].split('.')[1:]).add_run()
                font = run.font
                font.name = 'Calibri'
                font.size = Pt(12)
                image = os.path.join(ROOT_DIR, (f'image.png'))
                doc.add_picture(image, width=Inches(4), height=Inches(4))
                if i < len(experiences)-1:
                    next = list(experiences)[i+1]
                    run = doc.add_paragraph(f"Next we're going to get, {experiences[next]['description'].split('.')[0]}").add_run()
                    font = run.font
                    font.name = 'Calibri'
                    font.size = Pt(12)
                else:
                    run = doc.add_paragraph(f"Next we're going back to hotel to rest and take a meal\n").add_run()
                    font = run.font
                    font.name = 'Calibri'
                    font.size = Pt(12)
                    run = doc.add_paragraph(f"{meals}").add_run()
                    font = run.font
                    font.name = 'Calibri'
                    font.size = Pt(12)
                # else:
                #     doc.add_paragraph(f"Next we going to departure to Home", style='Intense Quote')
                doc.add_page_break()
        output = os.path.join(ROOT_DIR, (f'{dest_name}-{name}-output.docx'))
        doc.save(output)
        DOCS.append(output)


def doc_compose(files, name):
    composed = os.path.join(ROOT_DIR, (f'{name}-output.docx'))
    empty = os.path.join(ROOT_DIR, (f'empty.docx'))
    new_document = Document(empty)
    composer = Composer(new_document)
    for i in range(0, len(files)):
        doc = Document(files[i])
        if i != len(files) - 1:
            doc.add_page_break()
        composer.append(doc)
    composer.save(composed)


def combine_word_documents(files):
    cover = Document(files[0])
    new = os.path.join(ROOT_DIR, (f'new.docx'))
    for sub_doc in range(1, len(files)):
        sub_doc = Document(files[sub_doc])
        for element in sub_doc.element.body:
            cover.element.body.append(element)
        cover.add_page_break()
    cover.save(new)


if __name__ == '__main__':
    G = open(DATA_PATH, 'r', encoding="utf8")
    data = json.load(G)
    gen_tour_doc(data)
