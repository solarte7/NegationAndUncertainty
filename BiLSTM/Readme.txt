=======================================================
Negation and Uncertainty detection using BiLSTM-CRF
=======================================================

1) The BiLSTM-CRF models requires Tensorflow 2.0 and Keras before being executed.

2) The directory libs contains an implementation of the CRF layer.

3) Before using this model, the training corpus must be pre-processed using scripts from the Preprocessing directory. 

   
4) Word embeddings must be obtained before using the BiLSTM-CRF model,  as follow:
   - Biomedical embeddings can be downloaded from: https://zenodo.org/record/3626806#.X_w5mXUzY0Q
   
   - Clinical embeddings can be obtained after authorization of the hospital's ethics committee. 
     Please contact us (via email) to obtain Clinical embeddings ==> oswaldo.solartep@alumnos.upm.es
