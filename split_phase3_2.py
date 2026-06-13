import nbformat
nb = nbformat.read('credit_card_fraud_detection.ipynb', as_version=4)
nb_main = nbformat.read('credit_card_fraud_detection_main.ipynb', as_version=4)
code_source = nb_main.cells[15].source
train_code = '\n'.join(code_source.split('\n')[7:]).strip()

nb.cells.append(nbformat.v4.new_code_cell(train_code))
# Also carry over output if there is any?
# We can just copy the original cell 15 entirely for the final result, replacing the two cells, or keep them split.
# I'll just append it as a new code cell for simplicity.
nbformat.write(nb, 'credit_card_fraud_detection.ipynb')
