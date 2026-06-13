import nbformat
nb_main = nbformat.read('credit_card_fraud_detection_main.ipynb', as_version=4)
nb = nbformat.read('credit_card_fraud_detection.ipynb', as_version=4)

md_cell = nb_main.cells[14]
code_source = nb_main.cells[15].source
init_code = '\n'.join(code_source.split('\n')[:7])
train_code = '\n'.join(code_source.split('\n')[7:]).strip()

# Phase 3.1
nb.cells.append(md_cell)
nb.cells.append(nbformat.v4.new_code_cell(init_code))
nbformat.write(nb, 'credit_card_fraud_detection.ipynb')
