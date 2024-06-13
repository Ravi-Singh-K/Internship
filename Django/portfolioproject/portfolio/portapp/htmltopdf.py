from xhtml2pdf import pisa


source_html = "<html><body><p>Converted PDF File</p></body></html>"
output_filename = "test.pdf"


def convert_html_to_pdf(source_html, output_filename):

    result_file = open(output_filename, "w+b")
    pisa_status = pisa.CreatePDF(
        source_html,
        dest = result_file
    )

    result_file.close
    return pisa_status.err


if __name__ == "__main__":
    pisa.showLogging()
    convert_html_to_pdf(source_html, output_filename)