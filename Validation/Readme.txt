==================================================================================
Validating the Cancer dataset:
==================================================================================


1) To perform Validation,  we used trained models with the NUBES corpus.
   These models can be downloaded from this link (Please access to the "saved-models" directory): 
   https://drive.google.com/drive/folders/1ZWcNMXx876Vu28Kr39ZVFGDh3MiAVBcR?usp=sharing

2) The directory "Validation with BiLSTM"  contains two files:

    - loadBiLSTM: This script allows us to load a trained BiLSTM-CRF model and validate a set of sentences manually.

   -  Valitation_BiLSTM: This script allows us to load a trained BiLSTM model and validate a complete dataset (The cancer dataset). This script automatically 
      calculate performed metrics. The dataset to be validated must be pre-processed preoviosly using the sripts provided in the directory Pre-processing.
      
3)    The directory "Validation with BERT"  contains two files:
      -  loadBERT: This script allows us to load a trained BERT-based model and validate a set of sentences manually.

     -  Valitation_BERT: This script allows us to load a trainebasd BERT-based model and validate a complete dataset. 
      This script automatically calculate performed metrics.
      
            
 *** Please contact us via email to obtain the cancer dataset. (oswaldo.solartep@alumnos.upm.es)
