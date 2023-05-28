import os

from docx2pdf import convert


def file_convert_docx_pdf(dirs):
    file_in_dir = os.listdir(dirs)

    if not os.path.isdir(f'{dirs}\\convert_pdf'):
        os.mkdir(f'{dirs}\\convert_pdf')

    for file in file_in_dir:
        if file.endswith('.docx'):
            file_k = f'{file.split(".")[0].replace(".", "_")}.pdf'
            convert(f'{dirs}\\{file}', f'{dirs}\\convert_pdf\\{file_k}')
        else:
            continue


def main():
    dirs = input('Введите путь папки для сканирования: >> ')
    file_convert_docx_pdf(dirs)
    print(f'\n[+] - Конвертация завершена...')


if __name__ == "__main__":
    main()
