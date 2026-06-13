import nbformat

nb = nbformat.read('credit_card_fraud_detection.ipynb', as_version=4)
nb_main = nbformat.read('credit_card_fraud_detection_main.ipynb', as_version=4)

# Append cells 16, 17, 18 which correspond to Phase 4, Evaluation dictionary, Results comparison
for i in range(16, 19):
    nb.cells.append(nb_main.cells[i])

nbformat.write(nb, 'credit_card_fraud_detection.ipynb')
