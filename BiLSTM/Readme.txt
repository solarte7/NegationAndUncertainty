=======================================================
Negation and Uncertainty detection using BiLSTM-CRF
=======================================================

1) The BiLSTM-CRF.ipynb file requires Tensorflow 2.0 and Keras before being executed.

2) The directory libs contains an implementation of the CRF layer.

3) Before using this model, the training corpus must be pre-processed using scripts from the Preprocessing directory. 

4) We also provide a pre-processed version of the corpora. This data can be download from :
   https://drive.google.com/drive/folders/1r7LO53y2YY42Z43YzR8E6PevUtrlM2vI?usp=sharing

   Preprocessed files must be placed in the vectors directory.

5) Word embeddings must be obtained before using the BiLSTM-CRF model,  as follow:
   - Biomedical embeddings can be downloaded from: https://zenodo.org/record/3626806#.X_w5mXUzY0Q
   
   - Clinical embeddings can be obtained after authorization of the hospital's ethics committee. 
     Please contact us (via email) to obtain Clinical embeddings ==> oswaldo.solartep@alumnos.upm.es
