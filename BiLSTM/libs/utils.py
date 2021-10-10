from tqdm.auto import tqdm
from time import sleep
import datetime
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# ################################################################
#  Función para cargar archivos pre-entrenados en la memoria
#
# INPUT:
#              path: ruta donde se encuentra el pre-entrenado
#        num_tokens: Numero de palbras o tokens del conjunto
#                    de entrenamiento
#     embedding_dim: tamaño del embedding pre-entrenado
#        word_index: diccionario de todas las palbras
#
# OUTPUT:
#  embedding_matrix: matriz de tamaño num_tokens x embedding_dim
#                    que contiene los vectores especificos para
#                    el conjunto de entrenamiento
# ################################################################
def build_matrix_embeddings(path, num_tokens, embedding_dim, word_index):
    hits, misses = 0, 0
    embeddings_index = {}

    print('Cargando archivo...')

    sleep(0.5)

    for line in tqdm(open(path, encoding='utf-8')):
        word, coefs = line.split(maxsplit=1)
        embeddings_index[word] = np.fromstring(coefs, "f", sep=" ")

    print("Encontrados %s Vectores de pabras." % len(embeddings_index))

    sleep(0.5)

    # Preparara la matriz de embeddings
    embedding_matrix = np.zeros((num_tokens, embedding_dim))

    for word, i in tqdm(word_index.items()):
        if i >= num_tokens:
            continue
        try:
            embedding_vector = embeddings_index.get(word)
            if embedding_vector is not None:
                embedding_matrix[i] = embedding_vector
                hits += 1
            else:
                embedding_vector = embeddings_index.get(str(word).lower())
                if embedding_vector is not None:
                    embedding_matrix[i] = embedding_vector
                    hits += 1
                else:
                    embedding_vector = embeddings_index.get(str(word).upper())
                    if embedding_vector is not None:
                        embedding_matrix[i] = embedding_vector
                        hits += 1
                misses += 1
        except:
            embedding_matrix[i] = embeddings_index.get('UNK')

    print("Convertidos: %d Tokens | Perdidos: %d Tokens" % (hits, misses))

    return embedding_matrix

def plot_model_performance(train_loss, train_acc, train_val_loss, train_val_acc):
    """ Plot model loss and accuracy through epochs. """
    blue= '#34495E'
    green = '#2ECC71'
    orange = '#E23B13'
    
    # plot model loss
    #fig, (ax1, ax2) = plt.subplots(2, figsize=(10, 8))
    plt.figure(figsize=(18, 6))
    plt.subplot(1, 2, 1)
    plt.plot(range(1, len(train_loss) + 1), train_loss, blue, linewidth=5, label='training')
    plt.plot(range(1, len(train_val_loss) + 1), train_val_loss, green, linewidth=5, label='validation')
    plt.xlabel('# epoch')
    plt.ylabel('loss')
    plt.tick_params('y')
    plt.legend(loc='upper right', shadow=False)
    plt.title('Model loss through #epochs', color=orange, fontweight='bold')
    
    # plot model accuracy
    plt.subplot(1, 2, 2)
    plt.plot(range(1, len(train_acc) + 1), train_acc, blue, linewidth=5, label='training')
    plt.plot(range(1, len(train_val_acc) + 1), train_val_acc, green, linewidth=5, label='validation')
    plt.xlabel('# epoch')
    plt.ylabel('accuracy')
    plt.tick_params('y')
    plt.legend(loc='lower right', shadow=False)
    plt.title('Model accuracy through #epochs', color=orange, fontweight='bold')
    
    #fig.savefig('Plot/training/training-mb-00.png', bbox_inches='tight')

def logits_to_tokens(sequences, indexa):
    token_sequences = []
    for categorical_sequence in sequences:
        token_sequence = []
        for categorical in categorical_sequence:
            token_sequence.append(indexa[categorical])
 
        token_sequences.append(token_sequence)
 
    return token_sequences

def report_to_df(report):
    report = [x.split(' ') for x in report.split('\n')]
    header = ['Class Name']+[x for x in report[0] if x!='']
    values = []
    for row in report[1:-5]:
        row = [value for value in row if value!='']
        if row!=[]:
            values.append(row)
    df = pd.DataFrame(data = values, columns = header)
    return df

#########################################################
#
#          Funciones exclusivas modelo lample
#             usadas en el modelo original
#
#########################################################
# original de lample
def create_dico(item_list):
    """
    Create a dictionary of items from a list of list of items.
    """
    assert type(item_list) is list
    dico = {}
    for items in item_list:
        for item in items:
            if item not in dico:
                dico[item] = 1
            else:
                dico[item] += 1
    return dico

# original de lample
def create_mapping(dico):
    """
    Create a mapping (item to ID / ID to item) from a dictionary.
    Items are ordered by decreasing frequency.
    """
    sorted_items = sorted(dico.items(), key=lambda x: (-x[1], x[0]))
    id_to_item = {i: v[0] for i, v in enumerate(sorted_items)}
    item_to_id = {v: k for k, v in id_to_item.items()}
    return item_to_id, id_to_item

# original de lample
def char_mapping(sentences):
    """
    Create a dictionary and mapping of characters, sorted by frequency.
    """
    chars = ["".join([w[0] for w in s]) for s in sentences]
    dico = create_dico(chars)
    char_to_id, id_to_char = create_mapping(dico)
    print ("Found %i unique characters" % len(dico))
    
    return dico, char_to_id, id_to_char

def prepare_dataset(sentences, char_to_id):
    data = []
    
    for s in sentences:
        str_words = [w[0] for w in s]
        
        # Skip characters that are not in the training set
        ora = []
        for w in str_words:
            if w in char_to_id:
                ora.append(char_to_id[w])
            else:
                ora.append(10000)
        
        data.append(ora)
        
    return data


def pad_word_chars(oracc, max_length):
    #char_for = []
    padding = [0] * (max_length - len(oracc))
    char_for = oracc + padding

    return char_for

def create_input(oracc, max_length):
    char_for = pad_word_chars(oracc, max_length)

    return char_for
