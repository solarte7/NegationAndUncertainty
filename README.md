# Negation And Speculation Detection from clinical text written in Spanish
The detection of speculation and negation in medical texts is paramount as otherwise extracted information can be incorrectly identified as real or factual events.
Speculation and negation detection is commonly divided into two sub-tasks: <strong>cue identification</strong> and <strong>scope recognition </strong>. Cues are words or terms that express negation (e.g, not, nothing, negative) or speculation (e.g., possible, probable, suggest). The scope is the text fragment affected by the corresponding cue in a sentence.<br><br>
This repository contains a deep learning-based approach for speculation and negation detection from clinical texts written in Spanish. The approach addresses negation and speculation detection as a sequence-labeling task, where each token in a sentence is classified as being part of the cue or the scope. This approach recognizes cues and scopes using the BIO tagging format.


The proposed approach explores two deep learning methods to perform negation and speculation detection from clinical text written in Spanish: 
 <ul>

 <li> <strong>Bidirectional Long Short memory (BiLSTM):</strong> The first method that we explore to detect negation and speculation is BILSTM with a CRF layer (BiLSTM-CRF) neural net. This method consist of three layers: Embedding layer, BiLSTM layer, and CRF layer.
  <ul>
   <li><strong>Embedding layer:</strong> This layer allows the approach to automatically represent text features using dense vector representations. The approach uses two types of embeddings biomedical embeddings and clinical embeddings. Biomedical embeddings for the Spanish language can be download from <a href= "https://zenodo.org/record/3626806#.X_w5mXUzY0Q"> Zenodo. </a> 
   
  
  </ul>
 <li> <strong> Bidirectional Encoder Representation for Transformers (BERT): </strong>  This process consists of three steps: Tokenization, BERT Processing, and Classification \& Post-processing.
</ul>

<strong>References:</strong>
</br> </br>
Lample, G.; Ballesteros, M.; Subramanian, S.; Kawakami, K.; Dyer, C.  Neural architectures for named entity  recognition.2016  Conference  of  the  North  American  Chapter  of  the  Association  for  Computational Linguistics: Human Language Technologies, NAACL HLT 2016 

</br> 
Soares, F.; Villegas, M.; Gonzalez-Agirre, A.; Krallinger, M.; Armengol-Estapé, J. Medical Word Embeddings787for Spanish: Development and Evaluation.  Proceedings of the 2nd Clinical Natural Language Processing788Workshop; Association for Computational Linguistics: Minneapolis, Minnesota, USA, 2019
<br>
Lima, S.; Perez, N.; Cuadros, M.; Rigau, G.  NUBES: A Corpus of Negation and Uncertainty in Spanish Clinical Texts 2020.  Proceedings  of  the  Workshop  Computational  Semantics  Beyond  Events  and  Roles,  Valencia,  Spain.
<br>
Marimon, M.; Vivaldi, J.; Bel, N.  Annotation of negation in the IULA Spanish Clinical Record Corpus.806Proceedings  of  the  Workshop  Computational  Semantics  Beyond  Events  and  Roles;  Association  for807Computational Linguistics: Valencia, Spain, 2017; pp. 43–52.  doi:10.18653/v1/W17-1807
<br>
Devlin, J.; Chang, M.W.; Lee, K.; Toutanova, K. BERT: Pre-training of deep bidirectional transformers for795language understanding.NAACL HLT 2019 - 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies - Proceedings of the Conference 2019

