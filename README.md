# Negation And Speculation Detection from clinical texts written in Spanish: A deep learning approach
This repository contains a deep learning-based approach for speculation and negation detection from clinical texts written in Spanish. 
Speculation and negation detection is commonly divided into two sub-tasks: <strong>cue identification</strong> and <strong>scope recognition </strong>. Cues are words or terms that express negation (e.g, not, nothing, negative) or speculation (e.g., possible, probable, suggest). The scope is the text fragment affected by the corresponding cue in a sentence.<br>

The approach addresses negation and speculation detection as a sequence-labeling task, where each token in a sentence is classified as being part of the cue or the scope. This approach recognizes cues and scopes in a single step using the <strong>BIO</strong> tagging format.<br>

The proposed approach uses two deep learning methods to perform negation and speculation detection from clinical text written in Spanish: BILSTM and BERT:
 <ul>
 <li> <strong>Bidirectional Long Short memory (BiLSTM-CRF):</strong> This method consist of three layers: Embedding layer, BiLSTM layer, and CRF layer. The directory BiLSTM contains the implementation for this method.
  <ul>
   </br>
    <li><strong> Embedding layer:</strong> We used two types of embeddings: biomedical embeddings and clinical embeddings. Biomedical embeddings for the Spanish language [2] can be download from <a href= "https://zenodo.org/record/3626806#.X_w5mXUzY0Q"> Zenodo. </a> Clinical embeddings can be available only after an evaluation of the Hospital ethics committee.
  </br> </br> 
 <li> <strong> BiLSTM layer:</strong> this layer captures both left  and right contexts of words to produce a vector representation of text sequences using two steps: A Forward step process the sentence from left to right and, a Backward step process from right to left. 
   </br> </br>
  <li> <strong> CRF layer:</strong> this layer uses an implementation of the CRF algorithm to improve the predictions for each label. The CRF algorithm considers correlations between other labels. 
  
  </ul>
  </br> </br> 
 <li> <strong> Bidirectional Encoder Representation for Transformers (BERT): </strong>  We use the pre-trained BERT model fine tune with a classification layer on top. We use Multilingual BERT as contextualized embeddings. This process consists of three steps: Tokenization, BERT Processing, and Classification & Post-processing. The directory BERT contains the implementation for this method.</br> </br> 
 <ul>
  <li> <strong>Tokenization:</strong> the goal in this step is to take as input a raw text sentence and tokenize it using a WordPiece Tokenization method . For each word in the sentence, this method decides to keep the whole word or to split it in a set of sub-words. 
   </br> </br> 
  <li> <strong> BERT Processing:</strong> In this step, the approach takes as input the tokenized sentence from the previous step and process it as follows: First, the approach obtains an embedding representation for each word in the sentence. Next, the BERT Transformer Block takes as input the embedding representation , and produces a final representation  for each word in the processed sentence. 
 </br> </br> 
 <li><strong>Classification & Post-Processing:</strong> In this step, the approach takes as input the predicted BERT representations  and fed them into the softmax function.
 </ul>
</ul>
</br> </br>
<h3> Datasets</h3>
We use three datasets to evaluate the proposed approach for negation and speculation detection. NUBES [3]  and IULA [4] are two public corpus available for the Spanish language, and the third dataset is an in-house annotated corpus with real-life data of cancer patients. 
 </br> </br> 

<ul>
 <li> The NUBES corpus is available from <a href= https://github.com/Vicomtech/NUBes-negation-uncertainty-biomedical-corpus> https://github.com/Vicomtech/NUBes-negation-uncertainty-biomedical-corpus</a>  
  </br> </br>      
  <li> The IULA corpus is publicly available and can be access from <a href =http://eines.iula.upf.edu/brat/#/NegationOnCR_IULA> http://eines.iula.upf.edu/brat/#/NegationOnCR_IULA<a>
  </br> </br>   
  <li> The cancer dataset is an in-house manually annotated corpus with data from patients treated with lung and breast cancer. This corpus was extracted from clinical notes of real-life cancer patients' data from "Hospital Universitario Puerta de Hierro" in Madrid Spain. This dataset is not publicly available and can be accessed only after an evaluation of the Hospital ethics committee. This dataset is affected by General Data Protection Regulation (GDPR).
</ul>

<h3> Pre-processing </h3>
The datasets previously described must be pre-processed before being used in training the BiLSTM and BERT-based models. We provide the code that pre-processes the datasets and transform them into inputs for training the models. This code can be found y the Pre-processing directory.


<h3> Validation </h3>
This directory contains scripts for loading trained  models on the NUBES corpus, and perform negation and speculation  detetection in a different dataset. This code can be used to validate text sentences or to validate a complete dataset such as the Cancer dataset. 

<h3> Contact </h3>
If you have any question or suggestion, please contact us at the following email addresses:
<br><br>

<br>oswaldo.solartep@alumnos.upm.es</br>

</br> </br>
<strong>References:</strong>
</br> </br>
1. Lample, G.; Ballesteros, M.; Subramanian, S.; Kawakami, K.; Dyer, C.  Neural architectures for named entity  recognition.2016  Conference  of  the  North  American  Chapter  of  the  Association  for  Computational Linguistics: Human Language Technologies, NAACL HLT 2016
</br> </br> 
2. Soares, F.; Villegas, M.; Gonzalez-Agirre, A.; Krallinger, M.; Armengol-Estapé, J. Medical Word Embeddings787for Spanish: Development and Evaluation.  Proceedings of the 2nd Clinical Natural Language Processing788Workshop; Association for Computational Linguistics: Minneapolis, Minnesota, USA, 2019
</br> </br>
3. Lima, S.; Perez, N.; Cuadros, M.; Rigau, G.  NUBES: A Corpus of Negation and Uncertainty in Spanish Clinical Texts 2020.  Proceedings  of  the  Workshop  Computational  Semantics  Beyond  Events  and  Roles,  Valencia,  Spain.
</br> </br>
4. Marimon, M.; Vivaldi, J.; Bel, N.  Annotation of negation in the IULA Spanish Clinical Record Corpus. Proceedings  of  the  Workshop  Computational  Semantics  
Beyond  Events  and  Roles;  Association  for807Computational Linguistics: Valencia, Spain, 2017; pp. 43–52.  doi:10.18653/v1/W17-1807
</br> </br>
5. Devlin, J.; Chang, M.W.; Lee, K.; Toutanova, K. BERT: Pre-training of deep bidirectional transformers for795language understanding.NAACL HLT 2019 - 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies - Proceedings of the Conference 2019

