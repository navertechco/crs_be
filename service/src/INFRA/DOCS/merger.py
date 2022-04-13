import json
import os
from docx import Document
from docxcompose.composer import Composer
from docx.shared import Inches
from docx.shared import Pt
from datetime import datetime
from docx2pdf import convert

FILE_DIR = os.path.dirname(__file__)
ROOT_DIR = os.path.dirname(FILE_DIR)
DOC_DIR = os.path.join(ROOT_DIR, ('WEB\\static\\docs'))
DATA_PATH = os.path.join(FILE_DIR, ('data.json'))
DOCS = []


def gen_tour_doc(data):
    header = gen_header(data)
    travel_code = header.get('travel_code')
    gen_cover_doc(header, travel_code)
    gen_dest(data, travel_code)
    doc_compose(DOCS, travel_code)


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
    passengers = header.get('passengers')
    arrival_date = header.get('arrival_date')
    departure_date = header.get('departure_date')
    names = header.get('names').upper()
    last_names = header.get('last_names').upper()
    until_date = header.get('until_date')
    arrival = datetime.strptime(arrival_date, '%Y-%m-%d %H:%M:%S')
    departure = datetime.strptime(departure_date, '%Y-%m-%d %H:%M:%S')
    until = datetime.strptime(until_date, '%Y-%m-%d %H:%M:%S.%f')
    days = (departure - arrival).days
    nights = days - 1
    customer = f"{names} {last_names}"
    print(header)
    doc_template = os.path.join(FILE_DIR, (f"cover.docx"))
    doc_output = os.path.join(FILE_DIR, (f'cover-{name}.docx'))
    document = Document(doc_template)
    replace_word(document, "NIGHTS", f"{nights}")
    replace_word(document, "DAYS", f"{days}")
    replace_word(document, "CUSTOMER", f"{customer.upper()}")
    replace_word(document, "LEGAL_NAME", f"{customer.upper()}")
    replace_word(document, "PAX", f"{passengers}")
    replace_word(document, "VALID", f'{until.strftime("%Y-%m-%d")}')
    document.save(doc_output)
    DOCS.append(doc_output)


def gen_dest(data, name):
    dest_template = os.path.join(FILE_DIR, ("dest.docx"))
    destinations = data["destinations"]
    for dest_name in destinations:
        destination = destinations[dest_name]
        doc = Document()
        run = doc.add_heading(f'{dest_name.upper()}', 0).add_run()
        font = run.font
        font.name = 'Calibri'
        font.size = Pt(12)
        days = destination["daysData"]
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
                image = os.path.join(FILE_DIR, (f'image.png'))
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
        output = os.path.join(FILE_DIR, (f'{dest_name}-{name}.docx'))
        doc.save(output)
        DOCS.append(output)


def doc_compose(files, name):
    composed = os.path.join(DOC_DIR, (f'{name}.docx'))
    pdf = os.path.join(DOC_DIR, (f'{name}.pdf'))
    new_document = Document()
    composer = Composer(new_document)
    for i in range(0, len(files)):
        doc = Document(files[i])
        if i != len(files) - 1:
            doc.add_page_break()
        composer.append(doc)
    composer.save(composed)
    convert(composed, pdf)
 

if __name__ == '__main__':
    G = open(DATA_PATH, 'r', encoding="utf8")
    data = json.load(G)
    gen_tour_doc(data)
