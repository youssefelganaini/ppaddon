from pptx import Presentation
from gpt import send_gpt

pptx_path = "./Abschlusspräsentation Schalke hilft!.pptx"
output_path = "./response.txt"


def extract_text_from_pptx(pptx_path):
    # Load the presentation
    prs = Presentation(pptx_path)

    # Iterate through slides, then through slide elements to extract text
    full_text = []
    count_slide = 0
    for slide in prs.slides:
        count_slide += 1
        full_text.append([])
        full_text[-1].append("//Folie " + str(count_slide) + "\n")

        count_box = 0

        # Get Action title
        if slide.shapes.title is not None:
            full_text[-1].append(
                "BOX " + str(count_box) + "\n" + slide.shapes.title.text
            )
            full_text[-1].append(slide.shapes.title.text)

        # for shape in slide.shapes:
        #     if hasattr(shape, "text") and full_text is None:
        #         # count_box += 1
        #         # full_text[-1].append("BOX " + str(count_box) + "\n" + shape.text)
        #         print(full_text)
        #         full_text[-1].append(shape.text)

    return full_text


def save_to_txt_file(text, output_path):
    with open(output_path, "w") as file:
        file.write(text)


text = extract_text_from_pptx(pptx_path)

result = ""
for slide in text:
    for box in slide:
        result += box + "\n"
    result += "\n"

with open("bsp.txt", "w") as file:
    file.write(result)

# response = send_gpt(result)
# save_to_txt_file(response["choices"][0]["message"]["content"], output_path)
