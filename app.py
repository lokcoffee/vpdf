import argparse

# 使用示例
input_file = 'C:/Users/fernando/Desktop/anew/xs.pdf'
output_file = 'C:/Users/fernando/Desktop/anew/xsss.pdf'
password = '450345'  # 替换为实际的密码


from pypdf import PdfReader, PdfWriter

class PdfContext:
    def __init__(self, encrypt: bool, input_file: str, output_file: str, password: str):
        self.input_file = input_file
        self.output_file = output_file
        self.password = password
        self.encrypt = encrypt



def en_pdf(pdf_context: PdfContext):
    reader = PdfReader(pdf_context.input_file)
    writer = PdfWriter(clone_from=reader)

    # Add a password to the new PDF
    writer.encrypt(pdf_context.password, algorithm="AES-256")

    # Save the new PDF to a file
    with open(pdf_context.output_file, "wb") as f:
        writer.write(f)


def de_pdf(pdf_context: PdfContext):
    reader = PdfReader(pdf_context.input_file)

    if reader.is_encrypted:
        reader.decrypt(pdf_context.password)

    writer = PdfWriter(clone_from=reader)

    # Save the new PDF to a file
    with open(pdf_context.output_file, "wb") as f:
        writer.write(f)


def parse_args():
    parser = argparse.ArgumentParser(description='Process arguments.')

    parser.add_argument('--input', required=True, type=str, help='Input file')
    parser.add_argument('--output', required=True, type=str, help='Output file')
    parser.add_argument('--password', required=True, type=str, help='Password')
    parser.add_argument('--encrypt', type=str, default='Y', help='default is Y, if N decrypt')

    args = parser.parse_args()
    args.encrypt = args.encrypt.lower()
    pdf_context = PdfContext(args.input, args.output, password, args.encrypt)
    return pdf_context



def main():
    pdf_context: PdfContext = parse_args()
    if pdf_context.encrypt == "Y":
        en_pdf(pdf_context)
    else:
        de_pdf(pdf_context)


if __name__ == "__main__":
    main()