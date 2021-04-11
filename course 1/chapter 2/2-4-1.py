# 2.4 Работа с файловой системой и файлами
##############################
# Вам дается текстовый файл, содержащий некоторое количество непустых строк.
# На основе него сгенерируйте новый текстовый файл, содержащий те же строки в обратном порядке.

lines_reverse = []
with open('2-4-1-input.txt', 'r') as data_input, open('2-4-1-output.txt', 'w') as data_output:
    for line in data_input:
        lines_reverse.insert(0, line.strip())
    content = '\n'.join(lines_reverse)
    data_output.writelines(content)
